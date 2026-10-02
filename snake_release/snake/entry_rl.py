"""ANACONDA's entry, learned: buy this stock now, or wait a session for a better price?

The owner's request (2026-10-02): no hand-set "1% dip" threshold - the entry decision itself should be
trained, the way the Vipers' exit is. For a stock SNAKE ranks among its best, each session offers two
actions. Buying now is the reference (value 0). Waiting one session costs that session's move: if the
price rises r, buying tomorrow costs r more, so

  Q(wait, day j) = -r_j + gamma x max(0, Q(wait, day j+1))      for j < K-1
  Q(wait, day K-1) = -r_{K-1}                                   (after K sessions it must buy)

where r_j is the stock's return over the session a purchase decided on day j would first be exposed
to (fwd_ret_1: from the entry close onwards). Fitted Q-iteration with LightGBM learns Q(wait) from
every past top pick's next K sessions; the policy buys when waiting is not expected to pay (Q <= 0).
No threshold is chosen by hand.

Inputs: the stock's short-term state (snake/entry_timing.py: reversal, close location, distance from
its short and long averages, recent jumps, overnight versus intraday drift, volume trend, volatility),
SNAKE's own view (expected return, ranks at every horizon) and the market's state.
Trained walk-forward a year at a time with a 20-day embargo.
"""

from __future__ import annotations

import time

import numpy as np
import pandas as pd

from snake import entry_timing as A
from snake.model import HORIZONS

K = 5
GAMMA = 0.999
PASSES = 6
TOP = 20
EVERY = 2
EMBARGO_DAYS = 20
FIRST_YEAR = 2015
FEATURES = A.FEATURES


def log(msg: str) -> None:
    print(f"{time.strftime('%H:%M:%S')} anaconda-rl {msg}", flush=True)


def panel(o: pd.DataFrame, stock: pd.DataFrame, mkt: pd.DataFrame, symbols: set) -> pd.DataFrame:
    """Every row of the given symbols with the entry features and next-session return."""
    from snake.exit_model import expected_table
    E = expected_table(o).rename(columns={"exp": "expected"})
    r = o[o["symbol"].isin(symbols)][["symbol", "date"] + [f"p{h}" for h in HORIZONS] + ["fwd_ret_1"]].copy()
    allr = o[["symbol", "date"] + [f"p{h}" for h in HORIZONS]]
    for h in HORIZONS:
        rk = allr.groupby("date")[f"p{h}"].rank(pct=True)
        r[f"rank_p{h}"] = rk.reindex(r.index)
    r = r.merge(E, on=["symbol", "date"], how="left").merge(stock, on=["symbol", "date"], how="left")
    r = r.merge(mkt[["date"] + A.MKT_COLS], on="date", how="left")
    return r.sort_values(["symbol", "date"]).reset_index(drop=True)


def episodes(o: pd.DataFrame, P: pd.DataFrame) -> pd.DataFrame:
    """For the top TOP names every EVERY sessions: their next K sessions as one waiting episode."""
    from snake.exit_model import expected_table
    E = expected_table(o)
    dates = sorted(E["date"].unique())[::EVERY]
    starts = (E[E["date"].isin(set(dates))].sort_values("exp", ascending=False)
              .groupby("date").head(TOP)[["symbol", "date"]])
    pos = {(s, d): i for i, (s, d) in enumerate(zip(P["symbol"], P["date"]))}
    rows = []
    for ep, (s, d) in enumerate(zip(starts["symbol"], starts["date"])):
        i = pos.get((s, d))
        if i is None:
            continue
        for j in range(K):
            k = i + j
            if k >= len(P) or P.at[k, "symbol"] != s:
                break
            rows.append((ep, j, k))
    e = pd.DataFrame(rows, columns=["ep", "step", "row"])
    e = e.join(P[["symbol", "date", "fwd_ret_1"] + FEATURES], on="row")
    e["r"] = e["fwd_ret_1"].clip(-0.2, 0.2)
    last = e.groupby("ep")["step"].transform("max")
    e["terminal"] = e["step"] == last
    e["next"] = np.where(e["terminal"], -1, np.arange(len(e)) + 1)
    return e.dropna(subset=["r"]).reset_index(drop=True)


def fit_q(e: pd.DataFrame, seed: int = 42):
    import lightgbm as lgb
    X = e[FEATURES]
    nxt = e["next"].to_numpy()
    q_next = np.zeros(len(e))
    model = None
    for _ in range(PASSES):
        target = -e["r"].to_numpy() + GAMMA * np.where(nxt >= 0, np.maximum(q_next, 0.0), 0.0)
        model = lgb.LGBMRegressor(n_estimators=250, learning_rate=0.04, num_leaves=15, min_child_samples=200,
                                  subsample=0.8, subsample_freq=1, colsample_bytree=0.8, reg_lambda=5.0,
                                  random_state=seed, verbose=-1)
        model.fit(X, np.clip(target, -0.3, 0.3))
        q = model.predict(X)
        q_next = np.where(nxt >= 0, q[np.maximum(nxt, 0)], 0.0)
    return model


