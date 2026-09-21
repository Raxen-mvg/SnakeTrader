"""Latest frozen model snapshot -> state/picks_IN.json for the paper trader.

Top list (best first) plus every stock's rank percentile, so the hold-winners
strategy can see when a held name falls out of the top 25%. Fund units are
dropped even if an older snapshot still contains them.
Usage: python tools/export_picks.py [--market IN] [--out state/picks_IN.json]
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
from pathlib import Path

import pandas as pd

FUND = re.compile(r"(ETF|BEES|LIQUID|GILT|GSEC|NIFTY|SENSEX)", re.I)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--market", default="IN")
    ap.add_argument("--snapdir", default=r"C:\Projects\StockTradesModel\reports\forward")
    ap.add_argument("--out", default=str(Path(__file__).resolve().parent.parent / "state" / "picks_IN.json"))
    ap.add_argument("--top", type=int, default=30)
    a = ap.parse_args()
    files = glob.glob(os.path.join(a.snapdir, a.market, "asof_*.parquet"))
    if not files:
        raise SystemExit("no snapshot found")
    f = max(files, key=os.path.getmtime)
    s = pd.read_parquet(f)
    s = s[~s["symbol"].str.contains(FUND)]
    s["rank_pct"] = s["score"].rank(pct=True)
    s = s.sort_values("score", ascending=False)
    top = [{"symbol": r.symbol, "name": str(getattr(r, "name", "") or ""), "score": round(float(r.score), 6),
            "rank_pct": round(float(r.rank_pct), 4)} for r in s.head(a.top).itertuples()]
    out = {"asof": str(s["asof_date"].iloc[0]), "market": a.market, "source": os.path.basename(f),
           "top": top, "ranks": {r.symbol: round(float(r.rank_pct), 4) for r in s.itertuples()}}
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=1))
    print(f"exported {len(top)} picks as of {out['asof']} from {out['source']} -> {a.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
