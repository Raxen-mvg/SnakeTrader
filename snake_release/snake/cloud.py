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


GAP = 0.25


def adjust_gaps(d: pd.DataFrame) -> pd.DataFrame:
    """Back-adjust a corporate action Yahoo has not adjusted yet.

    NSE never lets a stock move 20% in one session, so a close more than 25% from the previous one is a
    split, bonus or demerger Yahoo has not yet folded into the history (BHAGYANGR.NS, demerger with
    record date 2026-10-08: 454.55 then 39 - the network read a 90% crash and SNAKE sold it). Every
    earlier price is scaled by the ex-date open over the prior close, the price the exchange discovers
    for the stock after the action, so that day's own move is kept and the action itself is not."""
    if d.empty or d["symbol"].iloc[0].startswith("^"):
        return d
    r = d["close"] / d["close"].shift(1)
    for i in d.index[((r < 1 - GAP) | (r > 1 / (1 - GAP))).fillna(False)][::-1]:
        prev = d.at[i - 1, "close"]
        f = (d.at[i, "open"] if pd.notna(d.at[i, "open"]) and d.at[i, "open"] > 0 else d.at[i, "close"]) / prev
        for c in ("open", "high", "low", "close", "adj_close"):
            d.loc[:i - 1, c] = d.loc[:i - 1, c] * f
    return d


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
            return adjust_gaps(d.dropna(subset=["close", "adj_close"]).reset_index(drop=True))
        except Exception:
            time.sleep(2 * (attempt + 1))
    return pd.DataFrame()


def nse_file(url: str) -> bytes | None:
    """One of the exchange's public end-of-day files; None if it does not exist (a holiday)."""
    import urllib.error
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Referer": "https://www.nseindia.com/"})
            return urllib.request.urlopen(req, timeout=60).read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            time.sleep(3 * (attempt + 1))
        except Exception:
            time.sleep(3 * (attempt + 1))
    return None


def exchange_day(day: date) -> pd.DataFrame:
    """NSE's own bhavcopy for one session: every listed company's raw open, high, low, close."""
    import io
    import zipfile
    raw = nse_file(f"https://nsearchives.nseindia.com/content/cm/BhavCopy_NSE_CM_0_0_0_{day:%Y%m%d}_F_0000.csv.zip")
    if not raw:
        return pd.DataFrame()
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        d = pd.read_csv(io.BytesIO(z.read(next(n for n in z.namelist() if n.lower().endswith(".csv")))))
    d.columns = [c.strip() for c in d.columns]
    d["SctySrs"] = d["SctySrs"].astype(str).str.strip()
    d = d[d["SctySrs"].isin(["EQ", "BE"])].sort_values("SctySrs", key=lambda s: s.map({"EQ": 0, "BE": 1}))
    out = pd.DataFrame({"symbol": d["TckrSymb"].astype(str).str.strip() + ".NS",
                        "open": pd.to_numeric(d["OpnPric"], errors="coerce"),
                        "high": pd.to_numeric(d["HghPric"], errors="coerce"),
                        "low": pd.to_numeric(d["LwPric"], errors="coerce"),
                        "close": pd.to_numeric(d["ClsPric"], errors="coerce"),
                        "prevclose": pd.to_numeric(d["PrvsClsgPric"], errors="coerce"),
                        "volume": pd.to_numeric(d["TtlTradgVol"], errors="coerce").fillna(0)})
    out["date"] = pd.Timestamp(day)
    return out.drop_duplicates("symbol").dropna(subset=["close"])


def exchange_index(day: date, name: str = "nifty 50") -> float | None:
    """The index's official close for one session, from the exchange's daily index file."""
    import io
    raw = nse_file(f"https://nsearchives.nseindia.com/content/indices/ind_close_all_{day:%d%m%Y}.csv")
    if not raw:
        return None
    d = pd.read_csv(io.BytesIO(raw))
    d.columns = [c.strip() for c in d.columns]
    row = d[d["Index Name"].astype(str).str.strip().str.lower() == name]
    return float(row["Closing Index Value"].iloc[0]) if len(row) else None


