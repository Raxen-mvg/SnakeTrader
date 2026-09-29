"""Harvest every NSE corporate announcement since 2010 into a database of its own.

This is the source that can tell the model WHAT happened rather than only that something did. The
event table already detects 101,997 Indian shocks from price and volume alone, and every one of
them carries explained = False, because the news was never collected. An announcement feed closes
that gap: symbol, category, a timestamp to the second, and a summary, published by the exchange as
regulatory data and free to read.

Design decisions worth stating, because each one is a way this could go wrong:

  windows, not pages      The API answers a date range. July 2026 returns almost seventeen
                          thousand rows and July 2010 returns twenty-four hundred, so a fixed
                          window that is safe in 2010 is not safe now. This walks the history in
                          short windows and VERIFIES each one by re-fetching it in halves whenever
                          the count looks suspiciously round, which is how a silent server-side
                          cap would announce itself.
  resumable               Every window that succeeds is recorded. Re-running skips what is done,
                          so an interrupted harvest costs only the window it was in. Sessions get
                          cut off on this machine often enough that this is not optional.
  a fresh session         NSE refuses API calls that arrive without a cookie from its own site,
                          and the cookie expires. The handshake is repeated on any refusal and
                          every fifty windows rather than waiting to be locked out.
  polite                  One request at a time, a real delay between them, and exponential
                          backoff on failure. This is public regulatory data and there is no
                          reason to be rude about collecting it.
  the trading day, not    An announcement at 18:10 cannot be traded at that day's close. Each row
  the calendar day        gets a session_date: the same day if it arrived before the close, the
                          next calendar day otherwise. Anything built on this must use that column
                          or it will be reading tomorrow's news into today's price.

Written to C:\\quantlab_data\\nse_announcements.duckdb, nothing else touched.

Usage: python collect_nse_announcements.py [--start 2010-01-01] [--days 7]
"""

from __future__ import annotations

import argparse
import hashlib
import http.client
import http.cookiejar
import json
import sys
import time
import urllib.error
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path

import pandas as pd

LOG = r"C:\Projects\StockTradesModel\logs\nse_announcements.log"
DEST = r"C:\quantlab_data\nse_announcements.duckdb"
TABLE = "announcements"
PROGRESS = "windows_done"
BASE = "https://www.nseindia.com/api/corporate-announcements?index=equities"
HOME = "https://www.nseindia.com/companies-listing/corporate-filings-announcements"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/122.0 Safari/537.36")
PAUSE = 1.6                 # seconds between requests
MARKET_CLOSE = 15, 30       # IST; an announcement after this belongs to the next session


class Nse:
    """A polite, self-renewing session against the announcements endpoint."""

    def __init__(self) -> None:
        self.calls = 0
        self._open()

    def _open(self) -> None:
        self.jar = http.cookiejar.CookieJar()
        self.op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.jar))
        self.op.addheaders = [("User-Agent", UA), ("Accept", "*/*"),
                              ("Accept-Language", "en-IN,en;q=0.9"), ("Referer", HOME)]
        self.op.open(HOME, timeout=25).read(500)
        self.calls = 0

    def window(self, start: date, end: date) -> list[dict]:
        url = f"{BASE}&from_date={start:%d-%m-%Y}&to_date={end:%d-%m-%Y}"
        for attempt in range(4):
            try:
                if self.calls >= 50:
                    self._open()
                raw = self.op.open(url, timeout=60).read().decode("utf-8", "replace")
                self.calls += 1
                j = json.loads(raw)
                if isinstance(j, list):
                    return j
                lists = [v for v in j.values() if isinstance(v, list)]
                return max(lists, key=len) if lists else []
            # IncompleteRead is what NSE's server produces when it drops a large response partway;
            # it killed the first full harvest at window 131, so every network-level failure is
            # now retried rather than only the ones anticipated.
            except (urllib.error.HTTPError, urllib.error.URLError, json.JSONDecodeError,
                    TimeoutError, http.client.IncompleteRead, ConnectionError, OSError) as e:
                wait = 4 * (attempt + 1) ** 2
                print(f"    retry {attempt + 1}/4 after {type(e).__name__}: waiting {wait}s",
                      flush=True)
                time.sleep(wait)
                try:
                    self._open()
                except Exception:
                    pass
        return []


