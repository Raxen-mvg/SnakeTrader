"""Live (slightly delayed) NSE prices at the moment a paper trade happens.

Free source: Yahoo Finance through yfinance, typically a few minutes behind
the exchange. Fills use the latest 1-minute bar at the time of the tick, then
add slippage, so a paper trade is priced at what the market showed right then.
"""

from __future__ import annotations

import datetime as dt
import logging
import time
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

log = logging.getLogger("papertrade.market")
IST = ZoneInfo("Asia/Kolkata")
OPEN, CLOSE = dt.time(9, 15), dt.time(15, 30)


def now_ist() -> dt.datetime:
    return dt.datetime.now(IST)


def session_open(t: dt.datetime) -> bool:
    return t.weekday() < 5 and OPEN <= t.time() <= CLOSE


def latest_prices(symbols: list[str], *, asof: dt.datetime | None = None) -> dict[str, float]:
    """Last traded price per symbol from today's 1-minute bars (delayed feed).

    A symbol with no bar today (holiday, suspended, circuit freeze with no
    trades) is left out, so a strategy cannot trade at a price that did not exist.
    """
    import yfinance as yf
    syms = sorted(set(symbols))
    if not syms:
        return {}
    for attempt in range(4):
        try:
            df = yf.download(syms, period="1d", interval="1m", group_by="ticker",
                             auto_adjust=False, progress=False, threads=True)
            break
        except Exception as exc:                      # network or rate limit
            log.warning("quote fetch failed (%s); retrying", exc)
            time.sleep(10 * (attempt + 1))
    else:
        return {}
    out = {}
    today = (asof or now_ist()).date()
    for s in syms:
        try:
            x = (df[s] if len(syms) > 1 else df).dropna(subset=["Close"])
        except KeyError:
            continue
        if x.empty:
            continue
        ts = x.index[-1]
        ts = ts.tz_convert(IST) if ts.tzinfo else ts.tz_localize("UTC").tz_convert(IST)
        if ts.date() != today:
            continue
        out[s] = float(x["Close"].iloc[-1])
    return out


def daily_closes(symbols: list[str], days: int = 400) -> pd.DataFrame:
    """Adjusted daily closes, for trend rules and volatility estimates."""
    import yfinance as yf
    df = yf.download(sorted(set(symbols)), period=f"{days}d", interval="1d",
                     auto_adjust=True, progress=False, threads=True)["Close"]
    return df if isinstance(df, pd.DataFrame) else df.to_frame(symbols[0])


def slippage(price: float, side: str, bps: float) -> float:
    """Pay up when buying, receive less when selling."""
    return price * (1 + bps / 1e4) if side == "buy" else price * (1 - bps / 1e4)


def annual_vol(closes: pd.Series, window: int = 60) -> float:
    r = np.log(closes).diff().dropna().tail(window)
    return float(r.std() * np.sqrt(252)) if len(r) > 10 else 0.2
