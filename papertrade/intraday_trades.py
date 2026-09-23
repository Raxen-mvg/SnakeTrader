"""Learn which same-day trades succeed: buy at one hour, sell at a later hour, win only if it pays after costs.

Every stock, every day, every entry hour and every later exit hour in the free
hourly history (Yahoo keeps about two years) is one example trade. It is a
SUCCESS if its return after the full round-trip cost clears a "decent profit"
bar; otherwise it is a failure. A classifier learns the probability of success
from what was known at the moment of entry (the day so far, yesterday, the
whole market so far, the time of day and the planned holding time).

Used as a trade filter: only take the trades the model is most confident in.
Walk-forward by month, so every test month is scored by a model that never saw it.
"""

from __future__ import annotations

import glob
import os
from pathlib import Path

import numpy as np
import pandas as pd

from .market import IST

RAW = Path(r"C:\quantlab_data\raw\intraday\60m")
CHARGES = 0.0006                    # Zerodha intraday brokerage, taxes and fees, round trip
COST = CHARGES + 2 * 0.0015         # reference cost for a liquid name
DECENT = 0.002                      # success = at least +0.20% after costs
FEATURES = ["ret_so_far", "gap", "last_bar_ret", "range_so_far", "pos_in_range", "vol_ratio_so_far",
            "prev_ret", "prev_intraday", "ret_5d", "vol_20d", "mkt_so_far", "mkt_last_bar",
            "rel_so_far", "entry_bar", "hold_bars"]


def load(symbols: list[str] | None = None) -> pd.DataFrame:
    files = glob.glob(str(RAW / "*.NS.parquet")) + [str(RAW / "^NSEI.parquet")]
    frames = []
    for f in files:
        sym = os.path.basename(f)[:-8]
        if symbols and sym not in symbols and sym != "^NSEI":
            continue
        # SME-platform listings (-SM, -ST) trade in lots, barely trade at all, and
        # cannot be bought at the screen price: they are not tradeable candidates.
        if sym.endswith(("-SM.NS", "-ST.NS")):
            continue
        if not os.path.exists(f):
            continue
        x = pd.read_parquet(f)
        x.columns = [c if isinstance(c, str) else c[-1] for c in x.columns]
        x = x.rename(columns=str.lower)[["open", "high", "low", "close", "volume"]].dropna(subset=["close"])
        x.index = x.index.tz_convert(IST) if x.index.tz is not None else x.index.tz_localize("UTC").tz_convert(IST)
        x["symbol"] = sym
        frames.append(x)
    b = pd.concat(frames).reset_index(names="ts").sort_values(["symbol", "ts"])
    b["date"] = b["ts"].dt.date
    b["bar"] = b.groupby(["symbol", "date"]).cumcount()
    return b


def entry_table(b: pd.DataFrame) -> pd.DataFrame:
    """One row per stock-day-bar with everything known at that bar's close."""
    g = b.groupby(["symbol", "date"], sort=False)
    b = b.copy()
    b["day_open"] = g["open"].transform("first")
    b["hi_so_far"] = g["high"].cummax()
    b["lo_so_far"] = g["low"].cummin()
    b["cumvol"] = g["volume"].cumsum()
    b["turnover_day"] = (b["close"] * b["volume"]).groupby([b["symbol"], b["date"]]).transform("sum")
    day = g.agg(d_open=("open", "first"), d_close=("close", "last")).reset_index()
    s = day.groupby("symbol", sort=False)
    day["prev_close"] = s["d_close"].shift(1)
    day["prev_ret"] = day["prev_close"] / s["d_close"].shift(2) - 1
    day["prev_intraday"] = s["d_close"].shift(1) / s["d_open"].shift(1) - 1
    day["ret_5d"] = day["prev_close"] / s["d_close"].shift(6) - 1
    dret = s["d_close"].pct_change()
    day["vol_20d"] = dret.groupby(day["symbol"]).transform(lambda r: r.shift(1).rolling(20, min_periods=10).std())
    b = b.merge(day[["symbol", "date", "prev_close", "prev_ret", "prev_intraday", "ret_5d", "vol_20d"]],
                on=["symbol", "date"], how="left")
    b["ret_so_far"] = b["close"] / b["day_open"] - 1
    b["gap"] = b["day_open"] / b["prev_close"] - 1
    b["last_bar_ret"] = b["close"] / b.groupby(["symbol", "date"])["close"].shift(1).fillna(b["day_open"]) - 1
    b["range_so_far"] = (b["hi_so_far"] - b["lo_so_far"]) / b["day_open"]
    b["pos_in_range"] = (b["close"] - b["lo_so_far"]) / (b["hi_so_far"] - b["lo_so_far"]).replace(0, np.nan)
    # Volume so far today against the average volume by the same bar over the prior 20 days.
    norm = b.groupby(["symbol", "bar"])["cumvol"].transform(lambda v: v.shift(1).rolling(20, min_periods=5).mean())
    b["vol_ratio_so_far"] = np.log1p(b["cumvol"]) - np.log1p(norm)
    mkt = b[b["symbol"] == "^NSEI"][["date", "bar", "ret_so_far", "last_bar_ret"]].rename(
        columns={"ret_so_far": "mkt_so_far", "last_bar_ret": "mkt_last_bar"})
    b = b[b["symbol"] != "^NSEI"].merge(mkt, on=["date", "bar"], how="left")
    b["rel_so_far"] = b["ret_so_far"] - b["mkt_so_far"]
    b["entry_bar"] = b["bar"]
    return b.replace([np.inf, -np.inf], np.nan)