def session_date(announced: pd.Timestamp) -> date:
    """The trading session this announcement can first be acted on."""
    if pd.isna(announced):
        return pd.NaT
    h, m = MARKET_CLOSE
    if (announced.hour, announced.minute) >= (h, m):
        return (announced + pd.Timedelta(days=1)).date()
    return announced.date()


def tidy(rows: list[dict]) -> pd.DataFrame:
    if not rows:
        return pd.DataFrame()
    d = pd.DataFrame(rows)
    out = pd.DataFrame({
        "symbol": d.get("symbol", pd.Series(dtype=str)).astype(str).str.strip(),
        "company": d.get("sm_name", pd.Series(dtype=str)).astype(str).str.strip(),
        "isin": d.get("sm_isin", pd.Series(dtype=str)).astype(str).str.strip(),
        "industry": d.get("smIndustry", pd.Series(dtype=str)).astype(str).str.strip(),
        "category": d.get("desc", pd.Series(dtype=str)).astype(str).str.strip(),
        "summary": d.get("attchmntText", pd.Series(dtype=str)).astype(str).str.strip(),
        "attachment": d.get("attchmntFile", pd.Series(dtype=str)).astype(str).str.strip(),
        "has_xbrl": d.get("hasXbrl", pd.Series(dtype=str)).astype(str).str.strip(),
        "seq_id": d.get("seq_id", pd.Series(dtype=str)).astype(str).str.strip(),
    })
    out["announced_at"] = pd.to_datetime(d.get("an_dt"), format="%d-%b-%Y %H:%M:%S",
                                         errors="coerce")
    bad = out["announced_at"].isna()
    if bad.any():                      # a few rows carry a different format
        out.loc[bad, "announced_at"] = pd.to_datetime(d.loc[bad.values, "an_dt"],
                                                      errors="coerce", dayfirst=True)
    out["session_date"] = out["announced_at"].map(session_date)
    out = out[out["symbol"].str.len() > 0]
    # A stable identity, so re-running a window never duplicates a row.
    out["row_id"] = [
        hashlib.sha1(f"{s}|{a}|{c}|{t[:200]}".encode("utf-8")).hexdigest()
        for s, a, c, t in zip(out["symbol"], out["announced_at"], out["category"], out["summary"])
    ]
    out["fetched_at"] = pd.Timestamp.now()
    return out.drop_duplicates("row_id")


