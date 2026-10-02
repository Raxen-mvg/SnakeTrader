"""SNAKE without the laptop: fresh prices and news on a cloud runner, then fresh picks.

The laptop is where SNAKE is trained, because training needs the GPU and eighty million rows. It
is not where SNAKE has to be used. Scoring one day of fifteen hundred Indian names needs a few
hundred sessions of their prices, a year of their announcements, and a model small enough to load
on a CPU - about a megabyte. So the laptop publishes a release of the model into the paper-trader
repository (snake/release.py), and this runs from it each morning on GitHub's servers:

  1. if the picks file already describes the latest session - because the laptop was on and did
     it - stop; two clocks, one answer
  2. prices for the release's universe and for anything SNAKE currently holds, from Yahoo, the
     same source that fills the laptop's database
  3. every NSE announcement of the past thirteen months, from the exchange, into a scratch file
  4. the same feature function the laptop uses, the same model, the same calibration
  5. an atomic write of state/picks_snake.json, which the workflow commits

The prices are fetched fresh each morning and discarded afterwards. They are never committed:
Yahoo's terms allow querying, not redistribution, and this repository may one day be public.

Usage (from the bundle directory): python -m snake.cloud --out ../state/picks_snake.json
"""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
BUNDLE = HERE.parent
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/122.0 Safari/537.36")
SESSIONS = 400
NEWS_DAYS = 400


def log(msg: str) -> None:
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} snake.cloud {msg}", flush=True)


def yahoo(symbol: str, rng: str = "2y") -> pd.DataFrame:
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
           f"?range={rng}&interval=1d&events=div%2Csplit")
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            j = json.loads(urllib.request.urlopen(req, timeout=30).read())
            r = j["chart"]["result"][0]
            q = r["indicators"]["quote"][0]
            adj = r["indicators"].get("adjclose", [{}])[0].get("adjclose", q["close"])
            d = pd.DataFrame({"date": pd.to_datetime(r["timestamp"], unit="s")
                              + pd.Timedelta(hours=5, minutes=30),
                              "open": q["open"], "high": q["high"], "low": q["low"],
                              "close": q["close"], "adj_close": adj, "volume": q["volume"]})
            d["date"] = d["date"].dt.normalize()
            d["symbol"] = symbol
            # Before the day's close Yahoo returns TODAY as a daily bar that is still moving. The
            # model was trained on closes, and scoring half a session would describe a day that
            # has not happened yet, so an unfinished bar is dropped until 16:00 IST.
            ist_now = pd.Timestamp.now(tz="Asia/Kolkata").tz_localize(None)
            if ist_now.hour < 16:
                d = d[d["date"] < ist_now.normalize()]
            return d.dropna(subset=["close", "adj_close"])
        except Exception:
            time.sleep(2 * (attempt + 1))
    return pd.DataFrame()


def prices(symbols: list[str]) -> tuple[pd.DataFrame, pd.DataFrame]:
    with ThreadPoolExecutor(max_workers=8) as ex:
        frames = list(ex.map(yahoo, symbols))
    got = [f for f in frames if not f.empty]
    log(f"prices for {len(got):,} of {len(symbols):,} symbols")
    px = pd.concat(got, ignore_index=True)
    px["market"] = "IN"
    px["volume"] = px["volume"].fillna(0).astype("int64")
    # During market hours Yahoo's daily series for many names carries today's moving bar in place
    # of yesterday's, so the latest date can exist for only half the universe (740 of 1,526 on
    # 2026-09-30 at 13:10). Score the latest session that at least 80% of names actually have.
    per_day = px.groupby("date")["symbol"].nunique()
    complete = per_day[per_day >= 0.8 * px["symbol"].nunique()]
    if len(complete):
        px = px[px["date"] <= complete.index.max()]
        if complete.index.max() < per_day.index.max():
            log(f"latest session {per_day.index.max().date()} has only {per_day.iloc[-1]:,} names; "
                f"scoring {complete.index.max().date()} instead")
    keep = sorted(px["date"].unique())[-SESSIONS:]
    px = px[px["date"].isin(set(keep))]
    bm = yahoo("^NSEI")[["date", "adj_close"]]
    return px, bm[bm["date"] >= keep[0]]


