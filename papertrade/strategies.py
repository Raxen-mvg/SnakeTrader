"""Every strategy, each trading its own Rs 50,000 paper account.

A tick arrives every ~15 minutes during NSE hours. Strategies act on the first
tick of a session at or after ENTRY_AFTER (prices settle after the open) and
intraday positions close on the first tick at or after EXIT_INTRADAY.

  intraday      top-5 model picks, bought after the open, sold before the close
  intraweek     top-5, held 5 trading days
  intramonth    top-5, bought on entry to the top list, held until a name drops
                out of the model's top 25% (hold winners, trade less)
  random_hold   top-5, each held a random 2-40 trading days: a control that
                shows whether the holding period matters at all
  gold          GOLDBEES held throughout
  gold_trend    GOLDBEES only while above its 200-day average, else cash
  nifty_calls   SIMULATED: one Nifty ATM call bought Monday, sold Thursday
  benchmark     NIFTYBEES bought once and held: every strategy must beat this
"""

from __future__ import annotations

import datetime as dt
import json
from pathlib import Path
import math
import random

import numpy as np
import pandas as pd

from .broker import Account
from .costs import ZERODHA, order_cost
from .market import annual_vol, daily_closes
from .options import NIFTY_LOT, atm_strike, call_premium

ENTRY_AFTER = dt.time(9, 30)
EXIT_INTRADAY = dt.time(15, 5)
TOP_N = 5
SLIP_STOCK = 15.0            # bps each way: mid/small-cap India
SLIP_ETF = 5.0


def trading_days_ahead(d: dt.date, n: int) -> dt.date:
    return (pd.Timestamp(d) + pd.offsets.BDay(n)).date()


class Ctx:
    """What a strategy may see on this tick."""

    def __init__(self, t: dt.datetime, prices: dict[str, float], picks: list[dict],
                 ranks: dict[str, float], first_tick_today: dict[str, bool]):
        self.t = t
        self.prices = prices
        self.picks = picks                   # model's top list, best first: {symbol, score, rank_pct}
        self.ranks = ranks                   # model rank percentile for every scored stock
        self.first = first_tick_today


def _entered_today(acc: Account, t: dt.datetime) -> bool:
    return acc.memo.get("last_entry") == t.date().isoformat()


MAX_WEIGHT = 0.35            # never more than this share of the account in one name
MIN_WEIGHT = 0.05


def _weights(picks: list[dict]) -> dict[str, float]:
    """Bet size by confidence: a pick's weight grows with how far above the pack the
    model ranks it. Equal weight is the special case where all ranks are the same.
    Capped so one name cannot dominate, floored so a tiny slice is not worth its fees."""
    # Rank percentiles bunch up at the top (0.996 vs 1.000 is meaningless as a size),
    # so size on the raw model score standardised across the day's picks: a pick one
    # standard deviation better than the pack gets e times the weight.
    scores = [float(p.get("score", 0.0)) for p in picks]
    mean = sum(scores) / len(scores)
    var = sum((s - mean) ** 2 for s in scores) / max(len(scores) - 1, 1)
    sd = var ** 0.5
    if sd > 0:
        edge = {p["symbol"]: math.exp((float(p.get("score", 0.0)) - mean) / sd) for p in picks}
    else:   # no scores (or all identical): fall back to rank, then to equal weight
        edge = {p["symbol"]: max(float(p.get("rank_pct", 0.5)) - 0.5, 1e-6) for p in picks}
    total = sum(edge.values())
    w = {s: v / total for s, v in edge.items()}
    # Cap, then hand the excess to the uncapped names, until every weight fits.
    # With few picks an equal share can exceed the cap, so the cap never goes below it.
    cap = max(MAX_WEIGHT, 1.0 / len(w))
    for _ in range(len(w)):
        over = {s: v for s, v in w.items() if v > cap}
        if not over:
            break
        spare = sum(v - cap for v in over.values())
        rest = {s: v for s, v in w.items() if s not in over}
        rest_total = sum(rest.values()) or 1.0
        w = {**{s: cap for s in over},
             **{s: v + spare * v / rest_total for s, v in rest.items()}}
    w = {s: v for s, v in w.items() if v >= MIN_WEIGHT} or w
    total = sum(w.values())
    return {s: min(v / total, cap) for s, v in w.items()}


def _buy_weighted(acc: Account, ctx: Ctx, picks: list[dict], product: str,
                  exit_on=None, reason="", budget: float | None = None) -> None:
    """Deploy cash across picks in proportion to model confidence.

    budget caps what may be spent, for an account that runs several sleeves out of
    one pot of money; by default the whole free balance is used."""
    live = [p for p in picks if p["symbol"] in ctx.prices and p["symbol"] not in acc.positions]
    if not live:
        return
    w = _weights(live)
    cash = acc.cash if budget is None else min(acc.cash, budget)
    for p in live:
        share = w.get(p["symbol"])
        if not share:
            continue
        e = exit_on(p) if callable(exit_on) else exit_on
        acc.buy(p["symbol"], cash * share, ctx.prices[p["symbol"]], ctx.t, product,
                slippage_bps=SLIP_STOCK, exit_on=e,
                reason=reason or f"rank {p.get('rank_pct', 0):.3f}, size {100 * share:.0f}% of cash")


def _buy_top(acc: Account, ctx: Ctx, n: int, product: str, exit_on=None, reason="") -> None:
    picks = [p for p in ctx.picks if p["symbol"] in ctx.prices][:n]
    free = [p for p in picks if p["symbol"] not in acc.positions]
    if not free:
        return
    budget = acc.cash / len(free)
    for p in free:
        e = exit_on(p) if callable(exit_on) else exit_on
        acc.buy(p["symbol"], budget, ctx.prices[p["symbol"]], ctx.t, product,
                slippage_bps=SLIP_STOCK, exit_on=e, reason=reason or f"model rank {p.get('rank_pct', 0):.3f}")


