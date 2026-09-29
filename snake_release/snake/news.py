"""Turn NSE announcements into features a model can read, without reading the future.

Each announcement already carries a session_date - the first trading session it could have been
acted on, which is the next day for the two thirds that arrive after the 15:30 close. Here that
date is snapped forward onto the stock's own trading calendar (an announcement on a Saturday belongs
to Monday), and then counted over trailing windows of sessions, never calendar days, so a week of
holidays does not dilute a count.

What gets counted is chosen to match the categories the exchange itself uses and that plausibly
move a price, grouped so that a thin category does not become a feature that is zero almost
everywhere:

  orders      order wins and contract awards - what moves a small defence or engineering name
  results     financial results and board-meeting outcomes, which is where results are announced
  rating      credit rating actions
  management  appointments, resignations, changes of director or auditor
  capital     allotments, buybacks, bonuses, splits, rights and preferential issues
  deals       acquisitions, mergers, amalgamations, schemes of arrangement
  queries     the exchange asking a company to explain a volume or price spurt, and the reply
  any         every announcement of any kind

Counts become log(1 + n) scaled to roughly [0, 1], and "sessions since the last one" is capped at a
year and scaled the same way, so the network sees bounded inputs like every other feature. Rows in
markets with no announcement feed get zeros and has_news = 0, so the model can tell "no news
collected" apart from "nothing happened".
"""

from __future__ import annotations

import os

import pandas as pd

# Overridable so tests and smoke runs can use a small stand-in while the harvest holds the real
# file: DuckDB on Windows locks a database against every other process while one is writing.
ANN_DB = os.environ.get("SNAKE_ANN_DB", r"C:\quantlab_data\nse_announcements.duckdb")

GROUPS = {
    "orders": ["order", "contract", "bagging"],
    "results": ["financial result", "outcome of board meeting", "results"],
    "rating": ["credit rating"],
    "management": ["appointment", "resignation", "change in director", "change in management",
                   "change in auditor", "cessation"],
    "capital": ["allotment", "buyback", "buy back", "bonus", "split", "rights", "preferential",
                "qip", "issue of securities"],
    "deals": ["acquisition", "amalgamation", "merger", "scheme of arrangement", "demerger",
              "disposal", "divestment"],
    "queries": ["spurt", "clarification"],
}
WINDOWS = {"any": [5, 21, 63], "orders": [21, 63], "results": [21], "rating": [63],
           "management": [63], "capital": [63], "deals": [63], "queries": [21]}
SINCE = ["any", "orders", "results"]
CAP_SESSIONS = 252


def columns() -> list[str]:
    cols = ["has_news"]
    for g, ws in WINDOWS.items():
        cols += [f"news_{g}_{w}" for w in ws]
    cols += [f"news_since_{g}" for g in SINCE]
    return cols


def _case(group: str) -> str:
    if group == "any":
        return "1"
    likes = " OR ".join(f"lower(category) LIKE '%{k}%'" for k in GROUPS[group])
    return f"CASE WHEN {likes} THEN 1 ELSE 0 END"


SEC_DB = r"C:\quantlab_data\sec_8k.duckdb"

# US 8-K item codes, translated into words the NSE category groups above already match, so one
# definition of every news feature serves both countries. Codes before August 2004 used a
# different numbering (1-12); the old codes that name a comparable event are mapped too.
SEC_ITEM_WORDS = {
    "1.01": "bagging of orders/contracts",         # material definitive agreement
    "2.02": "financial results",                   # results of operations
    "5.02": "appointment resignation",             # directors and officers
    "5.01": "change in management",                # change in control
    "4.01": "change in auditor",
    "2.01": "acquisition disposal",                # completion of acquisition or disposition
    "3.02": "allotment",                           # unregistered sales of equity
    "3.03": "rights",                              # modification of shareholder rights
    "3.01": "clarification",                       # delisting or listing-rule notice
    "4.02": "clarification",                       # non-reliance: a restatement is coming
    "12": "financial results",                     # pre-2004: results of operations
    "2": "acquisition disposal",                   # pre-2004: acquisition or disposition
    "1": "change in management",                   # pre-2004: change in control
    "4": "change in auditor",                      # pre-2004
    "6": "resignation",                            # pre-2004: director resignation
}


