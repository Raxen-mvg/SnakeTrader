"""Harvest NSE's board-meeting intimations since 2010: WHEN each company said its results are due.

A company must tell the exchange days in advance that its board will meet, and why. For results
meetings that is a public, dated promise of news to come: the results themselves may be good or bad,
but the date is known. This is the source for SNAKE's results-calendar features.

Each row carries two times, and the difference is what keeps it honest:

  meeting_date   the day the board meets - when the news arrives
  intimated_at   when the company told the exchange - the first moment anyone could know the date

Anything built on this must use known_session (the trading session on which intimated_at could first
be acted on, the next day after the 15:30 close) and never meeting_date, or it would be reading a
calendar nobody had yet published.

Same session, windows, resume and politeness as collect_nse_announcements.py; only the endpoint and
the columns differ. Written to C:\\quantlab_data\\nse_board_meetings.duckdb.

Usage: python collect_nse_board_meetings.py [--start 2010-01-01] [--end 2026-12-31] [--days 10]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from datetime import date, datetime, timedelta

import pandas as pd

import collect_nse_announcements as ann

LOG = r"C:\Projects\StockTradesModel\logs\nse_board_meetings.log"
DEST = r"C:\quantlab_data\nse_board_meetings.duckdb"
URL = "https://www.nseindia.com/api/corporate-board-meetings?index=equities"
RESULT_WORDS = ("result", "financial statement", "accounts")


class BoardMeetings(ann.Nse):
    def window(self, start: date, end: date) -> list[dict]:
        saved = ann.BASE
        ann.BASE = URL
        try:
            return super().window(start, end)
        finally:
            ann.BASE = saved


def tidy(rows: list[dict]) -> pd.DataFrame:
    if not rows:
        return pd.DataFrame()
    d = pd.DataFrame(rows)
    col = lambda k: d.get(k, pd.Series([None] * len(d))).astype(str).str.strip()
    out = pd.DataFrame({"symbol": col("bm_symbol"), "company": col("sm_name"),
                        "industry": col("sm_indusrty"), "purpose": col("bm_purpose"),
                        "description": col("bm_desc")})
    out["meeting_date"] = pd.to_datetime(d.get("bm_date"), format="%d-%b-%Y", errors="coerce")
    out["intimated_at"] = pd.to_datetime(d.get("bm_timestamp"), format="%d-%b-%Y %H:%M:%S",
                                         errors="coerce")
    out["known_session"] = out["intimated_at"].map(ann.session_date)
    text = (out["purpose"] + " " + out["description"]).str.lower()
    out["is_results"] = text.str.contains("|".join(RESULT_WORDS), regex=True)
    out = out[(out["symbol"].str.len() > 0) & out["meeting_date"].notna()]
    out["row_id"] = [hashlib.sha1(f"{s}|{m}|{i}|{p[:120]}".encode("utf-8")).hexdigest()
                     for s, m, i, p in zip(out["symbol"], out["meeting_date"],
                                           out["intimated_at"], out["purpose"])]
    out["fetched_at"] = pd.Timestamp.now()
    return out.drop_duplicates("row_id")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--log", default=LOG, help="'-' for the console")
    ap.add_argument("--dest", default=DEST)
    ap.add_argument("--start", default="2010-01-01")
    # Meetings are listed by their date, so a window reaching past today returns the ones
    # already announced for the coming weeks - exactly what the live model needs.
    ap.add_argument("--end", default=str(date.today() + timedelta(days=60)))
    ap.add_argument("--days", type=int, default=10)
    ap.add_argument("--refresh-days", type=int, default=0,
                    help="re-fetch windows ending within this many days of today, even if done")
    a = ap.parse_args()
    if a.log != "-":
        sys.stdout = sys.stderr = open(a.log, "a", buffering=1)

    import duckdb

    con = duckdb.connect(a.dest)
    con.execute("""CREATE TABLE IF NOT EXISTS board_meetings (
        row_id VARCHAR PRIMARY KEY, symbol VARCHAR, company VARCHAR, industry VARCHAR,
        purpose VARCHAR, description VARCHAR, meeting_date DATE, intimated_at TIMESTAMP,
        known_session DATE, is_results BOOLEAN, fetched_at TIMESTAMP)""")
    con.execute("""CREATE TABLE IF NOT EXISTS windows_done (start_date DATE, end_date DATE,
        rows_found INTEGER, fetched_at TIMESTAMP, PRIMARY KEY (start_date, end_date))""")
    done = set(map(tuple, con.execute("SELECT start_date, end_date FROM windows_done").fetchall()))

    start = datetime.strptime(a.start, "%Y-%m-%d").date()
    end = datetime.strptime(a.end, "%Y-%m-%d").date()
    fresh = date.today() - timedelta(days=a.refresh_days)
    windows, cur = [], start
    while cur <= end:
        stop = min(cur + timedelta(days=a.days - 1), end)
        windows.append((cur, stop))
        cur = stop + timedelta(days=1)
    # A window that reaches today or later can still gain meetings, so it is never marked done.
    todo = [w for w in windows if w not in done or (a.refresh_days and w[1] >= fresh)
            or w[1] >= date.today()]
    print(f"=== {time.strftime('%Y-%m-%d %H:%M')} NSE board meetings: {len(todo)} of "
          f"{len(windows)} windows to fetch ===", flush=True)

    nse = BoardMeetings()
    n_rows = 0
    for i, (s, e) in enumerate(todo, 1):
        df = tidy(nse.window(s, e))
        if not df.empty:
            con.register("incoming", df)
            con.execute("""INSERT OR REPLACE INTO board_meetings SELECT row_id, symbol, company,
                industry, purpose, description, meeting_date, intimated_at, known_session,
                is_results, fetched_at FROM incoming""")
            con.unregister("incoming")
            n_rows += len(df)
        if e < date.today():
            con.execute("INSERT OR REPLACE INTO windows_done VALUES (?, ?, ?, ?)",
                        [s, e, len(df), datetime.now()])
        if i % 25 == 0 or i == len(todo):
            print(f"  {i}/{len(todo)} windows, through {e}, {n_rows:,} rows this run", flush=True)
        time.sleep(ann.PAUSE)
    total, res = con.execute("SELECT COUNT(*), SUM(is_results::INT) FROM board_meetings").fetchone()
    con.close()
    print(f"{total:,} board meetings stored, {res:,} of them for results")
    print("NSE BOARD MEETINGS DONE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
