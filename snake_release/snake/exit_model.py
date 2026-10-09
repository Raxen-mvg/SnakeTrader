"""A trained exit for SNAKE: hold this stock, or sell it and buy today's best fresh pick?

The entry network only ever learned which stocks will do well. Selling was a fixed rule on top of
it. This model learns the selling decision itself, from every position the book would have held
since 2013, one row per position per session:

  state       sessions held, gain since entry, best gain since entry and the fall from it, what
              the network expected at entry and what it expects now, how much better the best
              fresh names look, where the stock now ranks at every horizon, and the market's state
  target      over the next ten sessions, the held stock's return minus the average return of the
              three best names not held, plus the cost of switching - positive means holding paid

All of it is known at the close of the day the decision is made: gains are measured on closes up
to that day, and the target starts at the next close, when a sale would execute. It is trained
walk-forward a year at a time on positions dated at least thirty days before the year it is used
in, so its target never reaches into that year.

In the book it sells a holding when the model says switching beats holding by more than a margin,
on top of every existing exit (the disaster stop, the expected-return floor).

Usage (research): python -m snake.exit_model --oos cache/snake_oos_india_abs.parquet
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import numpy as np
import pandas as pd

from snake import book
from snake.model import HORIZONS

HORIZON = 10
SWITCH = book.BUY_PCT + book.SELL_PCT + 2 * book.DP_FEE / 33_000
EMBARGO_DAYS = 30
FIRST_YEAR = 2015
FEATURES = (["age", "log_age", "gain", "peak_gain", "from_peak", "entry_exp", "expected",
             "exp_drop", "fresh_exp", "fresh_gap"] + [f"rank_p{h}" for h in HORIZONS]
            + ["mkt_ret_5", "mkt_ret_21", "mkt_ret_63", "mkt_above_200", "mkt_breadth_50",
               "mkt_vol_21"])


def log(msg: str) -> None:
    print(f"{time.strftime('%H:%M:%S')} exit {msg}", flush=True)


class Context:
    """Everything the state features need, prepared once: closes, ranks, market state."""

    def __init__(self, o: pd.DataFrame, prices: pd.DataFrame, mkt: pd.DataFrame):
        px = prices[prices["symbol"].isin(set(o["symbol"]))].sort_values(["symbol", "date"])
        self.close = {s: g.set_index("date")["adj_close"] for s, g in px.groupby("symbol")}
        r = o[["symbol", "date"] + [f"p{h}" for h in HORIZONS]].copy()
        for h in HORIZONS:
            r[f"rank_p{h}"] = r.groupby("date")[f"p{h}"].rank(pct=True)
        self.ranks = r.set_index(["symbol", "date"])[[f"rank_p{h}" for h in HORIZONS]]
        self.mkt = mkt.set_index("date")
        self.fwd = o.set_index(["symbol", "date"])[f"fwd_ret_{HORIZON}"]

    def path(self, sym: str, entry: pd.Timestamp, now: pd.Timestamp) -> tuple[float, float]:
        """Gain since the entry close (the session after the signal) up to now, and its best."""
        s = self.close.get(sym)
        if s is None:
            return 0.0, 0.0
        seg = s[(s.index > entry) & (s.index <= now)]
        if seg.empty:
            return 0.0, 0.0
        base = seg.iloc[0]
        g = seg / base - 1.0
        return float(g.iloc[-1]), float(max(g.max(), 0.0))

    def features(self, states: list[dict], now: pd.Timestamp, fresh_exp: float) -> pd.DataFrame:
        rows = []
        m = self.mkt.loc[now] if now in self.mkt.index else None
        for st in states:
            gain, peak = self.path(st["symbol"], st["entry"], now)
            row = {"age": st["age"], "log_age": np.log1p(st["age"]), "gain": gain,
                   "peak_gain": peak, "from_peak": (1 + gain) / (1 + peak) - 1,
                   "entry_exp": st["entry_exp"], "expected": st["expected"],
                   "exp_drop": st["entry_exp"] - st["expected"], "fresh_exp": fresh_exp,
                   "fresh_gap": fresh_exp - st["expected"]}
            key = (st["symbol"], now)
            rk = self.ranks.loc[key] if key in self.ranks.index else None
            for h in HORIZONS:
                row[f"rank_p{h}"] = float(rk[f"rank_p{h}"]) if rk is not None else np.nan
            for c in ["mkt_ret_5", "mkt_ret_21", "mkt_ret_63", "mkt_above_200", "mkt_breadth_50",
                      "mkt_vol_21"]:
                row[c] = float(m[c]) if m is not None and pd.notna(m[c]) else np.nan
            rows.append(row)
        return pd.DataFrame(rows, columns=FEATURES)


def training_rows(o: pd.DataFrame, ctx: Context, sizing_power: float = 0.0) -> pd.DataFrame:
    """Walk the ordinary book once and record every held position's state and its target."""
    trace: list = []
    book.simulate(o, sizing_power=sizing_power, first_session=True, trace=trace)
    t = pd.DataFrame(trace)
    log(f"{len(t):,} position-sessions from the ordinary book")
    feats = []
    for dt, g in t.groupby("date", sort=True):
        f = ctx.features(g.to_dict("records"), dt, float(g["fresh_exp"].iloc[0]))
        f.index = g.index
        feats.append(f)
    t = t.drop(columns=["age", "expected", "entry_exp", "fresh_exp"]).join(pd.concat(feats))
    held = [ctx.fwd.get((s, d), np.nan) for s, d in zip(t["symbol"], t["date"])]
    fresh = []
    for syms, d in zip(t["fresh_syms"], t["date"]):
        v = [ctx.fwd.get((s, d), np.nan) for s in syms.split(",") if s]
        v = [x for x in v if pd.notna(x)]
        fresh.append(np.mean(v) if v else np.nan)
    t["held_fwd"] = np.clip(held, -0.5, 1.0)
    t["fresh_fwd"] = np.clip(fresh, -0.5, 1.0)
    t["target"] = t["held_fwd"] - t["fresh_fwd"] + SWITCH
    return t.dropna(subset=["target"])


