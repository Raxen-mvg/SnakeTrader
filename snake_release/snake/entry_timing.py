"""ANACONDA's entry timing: SNAKE says WHAT to buy; this says whether TODAY is the day to buy it.

The mirror of the Vipers' trained exit. For every name SNAKE ranks among its best, a model learns what
the next few sessions usually hold for a purchase made now: if the stock is expected to get cheaper over
the next 1, 3 or 5 sessions, it is better to wait and buy the dip; if not, buy today.

Inputs are the stock's short-term state at the close the decision is made: its last five sessions'
reversal, where it closed in the day's range (q_kmid, q_rsv5, clv_21), its distance from its five- and
fifty-session averages, the size of its recent largest jump, overnight versus intraday drift, volume
trend, volatility, SNAKE's own ranks at every horizon, and the market's state.

The target for each horizon k is the return from the entry close (the session after the decision) over
the next k sessions - fwd_ret_k, the same numbers the book trades on. The timing signal is the LOWEST
of the three predictions: the deepest dip the model expects ahead. Trained walk-forward a year at a time
with a 20-day embargo on the top twenty names of every other session.

Daily granularity only: the history is daily closes back to 2005; minute data exists for a few weeks.
"""

from __future__ import annotations

import time

import numpy as np
import pandas as pd

from snake.model import HORIZONS

TOP = 20
EVERY = 2
GRID = (1, 3, 5)
EMBARGO_DAYS = 20
FIRST_YEAR = 2015
STOCK_COLS = ["reversal_5d", "mom_1m", "vol_21d", "px_to_ma50", "volume_trend", "max_ret_21d",
              "attention_5d", "overnight_ret_21", "intraday_ret_21", "clv_21", "q_kmid", "q_klen",
              "q_ma5", "q_rsv5", "q_imxd5", "q_cntd5", "q_sumd5"]
MKT_COLS = ["mkt_ret_5", "mkt_ret_21", "mkt_ret_63", "mkt_above_200", "mkt_breadth_50", "mkt_vol_21"]
FEATURES = ["expected"] + [f"rank_p{h}" for h in HORIZONS] + STOCK_COLS + MKT_COLS


def log(msg: str) -> None:
    print(f"{time.strftime('%H:%M:%S')} anaconda {msg}", flush=True)


def candidates(o: pd.DataFrame, stock: pd.DataFrame, mkt: pd.DataFrame, every: int = EVERY) -> pd.DataFrame:
    from snake.exit_model import expected_table
    E = expected_table(o)
    r = o[["symbol", "date"] + [f"p{h}" for h in HORIZONS] + [f"fwd_ret_{k}" for k in GRID]].copy()
    for h in HORIZONS:
        r[f"rank_p{h}"] = r.groupby("date")[f"p{h}"].rank(pct=True)
    dates = sorted(E["date"].unique())[::every]
    top = (E[E["date"].isin(set(dates))].sort_values("exp", ascending=False)
           .groupby("date").head(TOP).rename(columns={"exp": "expected"}))
    t = top.merge(r, on=["symbol", "date"], how="left").merge(stock, on=["symbol", "date"], how="left")
    return t.merge(mkt[["date"] + MKT_COLS], on="date", how="left")


def dip_scores(train: pd.DataFrame, score_on: pd.DataFrame, seed: int = 42) -> pd.Series:
    """For every (symbol, date) in score_on: the lowest predicted return over the next 1, 3 and 5
    sessions after entry, from models trained only on earlier years."""
    import lightgbm as lgb
    out = []
    for y in sorted(score_on["date"].dt.year.unique()):
        if y < FIRST_YEAR:
            continue
        cut = pd.Timestamp(f"{y}-01-01") - pd.Timedelta(days=EMBARGO_DAYS)
        tr = train[train["date"] < cut]
        if len(tr) < 3_000:
            continue
        te = score_on[score_on["date"].dt.year == y]
        preds = []
        for k in GRID:
            d = tr.dropna(subset=[f"fwd_ret_{k}"])
            m = lgb.LGBMRegressor(n_estimators=300, learning_rate=0.03, num_leaves=15,
                                  min_child_samples=100, subsample=0.8, subsample_freq=1,
                                  colsample_bytree=0.8, reg_lambda=5.0, random_state=seed, verbose=-1)
            m.fit(d[FEATURES], d[f"fwd_ret_{k}"].clip(-0.3, 0.3))
            preds.append(m.predict(te[FEATURES]))
        out.append(pd.Series(np.min(np.column_stack(preds), axis=1),
                             index=pd.MultiIndex.from_arrays([te["symbol"], te["date"]])))
    log(f"dip scores for {len(out)} years")
    return pd.concat(out) if out else pd.Series(dtype=float)
