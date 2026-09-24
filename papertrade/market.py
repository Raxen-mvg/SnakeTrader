"""Live NSE prices at the moment a paper trade happens.

Two free sources. Groww publishes the last traded price for an NSE symbol and is
effectively live, so it is asked first; Yahoo Finance is a few minutes behind and
fills in whatever Groww does not cover (indices, anything delisted from the site).
Fills take the price at the tick and then pay slippage, so a paper trade is priced
at what the market actually showed at that moment.

Groww also returns the day's circuit band for each stock. A price sitting at its
band is not something you could have traded, so quotes at a limit are marked and
the broker refuses to fill them - the mistake that made two earlier intraday
backtests look profitable.
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


GROWW_URL = "https://groww.in/v1/api/stocks_data/v1/tr_live_prices/exchange/NSE/segment/CASH/{}/latest"
GROWW_HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                               "(KHTML, like Gecko) Chrome/128.0 Safari/537.36",
                 "Accept": "application/json"}
BAND_TOUCH = 0.001            # within 0.1% of the band counts as stuck at the limit
AT_LIMIT: dict[str, str] = {}  # symbol -> "upper" or "lower", refreshed on every quote call


def groww_quotes(symbols: list[str]) -> dict[str, float]:
    """Last traded price straight from Groww for NSE symbols, and today's circuit bands.

    Only symbols that actually traded today are returned. Anything that fails, for any
    reason, is simply left out so the caller falls back to the slower feed.
    """
    import requests
    out: dict[str, float] = {}
    with requests.Session() as sess:
        sess.headers.update(GROWW_HEADERS)
        for sym in symbols:
            if not sym.endswith(".NS"):
                continue
            try:
                d = sess.get(GROWW_URL.format(sym[:-3]), timeout=8).json()
                ltp = float(d.get("ltp") or 0)
                if ltp <= 0 or not d.get("volume"):
                    continue
                out[sym] = ltp
                hi, lo = d.get("highPriceRange"), d.get("lowPriceRange")
                AT_LIMIT.pop(sym, None)
                if hi and ltp >= float(hi) * (1 - BAND_TOUCH):
                    AT_LIMIT[sym] = "upper"
                elif lo and ltp <= float(lo) * (1 + BAND_TOUCH):
                    AT_LIMIT[sym] = "lower"
            except Exception:                       # one bad symbol must not lose the rest
                continue
    return out


def at_circuit_limit(symbol: str) -> str | None:
    """"upper", "lower", or None - whether the last quote was stuck at a price band."""
    return AT_LIMIT.get(symbol)


def latest_prices(symbols: list[str], *, asof: dt.datetime | None = None) -> dict[str, float]:
    """Last traded price per symbol from today's 1-minute bars (delayed feed).

    A symbol with no bar today (holiday, suspended, circuit freeze with no
    trades) is left out, so a strategy cannot trade at a price that did not exist.
    """
    import yfinance as yf
    syms = sorted(set(symbols))
    if not syms:
        return {}
    live = {}
    if session_open(asof or now_ist()):
        try:
            live = groww_quotes(syms)
            log.info("live quotes from Groww for %d of %d symbols", len(live), len(syms))
        except Exception as exc:
            log.warning("live feed unavailable (%s); falling back to the delayed feed", exc)
    syms = [s for s in syms if s not in live]
    if not syms:
        return live
    for attempt in range(4):
        try:
            df = yf.download(syms, period="1d", interval="1m", group_by="ticker",
                             auto_adjust=False, progress=False, threads=True)
            break
        except Exception as exc:                      # network or rate limit
            log.warning("quote fetch failed (%s); retrying", exc)
            time.sleep(10 * (attempt + 1))
    else:
        return live
    out = dict(live)
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