def expected_table(o: pd.DataFrame) -> pd.DataFrame:
    """Every (symbol, date)'s expected return, calibrated exactly as the book does it."""
    years = sorted(o["date"].dt.year.unique())
    cal = {y: book.calibrate(o[o["date"] < pd.Timestamp(f"{y}-01-01")]) for y in years}
    parts = []
    for dt, g in o.groupby("date", sort=True):
        e = book.expected(g.set_index("symbol"), cal[dt.year])
        parts.append(pd.DataFrame({"symbol": e.index, "date": dt, "exp": e.values}))
    return pd.concat(parts, ignore_index=True)


def counterfactual_rows(o: pd.DataFrame, ctx: Context, every: int = 5, top: int = 10,
                        max_age: int = 126) -> pd.DataFrame:
    """Hypothetical positions: the top names every `every` sessions, each followed for up to
    max_age sessions whatever happens. Far more varied than the one path the ordinary book took,
    which only ever held names for months."""
    E = expected_table(o)
    dates = list(pd.DatetimeIndex(sorted(E["date"].unique())))
    pos_of = {d: i for i, d in enumerate(dates)}
    top3 = E.sort_values("exp", ascending=False).groupby("date").head(3)
    fresh_exp = top3.groupby("date")["exp"].mean()
    fwd = o.set_index(["symbol", "date"])[f"fwd_ret_{HORIZON}"].clip(-0.5, 1.0)
    top3 = top3.assign(f=[fwd.get((s, d), np.nan) for s, d in zip(top3["symbol"], top3["date"])])
    fresh_fwd = top3.groupby("date")["f"].mean()
    exp_idx = E.set_index(["symbol", "date"])["exp"]

    rows = []
    for i in range(0, len(dates), every):
        d0 = dates[i]
        picks = E[E["date"] == d0].nlargest(top, "exp")
        for sym, e0 in zip(picks["symbol"], picks["exp"]):
            s = ctx.close.get(sym)
            if s is None:
                continue
            seg = s[s.index > d0].iloc[:max_age + 1]
            if len(seg) < 3:
                continue
            g = seg.to_numpy() / seg.iloc[0] - 1.0
            peak = np.maximum.accumulate(np.maximum(g, 0.0))
            for k in range(1, len(seg)):
                d = seg.index[k]
                if d not in pos_of:
                    continue
                rows.append((sym, d0, d, k, g[k], peak[k], e0))
    t = pd.DataFrame(rows, columns=["symbol", "entry", "date", "age", "gain", "peak_gain", "entry_exp"])
    log(f"{len(t):,} hypothetical position-sessions from {len(range(0, len(dates), every)):,} entry days")
    t["log_age"] = np.log1p(t["age"])
    t["from_peak"] = (1 + t["gain"]) / (1 + t["peak_gain"]) - 1
    t["expected"] = [exp_idx.get((s, d), np.nan) for s, d in zip(t["symbol"], t["date"])]
    t["exp_drop"] = t["entry_exp"] - t["expected"]
    t["fresh_exp"] = t["date"].map(fresh_exp)
    t["fresh_gap"] = t["fresh_exp"] - t["expected"]
    t = t.merge(ctx.ranks.reset_index(), on=["symbol", "date"], how="left")
    t = t.merge(ctx.mkt.reset_index()[["date", "mkt_ret_5", "mkt_ret_21", "mkt_ret_63",
                                       "mkt_above_200", "mkt_breadth_50", "mkt_vol_21"]],
                on="date", how="left")
    t["held_fwd"] = [fwd.get((s, d), np.nan) for s, d in zip(t["symbol"], t["date"])]
    t["fresh_fwd"] = t["date"].map(fresh_fwd)
    t["target"] = t["held_fwd"] - t["fresh_fwd"] + SWITCH
    return t.dropna(subset=["target", "expected"])


