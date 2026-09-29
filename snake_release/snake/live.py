"""SNAKE's morning job: today's Indian features, the saved model, and a picks file for the account.

The features are computed by the SAME functions that built the training table - price_features,
alpha_features and probability_features from the production code, then the same era-neutral
liquidity filter and the same cross-sectional ranking - over the last four hundred sessions of
prices, which is enough history for the longest window (two hundred and fifty-two sessions) to be
full on the latest day. News comes from snake/news.py on the same terms as in training.

The work is split so that the laptop and the cloud share every step that matters:

  load_prices_db       the laptop's source: the production database
  features_from_prices one function, used by both, from a price panel to today's feature rows
  score                the saved model and its calibration, to every name's expected return
  write                an atomic write of the picks file

snake/cloud.py supplies the same price panel from Yahoo and the same announcements from NSE, so a
runner with no database and no laptop reaches the same picks.

Two guards, because the live path is where silent failures cost money:

  a stale benchmark    the Nifty series in the benchmarks table has lagged the price table by days
                       at a time, which makes beta, idiosyncratic volatility and relative strength
                       quietly wrong on exactly the dates that matter. When it ends before the
                       prices do, NIFTYBEES - an ETF on the same index - supplies the market's
                       daily returns.
  a partial universe   fewer than five hundred Indian names on the latest date means the day's data
                       is incomplete, and no picks are written. The account keeps its previous file
                       and stops buying once that goes stale.

Usage: python -m snake.live [--out C:/Projects/oracle-paper-trader/state/picks_snake.json]
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

from snake.model import HORIZONS, build

HERE = Path(__file__).resolve().parent
MODEL_DIR = HERE / "model"
MAIN_DB = r"C:\quantlab_data\quantlab.duckdb"
DEFAULT_OUT = r"C:\Projects\oracle-paper-trader\state\picks_snake.json"
PRODUCTION = r"C:\Projects\StockTradesModel"
HISTORY_SESSIONS = 400
MIN_NAMES = 500
TOP_N = 30
LIQUID_SHARE = 0.4        # production's min_turnover_percentile: keep the top 60% by turnover


def log(msg: str) -> None:
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} snake {msg}", flush=True)


def _production_on_path() -> None:
    # SNAKE_BUNDLE_ONLY proves a release is self-contained: with it set, nothing is borrowed from
    # the model repository on this machine, exactly as on a cloud runner.
    import os
    if os.environ.get("SNAKE_BUNDLE_ONLY"):
        return
    if Path(PRODUCTION).exists() and PRODUCTION not in sys.path:
        sys.path.insert(0, PRODUCTION)


def load_prices_db(db_path: str = MAIN_DB) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Price panel and benchmark from the production database (the laptop's source)."""
    _production_on_path()
    from quantlab.db import DB, OPERATING_COMPANY_SQL

    db = DB(db_path, read_only=True, threads=8, memory_limit="6GB")
    syms = db.q(f"SELECT symbol FROM universe WHERE market = 'IN' AND ({OPERATING_COMPANY_SQL})"
                )["symbol"].tolist()
    cal = db.q("""SELECT DISTINCT p.date FROM prices p JOIN universe u USING (symbol)
                  WHERE u.market = 'IN' ORDER BY p.date DESC LIMIT ?""", [HISTORY_SESSIONS])
    start = pd.to_datetime(cal["date"]).min()
    last = pd.to_datetime(cal["date"]).max()

    bm = db.q("SELECT date, adj_close FROM benchmarks WHERE symbol = '^NSEI' AND date >= ? "
              "ORDER BY date", [start])
    if bm.empty or pd.to_datetime(bm["date"]).max() < last:
        etf = db.q("SELECT date, adj_close FROM prices WHERE symbol = 'NIFTYBEES.NS' AND date >= ? "
                   "ORDER BY date", [start])
        if not etf.empty and pd.to_datetime(etf["date"]).max() >= last:
            log(f"benchmark ends {pd.to_datetime(bm['date']).max().date() if len(bm) else 'never'} "
                f"but prices run to {last.date()}: using NIFTYBEES for market returns")
            bm = etf
    parts = []
    for i in range(0, len(syms), 300):
        px = db.price_panel(symbols=syms[i:i + 300], market="IN")
        if not px.empty:
            px["date"] = pd.to_datetime(px["date"])
            parts.append(px[px["date"] >= start])
    db.con.close()
    bm["date"] = pd.to_datetime(bm["date"])
    return pd.concat(parts, ignore_index=True), bm


