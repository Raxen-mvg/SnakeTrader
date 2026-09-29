"""Signals from the published literature and quant-firm formula sets, daily OHLCV only.

Every value at date t uses prices up to and including t's close, the same
convention as price_features; labels start at t's close.

turnover-split reversal   Last month's return scaled by ABNORMAL turnover. Winners
                          bought on heavy volume keep going, thin-volume winners
                          revert (Lee and Swaminathan 2000; Medhat and Schmeling
                          2022, Review of Financial Studies).
information discreteness  Momentum built from many small moves persists; momentum
                          from a few jumps fades (Da, Gurun and Warachka 2014,
                          "Frog in the Pan", RFS). ID = sign(PRET) * (%neg - %pos).
residual momentum         Momentum of the stock's own returns after removing the
                          market's, scaled by its volatility (Blitz, Huij and
                          Martens 2011, Journal of Empirical Finance).
overnight vs intraday     Returns while the market is closed and while it is open
                          come from different traders and persist differently
                          (Lou, Polk and Skouras 2019, JFE).
Abdi-Ranaldo spread       Bid-ask spread estimated from close, high and low
                          (2017, RFS). A cost and an illiquidity premium signal.
Parkinson volatility      Range-based volatility, more efficient than close-to-close.
close location value      Where the close sits in the day's range, averaged.
WorldQuant 101 alphas     Kakushadze (2016), "101 Formulaic Alphas", Wilmott 84.
                          Only those needing daily OHLCV and volume: #6, #12, #33,
                          #54 and #101, each averaged over a month so they speak
                          to the 21-day horizon rather than to tomorrow.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

FEATURE_COLS_ALPHA = [
    "rev_x_abn_turnover", "info_discreteness", "resid_mom", "overnight_ret_21",
    "intraday_ret_21", "ar_spread_21", "parkinson_vol_21", "clv_21",
    "wq006_21", "wq012_21", "wq033_21", "wq054_21", "wq101_21",
]


def _roll(g, s: pd.Series, w: int, fn: str, minp: int | None = None) -> pd.Series:
    return getattr(s.groupby(g, observed=True).rolling(w, min_periods=minp or max(2, w // 2)), fn)() \
        .reset_index(level=0, drop=True)


def _rcorr(g, x: pd.Series, y: pd.Series, w: int, minp: int) -> pd.Series:
    """Rolling correlation per stock from rolling means (pandas' grouped rolling .corr
    misaligns when an index label repeats)."""
    x, y = x.astype(float), y.astype(float)
    both = x.notna() & y.notna()
    x, y = x.where(both), y.where(both)
    mx, my = _roll(g, x, w, "mean", minp), _roll(g, y, w, "mean", minp)
    cov = _roll(g, x * y, w, "mean", minp) - mx * my
    vx = _roll(g, x * x, w, "mean", minp) - mx * mx
    vy = _roll(g, y * y, w, "mean", minp) - my * my
    return cov / np.sqrt((vx * vy).clip(lower=0)).replace(0, np.nan)


def alpha_features(px: pd.DataFrame, bm: pd.DataFrame | None = None) -> pd.DataFrame:
    need = {"open", "high", "low"}
    df = px.sort_values(["symbol", "date"]).reset_index(drop=True)
    df["date"] = pd.to_datetime(df["date"])
    sym = df["symbol"]
    g = df.groupby("symbol", observed=True, sort=False)
    out = df[["symbol", "date"]].copy()

    ret = g["adj_close"].pct_change()
    logret = np.log1p(ret)

    # Turnover-split reversal: last month's return x how unusual its volume was.
    turn = np.log1p((df["close"] * df["volume"]).clip(lower=0))
    t21 = _roll(sym, turn, 21, "mean")
    t252 = _roll(sym, turn, 252, "mean", 120)
    ret21 = g["adj_close"].transform(lambda s: s / s.shift(21) - 1.0)
    out["rev_x_abn_turnover"] = ret21 * (t21 - t252)

    # Information discreteness over the 12-1 momentum window.
    pos = (ret > 0).astype(float).where(ret.notna())
    neg = (ret < 0).astype(float).where(ret.notna())
    frac_pos = _roll(sym, pos, 231, "mean", 150).groupby(sym, observed=True).shift(21)
    frac_neg = _roll(sym, neg, 231, "mean", 150).groupby(sym, observed=True).shift(21)
    pret = g["adj_close"].transform(lambda s: s.shift(21) / s.shift(252) - 1.0)
    out["info_discreteness"] = np.sign(pret) * (frac_neg - frac_pos)

    # Residual momentum: market-model residuals, t-252..t-21, over their volatility.
    if bm is not None and not bm.empty:
        b = bm[["date", "adj_close"]].copy()
        b["date"] = pd.to_datetime(b["date"])
        b = b.sort_values("date").assign(mret=lambda x: x["adj_close"].pct_change())[["date", "mret"]]
        m = df[["date"]].merge(b, on="date", how="left")["mret"].to_numpy()
        mret = pd.Series(m, index=df.index)
        cov = _roll(sym, ret * mret, 252, "mean", 150) - _roll(sym, ret, 252, "mean", 150) * _roll(sym, mret, 252, "mean", 150)
        var = _roll(sym, mret * mret, 252, "mean", 150) - _roll(sym, mret, 252, "mean", 150) ** 2
        beta = cov / var.replace(0, np.nan)
        resid = ret - beta.groupby(sym, observed=True).shift(1) * mret     # beta from before today
        rsum = _roll(sym, resid, 231, "sum", 150).groupby(sym, observed=True).shift(21)
        rstd = _roll(sym, resid, 231, "std", 150).groupby(sym, observed=True).shift(21)
        out["resid_mom"] = rsum / (rstd * np.sqrt(231)).replace(0, np.nan)

    if need <= set(df.columns):
        f = (df["adj_close"] / df["close"]).replace([np.inf, -np.inf], np.nan)   # adjustment factor
        o, h, l, c = (df[k] * f for k in ("open", "high", "low", "close"))
        valid = (h >= l) & (l > 0) & (o > 0)
        o, h, l, c = (x.where(valid) for x in (o, h, l, c))
        prev_c = c.groupby(sym, observed=True).shift(1)
        on = np.log(o / prev_c)
        intra = np.log(c / o)
        out["overnight_ret_21"] = _roll(sym, on, 21, "sum", 15)
        out["intraday_ret_21"] = _roll(sym, intra, 21, "sum", 15)

        # Abdi-Ranaldo with only past quantities: close t-1 against mids t-1 and t.
        lc, lh, ll = np.log(c), np.log(h), np.log(l)
        eta = (lh + ll) / 2
        lc_prev = lc.groupby(sym, observed=True).shift(1)
        eta_prev = eta.groupby(sym, observed=True).shift(1)
        prod = (lc_prev - eta_prev) * (lc_prev - eta)
        out["ar_spread_21"] = 2 * np.sqrt(_roll(sym, prod, 21, "mean", 15).clip(lower=0))

        out["parkinson_vol_21"] = np.sqrt(_roll(sym, (lh - ll) ** 2, 21, "mean", 15) / (4 * np.log(2)))
        rng_ = (h - l).replace(0, np.nan)
        out["clv_21"] = _roll(sym, ((c - l) - (h - c)) / rng_, 21, "mean", 15)

        vol = df["volume"].astype(float)
        # WQ #6: -corr(open, volume, 10)
        corr = _rcorr(sym, o, vol, 10, 8)
        out["wq006_21"] = _roll(sym, -corr, 21, "mean", 15)
        # WQ #12: sign(delta volume) * -(delta close), scaled by price to be comparable
        d_close = c.groupby(sym, observed=True).diff() / prev_c
        d_vol = vol.groupby(sym, observed=True).diff()
        out["wq012_21"] = _roll(sym, np.sign(d_vol) * -d_close, 21, "mean", 15)
        # WQ #33: -(1 - open/close)
        out["wq033_21"] = _roll(sym, -(1 - o / c), 21, "mean", 15)
        # WQ #54: -(low - close) * open^5 / ((low - high) * close^5)
        den = ((l - h) * c ** 5).replace(0, np.nan)
        out["wq054_21"] = _roll(sym, -((l - c) * o ** 5) / den, 21, "mean", 15)
        # WQ #101: (close - open) / (high - low + 0.001 * close)
        out["wq101_21"] = _roll(sym, (c - o) / (h - l + 0.001 * c), 21, "mean", 15)

    if need <= set(df.columns):
        out = out.join(qlib_features(df))

    for col in FEATURE_COLS_ALPHA:
        if col in out:
            out[col] = out[col].replace([np.inf, -np.inf], np.nan).astype("float32")
    return out


# --- Qlib Alpha158, the operators new to this model -------------------------------------
# Source: microsoft/qlib, qlib/contrib/data/loader.py (MIT licence). Formulas reimplemented
# from their published definitions. Every price feature is scaled by today's close, so
# values pool across currencies.

QLIB_WINDOWS = (5, 20, 60)
_QLIB_ROLL = ("ma", "rsqr", "resi", "rsv", "imxd", "cord", "cntd", "sumd", "vsumd", "wvma")
FEATURE_COLS_QLIB = (["q_kmid", "q_klen", "q_kmid2", "q_kup2", "q_klow2", "q_ksft2"]
                     + [f"q_{op}{d}" for op in _QLIB_ROLL for d in QLIB_WINDOWS])
FEATURE_COLS_ALPHA += FEATURE_COLS_QLIB


def _argmax_pos(x: np.ndarray, d: int, fn) -> np.ndarray:
    """Position (0..d-1, oldest first) of the max/min within each trailing window."""
    out = np.full(len(x), np.nan)
    if len(x) >= d:
        w = np.lib.stride_tricks.sliding_window_view(x, d)
        ok = ~np.isnan(w).any(axis=1)
        pos = np.full(len(w), np.nan)
        if ok.any():
            pos[ok] = fn(w[ok], axis=1)
        out[d - 1:] = pos
    return out


def qlib_features(df: pd.DataFrame) -> pd.DataFrame:
    """df sorted by symbol, date with open/high/low/close/adj_close/volume."""
    sym = df["symbol"]
    f = (df["adj_close"] / df["close"]).replace([np.inf, -np.inf], np.nan)
    o, h, l, c = (df[k] * f for k in ("open", "high", "low", "close"))
    v = df["volume"].astype(float)
    rng = (h - l) + 1e-12
    q = pd.DataFrame(index=df.index)
    q["q_kmid"] = (c - o) / o
    q["q_klen"] = (h - l) / o
    q["q_kmid2"] = (c - o) / rng
    q["q_kup2"] = (h - np.maximum(o, c)) / rng
    q["q_klow2"] = (np.minimum(o, c) - l) / rng
    q["q_ksft2"] = (2 * c - h - l) / rng

    g = lambda s: s.groupby(sym, observed=True)                     # noqa: E731
    prev_c = g(c).shift(1)
    dc = c - prev_c
    up, dn = dc.clip(lower=0), (-dc).clip(lower=0)
    dv = v - g(v).shift(1)
    vup, vdn = dv.clip(lower=0), (-dv).clip(lower=0)
    ret = c / prev_c - 1
    lvchg = np.log(v / g(v).shift(1).replace(0, np.nan) + 1)
    absrv = ret.abs() * v
    t = g(c).cumcount().astype(float)                               # time index within each stock

    for d in QLIB_WINDOWS:
        r = lambda s, fn: _roll(sym, s, d, fn, max(2, d // 2))       # noqa: E731
        q[f"q_ma{d}"] = r(c, "mean") / c
        mt, my = r(t, "mean"), r(c, "mean")
        cov = r(t * c, "mean") - mt * my
        vt = r(t * t, "mean") - mt * mt
        vy = r(c * c, "mean") - my * my
        slope = cov / vt.replace(0, np.nan)
        q[f"q_rsqr{d}"] = (cov * cov) / (vt * vy).replace(0, np.nan)
        q[f"q_resi{d}"] = (c - (my + slope * (t - mt))) / c
        hi, lo = r(h, "max"), r(l, "min")
        q[f"q_rsv{d}"] = (c - lo) / (hi - lo + 1e-12)
        imax = pd.Series(np.nan, index=df.index)
        imin = pd.Series(np.nan, index=df.index)
        for _, idx in df.groupby("symbol", observed=True, sort=False).groups.items():
            imax.loc[idx] = _argmax_pos(h.loc[idx].to_numpy(dtype=float), d, np.argmax)
            imin.loc[idx] = _argmax_pos(l.loc[idx].to_numpy(dtype=float), d, np.argmin)
        q[f"q_imxd{d}"] = (imax - imin) / d
        q[f"q_cord{d}"] = _rcorr(sym, ret, lvchg, d, max(3, d // 2))
        q[f"q_cntd{d}"] = r((dc > 0).astype(float).where(dc.notna()), "mean") \
            - r((dc < 0).astype(float).where(dc.notna()), "mean")
        tot = r(up, "sum") + r(dn, "sum") + 1e-12
        q[f"q_sumd{d}"] = (r(up, "sum") - r(dn, "sum")) / tot
        vtot = r(vup, "sum") + r(vdn, "sum") + 1e-12
        q[f"q_vsumd{d}"] = (r(vup, "sum") - r(vdn, "sum")) / vtot
        q[f"q_wvma{d}"] = r(absrv, "std") / (r(absrv, "mean") + 1e-12)
    return q.replace([np.inf, -np.inf], np.nan).astype("float32")