def fit_by_year(rows: pd.DataFrame, years: list[int], seed: int = 42) -> dict:
    """One LightGBM per year, trained only on positions dated well before that year."""
    import lightgbm as lgb
    models = {}
    for y in years:
        cut = pd.Timestamp(f"{y}-01-01") - pd.Timedelta(days=EMBARGO_DAYS)
        tr = rows[rows["date"] < cut]
        if len(tr) < 2_000 or y < FIRST_YEAR:
            continue
        m = lgb.LGBMRegressor(n_estimators=300, learning_rate=0.03, num_leaves=15,
                              min_child_samples=200, subsample=0.8, subsample_freq=1,
                              colsample_bytree=0.8, reg_lambda=5.0, random_state=seed, verbose=-1)
        m.fit(tr[FEATURES], tr["target"].clip(-0.3, 0.3))
        models[y] = m
    log(f"exit models for {sorted(models)}")
    return models


class Policy:
    """The book's exit_policy: sell where the model says switching beats holding by a margin."""

    def __init__(self, models: dict, ctx: Context, margin: float = 0.0, min_age: int = 3):
        self.models, self.ctx, self.margin, self.min_age = models, ctx, margin, min_age

    def __call__(self, dt, states, fresh) -> list[str]:
        m = self.models.get(dt.year)
        if m is None or not states:
            return []
        fresh_exp = float(fresh.mean()) if fresh is not None and len(fresh) else 0.0
        X = self.ctx.features(states, dt, fresh_exp)
        pred = m.predict(X)
        return [st["symbol"] for st, p in zip(states, pred)
                if st["age"] >= self.min_age and p < -self.margin]


# --- any-horizon exit (2026-10-01, the owner's framing) ------------------------------------------
# "Will holding this make me more, or is this the most it will give me?" - asked at every horizon
# the entry model knows, not over one fixed window. For each H, the target is the held stock's return
# over the next H sessions minus that of the best fresh names, plus the whole cost of switching. A
# holding is sold only when switching wins at EVERY horizon: no later point is expected to pay more
# than taking the money now. It may sell from the first session after the purchase settles.
GRID = (5, 10, 21, 63)
EMBARGO_MULTI_DAYS = 100           # longer than the 63-session target, in calendar days


def multi_targets(t: pd.DataFrame, o: pd.DataFrame, E_top3: pd.DataFrame) -> pd.DataFrame:
    """Add target_H for every H in GRID to rows that have symbol and date."""
    for h in GRID:
        fwd = o.set_index(["symbol", "date"])[f"fwd_ret_{h}"].clip(-0.5, 2.0)
        f3 = E_top3.assign(f=[fwd.get((s_, d), np.nan) for s_, d in zip(E_top3["symbol"], E_top3["date"])])
        fresh = f3.groupby("date")["f"].mean()
        held = np.array([fwd.get((s_, d), np.nan) for s_, d in zip(t["symbol"], t["date"])])
        t[f"target_{h}"] = held - t["date"].map(fresh).to_numpy() + SWITCH
    return t


def counterfactual_rows_multi(o: pd.DataFrame, ctx: Context) -> pd.DataFrame:
    t = counterfactual_rows(o, ctx)
    E = expected_table(o)
    top3 = E.sort_values("exp", ascending=False).groupby("date").head(3)
    t = multi_targets(t, o, top3)
    return t


def fit_by_year_multi(rows: pd.DataFrame, years: list[int], seed: int = 42) -> dict:
    """{year: {H: model}}, each trained only on positions whose longest target ends before the year."""
    import lightgbm as lgb
    models = {}
    for y in years:
        if y < FIRST_YEAR:
            continue
        cut = pd.Timestamp(f"{y}-01-01") - pd.Timedelta(days=EMBARGO_MULTI_DAYS)
        tr = rows[rows["date"] < cut]
        if len(tr) < 2_000:
            continue
        models[y] = {}
        for h in GRID:
            d = tr.dropna(subset=[f"target_{h}"])
            m = lgb.LGBMRegressor(n_estimators=300, learning_rate=0.03, num_leaves=15,
                                  min_child_samples=200, subsample=0.8, subsample_freq=1,
                                  colsample_bytree=0.8, reg_lambda=5.0, random_state=seed, verbose=-1)
            m.fit(d[FEATURES], d[f"target_{h}"].clip(-0.5, 0.5))
            models[y][h] = m
    log(f"any-horizon exit models for {sorted(models)}")
    return models


