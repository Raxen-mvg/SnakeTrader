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


def intraday(acc: Account, ctx: Ctx) -> None:
    """With a trained intraday model: enter at 10:20 on its picks (it needs the first
    hour). Without one: enter at 09:30 on the daily model's picks."""
    today = ctx.t.date().isoformat()
    for s, p in list(acc.positions.items()):
        if p.opened[:10] < today and s in ctx.prices:     # a run was missed before yesterday's close
            acc.sell(s, ctx.prices[s], ctx.t, slippage_bps=SLIP_STOCK, reason="missed close; sold next session")
    if ctx.t.time() >= EXIT_INTRADAY:
        for s in list(acc.positions):
            if s in ctx.prices:
                acc.sell(s, ctx.prices[s], ctx.t, slippage_bps=SLIP_STOCK, reason="intraday close")
        return
    if acc.memo.get("last_entry") == today or acc.positions:
        return
    ipicks = getattr(ctx, "intraday_picks", None)
    if ipicks is not None:
        if ctx.t.time() < INTRADAY_MODEL_AFTER or not ipicks:
            return
        sub = Ctx(ctx.t, ctx.prices, ipicks, ctx.ranks, ctx.first)
        _buy_top(acc, sub, TOP_N, "intraday", reason="intraday model pick at 10:20")
    elif ctx.t.time() >= ENTRY_AFTER:
        _buy_top(acc, ctx, TOP_N, "intraday", reason="daily model pick (no intraday model yet)")
    else:
        return
    acc.memo["last_entry"] = today


def _exit_due(acc: Account, ctx: Ctx, reason: str) -> None:
    for s, p in list(acc.positions.items()):
        if p.exit_on and ctx.t.date().isoformat() >= p.exit_on and s in ctx.prices:
            acc.sell(s, ctx.prices[s], ctx.t, slippage_bps=SLIP_STOCK, reason=reason)


def intraweek(acc: Account, ctx: Ctx) -> None:
    if ctx.t.time() < ENTRY_AFTER:
        return
    _exit_due(acc, ctx, "5 trading days elapsed")
    if not _entered_today(acc, ctx.t) and not acc.positions:
        _buy_top(acc, ctx, TOP_N, "delivery", exit_on=trading_days_ahead(ctx.t.date(), 5).isoformat())
        acc.memo["last_entry"] = ctx.t.date().isoformat()


def intramonth(acc: Account, ctx: Ctx) -> None:
    """Hold winners: keep a name while the model ranks it in its top 25%."""
    if ctx.t.time() < ENTRY_AFTER or _entered_today(acc, ctx.t):
        return
    for s in list(acc.positions):
        if ctx.ranks and ctx.ranks.get(s, 0.0) < 0.75 and s in ctx.prices:
            acc.sell(s, ctx.prices[s], ctx.t, slippage_bps=SLIP_STOCK, reason="fell out of the top 25%")
    if len(acc.positions) < TOP_N:
        _buy_top(acc, ctx, TOP_N, "delivery")
    acc.memo["last_entry"] = ctx.t.date().isoformat()


def random_hold(acc: Account, ctx: Ctx) -> None:
    if ctx.t.time() < ENTRY_AFTER or _entered_today(acc, ctx.t):
        return
    _exit_due(acc, ctx, "random holding period elapsed")
    rng = random.Random(ctx.t.date().toordinal())
    if len(acc.positions) < TOP_N:
        _buy_top(acc, ctx, TOP_N, "delivery",
                 exit_on=lambda p: trading_days_ahead(ctx.t.date(), rng.randint(2, 40)).isoformat())
    acc.memo["last_entry"] = ctx.t.date().isoformat()


def gold(acc: Account, ctx: Ctx) -> None:
    s = "GOLDBEES.NS"
    if not acc.positions and s in ctx.prices and ctx.t.time() >= ENTRY_AFTER:
        acc.buy(s, acc.cash, ctx.prices[s], ctx.t, "delivery", slippage_bps=SLIP_ETF, reason="gold held")


def gold_trend(acc: Account, ctx: Ctx) -> None:
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


def benchmark(acc: Account, ctx: Ctx) -> None:
    s = "NIFTYBEES.NS"
    if not acc.positions and s in ctx.prices and ctx.t.time() >= ENTRY_AFTER:
        acc.buy(s, acc.cash, ctx.prices[s], ctx.t, "delivery", slippage_bps=SLIP_ETF, reason="benchmark held")


STRATEGIES = {
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