def main() -> int:
    ap = argparse.ArgumentParser()
    # The log redirect lives here rather than at import, so the cloud runner can import the
    # session and tidy functions without writing to a laptop path that does not exist there.
    ap.add_argument("--log", default=LOG, help="'-' for the console")
    ap.add_argument("--dest", default=DEST)
    ap.add_argument("--start", default="2010-01-01")
    ap.add_argument("--end", default=str(date.today()))
    ap.add_argument("--days", type=int, default=7, help="window width in days")
    ap.add_argument("--verify-every", type=int, default=25,
                    help="re-fetch one window in halves this often, to catch a silent row cap")
    a = ap.parse_args()
    if a.log != "-":
        sys.stdout = sys.stderr = open(a.log, "a", buffering=1)

    import duckdb

    con = duckdb.connect(a.dest)
    con.execute(f"""CREATE TABLE IF NOT EXISTS {TABLE} (
        row_id VARCHAR PRIMARY KEY, symbol VARCHAR, company VARCHAR, isin VARCHAR,
        industry VARCHAR, category VARCHAR, summary VARCHAR, attachment VARCHAR,
        has_xbrl VARCHAR, seq_id VARCHAR, announced_at TIMESTAMP, session_date DATE,
        fetched_at TIMESTAMP)""")
    con.execute(f"""CREATE TABLE IF NOT EXISTS {PROGRESS} (
        start_date DATE, end_date DATE, rows_found INTEGER, fetched_at TIMESTAMP,
        PRIMARY KEY (start_date, end_date))""")

    done = set(map(tuple, con.execute(
        f"SELECT start_date, end_date FROM {PROGRESS}").fetchall()))
    start = datetime.strptime(a.start, "%Y-%m-%d").date()
    end = datetime.strptime(a.end, "%Y-%m-%d").date()

    windows = []
    cur = start
    while cur <= end:
        stop = min(cur + timedelta(days=a.days - 1), end)
        windows.append((cur, stop))
        cur = stop + timedelta(days=1)
    todo = [w for w in windows if w not in done]
    print(f"=== {time.strftime('%Y-%m-%d %H:%M')} NSE announcements: {len(windows)} windows of "
          f"{a.days} days from {start} to {end}, {len(done)} already done, {len(todo)} to fetch "
          f"===", flush=True)
    if not todo:
        total = con.execute(f"SELECT COUNT(*) FROM {TABLE}").fetchone()[0]
        print(f"nothing to do; {total:,} announcements already stored")
        print("NSE ANNOUNCEMENTS DONE")
        return 0

    nse = Nse()
    t0 = time.time()
    stored_total = 0
    for i, (s, e) in enumerate(todo, 1):
        rows = nse.window(s, e)
        df = tidy(rows)

        # A silent server-side cap would show up as a window returning fewer rows than its own
        # halves do. Check occasionally rather than never.
        if a.verify_every and i % a.verify_every == 0 and len(rows):
            mid = s + (e - s) / 2
            time.sleep(PAUSE)
            h1 = nse.window(s, mid)
            time.sleep(PAUSE)
            h2 = nse.window(mid + timedelta(days=1), e)
            halves = len(tidy(h1)) + len(tidy(h2))
            if halves > len(df) * 1.05:
                print(f"    WINDOW CAP SUSPECTED at {s}..{e}: whole={len(df)}, halves={halves}. "
                      f"Re-run with a smaller --days.", flush=True)
                df = pd.concat([df, tidy(h1), tidy(h2)], ignore_index=True)
                df = df.drop_duplicates("row_id")

        if not df.empty:
            con.register("incoming", df)
            con.execute(f"""INSERT INTO {TABLE} SELECT
                row_id, symbol, company, isin, industry, category, summary, attachment,
                has_xbrl, seq_id, announced_at, session_date, fetched_at
                FROM incoming WHERE row_id NOT IN (SELECT row_id FROM {TABLE})""")
            con.unregister("incoming")
            stored_total += len(df)

        con.execute(f"INSERT OR REPLACE INTO {PROGRESS} VALUES (?, ?, ?, ?)",
                    [s, e, len(df), pd.Timestamp.now()])
        if i % 10 == 0 or i == len(todo):
            have = con.execute(f"SELECT COUNT(*) FROM {TABLE}").fetchone()[0]
            rate = i / max(time.time() - t0, 1) * 60
            left = (len(todo) - i) / max(rate, 0.01)
            print(f"  [{i}/{len(todo)}] {s}..{e}: +{len(df)} rows, {have:,} stored, "
                  f"{rate:.1f} windows/min, ~{left:.0f} min left", flush=True)
        time.sleep(PAUSE)

    n, syms, lo, hi = con.execute(
        f"SELECT COUNT(*), COUNT(DISTINCT symbol), MIN(session_date), MAX(session_date) "
        f"FROM {TABLE}").fetchone()
    print(f"\n{n:,} announcements, {syms:,} symbols, {lo} to {hi}", flush=True)
    print("\ntop categories:", flush=True)
    cats = con.execute(f"""SELECT category, COUNT(*) n FROM {TABLE}
                           GROUP BY category ORDER BY n DESC LIMIT 20""").df()
    for _, r in cats.iterrows():
        print(f"  {r['n']:>8,}  {r['category'][:70]}", flush=True)
    close_minutes = MARKET_CLOSE[0] * 60 + MARKET_CLOSE[1]
    after = con.execute(
        f"SELECT ROUND(100.0 * AVG(CASE WHEN HOUR(announced_at) * 60 + MINUTE(announced_at) >= "
        f"{close_minutes} THEN 1 ELSE 0 END), 1) FROM {TABLE}").fetchone()[0]
    print(f"\nannounced after the close, so tradable only next session: {after}%", flush=True)
    con.close()
    print(f"total {(time.time() - t0) / 60:.1f} min")
    print("NSE ANNOUNCEMENTS DONE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