def sec_events(symbols_ciks: pd.DataFrame, sec_db: str | None = None) -> pd.DataFrame:
    """US 8-K filings as (symbol, sdate, category) rows, on the session each could be traded.

    EDGAR's acceptance time is UTC. A filing accepted at or after 16:00 New York time is known
    only after that day's close, so it belongs to the next calendar day; anything earlier is
    known before the close and belongs to the same day.
    """
    import duckdb

    con = duckdb.connect(sec_db or SEC_DB, read_only=True)
    f = con.execute("SELECT cik, form, accepted_raw, items FROM filings").df()
    con.close()
    if f.empty:
        return pd.DataFrame(columns=["symbol", "sdate", "category"])
    t = pd.to_datetime(f["accepted_raw"], utc=True, errors="coerce").dt.tz_convert(
        "America/New_York")
    after_close = (t.dt.hour * 60 + t.dt.minute) >= 16 * 60
    f["sdate"] = (t.dt.tz_localize(None).dt.normalize()
                  + pd.to_timedelta(after_close.astype(int), unit="D"))
    words = f["items"].fillna("").map(
        lambda s: " ".join(SEC_ITEM_WORDS.get(i.strip(), "") for i in s.split(",")).strip())
    f["category"] = words.where(words != "", "other")
    m = symbols_ciks[["symbol", "cik"]].dropna().copy()
    m["cik"] = m["cik"].astype("int64")
    f["cik"] = f["cik"].astype("int64")
    return f.merge(m, on="cik", how="inner")[["symbol", "sdate", "category"]].dropna()


def news_features(calendar: pd.DataFrame, ann_db: str | None = None,
                  events: pd.DataFrame | None = None) -> pd.DataFrame:
    """Features for every (symbol, date) in calendar, which must be one market's trading days.

    calendar: DataFrame with columns symbol (e.g. 'DATAPATTNS.NS') and date.
    events:   optional (symbol, sdate, category) rows from another feed - the US 8-Ks from
              sec_events(). Without it, the NSE announcement database is used.
    Returns the same rows with has_news and the news_* columns attached.
    """
    import duckdb

    ann_db = ann_db or os.environ.get("SNAKE_ANN_DB", ANN_DB)
    cal = calendar[["symbol", "date"]].drop_duplicates().copy()
    cal["date"] = pd.to_datetime(cal["date"]).dt.normalize()
    con = duckdb.connect()
    con.register("cal", cal)
    if events is None:
        con.execute(f"ATTACH '{ann_db}' AS ann (READ_ONLY)")
        source = ("SELECT symbol || '.NS' AS symbol, CAST(session_date AS TIMESTAMP) AS sdate, "
                  "category FROM ann.announcements WHERE session_date IS NOT NULL")
    else:
        ev = events[["symbol", "sdate", "category"]].copy()
        ev["sdate"] = pd.to_datetime(ev["sdate"])
        con.register("ev", ev)
        source = "SELECT symbol, CAST(sdate AS TIMESTAMP) AS sdate, category FROM ev"

    groups = ["any"] + list(GROUPS)
    counts_sql = ", ".join(f"SUM({_case(g)}) AS n_{g}" for g in groups)
    rolling = []
    for g, ws in WINDOWS.items():
        for w in ws:
            rolling.append(
                f"LN(1 + SUM(COALESCE(n_{g}, 0)) OVER (PARTITION BY c.symbol ORDER BY c.date "
                f"ROWS BETWEEN {w - 1} PRECEDING AND CURRENT ROW)) / LN(1 + {max(w, 10)}) "
                f"AS news_{g}_{w}")
    since = []
    for g in SINCE:
        since.append(
            f"LEAST(c.rn - MAX(CASE WHEN COALESCE(n_{g}, 0) > 0 THEN c.rn END) OVER "
            f"(PARTITION BY c.symbol ORDER BY c.date ROWS UNBOUNDED PRECEDING), {CAP_SESSIONS}) "
            f"AS raw_since_{g}")

    q = f"""
    WITH a AS ({source}),
    c AS (
        SELECT symbol, date, ROW_NUMBER() OVER (PARTITION BY symbol ORDER BY date) AS rn FROM cal
    ),
    -- Snap each announcement forward onto that stock's own next trading session.
    snapped AS (
        SELECT a.symbol, c.date, a.category
        FROM a ASOF JOIN c ON a.symbol = c.symbol AND a.sdate <= c.date
    ),
    daily AS (
        SELECT symbol, date, {counts_sql} FROM snapped GROUP BY symbol, date
    )
    SELECT c.symbol, c.date, {", ".join(rolling)}, {", ".join(since)}
    FROM c LEFT JOIN daily d ON c.symbol = d.symbol AND c.date = d.date
    """
    out = con.execute(q).df()
    first = con.execute(f"SELECT MIN(sdate) FROM ({source})").fetchone()[0]
    con.close()
    for g in SINCE:
        raw = out.pop(f"raw_since_{g}")
        # Never announced anything in the window of history we can see: treat as a year ago.
        out[f"news_since_{g}"] = (raw.fillna(CAP_SESSIONS) / CAP_SESSIONS).astype("float32")
    # Before the feed begins (NSE's archive starts in 2010) there is no news DATA, which is not
    # the same as a quiet company. Those rows look exactly like a market with no feed: zeros and
    # has_news = 0. Marking them has_news = 1 taught the first version that twenty years of
    # silence was normal, and it lost 93% when the announcements began.
    covered = out["date"] >= pd.Timestamp(first) if first is not None else out["date"] < out["date"].min()
    out["has_news"] = 1.0
    for c in columns():
        out[c] = out[c].fillna(0.0).astype("float32")
        out.loc[~covered, c] = 0.0
    return out[["symbol", "date"] + columns()]
