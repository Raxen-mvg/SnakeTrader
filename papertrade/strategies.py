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
import math
import random

import numpy as np
import pandas as pd

from .broker import Account
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


INTRADAY_MIN_PROB = 0.45          # only trades the model is confident about
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

    wanted = {p["symbol"]: p for p in ipicks if p.get("score", 0) >= INTRADAY_MIN_PROB}
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
CORE_TOP_EXCESS = 0.0116          # measured: 21-day excess of the top 5, India, before costs
ROUND_TRIP_DELIVERY = 0.006       # 0.60% in and out, India delivery
ROUND_TRIP_INTRADAY = 0.0036      # 0.36% in and out, India intraday
EDGE_MULTIPLE = 2.0               # a trade must expect to earn at least this many times its cost
MAX_NAME_WEIGHT = 0.30


def core_edge(rank_pct: float) -> float:
    """Expected net return per trading day from holding a name at this model rank.

    The model's top name earns about CORE_TOP_EXCESS over 21 days before costs and
    the edge fades linearly towards the median, so a name must be ranked high enough
    that its expected gain covers a round trip before it is worth owning at all.
    """
    gross = CORE_TOP_EXCESS * max(0.0, (rank_pct - 0.5) / 0.5)
    return (gross - ROUND_TRIP_DELIVERY) / CORE_HORIZON


def intraday_edge(prob: float, take: float = TAKE_PROFIT, stop: float = STOP_LOSS) -> float:
    """Expected net return of one intraday trade at this model confidence.

    Wins take the profit target, losses hit the stop. The trade is only worth taking
    when what is left after charges is a real multiple of those charges, not a sliver
    of one - which is why the sleeve sits out most days.
    """
    return prob * take + (1 - prob) * stop - ROUND_TRIP_INTRADAY


def intraday_worth_it(prob: float) -> bool:
    return intraday_edge(prob) >= EDGE_MULTIPLE * ROUND_TRIP_INTRADAY


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

    # Core book: hold a name while it still expects to earn more than it costs to keep.
    for s, pos in list(acc.positions.items()):
        if pos.product == "intraday" or s not in ctx.prices:
            continue
        if core_edge(ctx.ranks.get(s, 0.0)) <= 0:
            acc.sell(s, ctx.prices[s], ctx.t, slippage_bps=SLIP_STOCK, reason="expected return no longer covers costs")
    if acc.cash < MIN_TICKET:
        return
    cand = [p for p in ctx.picks
            if p["symbol"] not in acc.positions and p["symbol"] in ctx.prices
            and core_edge(ctx.ranks.get(p["symbol"], p.get("rank_pct", 0.0))) > 0]
    if not cand:
        return
    # As many names as the cash supports at a sensible ticket, sized by expected edge.
    cand = cand[:max(1, int(acc.cash // MIN_TICKET))]
    edges = {p["symbol"]: core_edge(ctx.ranks.get(p["symbol"], p.get("rank_pct", 0.0))) for p in cand}
    total = sum(edges.values())
    budget = acc.cash                     # shares are of the cash we started the tick with,
    for p in cand:                        # not of what is left after each purchase
        share = min(edges[p["symbol"]] / total, MAX_NAME_WEIGHT) if total > 0 else 1.0 / len(cand)
        amount = min(budget * share, acc.cash)
        if amount >= MIN_TICKET:
            acc.buy(p["symbol"], amount, ctx.prices[p["symbol"]], ctx.t, "delivery", slippage_bps=SLIP_STOCK,
                    reason=f"expected {100 * edges[p['symbol']] * CORE_HORIZON:+.2f}% net over {CORE_HORIZON} days")


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
    "MARUTI.NS", "SUNPHARMA.NS", "TATAMOTORS.NS", "TATASTEEL.NS", "WIPRO.NS", "HCLTECH.NS",
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


def _day_open(acc: Account, ctx: Ctx) -> dict:
    """First price seen for each name today - the account's own record of the open."""
    day = ctx.t.date().isoformat()
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
    if room <= 0 or acc.cash < MIN_TICKET or sd < STATARB_MIN_SD:
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