def wait_scores(o, stock, mkt) -> pd.Series:
    """Q(wait) for every top-TOP name on every session, walk-forward by year. Positive = wait."""
    from snake.exit_model import expected_table
    E = expected_table(o)
    daily = E.sort_values("exp", ascending=False).groupby("date").head(TOP)[["symbol", "date"]]
    syms = set(daily["symbol"])
    P = panel(o, stock, mkt, syms)
    e = episodes(o, P)
    log(f"{e['ep'].nunique():,} waiting episodes, {len(e):,} steps; mean next-session move {e['r'].mean():+.3%}")
    score_on = daily.merge(P, on=["symbol", "date"], how="left")
    out = []
    for y in sorted(score_on["date"].dt.year.unique()):
        if y < FIRST_YEAR:
            continue
        cut = pd.Timestamp(f"{y}-01-01") - pd.Timedelta(days=EMBARGO_DAYS)
        tr = e[e["date"] < cut].reset_index(drop=True)
        same = (tr["ep"].shift(-1) == tr["ep"]) & (tr["step"].shift(-1) == tr["step"] + 1)
        tr["next"] = np.where(same, np.arange(len(tr)) + 1, -1)
        if len(tr) < 5_000:
            continue
        m = fit_q(tr)
        te = score_on[score_on["date"].dt.year == y]
        out.append(pd.Series(m.predict(te[FEATURES]), index=pd.MultiIndex.from_arrays([te["symbol"], te["date"]])))
    log(f"wait scores for {len(out)} years")
    return pd.concat(out) if out else pd.Series(dtype=float)


ENTRY_ACCOUNTS = ("snake_anaconda",)
LIVE_TOP = 30


def train_production(oos_path: str, model_dir: str) -> None:
    """The learned entry for the live ANACONDA account, on every year, saved beside the entry model."""
    import json
    import duckdb
    from snake import calendar as C
    o = pd.read_parquet(oos_path)
    o = o[o["date"] >= "2013-01-01"]
    con = duckdb.connect(r"C:\quantlab_data\daily_in.duckdb", read_only=True)
    stock = con.execute(f"SELECT symbol, date, {', '.join(A.STOCK_COLS)} FROM features_daily").df()
    con.close()
    stock["date"] = pd.to_datetime(stock["date"])
    prices = C.load_prices()
    mkt = C.market_features(prices)
    from snake.exit_model import expected_table
    E = expected_table(o)
    syms = set(E.sort_values("exp", ascending=False).groupby("date").head(TOP)["symbol"])
    e = episodes(o, panel(o, stock, mkt, syms))
    same = (e["ep"].shift(-1) == e["ep"]) & (e["step"].shift(-1) == e["step"] + 1)
    e["next"] = np.where(same, np.arange(len(e)) + 1, -1)
    m = fit_q(e)
    from pathlib import Path
    out = Path(model_dir)
    m.booster_.save_model(str(out / "entry_q.txt"))
    (out / "entry_meta.json").write_text(json.dumps({
        "features": FEATURES, "rule": "wait while Q(wait) > 0", "max_wait_sessions": K,
        "steps": int(len(e)), "trained_through": str(e["date"].max().date()),
        "built": time.strftime("%Y-%m-%d %H:%M"), "from_oos": Path(oos_path).name}, indent=1))
    log(f"production entry model: {len(e):,} steps -> {out / 'entry_q.txt'}")


def live_wait(model_dir, today: pd.DataFrame, p: pd.DataFrame, best: pd.Series) -> dict:
    """Q(wait) for today's top LIVE_TOP names. today: the scored feature rows (raw columns kept)."""
    import json
    from pathlib import Path
    import lightgbm as lgb
    md = Path(model_dir)
    if not (md / "entry_q.txt").exists():
        return {}
    meta = json.loads((md / "entry_meta.json").read_text())
    booster = lgb.Booster(model_file=str(md / "entry_q.txt"))
    top = best.sort_values(ascending=False).index[:LIVE_TOP]
    t = today.set_index("symbol")
    X = pd.DataFrame(index=top)
    X["expected"] = best.reindex(top).values
    for h in HORIZONS:
        X[f"rank_p{h}"] = p[f"p{h}"].rank(pct=True).reindex(top).values
    for c in A.STOCK_COLS + A.MKT_COLS:
        X[c] = t[c].reindex(top).values if c in t.columns else np.nan
    q = booster.predict(X[meta["features"]])
    return {"entry_wait": {s: round(float(v), 5) for s, v in zip(top, q)},
            "entry_rule": meta["rule"], "entry_model_built": meta["built"]}