class PolicyMulti:
    """Sell when switching beats holding at every horizon by more than margin; no waiting period
    beyond the session the purchase settles in."""

    def __init__(self, models: dict, ctx: Context, margin: float = 0.0, min_age: int = 1):
        self.models, self.ctx, self.margin, self.min_age = models, ctx, margin, min_age

    def __call__(self, dt, states, fresh) -> list[str]:
        ms = self.models.get(dt.year)
        if not ms or not states:
            return []
        fresh_exp = float(fresh.mean()) if fresh is not None and len(fresh) else 0.0
        X = self.ctx.features(states, dt, fresh_exp)
        best = np.max(np.column_stack([ms[h].predict(X) for h in GRID]), axis=1)
        return [st["symbol"] for st, p in zip(states, best)
                if st["age"] >= self.min_age and p < -self.margin]


EXIT_ACCOUNTS = ("snake_abs_exit", "snake_abs_exit_conv", "snake_anaconda", "snake_viper_wild")
DEFAULT_RULE = {"margin": 0.02, "min_age": 10}


def train_production(oos_path: str, model_dir: str, rule: dict | None = None) -> str:
    """One exit model on every year, for the live accounts, saved beside the entry model."""
    import json
    import lightgbm as lgb
    from snake import calendar as C
    o = pd.read_parquet(oos_path)
    o = o[o["date"] >= "2013-01-01"]
    prices = C.load_prices()
    ctx = Context(o, prices, C.market_features(prices))
    rows = counterfactual_rows(o, ctx)
    m = lgb.LGBMRegressor(n_estimators=300, learning_rate=0.03, num_leaves=15, min_child_samples=200,
                          subsample=0.8, subsample_freq=1, colsample_bytree=0.8, reg_lambda=5.0,
                          random_state=42, verbose=-1)
    m.fit(rows[FEATURES], rows["target"].clip(-0.3, 0.3))
    out = Path(model_dir)
    m.booster_.save_model(str(out / "exit_model.txt"))
    (out / "exit_meta.json").write_text(json.dumps({
        "features": FEATURES, "horizon": HORIZON, "rule": rule or DEFAULT_RULE,
        "rows": int(len(rows)), "trained_through": str(rows["date"].max().date()),
        "built": time.strftime("%Y-%m-%d %H:%M"), "from_oos": Path(oos_path).name}, indent=1))
    log(f"production exit model: {len(rows):,} rows -> {out / 'exit_model.txt'}")
    return str(out / "exit_model.txt")


def train_production_multi(oos_path: str, model_dir: str, margin: float = 0.0) -> None:
    """The any-horizon exit for the live accounts: one model per horizon, on every year."""
    import json
    import lightgbm as lgb
    from snake import calendar as C
    o = pd.read_parquet(oos_path)
    o = o[o["date"] >= "2013-01-01"]
    prices = C.load_prices()
    ctx = Context(o, prices, C.market_features(prices))
    rows = counterfactual_rows_multi(o, ctx)
    out = Path(model_dir)
    for h in GRID:
        d = rows.dropna(subset=[f"target_{h}"])
        m = lgb.LGBMRegressor(n_estimators=300, learning_rate=0.03, num_leaves=15, min_child_samples=200,
                              subsample=0.8, subsample_freq=1, colsample_bytree=0.8, reg_lambda=5.0,
                              random_state=42, verbose=-1)
        m.fit(d[FEATURES], d[f"target_{h}"].clip(-0.5, 0.5))
        m.booster_.save_model(str(out / f"exit_model_h{h}.txt"))
    (out / "exit_meta.json").write_text(json.dumps({
        "features": FEATURES, "horizons": list(GRID), "rule": {"margin": margin, "min_age": 1},
        "question": "does holding beat switching to the best fresh names, after every fee, at ANY horizon?",
        "rows": int(len(rows)), "trained_through": str(rows["date"].max().date()),
        "built": time.strftime("%Y-%m-%d %H:%M"), "from_oos": Path(oos_path).name}, indent=1))
    log(f"any-horizon production exit: {len(rows):,} rows, horizons {list(GRID)} -> {out}")