MIN_TURNOVER = 5e7          # Rs 5 crore average daily turnover: enough to trade a small position
MAX_MOVE = 0.20             # a same-day move beyond this is a data error, not a trade
SLIP_BY_TURNOVER = [(5e8, 0.0010), (2e8, 0.0020), (0.0, 0.0035)]   # each way, by liquidity


def tradeable(e: pd.DataFrame) -> pd.DataFrame:
    """Keep only names liquid enough to trade, and attach a realistic slippage."""
    day_turn = e.groupby(["symbol", "date"])["turnover_day"].first().reset_index()
    day_turn["avg20"] = (day_turn.groupby("symbol")["turnover_day"]
                         .transform(lambda s: s.shift(1).rolling(20, min_periods=10).mean()))
    e = e.merge(day_turn[["symbol", "date", "avg20"]], on=["symbol", "date"], how="left")
    e = e[(e["avg20"] >= MIN_TURNOVER) & (e["close"] >= 20)]
    slip = pd.Series(SLIP_BY_TURNOVER[-1][1], index=e.index)
    for thr, s in SLIP_BY_TURNOVER[:-1]:
        slip = slip.mask(e["avg20"] >= thr, s)
    e = e.assign(slippage=slip)
    return e


def trades(e: pd.DataFrame, max_hold: int = 5) -> pd.DataFrame:
    """Every (entry bar, later exit bar) pair in the same day, with its net result."""
    out = []
    closes = e.pivot_table(index=["symbol", "date"], columns="bar", values="close")
    for h in range(1, max_hold + 1):
        exit_px = closes.shift(-h, axis=1).stack().rename("exit_close")
        t = e.merge(exit_px.reset_index(), on=["symbol", "date", "bar"], how="inner")
        t["hold_bars"] = h
        out.append(t)
    t = pd.concat(out, ignore_index=True)
    gross = t["exit_close"] / t["close"] - 1
    t["net"] = gross - CHARGES - 2 * t.get("slippage", pd.Series(0.0015, index=t.index))
    t = t[gross.abs() <= MAX_MOVE]          # drop corrupt bars: one bad row moved the average from +1.4% to +55%
    t["success"] = (t["net"] > DECENT).astype(int)
    return t.dropna(subset=["net"])


def walk_forward(t: pd.DataFrame, min_train_months: int = 6, seed: int = 42,
                 max_train_rows: int = 3_000_000) -> pd.DataFrame:
    import lightgbm as lgb
    t = t.copy()
    t["month"] = pd.to_datetime(t["date"]).dt.to_period("M")
    months = sorted(t["month"].unique())
    rng = np.random.default_rng(seed)
    preds = []
    for i, m in enumerate(months):
        if i < min_train_months:
            continue
        test = t[t["month"] == m]
        train = t[pd.to_datetime(t["date"]) < pd.Timestamp(test["date"].min()) - pd.Timedelta(days=1)]
        if len(train) > max_train_rows:
            train = train.iloc[rng.choice(len(train), max_train_rows, replace=False)]
        clf = lgb.LGBMClassifier(n_estimators=300, learning_rate=0.03, num_leaves=31, min_child_samples=500,
                                 subsample=0.8, subsample_freq=1, colsample_bytree=0.8,
                                 random_state=seed, verbose=-1, n_jobs=8)
        clf.fit(train[FEATURES], train["success"])
        p = test[["symbol", "date", "entry_bar", "hold_bars", "net", "success"]].copy()
        p["prob"] = clf.predict_proba(test[FEATURES])[:, 1]
        preds.append(p)
    return pd.concat(preds, ignore_index=True)


def evaluate(p: pd.DataFrame) -> pd.DataFrame:
    """Take only the most confident trades; how often do they succeed and what do they earn?"""
    rows = [{"rule": "all trades (base rate)", "trades_per_day": p.groupby("date").size().mean(),
             "success_rate": p["success"].mean(), "avg_net": p["net"].mean(),
             "median_net": p["net"].median()}]
    for thr in (0.3, 0.4, 0.5, 0.6):
        s = p[p["prob"] >= thr]
        if len(s):
            rows.append({"rule": f"probability >= {thr:.0%}", "trades_per_day": s.groupby("date").size().mean(),
                         "success_rate": s["success"].mean(), "avg_net": s["net"].mean(),
                         "median_net": s["net"].median(), "days_with_trades": s["date"].nunique()})
    for k in (1, 3, 5):
        s = p.sort_values("prob", ascending=False).groupby("date").head(k)
        per_day = s.groupby("date")["net"].mean()
        rows.append({"rule": f"best {k} per day", "trades_per_day": k, "success_rate": s["success"].mean(),
                     "avg_net": s["net"].mean(), "median_net": s["net"].median(),
                     "days_profitable": (per_day > 0).mean()})
    return pd.DataFrame(rows)