INTRADAY_MODEL_AFTER = dt.time(10, 20)


INTRADAY_MIN_PROB = 0.45          # kept for reference: the old rule, which lost money
INTRADAY_MIN_TICKET = 5_000.0     # no dust trades: costs would swamp them
TAKE_PROFIT = 0.02
STOP_LOSS = -0.015


def intraday(acc: Account, ctx: Ctx) -> None:
    """Free-running: re-scores on every tick and may enter or exit whenever it likes.

    A position is closed on a profit target, a stop-loss, when the model stops
    liking it, or at the hard exit before the close. With no trained intraday
    model it falls back to one entry a day on the daily model's picks.
    """
    today = ctx.t.date().isoformat()
    for s, p in list(acc.positions.items()):
        if p.opened[:10] < today and s in ctx.prices:     # a run was missed before yesterday's close
            acc.sell(s, ctx.prices[s], ctx.t, slippage_bps=SLIP_STOCK, reason="missed close; sold next session")
    if ctx.t.time() >= EXIT_INTRADAY:
        for s in list(acc.positions):
            if s in ctx.prices:
                acc.sell(s, ctx.prices[s], ctx.t, slippage_bps=SLIP_STOCK, reason="intraday hard exit")
        return

    ipicks = getattr(ctx, "intraday_picks", None)
    if ipicks is None:                                    # no intraday model yet
        if acc.memo.get("last_entry") == today or acc.positions or ctx.t.time() < ENTRY_AFTER:
            return
        _buy_top(acc, ctx, TOP_N, "intraday", reason="daily model pick (no intraday model yet)")
        acc.memo["last_entry"] = today
        return

    # Same rule as the Rs 50,000 account: a trade happens only where the score has been
    # measured to pay several times what the round trip costs. Measured to date it never
    # does, so this account now sits out rather than paying charges to lose slowly.
    wanted = {p["symbol"]: p for p in ipicks if intraday_worth_it(float(p.get("score", 0.0)))}
    for s, p in list(acc.positions.items()):
        if s not in ctx.prices:
            continue
        move = ctx.prices[s] / p.avg_price - 1
        if move >= TAKE_PROFIT:
            acc.sell(s, ctx.prices[s], ctx.t, slippage_bps=SLIP_STOCK, reason=f"target hit {100 * move:+.2f}%")
        elif move <= STOP_LOSS:
            acc.sell(s, ctx.prices[s], ctx.t, slippage_bps=SLIP_STOCK, reason=f"stop loss {100 * move:+.2f}%")
        elif s not in wanted:
            acc.sell(s, ctx.prices[s], ctx.t, slippage_bps=SLIP_STOCK, reason=f"model dropped it {100 * move:+.2f}%")

    if ctx.t.time() < INTRADAY_MODEL_AFTER:
        return
    fresh = [p for s, p in wanted.items() if s not in acc.positions and s in ctx.prices]
    # As many positions as the model likes; cash is the only limit, and each
    # ticket must be big enough that charges do not swamp it.
    fresh = fresh[:max(1, int(acc.cash // INTRADAY_MIN_TICKET))]
    if not fresh or acc.cash < INTRADAY_MIN_TICKET:
        return
    budget = acc.cash / len(fresh)
    for p in fresh:
        acc.buy(p["symbol"], budget, ctx.prices[p["symbol"]], ctx.t, "intraday", slippage_bps=SLIP_STOCK,
                reason=f"intraday model, confidence {100 * p.get('score', 0):.0f}%")


def _exit_due(acc: Account, ctx: Ctx, reason: str) -> None:
    for s, p in list(acc.positions.items()):
        if p.exit_on and ctx.t.date().isoformat() >= p.exit_on and s in ctx.prices:
            acc.sell(s, ctx.prices[s], ctx.t, slippage_bps=SLIP_STOCK, reason=reason)


MIN_TICKET = 5_000.0


def _has_room(acc: Account) -> bool:
    """Free-running strategies may act on any tick, but only with a real ticket."""
    return acc.cash >= MIN_TICKET


def intraweek(acc: Account, ctx: Ctx) -> None:
    """Exits when its five days are up, refills whenever cash frees up."""
    if ctx.t.time() < ENTRY_AFTER:
        return
    _exit_due(acc, ctx, "5 trading days elapsed")
    if _has_room(acc) and len(acc.positions) < TOP_N:
        _buy_top(acc, ctx, TOP_N, "delivery", exit_on=trading_days_ahead(ctx.t.date(), 5).isoformat())


def intramonth(acc: Account, ctx: Ctx) -> None:
    """Hold winners: keep a name while the model ranks it in its top 25%. Checked every tick."""
    if ctx.t.time() < ENTRY_AFTER:
        return
    for s in list(acc.positions):
        if ctx.ranks and ctx.ranks.get(s, 0.0) < 0.75 and s in ctx.prices:
            acc.sell(s, ctx.prices[s], ctx.t, slippage_bps=SLIP_STOCK, reason="fell out of the top 25%")
    if _has_room(acc) and len(acc.positions) < TOP_N:
        _buy_top(acc, ctx, TOP_N, "delivery")


def random_hold(acc: Account, ctx: Ctx) -> None:
    """Control strategy: same picks, a random holding period per trade."""
    if ctx.t.time() < ENTRY_AFTER:
        return
    _exit_due(acc, ctx, "random holding period elapsed")
    rng = random.Random(ctx.t.date().toordinal())
    if _has_room(acc) and len(acc.positions) < TOP_N:
        _buy_top(acc, ctx, TOP_N, "delivery",
                 exit_on=lambda p: trading_days_ahead(ctx.t.date(), rng.randint(2, 40)).isoformat())


def gold(acc: Account, ctx: Ctx) -> None:
    s = "GOLDBEES.NS"
    if not acc.positions and s in ctx.prices and ctx.t.time() >= ENTRY_AFTER:
        acc.buy(s, acc.cash, ctx.prices[s], ctx.t, "delivery", slippage_bps=SLIP_ETF, reason="gold held")


def gold_trend(acc: Account, ctx: Ctx) -> None:
    """Checked once a day: the 200-day average does not move within a session."""
    s = "GOLDBEES.NS"
    if ctx.t.time() < ENTRY_AFTER or _entered_today(acc, ctx.t) or s not in ctx.prices:
        return
    closes = daily_closes([s], 300)[s].dropna()
    above = len(closes) > 200 and ctx.prices[s] > closes.tail(200).mean()
    if above and not acc.positions:
        acc.buy(s, acc.cash, ctx.prices[s], ctx.t, "delivery", slippage_bps=SLIP_ETF, reason="above 200-day average")
    elif not above and acc.positions:
        acc.sell(s, ctx.prices[s], ctx.t, slippage_bps=SLIP_ETF, reason="below 200-day average")
    acc.memo["last_entry"] = ctx.t.date().isoformat()


def nifty_calls(acc: Account, ctx: Ctx) -> None:
    """SIMULATED option: buy one ATM Nifty call on Monday, sell Thursday (weekly expiry style)."""
    spot = ctx.prices.get("^NSEI")
    if spot is None or ctx.t.time() < ENTRY_AFTER:
        return
    wd = ctx.t.weekday()
    sym = next(iter(acc.positions), None)
    if sym and (wd >= 3 or ctx.t.date().isoformat() >= acc.positions[sym].exit_on):
        p = acc.positions[sym]
        days_left = (pd.Timestamp(p.meta["expiry"]) - pd.Timestamp(ctx.t.date())).days
        prem = call_premium(spot, p.meta["strike"], days_left, p.meta["vol"])
        acc.sell(sym, prem, ctx.t, slippage_bps=50.0, reason="SIMULATED option exit")
        return
    if wd == 0 and not acc.positions and not _entered_today(acc, ctx.t):
        closes = daily_closes(["^NSEI"], 120)["^NSEI"].dropna()
        vol = annual_vol(closes)
        strike = atm_strike(spot)
        expiry = trading_days_ahead(ctx.t.date(), 3)
        prem = call_premium(spot, strike, (pd.Timestamp(expiry) - pd.Timestamp(ctx.t.date())).days, vol)
        name = f"NIFTY {expiry:%d%b} {strike:.0f} CE (SIMULATED)"
        one_lot = prem * NIFTY_LOT * 1.01 + 60           # one lot and its charges, never the whole account
        acc.buy(name, min(acc.cash, one_lot), prem, ctx.t, "option", slippage_bps=50.0, lot=NIFTY_LOT,
                exit_on=expiry.isoformat(), meta={"strike": strike, "expiry": expiry.isoformat(), "vol": vol},
                reason=f"SIMULATED Black-Scholes, realised vol {vol:.1%}")
        acc.memo["last_entry"] = ctx.t.date().isoformat()


UNIFIED_NAMES = 8
UNIFIED_EXIT_RANK = 0.75


def unified(acc: Account, ctx: Ctx) -> None:
    """One Rs 50,000 account running the model's best ideas together.

    Holds up to eight names, sized by confidence, keeps each while the model still
    ranks it in the top 25%, and refills from the current top list whenever a slot
    and enough cash are free. This is the account that answers "what does the whole
    system make on Rs 50,000".
    """
    if ctx.t.time() < ENTRY_AFTER:
        return
    for s in list(acc.positions):
        if ctx.ranks and ctx.ranks.get(s, 0.0) < UNIFIED_EXIT_RANK and s in ctx.prices:
            acc.sell(s, ctx.prices[s], ctx.t, slippage_bps=SLIP_STOCK, reason="fell out of the top 25%")
    room = UNIFIED_NAMES - len(acc.positions)
    if room <= 0 or acc.cash < MIN_TICKET:
        return
    # Only names the model still ranks highly, so a name sold for falling out of
    # the top 25% cannot be bought straight back on the same tick.
    fresh = [p for p in ctx.picks
             if p["symbol"] not in acc.positions
             and ctx.ranks.get(p["symbol"], p.get("rank_pct", 1.0)) >= UNIFIED_EXIT_RANK][:room]
    _buy_weighted(acc, ctx, fresh, "delivery")


def benchmark(acc: Account, ctx: Ctx) -> None:
    s = "NIFTYBEES.NS"
    if not acc.positions and s in ctx.prices and ctx.t.time() >= ENTRY_AFTER:
        acc.buy(s, acc.cash, ctx.prices[s], ctx.t, "delivery", slippage_bps=SLIP_ETF, reason="benchmark held")


STRATEGIES = {
    "unified": unified,
    "intraday": intraday, "intraweek": intraweek, "intramonth": intramonth,
    "random_hold": random_hold, "gold": gold, "gold_trend": gold_trend,
    "nifty_calls": nifty_calls, "benchmark": benchmark,
}
ALWAYS_QUOTE = ["NIFTYBEES.NS", "GOLDBEES.NS", "^NSEI"]


def option_marks(acc: Account, ctx: Ctx) -> dict[str, float]:
    """Mark simulated options to their model price so equity is meaningful."""
    out = {}
    spot = ctx.prices.get("^NSEI")
    for s, p in acc.positions.items():
        if p.product == "option" and spot:
            days = (pd.Timestamp(p.meta["expiry"]) - pd.Timestamp(ctx.t.date())).days
            out[s] = call_premium(spot, p.meta["strike"], days, p.meta["vol"])
    return out


# --- the whole model on one account -----------------------------------------
# No fixed split between sleeves. Every possible action is priced the same way -
# what do I expect to earn, and what will it cost me - and money goes wherever that
# number is positive. A sleeve that cannot clear its own costs simply gets nothing,
# for as long as that stays true.
#
# The expected-return figures below are measured, not chosen: they are the average
# 21-day excess returns of the model's top names in the walk-forward backtest, and
# the round-trip costs are Zerodha's published charges plus the slippage tier.
GOLD_SYMBOL = "GOLDBEES.NS"
CORE_HORIZON = 21                 # trading days the ranking model forecasts
# Recalibrated 2026-09-28, downwards, twice over.
#
# The 2.16% here came from the adopted-features measurement, and that measurement did not
# replicate: on fresh seeds the adopted families went from five of five to one of five in
# India and their mean net return fell below the baseline. They are out of the live model.
#
# The replacement comes from a cost-aware grid run on cached out-of-sample predictions over
# the full history: at Rs 50,000 the India book nets +0.61% per 21 sessions at two names and
# +0.48% at three, against round-trip costs of 0.62% to 0.66%, which puts the gross excess of
# a very short India book at roughly 1.1% rather than 2.16%. Every t-statistic in that grid is
# below 1.5, so this is a better-founded number and still not a precise one.
#
# The direction of the error matters: too high a figure makes the account buy more names than
# its edge can pay for, because each extra name costs a certain fee to earn an uncertain edge.
CORE_TOP_EXCESS = 0.0110          # 21-day excess of the top few, India, BEFORE costs
ROUND_TRIP_DELIVERY = 0.006       # 0.60% in and out, India delivery
ROUND_TRIP_INTRADAY = 0.0036      # 0.36% in and out, India intraday
EDGE_MULTIPLE = 2.0               # a trade must expect to earn at least this many times its cost
MAX_NAME_WEIGHT = 0.30
TYPICAL_CORRELATION = 0.35   # how much two Indian stocks move together, day to day
# Sessions a name is kept before an ordinary exit is even considered. Sixty-three was the
# best of the holding periods measured; a hundred and twenty-six was better still but
# commits the account for half a year on evidence that is monotone rather than precise.
MIN_HOLD_SESSIONS = 63
DISASTER_STOP = -0.25        # sell at any age if a holding falls this far from entry


def round_trip_cost(value: float, product: str = "delivery") -> float:
    """What it really costs to buy and sell a position of this size, as a fraction of it.

    Not a flat percentage. Selling from a demat account carries a fixed depository charge
    of about Rs 15 per scrip per sell day whatever the size, so cost per rupee falls as the
    position grows: a Rs 5,000 ticket pays 0.83% for a round trip and a Rs 37,500 one pays
    0.56%. On a Rs 50,000 account that difference decides how many names it can afford to
    hold at all, which is why the figure is computed rather than assumed.
    """
    if value <= 0:
        return 1.0
    buy = order_cost("buy", product, value, ZERODHA)["total"]
    sell = order_cost("sell", product, value, ZERODHA)["total"]
    return (buy + sell) / value + 2 * SLIP_STOCK / 1e4


def exit_cost(value: float, product: str = "delivery") -> float:
    """Cost of selling a position of this size, as a fraction of it.

    What was paid to get in is spent and gone; the only question about a holding is
    whether what it is still expected to earn beats the cost of leaving.
    """
    if value <= 0:
        return 1.0
    return order_cost("sell", product, value, ZERODHA)["total"] / value + SLIP_STOCK / 1e4


def core_gross(rank_pct: float) -> float:
    """Expected excess return over the horizon, before any costs, at this model rank.

    Symmetric about the median on purpose. Clamping this at zero said a bottom-ranked stock
    is merely expected to earn nothing, when the model's own history says such names
    underperform - and it silently disabled the rule that sells a holding which has turned
    bad, because "worse than nothing" could never be expressed.
    """
    return CORE_TOP_EXCESS * (rank_pct - 0.5) / 0.5


# The owner's instruction is that a trade must make SIGNIFICANTLY more than it costs, not
# merely more. Expressed as a margin: expected net return must be at least this fraction of
# the round trip. It is set low deliberately, and the reason is uncomfortable - with the
# expected excess of the best name at 1.1% and a round trip of 0.645% on a Rs 12,500 ticket,
# the very best name the model can find nets 0.455%, which is 0.7 times its own cost. A
# demand of "net at least equal to the cost" would mean never trading at all. That the bar
# has to be set here to permit any trade is itself the measurement.
CORE_MARGIN = 0.25


def core_edge(rank_pct: float, value: float = 12_500.0) -> float:
    """Expected net return per trading day from holding a name of this size at this rank.

    The default position size is a quarter of a Rs 50,000 account, which is roughly what
    the account can hold once the fixed selling charge is paid for.
    """
    return (core_gross(rank_pct) - round_trip_cost(value)) / CORE_HORIZON


def core_worth_it(rank_pct: float, value: float) -> bool:
    """Is this name expected to make significantly more than it costs, not merely more?"""
    cost = round_trip_cost(value)
    return core_gross(rank_pct) - cost >= CORE_MARGIN * cost


def best_book(ranks: list[float], budget: float, max_names: int = 12) -> tuple[int, float]:
    """How many of these names the account should hold, and the ticket size.

    Three forces pull against each other. Adding a name means a lower-ranked name, so the
    average edge falls. It also means a smaller ticket, and every ticket pays the same fixed
    depository charge on the way out, so the cost per rupee rises. But holding more names
    cuts the risk of the book roughly as the square root of their number.

    Maximising expected rupees alone would put the whole account in one stock, which is not
    a portfolio. So the quantity maximised here is expected net return times the square root
    of the number of names - expected return per unit of risk, for a book of roughly equal
    and roughly independent positions. Zero names means nothing on the list clears its own
    cost at any size this account can afford.
    """
    best = (0, 0.0, 0.0)
    for n in range(1, min(max_names, len(ranks)) + 1):
        ticket = budget / n
        if ticket < MIN_TICKET:
            break
        cost = round_trip_cost(ticket)
        nets = [core_gross(r) - cost for r in ranks[:n]]
        if min(nets) < CORE_MARGIN * cost:       # the marginal name must clear the margin
            continue
        # Diversification does not keep paying. Stocks in one market move together - pairwise
        # correlation of about a third is normal - so the tenth name reduces risk far less than
        # the second did, and the benefit saturates. Treating positions as independent (a plain
        # square root of n) makes the score rise forever and the book size become whatever cap
        # happens to be written down, which is how this account ended up holding exactly its
        # maximum of twelve names rather than a number anything chose.
        effective = n / (1 + (n - 1) * TYPICAL_CORRELATION)
        score = (sum(nets) / n) * effective ** 0.5
        if score > best[2]:
            best = (n, ticket, score)
    return best[0], best[1]


CALIBRATION = Path(__file__).resolve().parent.parent / "state" / "intraday_calibration.json"


def _calibration() -> list[tuple[float, float]] | None:
    """Pairs of (model score, realised net return) measured on out-of-sample history.

    The intraday model outputs a cross-sectional RANK, not a probability, so a score
    of 0.55 means "a bit above average today" and not "55% likely to win". Nothing can
    be inferred about money from a rank until the rank has been measured against what
    it actually paid, which is what this file holds. No file, no trading.
    """
    try:
        d = json.loads(CALIBRATION.read_text())
        pts = sorted((float(a), float(b)) for a, b in zip(d["score"], d["expected_net"]))
        return pts or None
    except Exception:
        return None


def intraday_expected_net(score: float) -> float | None:
    """What a trade at this score has historically paid, after charges. None if unmeasured."""
    pts = _calibration()
    if not pts:
        return None
    if score <= pts[0][0]:
        return pts[0][1]
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if score <= x1:
            return y0 + (y1 - y0) * (score - x0) / (x1 - x0) if x1 > x0 else y1
    return pts[-1][1]


def intraday_edge(score: float) -> float:
    """Expected net return of one intraday trade at this score; zero when unmeasured."""
    e = intraday_expected_net(score)
    return 0.0 if e is None else e


def intraday_worth_it(score: float) -> bool:
    """Only when the measured payoff is several times what the round trip costs.

    Measured to date: the live intraday model ranks well (IC 0.069, t 14.6) but its
    top five move +0.129% from 10:15 to the close against a 0.36% round trip, which
    is -0.231% a day after charges and profitable on 27% of days. There is therefore
    no score at which it currently pays, and with no calibration file present this
    returns False for everything. That is deliberate: not trading is the correct
    action until something can be shown to beat its own costs.
    """
    e = intraday_expected_net(score)
    return e is not None and e >= EDGE_MULTIPLE * ROUND_TRIP_INTRADAY


def _capped_shares(edges: dict[str, float]) -> dict[str, float]:
    """Split the cash in proportion to expected edge, with no name over the cap.

    Whatever the cap takes off a large position is handed back to the others rather
    than left sitting as idle cash, so the account stays invested in what it believes.
    """
    live = {k: v for k, v in edges.items() if v > 0}
    if not live:
        return {k: 0.0 for k in edges}
    # With only two or three names worth owning, a 30% cap would force money to sit
    # idle; the cap then loosens to an equal split rather than leaving cash unused.
    cap = max(MAX_NAME_WEIGHT, 1.0 / len(live))
    out = {k: 0.0 for k in edges}
    free, remaining = dict(live), 1.0
    while free and remaining > 1e-9:
        total = sum(free.values())
        capped = [k for k, v in free.items() if remaining * v / total > cap]
        if not capped:
            for k, v in free.items():
                out[k] += remaining * v / total
            break
        for k in capped:
            out[k] = cap
            remaining -= cap
            free.pop(k)
    return out


def _barred_today(acc: Account, ctx: Ctx) -> set:
    """Names sold today, which must not be bought back on the same day.

    Without this the disaster stop defeats itself: a holding that has collapsed is sold and
    then, still carrying a high model rank, bought straight back on the same tick - paying
    both sides of a round trip to end up where it started.
    """
    bar = acc.memo.get("sold_today") or {}
    return set(bar.get("names", [])) if bar.get("day") == ctx.t.date().isoformat() else set()


def _bar_today(acc: Account, ctx: Ctx, symbol: str) -> None:
    day = ctx.t.date().isoformat()
    bar = acc.memo.get("sold_today") or {}
    if bar.get("day") != day:
        bar = {"day": day, "names": []}
    if symbol not in bar["names"]:
        bar["names"].append(symbol)
    acc.memo["sold_today"] = bar


def _sessions_held(pos, now) -> int:
    """Trading sessions since a position was opened, counted as weekdays."""
    import datetime as _dt
    opened = _dt.date.fromisoformat(pos.opened[:10])
    days = (now.date() - opened).days
    return max(int(days * 5 / 7), 0)


def oracle(acc: Account, ctx: Ctx) -> None:
    """Rs 50,000, one pot of cash, and no human-chosen allocation.

    Each candidate is priced by what it is expected to earn per day net of what it
    costs to get in and out. Anything with a positive number competes for the cash;
    anything without one is not bought. The intraday sleeve therefore funds itself
    only on the days it can show a real edge, and holds nothing overnight.
    """
    if ctx.t.time() < ENTRY_AFTER:
        return

    # Intraday first: it must be flat by the close, and it borrows cash only for the day.
    if ctx.t.time() >= EXIT_INTRADAY:
        for s, pos in list(acc.positions.items()):
            if pos.product == "intraday" and s in ctx.prices:
                acc.sell(s, ctx.prices[s], ctx.t, slippage_bps=SLIP_STOCK, reason="intraday hard exit")
    else:
        ipicks = getattr(ctx, "intraday_picks", None) or []
        wanted = {p["symbol"]: p for p in ipicks if intraday_worth_it(float(p.get("score", 0.0)))}
        for s, pos in list(acc.positions.items()):
            if pos.product != "intraday" or s not in ctx.prices:
                continue
            move = ctx.prices[s] / pos.avg_price - 1
            if move >= TAKE_PROFIT:
                acc.sell(s, ctx.prices[s], ctx.t, slippage_bps=SLIP_STOCK, reason=f"target hit {100 * move:+.2f}%")
            elif move <= STOP_LOSS:
                acc.sell(s, ctx.prices[s], ctx.t, slippage_bps=SLIP_STOCK, reason=f"stop loss {100 * move:+.2f}%")
            elif s not in wanted:
                acc.sell(s, ctx.prices[s], ctx.t, slippage_bps=SLIP_STOCK, reason=f"edge gone {100 * move:+.2f}%")
        fresh = [p for s, p in wanted.items() if s not in acc.positions and s in ctx.prices]
        if fresh and ctx.t.time() >= INTRADAY_MODEL_AFTER and acc.cash >= MIN_TICKET:
            # An intraday trade earns its day's edge now, so it outbids the core book
            # for cash whenever it qualifies at all - which is rare by construction.
            fresh.sort(key=lambda p: -intraday_edge(float(p.get("score", 0.0))))
            fresh = fresh[:max(1, int(acc.cash // MIN_TICKET))]
            each = acc.cash / len(fresh)
            for p in fresh:
                acc.buy(p["symbol"], each, ctx.prices[p["symbol"]], ctx.t, "intraday", slippage_bps=SLIP_STOCK,
                        reason=f"expected {100 * intraday_edge(float(p.get('score', 0.0))):+.2f}% net, "
                               f"confidence {100 * float(p.get('score', 0.0)):.0f}%")

    # Core book: keep a name while what it is still expected to earn beats the cost of
    # selling it. The money already spent getting in is gone and does not enter the decision.
    for s, pos in list(acc.positions.items()):
        if pos.product == "intraday" or s not in ctx.prices:
            continue
        value = pos.qty * ctx.prices[s]
        expected, leaving = core_gross(ctx.ranks.get(s, 0.0)), exit_cost(value)
        held = _sessions_held(pos, ctx.t)
        # Measured 2026-09-28: selling as soon as the expected gain dips below the cost of
        # leaving was the WORST of four policies tested - worse than any fixed holding period -
        # because it churns. Longer holds lost less and won more often, monotonically: 21
        # sessions -0.019% a day and 42% of trades profitable, 63 sessions -0.010% and 46%,
        # 126 sessions -0.004% and 51%. The fee is charged per sale, so time is the cheapest
        # thing an account owns. Before the minimum hold a name is sold only if it has turned
        # actively bad, not merely unexciting.
        # A safety net, not an edge. The minimum hold assumes the model's rank keeps telling
        # the truth about a name, and last week the frozen snapshot went three days stale
        # without anyone noticing - during which every rank would have been frozen too, and a
        # collapsing holding would never have triggered the deterioration exit. This fires
        # only on a disaster and is deliberately far outside normal movement, so it should
        # almost never be the reason for a sale. If it starts firing regularly, something
        # upstream is broken and that is what wants fixing.
        drop = ctx.prices[s] / pos.avg_price - 1
        if drop <= DISASTER_STOP:
            acc.sell(s, ctx.prices[s], ctx.t, slippage_bps=SLIP_STOCK,
                     reason=f"down {100 * drop:.0f}% from entry; selling regardless of rank")
            _bar_today(acc, ctx, s)
            continue
        if held < MIN_HOLD_SESSIONS:
            if expected < -leaving:
                acc.sell(s, ctx.prices[s], ctx.t, slippage_bps=SLIP_STOCK,
                         reason=f"deteriorated after {held} sessions, not merely gone quiet")
        elif expected <= leaving:
            acc.sell(s, ctx.prices[s], ctx.t, slippage_bps=SLIP_STOCK,
                     reason=f"held {held} sessions; expected return no longer covers selling")
    if acc.cash < MIN_TICKET:
        return
    cand = [p for p in ctx.picks if p["symbol"] not in acc.positions and p["symbol"] in ctx.prices
            and p["symbol"] not in _barred_today(acc, ctx)]
    if not cand:
        return
    # How many names this much money can afford to hold, given that every position pays the
    # same fixed charge on the way out, and how big each one should therefore be.
    ranked = [ctx.ranks.get(p["symbol"], p.get("rank_pct", 0.0)) for p in cand]
    n, ticket = best_book(ranked, acc.cash)
    if n == 0:
        return
    # Beyond paying for itself, each name must clear the margin.
    cand = [p for p in cand[:n]
            if core_worth_it(ctx.ranks.get(p["symbol"], p.get("rank_pct", 0.0)), ticket)]
    if not cand:
        return
    cost = round_trip_cost(ticket)
    edges = {p["symbol"]: core_gross(ctx.ranks.get(p["symbol"], p.get("rank_pct", 0.0))) - cost
             for p in cand}
    shares = _capped_shares(edges)
    budget = acc.cash                     # shares are of the cash we started the tick with,
    for p in cand:                        # not of what is left after each purchase
        share = shares[p["symbol"]]
        amount = min(budget * share, acc.cash)
        if amount >= MIN_TICKET:
            acc.buy(p["symbol"], amount, ctx.prices[p["symbol"]], ctx.t, "delivery", slippage_bps=SLIP_STOCK,
                    reason=f"expected {100 * edges[p['symbol']]:+.2f}% net over {CORE_HORIZON} days "
                           f"after {100 * cost:.2f}% costs")


# --- a second account, run on different principles --------------------------
# Not the ranking model. This is the market-making family of ideas as a retail
# account can honestly run them: no rebates, no queue priority, no colocation, and
# the spread is crossed in both directions. What is left is statistical arbitrage -
# a stock that has fallen much further than its peers today, with no news to justify
# it, tends to close part of that gap before the bell. Many small trades, each one
# taken only when the expected snap-back is a real multiple of the charges.
STATARB_UNIVERSE = [
    "RELIANCE.NS", "HDFCBANK.NS", "ICICIBANK.NS", "INFY.NS", "TCS.NS", "ITC.NS",
    "LT.NS", "AXISBANK.NS", "SBIN.NS", "BHARTIARTL.NS", "KOTAKBANK.NS", "HINDUNILVR.NS",
    "MARUTI.NS", "SUNPHARMA.NS", "TMPV.NS", "TATASTEEL.NS", "WIPRO.NS", "HCLTECH.NS",
    "ULTRACEMCO.NS", "TITAN.NS", "ASIANPAINT.NS", "BAJFINANCE.NS", "POWERGRID.NS", "NTPC.NS",
    "ONGC.NS", "GRASIM.NS", "JSWSTEEL.NS", "COALINDIA.NS", "CIPLA.NS", "DRREDDY.NS",
]
STATARB_ENTRY_Z = 1.5             # how far below its peers a name must be to be worth buying
STATARB_EXIT_Z = 0.25             # where the gap is considered closed
STATARB_EXIT_GAP = 0.003          # or where it is simply too small to be worth holding
STATARB_MIN_SD = 0.003            # a quiet cross-section makes z-scores meaningless
STATARB_MIN_NAMES = 12            # below this the cross-section is too thin to mean anything
STATARB_MAX_POSITIONS = 8
STATARB_TICKET = 0.12             # of equity per name: many small trades, not a few big ones
# Measured before it was trusted with money (research/STATARB_RESULT.md, STATARB_SWEEP.md,
# STATARB_VARIANTS.md): on 62 days of five-minute bars the rule returns -0.385% net per
# trade, and the whole grid of entry and exit settings - in BOTH directions, fading the
# laggards and following the leaders - is negative BEFORE costs, best case -0.014%. The
# idea has no gross edge at this resolution, so costs are not even the binding problem.
# It wins 55% of the time with a positive median and loses the lot on the tail, which is
# what a mean-reversion payoff looks like when there is nothing behind it.
# The account stays at Rs 50,000 and stays flat until some version of this shows a
# positive GROSS return out of sample.
STATARB_ENABLED = False


MARKET_OPEN = dt.time(9, 15)


def _day_open(acc: Account, ctx: Ctx) -> dict:
    """First price seen for each name today - the account's own record of the open.

    Only ticks inside market hours count. A tick before the bell carries yesterday's
    closing prices, and recording those as today's open would make every move look
    like a gap that needs closing.
    """
    day = ctx.t.date().isoformat()
    if ctx.t.time() < MARKET_OPEN:
        return (acc.memo.get("day_open") or {}).get("px", {}) if (acc.memo.get("day_open") or {}).get("day") == day else {}
    book = acc.memo.get("day_open") or {}
    if book.get("day") != day:
        book = {"day": day, "px": {}}
    for s, px in ctx.prices.items():
        book["px"].setdefault(s, px)
    acc.memo["day_open"] = book
    return book["px"]


def statarb(acc: Account, ctx: Ctx) -> None:
    """Rs 50,000 run as intraday statistical arbitrage instead of forecasting.

    Every name in a liquid universe is measured against how the rest of that universe
    has moved since the open. A name far below the crowd is bought and sold back when
    the gap closes; nothing is held overnight. A trade is only opened when the gap it
    expects to close is worth several times the cost of trading it.
    """
    opens = _day_open(acc, ctx)
    if not STATARB_ENABLED and not acc.positions:
        return
    if ctx.t.time() >= EXIT_INTRADAY:
        for s, pos in list(acc.positions.items()):
            if s in ctx.prices:
                acc.sell(s, ctx.prices[s], ctx.t, slippage_bps=SLIP_STOCK, reason="flat before the close")
        return
    if ctx.t.time() < ENTRY_AFTER:
        return

    moves = {s: ctx.prices[s] / opens[s] - 1
             for s in STATARB_UNIVERSE if s in ctx.prices and opens.get(s)}
    if len(moves) < STATARB_MIN_NAMES:
        return
    vals = list(moves.values())
    mean = sum(vals) / len(vals)
    sd = (sum((v - mean) ** 2 for v in vals) / max(len(vals) - 1, 1)) ** 0.5
    if sd <= 0:
        return
    z = {s: (v - mean) / sd for s, v in moves.items()}

    for s, pos in list(acc.positions.items()):
        if s not in ctx.prices:
            continue
        move = ctx.prices[s] / pos.avg_price - 1
        gap = mean - moves.get(s, mean)       # how far it still trails the crowd, in returns
        if z.get(s, 0.0) >= -STATARB_EXIT_Z or gap <= STATARB_EXIT_GAP:
            acc.sell(s, ctx.prices[s], ctx.t, slippage_bps=SLIP_STOCK, reason=f"gap closed {100 * move:+.2f}%")
        elif move <= STOP_LOSS:
            acc.sell(s, ctx.prices[s], ctx.t, slippage_bps=SLIP_STOCK, reason=f"stop loss {100 * move:+.2f}%")

    room = STATARB_MAX_POSITIONS - len(acc.positions)
    if room <= 0 or acc.cash < MIN_TICKET or sd < STATARB_MIN_SD or not STATARB_ENABLED:
        return
    # Expected gain is the part of the gap that is expected to close, in return terms.
    cand = []
    for s, zs in z.items():
        if zs > -STATARB_ENTRY_Z or s in acc.positions:
            continue
        expected = (abs(zs) - STATARB_EXIT_Z) * sd
        if expected >= EDGE_MULTIPLE * ROUND_TRIP_INTRADAY:
            cand.append((expected, s))
    cand.sort(reverse=True)
    ticket = min(acc.equity(ctx.prices) * STATARB_TICKET, acc.cash)
    for expected, s in cand[:room]:
        if acc.cash < MIN_TICKET:
            break
        acc.buy(s, min(ticket, acc.cash), ctx.prices[s], ctx.t, "intraday", slippage_bps=SLIP_STOCK,
                reason=f"{z[s]:.1f} sd below its peers, expecting {100 * expected:+.2f}% back")


STRATEGIES["oracle"] = oracle
STRATEGIES["statarb"] = statarb
ALWAYS_QUOTE = ALWAYS_QUOTE + STATARB_UNIVERSE   # the stat-arb book needs its whole cross-section quoted      # defined below the table, so registered here


# ---------------------------------------------------------------------------------------------
# SNAKE: a separate model with its own Rs 2 lakh, trading India from 2026-09-29.
#
# A deep network trained on every market's daily history plus Indian exchange announcements,
# predicting six holding periods at once. Its picks file carries, for every scored name, the
# best return it expects across those horizons after calibration against what that level of
# prediction actually paid. The account uses one rule for everything, the same one measured in
# its backtest: buy only what is expected to beat its own round trip, keep a holding only while
# it is still expected to beat the cost of selling it. The holding period is therefore whatever
# the model says - it is never set in advance.
# ---------------------------------------------------------------------------------------------
SNAKE_NAMES = 6
SNAKE_STALE_DAYS = 4          # calendar days: stop BUYING on a picks file older than this


def _snake_fresh(ctx: Ctx) -> bool:
    s = getattr(ctx, "snake", None) or {}
    try:
        asof = dt.date.fromisoformat(s.get("asof", ""))
    except ValueError:
        return False
    return (ctx.t.date() - asof).days <= SNAKE_STALE_DAYS


def snake(acc: Account, ctx: Ctx) -> None:
    """SNAKE's own book: expected return against real cost, decided per name."""
    if ctx.t.time() < ENTRY_AFTER:
        return
    s = getattr(ctx, "snake", None) or {}
    expected = s.get("expected", {})
    fresh = _snake_fresh(ctx)

    for sym, pos in list(acc.positions.items()):
        if sym not in ctx.prices:
            continue
        price = ctx.prices[sym]
        move = price / pos.avg_price - 1
        if move <= DISASTER_STOP:
            acc.sell(sym, price, ctx.t, slippage_bps=SLIP_STOCK, reason=f"disaster stop {100 * move:+.1f}%")
            _bar_today(acc, ctx, sym)
            continue
        if not fresh:
            continue                      # no current view of this name: hold, do not guess
        want = expected.get(sym)
        leaving = exit_cost(pos.qty * price)
        if want is None or want <= leaving:
            why = ("no longer scored" if want is None
                   else f"expects {100 * want:+.2f}%, selling costs {100 * leaving:.2f}%")
            acc.sell(sym, price, ctx.t, slippage_bps=SLIP_STOCK, reason=f"SNAKE exit: {why}")
            _bar_today(acc, ctx, sym)

    if not fresh or acc.memo.get("snake_entry") == ctx.t.date().isoformat():
        return
    free = SNAKE_NAMES - len(acc.positions)
    if free <= 0 or acc.cash < MIN_TICKET:
        return
    equity = acc.equity(ctx.prices)
    ticket = min(equity / SNAKE_NAMES, acc.cash / free)
    if ticket < MIN_TICKET:
        return
    barred = _barred_today(acc, ctx)
    bought = 0
    for p in s.get("top", []):
        sym = p["symbol"]
        if bought >= free or sym in acc.positions or sym in barred or sym not in ctx.prices:
            continue
        need = round_trip_cost(ticket)
        if float(p.get("expected", 0.0)) <= need:
            break                         # the list is sorted: nothing further down clears it
        ok = acc.buy(sym, min(ticket, acc.cash), ctx.prices[sym], ctx.t, "delivery",
                     slippage_bps=SLIP_STOCK,
                     reason=f"SNAKE expects {100 * float(p['expected']):+.2f}% over "
                            f"{p.get('horizon', '?')} sessions against a {100 * need:.2f}% round trip")
        bought += int(bool(ok))
    acc.memo["snake_entry"] = ctx.t.date().isoformat()


STRATEGIES["snake"] = snake              # trained with news; reads picks_snake.json
STRATEGIES["snake_nonews"] = snake       # same rule, no-news model; reads picks_snake_nonews.json
STRATEGIES["snake_abs"] = snake          # same rule, absolute-return model; reads picks_snake_abs.json
