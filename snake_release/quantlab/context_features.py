"""Fourier cycles, probability profiles, and the world's mood: three new families of inputs.

FOURIER (per stock, 128-day window of daily log returns, strictly past data)
  fft_low_power     share of return variance in slow cycles (periods > 21 days):
                    high = trending, low = choppy / mean-reverting
  fft_entropy       spectral entropy: flat spectrum (noise) vs a few dominant cycles
  fft_dom_period    period in days of the strongest cycle
  fft_forecast_21   the three strongest harmonics of the de-trended log price,
                    extended 21 days forward: a pure cycle extrapolation

PROBABILITY (per stock, from its own past 252 days)
  prob_up_21        chance a 21-day holding period ended positive, shrunk toward
                    50% with a Beta(10, 10) prior so a short lucky run cannot dominate
  crash_prob        share of 21-day periods that lost more than 10%
  tail_prob         share of days with a move beyond 2.5 standard deviations
  kelly_edge        p * average win - (1 - p) * average loss, over average win

WORLD MOOD AND PSYCHOLOGY (one value per market and day; raw, not ranked, so the
trees can combine them with each stock's traits, e.g. high-beta names when fear jumps)
  ctx_vix, ctx_vix_chg21      US fear index (^VIX), level and one-month change
  ctx_indiavix, ctx_indiavix_chg21
  ctx_tone_7, ctx_tone_chg21  GDELT average news tone about the market's country
                              economy (India for IN, United States for US, world for
                              others), 7-day mean and one-month change
  ctx_conflict_7              GDELT tone of global war/conflict coverage, 7-day mean
Every context series is lagged one day: a day's news is only used the next session.
"""

from __future__ import annotations

import hashlib
import json
import logging
import time
import urllib.parse
from pathlib import Path

import numpy as np
import pandas as pd
import requests

log = logging.getLogger("quantlab.context")

FEATURE_COLS_FOURIER = ["fft_low_power", "fft_entropy", "fft_dom_period", "fft_forecast_21"]
FEATURE_COLS_PROB = ["prob_up_21", "crash_prob", "tail_prob", "kelly_edge"]
FEATURE_COLS_CTX = ["ctx_vix", "ctx_vix_chg21", "ctx_indiavix", "ctx_indiavix_chg21",
                    "ctx_tone_7", "ctx_tone_chg21", "ctx_conflict_7"]
CACHE = Path(r"C:\quantlab_data\raw\context")


# --- Fourier -------------------------------------------------------------------------------

def fourier_features(px: pd.DataFrame, dates: set, window: int = 128) -> pd.DataFrame:
    """Only computed on the grid dates the model samples, vectorised per stock."""
    out = []
    freqs = np.fft.rfftfreq(window)              # cycles per day
    low = (freqs > 0) & (freqs < 1 / 21)
    for sym, g in px.sort_values("date").groupby("symbol", sort=False):
        lp = np.log(g["adj_close"].to_numpy(dtype=float))
        if len(lp) <= window + 1:
            continue
        d = pd.to_datetime(g["date"]).to_numpy()
        idx = np.nonzero(np.isin(d, np.array(sorted(dates), dtype="datetime64[ns]")))[0]
        idx = idx[idx >= window]
        if not len(idx):
            continue
        r = np.diff(lp)                                   # r[i] = lp[i+1] - lp[i]
        W = np.stack([r[i - window:i] for i in idx])      # returns up to and including day i
        W = W - np.nanmean(W, axis=1, keepdims=True)
        W = np.nan_to_num(W)
        P = np.abs(np.fft.rfft(W, axis=1)) ** 2
        P[:, 0] = 0
        tot = P.sum(axis=1) + 1e-18
        pn = P / tot[:, None]
        ent = -(pn * np.log(pn + 1e-18)).sum(axis=1) / np.log(P.shape[1] - 1)
        dom = np.argmax(P, axis=1)
        # Harmonic extrapolation of the de-trended log price over the same window.
        L = np.stack([lp[i - window + 1:i + 1] for i in idx])
        t = np.arange(window)
        slope = np.polyfit(t, L.T, 1)
        resid = L - (slope[0][:, None] * t + slope[1][:, None])
        F = np.fft.rfft(resid, axis=1)
        keep = np.argsort(np.abs(F[:, 1:]), axis=1)[:, -3:] + 1
        mask = np.zeros_like(F, dtype=bool)
        np.put_along_axis(mask, keep, True, axis=1)
        Fk = np.where(mask, F, 0)
        tf = np.arange(window, window + 21)
        k = np.arange(F.shape[1])
        amp = Fk / window * 2
        wave = lambda tt: (amp[:, :, None] * np.exp(2j * np.pi * k[None, :, None] * tt[None, None, :] / window)).real.sum(axis=1)  # noqa: E731
        fut, now = wave(tf)[:, -1], wave(np.array([window - 1]))[:, 0]
        out.append(pd.DataFrame({
            "symbol": sym, "date": d[idx],
            "fft_low_power": P[:, low].sum(axis=1) / tot,
            "fft_entropy": ent,
            "fft_dom_period": np.where(dom > 0, window / np.maximum(dom, 1), np.nan),
            "fft_forecast_21": fut - now,
        }))
    return pd.concat(out, ignore_index=True) if out else pd.DataFrame(columns=["symbol", "date"] + FEATURE_COLS_FOURIER)


# --- probability -----------------------------------------------------------------------------