def features_from_prices(px: pd.DataFrame, bm: pd.DataFrame, liquidity_filter: bool = True,
                         ann_db: str | None = None) -> tuple[pd.DataFrame, pd.Timestamp]:
    """From a price panel to today's feature rows, exactly as the training table was built.

    liquidity_filter=False is for a panel that has ALREADY been restricted to yesterday's liquid
    names (the cloud's case): filtering it again would keep only the top sixty percent of the top
    sixty percent.
    """
    _production_on_path()
    from quantlab.alpha_features import FEATURE_COLS_ALPHA, alpha_features
    from quantlab.context_features import FEATURE_COLS_PROB, probability_features
    from quantlab.features import FEATURE_COLS_PRICE, cross_sectional_rank, price_features

    parts = []
    syms = sorted(px["symbol"].unique())
    for i in range(0, len(syms), 300):
        p = px[px["symbol"].isin(syms[i:i + 300])]
        pf = price_features(p, bm if not bm.empty else None)
        pf = pf.merge(alpha_features(p, bm if not bm.empty else None), on=["symbol", "date"],
                      how="left")
        pf = pf.merge(probability_features(p), on=["symbol", "date"], how="left")
        parts.append(pf)
    d = pd.concat(parts, ignore_index=True)
    asof = d["date"].max()
    feats = [c for c in FEATURE_COLS_PRICE + FEATURE_COLS_ALPHA + FEATURE_COLS_PROB
             if c in d.columns]

    today = d[d["date"] == asof].copy()
    if liquidity_filter:
        today = today[today["log_turnover_21d"].rank(pct=True) >= LIQUID_SHARE]
    for c in feats:
        lo, hi = today[c].quantile([0.001, 0.999])
        today[c] = today[c].clip(lo, hi)
    today = cross_sectional_rank(today, feats)

    from snake import news
    nf = news.news_features(d[d["symbol"].isin(today["symbol"])][["symbol", "date"]], ann_db)
    today = today.merge(nf[nf["date"] == asof], on=["symbol", "date"], how="left")
    return today, asof


def score(today: pd.DataFrame, asof: pd.Timestamp, model_dir: Path = MODEL_DIR,
          tag: str = "") -> dict:
    """Every name's best expected return across horizons, from the saved model."""
    import torch

    meta = json.loads((Path(model_dir) / f"{tag}meta.json").read_text())
    cols = meta["features"]
    for c in cols:
        if c not in today.columns:
            today[c] = 0.0
    X = today[cols].fillna(0.0).to_numpy(np.float32)
    preds = []
    for seed in meta["seeds"]:
        m = build(len(cols), len(HORIZONS))
        m.load_state_dict(torch.load(Path(model_dir) / f"{tag}snake_seed{seed}.pt",
                                     map_location="cpu"))
        m.eval()
        with torch.no_grad():
            preds.append(m.predict(torch.from_numpy(X)).numpy())
    p = np.mean(preds, axis=0)

    cal = {int(k): float(v) for k, v in meta["calibration"].items()}
    exp = pd.DataFrame(index=today["symbol"].values)
    for j, h in enumerate(HORIZONS):
        r = pd.Series(p[:, j], index=exp.index).rank(pct=True)
        exp[h] = (r - 0.5) * 2.0 * cal.get(h, 0.0)
    best = exp.max(axis=1)
    horizon = exp.idxmax(axis=1)
    order = best.sort_values(ascending=False)
    return {"asof": str(pd.Timestamp(asof).date()), "model": "SNAKE",
            "model_built": meta.get("built"), "trained_through": meta.get("trained_through"),
            "names_scored": int(len(order)),
            "top": [{"symbol": s, "expected": round(float(best[s]), 6),
                     "horizon": int(horizon[s]), "rank": i + 1}
                    for i, s in enumerate(order.index[:TOP_N])],
            "expected": {s: round(float(v), 6) for s, v in order.items()}}


def write(out: dict, path: str) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    tmp = Path(path).with_suffix(".tmp")
    tmp.write_text(json.dumps(out, indent=1))
    tmp.replace(path)
    top = out["top"][0] if out["top"] else {}
    log(f"wrote {len(out['top'])} picks as of {out['asof']} -> {path}"
        + (f"; best {top['symbol']} expecting {100 * top['expected']:+.2f}% over "
           f"{top['horizon']} sessions" if top else ""))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=DEFAULT_OUT)
    ap.add_argument("--model-tag", default="", help="'smoke_' to test with the smoke model")
    a = ap.parse_args()
    px, bm = load_prices_db()
    today, asof = features_from_prices(px, bm, liquidity_filter=True)
    log(f"{len(today):,} liquid Indian names as of {asof.date()}")
    if len(today) < MIN_NAMES:
        log(f"only {len(today)} names - incomplete day, picks NOT written")
        return 1
    # The live account scores with whichever variant has been promoted (snake/production.py);
    # --model-tag is only for testing against the default folder.
    from snake.production import model_dir
    folder = MODEL_DIR if a.model_tag else model_dir()
    log(f"scoring with {folder.name}")
    write(score(today, asof, folder, a.model_tag), a.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