def live_scores(model_dir, p: pd.DataFrame, expected: pd.Series, panel: pd.DataFrame,
                market: dict, accounts: dict, asof: pd.Timestamp) -> dict:
    """Exit scores for every held name of every exit account, for the next session.

    p        today's raw predictions, one column per horizon (p1 ... p63), indexed by symbol
    panel    the price panel the features were built from (symbol, date, adj_close)
    accounts {account: {symbol: position dict from accounts.json}}
    Returns {account: {symbol: {"pred", "age"}}} and the rule, so the trader only compares.
    """
    import json
    import lightgbm as lgb
    md = Path(model_dir)
    if not (md / "exit_meta.json").exists():
        return {}
    meta = json.loads((md / "exit_meta.json").read_text())
    if meta.get("horizons"):                    # any-horizon exit: the best horizon decides
        boosters = [lgb.Booster(model_file=str(md / f"exit_model_h{h}.txt")) for h in meta["horizons"]]
    else:
        boosters = [lgb.Booster(model_file=str(md / "exit_model.txt"))]
    ranks = {h: p[f"p{h}"].rank(pct=True) for h in HORIZONS}
    px = panel.copy()
    px["date"] = pd.to_datetime(px["date"])
    close = {s: g.set_index("date")["adj_close"].sort_index() for s, g in px.groupby("symbol")}
    out = {}
    for acc, positions in accounts.items():
        held = list(positions)
        fresh = expected.drop(labels=[s for s in held if s in expected.index]).nlargest(3)
        fresh_exp = float(fresh.mean()) if len(fresh) else 0.0
        rows, keys = [], []
        for sym, pos in positions.items():
            s = close.get(sym)
            if s is None or sym not in expected.index:
                continue
            opened = pd.Timestamp(str(pos.get("opened") or pos.get("entry_time") or asof)[:10])
            seg = s[(s.index >= opened) & (s.index <= asof)]
            if seg.empty:
                continue
            g = seg / seg.iloc[0] - 1.0
            age = int((seg.index > opened).sum()) + 1
            gain, peak = float(g.iloc[-1]), float(max(g.max(), 0.0))
            e_now = float(expected[sym])
            e0 = float((pos.get("meta") or {}).get("entry_exp", e_now))
            r = {"age": age, "log_age": np.log1p(age), "gain": gain, "peak_gain": peak,
                 "from_peak": (1 + gain) / (1 + peak) - 1, "entry_exp": e0, "expected": e_now,
                 "exp_drop": e0 - e_now, "fresh_exp": fresh_exp, "fresh_gap": fresh_exp - e_now}
            for h in HORIZONS:
                r[f"rank_p{h}"] = float(ranks[h].get(sym, np.nan))
            for c in ["mkt_ret_5", "mkt_ret_21", "mkt_ret_63", "mkt_above_200", "mkt_breadth_50",
                      "mkt_vol_21"]:
                r[c] = market.get(c, np.nan)
            rows.append(r)
            keys.append((sym, age))
        if rows:
            X = pd.DataFrame(rows, columns=meta["features"])
            pred = np.max(np.column_stack([b.predict(X) for b in boosters]), axis=1)
            out[acc] = {s: {"pred": round(float(v), 5), "age": a} for (s, a), v in zip(keys, pred)}
    return {"exit_scores": out, "exit_rule": meta["rule"], "exit_model_built": meta["built"]}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--oos", required=True)
    ap.add_argument("--production", default="", help="model folder: train the live exit model there")
    ap.add_argument("--any-horizon", action="store_true", help="with --production: the any-horizon exit")
    a = ap.parse_args()
    if a.production and a.any_horizon:
        train_production_multi(a.oos, a.production)
        return 0
    if a.production:
        train_production(a.oos, a.production)
        return 0
    from snake import calendar as C
    o = pd.read_parquet(a.oos)
    o = o[o["date"] >= "2013-01-01"]
    prices = C.load_prices()
    ctx = Context(o, prices, C.market_features(prices))
    rows = training_rows(o, ctx)
    log(f"{len(rows):,} training rows; holding beat switching on {(rows['target'] > 0).mean():.0%}")
    models = fit_by_year(rows, sorted(o["date"].dt.year.unique()))
    for margin in (0.0, 0.01, 0.02):
        s, _ = book.simulate(o, first_session=True, exit_policy=Policy(models, ctx, margin))
        log(f"margin {margin:.2f}: Rs {s['final']:,.0f} ({100 * s['cagr']:+.1f}%/yr), dd "
            f"{100 * s['worst_drawdown']:.0f}%, {s['trades']} trades, median hold {s['median_hold']:.0f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
