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
# Sleeve sizes come from what was measured, not from taste. The 21-day book is the
# only part with a tested edge (top-decile hit 54-56%, positive net excess), so it
# gets most of the money. Gold is there because it is the one holding uncorrelated
# with the equity book. Intraday is capped hard and only fires above 55% confidence:
# at the old 45% floor it lost money after charges, both in the backtest and live.
GOLD_SYMBOL = "GOLDBEES.NS"
ORACLE_CORE, ORACLE_HEDGE, ORACLE_TRADE = 0.75, 0.10, 0.15
ORACLE_NAMES = 8
ORACLE_EXIT_RANK = 0.75
ORACLE_MIN_PROB = 0.55


def _sleeve(acc: Account, ctx: Ctx, which: str) -> float:
    """Rupees currently held in one sleeve of a multi-sleeve account."""
    total = 0.0
    for s, pos in acc.positions.items():
        kind = "hedge" if s == GOLD_SYMBOL else ("trade" if pos.product == "intraday" else "core")
        if kind == which:
            total += pos.qty * ctx.prices.get(s, pos.avg_price)
    return total


def oracle(acc: Account, ctx: Ctx) -> None:
    """Rs 50,000, one pot of cash, the whole model deciding what to do with it.

    Three sleeves: the medium-horizon picks (75%), a gold hedge (10%), and an
    intraday sleeve (15%) that is always flat before the close. Each sleeve is
    topped up only to its share of current equity, so a winning sleeve is not
    allowed to quietly take over the account.
    """
    if ctx.t.time() < ENTRY_AFTER:
        return
    equity = acc.equity(ctx.prices)

    # Intraday sleeve.
    if ctx.t.time() >= EXIT_INTRADAY:
        for s, pos in list(acc.positions.items()):
            if pos.product == "intraday" and s in ctx.prices:
                acc.sell(s, ctx.prices[s], ctx.t, slippage_bps=SLIP_STOCK, reason="intraday hard exit")
    else:
        ipicks = getattr(ctx, "intraday_picks", None) or []
        wanted = {p["symbol"]: p for p in ipicks if p.get("score", 0) >= ORACLE_MIN_PROB}
        for s, pos in list(acc.positions.items()):
            if pos.product != "intraday" or s not in ctx.prices:
                continue
            move = ctx.prices[s] / pos.avg_price - 1
            if move >= TAKE_PROFIT:
                acc.sell(s, ctx.prices[s], ctx.t, slippage_bps=SLIP_STOCK, reason=f"target hit {100 * move:+.2f}%")
            elif move <= STOP_LOSS:
                acc.sell(s, ctx.prices[s], ctx.t, slippage_bps=SLIP_STOCK, reason=f"stop loss {100 * move:+.2f}%")
            elif s not in wanted:
                acc.sell(s, ctx.prices[s], ctx.t, slippage_bps=SLIP_STOCK, reason=f"model dropped it {100 * move:+.2f}%")
        room = min(acc.cash, ORACLE_TRADE * equity - _sleeve(acc, ctx, "trade"))
        if ctx.t.time() >= INTRADAY_MODEL_AFTER and room >= MIN_TICKET:
            fresh = [p for s, p in wanted.items() if s not in acc.positions and s in ctx.prices]
            fresh = fresh[:max(1, int(room // MIN_TICKET))]
            if fresh:
                each = room / len(fresh)
                for p in fresh:
                    acc.buy(p["symbol"], each, ctx.prices[p["symbol"]], ctx.t, "intraday",
                            slippage_bps=SLIP_STOCK,
                            reason=f"intraday sleeve, confidence {100 * p.get('score', 0):.0f}%")

    # Gold hedge.
    need = ORACLE_HEDGE * equity - _sleeve(acc, ctx, "hedge")
    if GOLD_SYMBOL in ctx.prices and need >= MIN_TICKET and acc.cash >= MIN_TICKET:
        acc.buy(GOLD_SYMBOL, min(need, acc.cash), ctx.prices[GOLD_SYMBOL], ctx.t, "delivery",
                slippage_bps=SLIP_ETF, reason="gold hedge, 10% of the account")

    # Core book: hold while the model still ranks it in the top 25%.
    for s, pos in list(acc.positions.items()):
        if pos.product == "intraday" or s == GOLD_SYMBOL:
            continue
        if ctx.ranks and ctx.ranks.get(s, 0.0) < ORACLE_EXIT_RANK and s in ctx.prices:
            acc.sell(s, ctx.prices[s], ctx.t, slippage_bps=SLIP_STOCK, reason="fell out of the top 25%")
    core = [s for s, pos in acc.positions.items() if pos.product != "intraday" and s != GOLD_SYMBOL]
    budget = min(acc.cash, ORACLE_CORE * equity - _sleeve(acc, ctx, "core"))
    if len(core) >= ORACLE_NAMES or budget < MIN_TICKET:
        return
    fresh = [p for p in ctx.picks
             if p["symbol"] not in acc.positions
             and ctx.ranks.get(p["symbol"], p.get("rank_pct", 1.0)) >= ORACLE_EXIT_RANK][:ORACLE_NAMES - len(core)]
    _buy_weighted(acc, ctx, fresh, "delivery", budget=budget, reason="oracle core, sized by confidence")


STRATEGIES["oracle"] = oracle      # defined below the table, so registered here