def fill_from_exchange(px: pd.DataFrame) -> pd.DataFrame:
    """Complete the latest sessions Yahoo has only partly from the exchange's own files.

    Yahoo publishes Indian daily bars a few hundred names at a time (631 of 1,527 for 5 Oct at
    11:00 the next morning), so the cloud kept scoring a session that was days old. The laptop
    has filled these from the bhavcopy for months (india_close_from_exchange.py); this is the same
    fill for the cloud. A name is filled only when the exchange's previous close agrees with ours
    within 2%: otherwise a split or bonus sits between them and a raw close would look like a crash."""
    n = px["symbol"].nunique()
    per_day = px.groupby("date")["symbol"].nunique()
    full = per_day[per_day >= 0.8 * n]
    if full.empty:
        return px
    ist = pd.Timestamp.now(tz="Asia/Kolkata").tz_localize(None)
    end = ist.normalize() if ist.hour >= 16 else ist.normalize() - pd.Timedelta(days=1)
    todo = pd.bdate_range(full.index.max() + pd.Timedelta(days=1), end)[-5:]
    universe = set(px["symbol"])
    for d in todo:
        ex = exchange_day(d.date())
        if ex.empty:
            log(f"no exchange file for {d.date()} (a holiday, or not published yet)")
            continue
        have = set(px.loc[px["date"] == d, "symbol"])
        last = px[px["date"] < d].sort_values("date").groupby("symbol").tail(1).set_index("symbol")
        ex = ex[ex["symbol"].isin(universe - have) & ex["symbol"].isin(last.index)]
        agree = (ex["prevclose"] / ex["symbol"].map(last["close"]) - 1).abs() < 0.02
        ex = ex[agree].copy()
        ex["adj_close"] = ex["close"] * ex["symbol"].map(last["adj_close"] / last["close"])
        add = ex[["date", "open", "high", "low", "close", "adj_close", "volume", "symbol"]].copy()
        add["market"] = "IN"
        add["volume"] = add["volume"].astype("int64")
        px = pd.concat([px, add[px.columns]], ignore_index=True)
        log(f"{d.date()}: Yahoo had {len(have):,} names, the exchange's file added {len(add):,} "
            f"({int((~agree).sum())} skipped: previous close disagrees, likely a split or bonus)")
    return px


def prices(symbols: list[str]) -> tuple[pd.DataFrame, pd.DataFrame]:
    with ThreadPoolExecutor(max_workers=8) as ex:
        frames = list(ex.map(yahoo, symbols))
    got = [f for f in frames if not f.empty]
    log(f"prices for {len(got):,} of {len(symbols):,} symbols")
    px = pd.concat(got, ignore_index=True)
    px["market"] = "IN"
    px["volume"] = px["volume"].fillna(0).astype("int64")
    px = fill_from_exchange(px)
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
    for d in sorted(set(keep) - set(bm["date"])):
        if d > bm["date"].max():                   # the index's close missing for a scored session
            v = exchange_index(pd.Timestamp(d).date())
            if v:
                bm = pd.concat([bm, pd.DataFrame({"date": [d], "adj_close": [v]})], ignore_index=True)
                log(f"Nifty 50 close for {pd.Timestamp(d).date()} from the exchange: {v:,.2f}")
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

    # Overnight Yahoo sometimes serves the index's latest bar with no close (2026-10-06 01:22 IST:
    # ^NSEI had no 5 Oct close, so 1 Oct looked current and no picks were made). Take the latest
    # session any of the index and a few of the largest names has a close for.
    seen = [yahoo(s, "5d") for s in ("^NSEI", "RELIANCE.NS", "HDFCBANK.NS", "TCS.NS", "INFY.NS")]
    seen = [d for d in seen if not d.empty]
    if not seen:
        log("could not reach Yahoo for the latest session; nothing written")
        return 1
    last_session = str(max(d["date"].max() for d in seen).date())
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