def probability_features(px: pd.DataFrame) -> pd.DataFrame:
    df = px.sort_values(["symbol", "date"]).reset_index(drop=True)
    g = df.groupby("symbol", sort=False)["adj_close"]
    r1 = g.pct_change()
    r21 = g.transform(lambda s: s / s.shift(21) - 1)          # 21-day return ENDING today (past)
    sym = df["symbol"]

    def roll(s, w=252, fn="mean", minp=120):
        return getattr(s.groupby(sym).rolling(w, min_periods=minp), fn)().reset_index(level=0, drop=True)

    up = (r21 > 0).astype(float).where(r21.notna())
    n = roll(up.notna().astype(float), fn="sum")
    k = roll(up, fn="sum")
    p = (k + 10) / (n + 20)
    df["prob_up_21"] = p
    df["crash_prob"] = roll((r21 < -0.10).astype(float).where(r21.notna()))
    sd = roll(r1, fn="std")
    df["tail_prob"] = roll((r1.abs() > 2.5 * sd.groupby(sym).shift(1)).astype(float).where(r1.notna()))
    win = roll(r21.where(r21 > 0))
    loss = roll((-r21).where(r21 < 0))
    df["kelly_edge"] = (p * win - (1 - p) * loss) / win.replace(0, np.nan)
    return df[["symbol", "date"] + FEATURE_COLS_PROB]


# --- world mood ---------------------------------------------------------------------------------

GDELT = "https://api.gdeltproject.org/api/v2/doc/doc"
QUERIES = {"IN": '"economy" sourcecountry:IN', "US": '"economy" sourcecountry:US',
           "WORLD": '"economy"', "CONFLICT": '(war OR conflict OR attack)'}


def _gdelt_tone(query: str, start: str = "20170101000000") -> pd.Series:
    # hash() is salted per process, so it cannot name a file a later run will find.
    cache = CACHE / f"gdelt_{hashlib.sha1(query.encode()).hexdigest()[:10]}.json"
    if cache.exists() and time.time() - cache.stat().st_mtime < 86400:
        d = json.loads(cache.read_text())
    else:
        end = pd.Timestamp.today().strftime("%Y%m%d000000")
        url = (f"{GDELT}?query={urllib.parse.quote(query)}&mode=timelinetone&format=json"
               f"&startdatetime={start}&enddatetime={end}")
        # A dead feed must not hold up the nightly build. Eight attempts with growing
        # pauses and a 90 second timeout could burn eighteen minutes on ONE query, and
        # there are several; on the night of 2026-09-25 that nearly cost the morning's
        # snapshot. Three quick attempts, then give up and remember the failure.
        miss = CACHE / f"{cache.stem}.missing"
        if miss.exists() and time.time() - miss.stat().st_mtime < 6 * 3600:
            log.info("GDELT skipped for %s (unavailable within the last few hours)", query)
            return pd.Series(dtype=float)
        d = None
        for attempt in range(3):
            try:
                r = requests.get(url, timeout=20)
                if r.status_code == 200:
                    d = r.json()
                    break
                time.sleep(5 * (attempt + 1))               # GDELT asks for one request per 5 s
            except (requests.RequestException, ValueError):
                time.sleep(5 * (attempt + 1))
        if d is None:
            log.warning("GDELT unavailable for %s", query)
            CACHE.mkdir(parents=True, exist_ok=True)
            miss.write_text("unavailable")
            return pd.Series(dtype=float)
        CACHE.mkdir(parents=True, exist_ok=True)
        cache.write_text(json.dumps(d))
        miss.unlink(missing_ok=True)
    pts = (d.get("timeline") or [{}])[0].get("data", [])
    s = pd.Series({pd.Timestamp(x["date"][:8]): float(x["value"]) for x in pts}).sort_index()
    return s.resample("D").mean()


def context_table(dates: pd.DatetimeIndex) -> pd.DataFrame:
    """Per (market group, date) context, each input lagged one day."""
    import yfinance as yf
    idx = pd.DatetimeIndex(sorted(set(pd.to_datetime(dates))))
    days = pd.date_range(idx.min() - pd.Timedelta(days=60), idx.max(), freq="D")
    vix = yf.download(["^VIX", "^INDIAVIX"], start=days.min(), end=days.max() + pd.Timedelta(days=1),
                      auto_adjust=True, progress=False)["Close"].reindex(days).ffill()
    base = pd.DataFrame(index=days)
    for col, name in (("^VIX", "ctx_vix"), ("^INDIAVIX", "ctx_indiavix")):
        s = vix[col].shift(1) if col in vix else pd.Series(np.nan, index=days)
        base[name] = s
        base[f"{name}_chg21"] = s / s.shift(21) - 1
    tones = {}
    for key, q in QUERIES.items():
        tones[key] = _gdelt_tone(q).reindex(days).shift(1)
        time.sleep(6)
    base["ctx_conflict_7"] = tones["CONFLICT"].rolling(7, min_periods=3).mean()
    rows = []
    for grp in ("IN", "US", "WORLD"):
        t = base.copy()
        tone7 = tones[grp].rolling(7, min_periods=3).mean()
        t["ctx_tone_7"] = tone7
        t["ctx_tone_chg21"] = tone7 - tone7.shift(21)
        t["group"] = grp
        rows.append(t.loc[t.index.isin(idx)].reset_index(names="date"))
    return pd.concat(rows, ignore_index=True)


def attach_context(df: pd.DataFrame) -> pd.DataFrame:
    ctx = context_table(pd.DatetimeIndex(df["date"].unique()))
    df = df.copy()
    df["group"] = np.where(df["market"].isin(["IN", "US"]), df["market"], "WORLD")
    out = df.merge(ctx, on=["group", "date"], how="left").drop(columns="group")
    return out