def announcements(path: str) -> int:
    """The past thirteen months of NSE announcements into a scratch DuckDB file."""
    import duckdb

    sys.path.insert(0, str(BUNDLE))
    import collect_nse_announcements as c

    con = duckdb.connect(path)
    con.execute("""CREATE TABLE announcements (row_id VARCHAR, symbol VARCHAR, company VARCHAR,
        isin VARCHAR, industry VARCHAR, category VARCHAR, summary VARCHAR, attachment VARCHAR,
        has_xbrl VARCHAR, seq_id VARCHAR, announced_at TIMESTAMP, session_date DATE,
        fetched_at TIMESTAMP)""")
    nse = c.Nse()
    end = date.today()
    cur = end - timedelta(days=NEWS_DAYS)
    n = 0
    while cur <= end:
        stop = min(cur + timedelta(days=6), end)
        df = c.tidy(nse.window(cur, stop))
        if not df.empty:
            con.register("incoming", df)
            con.execute("""INSERT INTO announcements SELECT row_id, symbol, company, isin, industry,
                category, summary, attachment, has_xbrl, seq_id, announced_at, session_date,
                fetched_at FROM incoming""")
            con.unregister("incoming")
            n += len(df)
        cur = stop + timedelta(days=1)
        time.sleep(c.PAUSE)
    con.close()
    return n


def board_meetings(path: str) -> int:
    """Results meetings announced over the past NEWS_DAYS and the next sixty days, into scratch."""
    import subprocess
    r = subprocess.run([sys.executable, str(BUNDLE / "collect_nse_board_meetings.py"), "--log", "-",
                        "--dest", path, "--start", str(date.today() - timedelta(days=NEWS_DAYS))],
                       cwd=BUNDLE, capture_output=True, text=True)
    import duckdb
    try:
        con = duckdb.connect(path, read_only=True)
        n = con.execute("SELECT COUNT(*) FROM board_meetings").fetchone()[0]
        con.close()
    except Exception:
        n = 0
    if r.returncode != 0:
        log(f"board-meeting fetch failed: {r.stderr.strip()[-300:]}")
    return n


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--out-nonews", default=None,
                    help="picks for the no-news account, scored with model_nonews/ in the bundle")
    ap.add_argument("--out-abs", default=None,
                    help="picks for the absolute-return account, scored with model_abs/ in the bundle")
    ap.add_argument("--accounts", default=None, help="state/accounts.json, to include holdings")
    ap.add_argument("--force", action="store_true", help="score even if the file looks current")
    a = ap.parse_args()

    sys.path.insert(0, str(BUNDLE))
    from snake import live

    universe = [s for s in json.loads((BUNDLE / "universe.json").read_text()) if s.endswith(".NS")]
    held = []
    if a.accounts and Path(a.accounts).exists():
        accs = json.loads(Path(a.accounts).read_text())
        for name in ("snake", "snake_nonews", "snake_abs", "snake_abs_conv", "snake_abs_exit",
                     "snake_abs_exit_conv", "snake_anaconda"):
            held += list((accs.get(name, {}).get("positions") or {}).keys())
    symbols = sorted(set(universe) | set(held))

    latest = yahoo("^NSEI", "5d")
    if latest.empty:
        log("could not reach Yahoo for the latest session; nothing written")
        return 1
    last_session = str(latest["date"].max().date())
    nonews = BUNDLE / "model_nonews"
    absm = BUNDLE / "model_abs"
    outs = [Path(a.out)] + ([Path(a.out_nonews)] if a.out_nonews and nonews.exists() else [])
    if a.out_abs and absm.exists():
        outs.append(Path(a.out_abs))

    def current(p: Path) -> bool:
        cur = json.loads(p.read_text()).get("asof") if p.exists() else None
        return bool(cur and cur >= last_session)
    if not a.force and all(current(p) for p in outs):
        log(f"picks already describe {last_session}; the laptop got there first, nothing to do")
        return 0

    px, bm = prices(symbols)
    with tempfile.TemporaryDirectory() as td:
        ann = str(Path(td) / "ann.duckdb")
        log(f"{announcements(ann):,} announcements from the past {NEWS_DAYS} days")
        bmdb = str(Path(td) / "bm.duckdb")
        log(f"{board_meetings(bmdb):,} board meetings from the past {NEWS_DAYS} days and next 60")
        # The universe is yesterday's liquid list already, so it is not filtered a second time.
        today, asof = live.features_from_prices(px, bm, liquidity_filter=False, ann_db=ann,
                                                bm_db=bmdb)
    log(f"{len(today):,} names scored as of {asof.date()}")
    if len(today) < live.MIN_NAMES:
        log("too few names - incomplete day, picks NOT written")
        return 1
    live.write(live.score(today, asof, BUNDLE / "model"), a.out)
    if a.out_nonews and nonews.exists():
        live.write(live.score(today, asof, nonews), a.out_nonews)
    if a.out_abs and absm.exists():
        ectx = live.exit_context(a.accounts, px) if a.accounts else None
        live.write(live.score(today, asof, absm, exit_ctx=ectx), a.out_abs)
    return 0


if __name__ == "__main__":
    sys.exit(main())
