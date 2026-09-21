"""Intraday model: at 10:15 IST, rank stocks by expected return for the rest of the day.

Trained on free hourly bars (Yahoo keeps about two years of 60-minute data).
Everything the model sees is known at 10:15: the overnight gap, the first
hour's move and volume, recent days' behaviour and the whole market's first
hour. The label is the return from the 10:15 bar's close to the day's close,
minus that day's average across stocks (so the model learns relative moves,
not the market's direction).

Validation is walk-forward by month with a one-day gap, and results are
reported after intraday costs, because at this speed slippage is the
difference between a good-looking model and a losing one.
"""

from __future__ import annotations

import glob
import os
from pathlib import Path

import numpy as np
import pandas as pd

from .market import IST

RAW = Path(r"C:\quantlab_data\raw\intraday\60m")
FEATURES = ["gap", "first_hr_ret", "first_hr_vol_ratio", "prev_ret", "prev_intraday",
            "prev_range", "ret_5d", "ret_20d", "vol_20d", "dist_20d_high",
            "mkt_gap", "mkt_first_hr", "rel_first_hr", "first_hr_range"]
ROUND_TRIP_COST = 0.0006 + 2 * 0.0015      # Zerodha intraday charges + 0.15% slippage each way


def load_bars(path: Path = RAW) -> pd.DataFrame:
    frames = []
    for f in glob.glob(str(path / "*.parquet")):
        sym = os.path.basename(f)[:-8]
        x = pd.read_parquet(f)
        x.columns = [c if isinstance(c, str) else c[-1] for c in x.columns]
        x = x.rename(columns=str.lower)[["open", "high", "low", "close", "volume"]].dropna(subset=["close"])
        idx = x.index.tz_convert(IST) if x.index.tz is not None else x.index.tz_localize("UTC").tz_convert(IST)
        x.index = idx
        x["symbol"] = sym
        frames.append(x)
    df = pd.concat(frames).reset_index(names="ts")
    df["date"] = df["ts"].dt.date
    return df


def daily_table(bars: pd.DataFrame) -> pd.DataFrame:
    """One row per stock-day with features known at 10:15 and the rest-of-day label."""
    b = bars.sort_values(["symbol", "ts"])
    g = b.groupby(["symbol", "date"], sort=False)
    day = g.agg(open=("open", "first"), high=("high", "max"), low=("low", "min"),
                close=("close", "last"), n=("close", "size")).reset_index()
    first = b[b["ts"].dt.time < pd.Timestamp("10:15").time()]
    fh = first.groupby(["symbol", "date"]).agg(fh_close=("close", "last"), fh_high=("high", "max"),
                                               fh_low=("low", "min"), fh_vol=("volume", "sum")).reset_index()
    d = day.merge(fh, on=["symbol", "date"], how="inner").sort_values(["symbol", "date"])
    s = d.groupby("symbol", sort=False)
    prev_close = s["close"].shift(1)
    d["gap"] = d["open"] / prev_close - 1
    d["first_hr_ret"] = d["fh_close"] / d["open"] - 1
    d["first_hr_range"] = (d["fh_high"] - d["fh_low"]) / d["open"]
    d["first_hr_vol_ratio"] = np.log1p(d["fh_vol"]) - s["fh_vol"].transform(
        lambda v: np.log1p(v).shift(1).rolling(20, min_periods=10).mean())
    d["prev_ret"] = prev_close / s["close"].shift(2) - 1
    d["prev_intraday"] = s["close"].shift(1) / s["open"].shift(1) - 1
    d["prev_range"] = (s["high"].shift(1) - s["low"].shift(1)) / prev_close
    d["ret_5d"] = prev_close / s["close"].shift(6) - 1
    d["ret_20d"] = prev_close / s["close"].shift(21) - 1
    dr = s["close"].pct_change()
    d["vol_20d"] = dr.groupby(d["symbol"]).transform(lambda r: r.shift(1).rolling(20, min_periods=10).std())
    d["dist_20d_high"] = prev_close / s["high"].transform(lambda h: h.shift(1).rolling(20, min_periods=10).max()) - 1
    d["label_ret"] = d["close"] / d["fh_close"] - 1          # 10:15 -> close
    mkt = d[d["symbol"] == "^NSEI"][["date", "gap", "first_hr_ret"]].rename(
        columns={"gap": "mkt_gap", "first_hr_ret": "mkt_first_hr"})
    d = d[~d["symbol"].str.startswith("^")].merge(mkt, on="date", how="left")
    d["rel_first_hr"] = d["first_hr_ret"] - d["mkt_first_hr"]
    d["label_excess"] = d["label_ret"] - d.groupby("date")["label_ret"].transform("mean")
    d["label_rank"] = d.groupby("date")["label_excess"].rank(pct=True)
    return d.replace([np.inf, -np.inf], np.nan)


def walk_forward(d: pd.DataFrame, min_train_months: int = 6, seed: int = 42) -> pd.DataFrame:
    import lightgbm as lgb
    d = d.dropna(subset=["label_rank"]).copy()
    d["month"] = pd.to_datetime(d["date"]).dt.to_period("M")
    months = sorted(d["month"].unique())
    preds = []
    for i, m in enumerate(months):
        if i < min_train_months:
            continue
        test = d[d["month"] == m]
        cutoff = pd.Timestamp(test["date"].min()) - pd.Timedelta(days=1)    # one-day gap
        train = d[pd.to_datetime(d["date"]) < cutoff]
        model = lgb.LGBMRegressor(n_estimators=300, learning_rate=0.03, num_leaves=31,
                                  min_child_samples=200, subsample=0.8, subsample_freq=1,
                                  colsample_bytree=0.8, random_state=seed, verbose=-1, n_jobs=8)
        model.fit(train[FEATURES], train["label_rank"])
        t = test[["symbol", "date", "label_ret", "label_excess"]].copy()
        t["prediction"] = model.predict(test[FEATURES])
        preds.append(t)
    return pd.concat(preds, ignore_index=True) if preds else pd.DataFrame()


def evaluate(p: pd.DataFrame, top: int = 5) -> dict:
    p = p.copy()
    ic = p.groupby("date").apply(lambda g: g["prediction"].corr(g["label_excess"], method="spearman"))
    p["pos"] = p.groupby("date")["prediction"].rank(ascending=False, method="first")
    t = p[p["pos"] <= top]
    per_day = t.groupby("date")["label_ret"].mean()
    mkt = p.groupby("date")["label_ret"].mean()
    return {"days": int(p["date"].nunique()), "mean_ic": float(ic.mean()),
            "ic_t": float(ic.mean() / ic.std() * np.sqrt(len(ic))),
            "top_hit_vs_avg": float((t["label_excess"] > 0).mean()),
            "top_avg_ret": float(per_day.mean()), "market_avg_ret": float(mkt.mean()),
            "top_net_after_costs": float(per_day.mean() - ROUND_TRIP_COST),
            "days_net_positive": float((per_day - ROUND_TRIP_COST > 0).mean())}


def live_picks(model_file: Path, universe: list[str], top: int = 5) -> list[dict]:
    """Score today's cross-section after the first hour, from live hourly bars."""
    import lightgbm as lgb
    import yfinance as yf
    syms = sorted(set(universe) | {"^NSEI"})
    raw = yf.download(syms, period="40d", interval="60m", group_by="ticker",
                      auto_adjust=False, progress=False, threads=True)
    frames = []
    for s in syms:
        try:
            x = raw[s].dropna(subset=["Close"]).rename(columns=str.lower)
        except KeyError:
            continue
        x.index = x.index.tz_convert(IST) if x.index.tz is not None else x.index.tz_localize("UTC").tz_convert(IST)
        x = x[["open", "high", "low", "close", "volume"]].copy()
        x["symbol"] = s
        frames.append(x)
    if not frames:
        return []
    bars = pd.concat(frames).reset_index(names="ts")
    bars["date"] = bars["ts"].dt.date
    d = daily_table(bars)
    today = d["date"].max()
    t = d[d["date"] == today].dropna(subset=["first_hr_ret"])
    if t.empty:
        return []
    booster = lgb.Booster(model_file=str(model_file))
    t = t.assign(score=booster.predict(t[FEATURES])).sort_values("score", ascending=False)
    return [{"symbol": r.symbol, "score": float(r.score), "rank_pct": 1.0} for r in t.head(top).itertuples()]


def fit_final(d: pd.DataFrame, out: Path, seed: int = 42) -> Path:
    import lightgbm as lgb
    d = d.dropna(subset=["label_rank"])
    model = lgb.LGBMRegressor(n_estimators=300, learning_rate=0.03, num_leaves=31, min_child_samples=200,
                              subsample=0.8, subsample_freq=1, colsample_bytree=0.8,
                              random_state=seed, verbose=-1, n_jobs=8)
    model.fit(d[FEATURES], d["label_rank"])
    out.parent.mkdir(parents=True, exist_ok=True)
    model.booster_.save_model(str(out))
    syms = sorted(s for s in d["symbol"].unique() if not s.startswith("^"))
    (out.parent / "intraday_universe.json").write_text(__import__("json").dumps(syms))
    return out
