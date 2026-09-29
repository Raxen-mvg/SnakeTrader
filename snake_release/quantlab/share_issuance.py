"""Net share issuance (Pontiff and Woodgate 2008): growth in the share count.

Firms tend to issue shares when their stock is expensive and buy back when it
is cheap, so a growing share count predicts lower returns and a shrinking one
(buybacks) higher returns.

    issuance_12m = log(shares at the latest reported period
                       / shares at the period about 12 months earlier)
    issuance_36m = the same over about 36 months

POINT-IN-TIME RULES (the same ones fundamentals_asof enforces):
  * Only facts with `filed <= date` are visible on `date`.
  * If a period was restated, the latest version filed by `date` is used.
    Weighted-average share counts for the year-ago comparative are restated
    for splits in the very filing that reports the current period, so this
    alone fixes most splits. Among versions filed on the same day for the same
    period end, the shortest duration (the quarter, not the year-to-date) wins.
  * Splits and bonus issues not yet restated: the price table's close is
    already split-adjusted, so prices cannot reveal them. Instead a jump whose
    ratio is within SPLIT_TOL (log) of a standard split ratio (3:2, 2:1, ...
    100:1 and the reverse-split inverses) is treated as a split and that ratio
    is removed. A genuine issuance of exactly 2x is rare; the cost of
    mislabelling one is small.
  * Anything still beyond MAX_ABS_LOG (10x either way) is a data error
    (XBRL unit slips of 1000x exist, e.g. Apple's FY2013 comparative filed
    2014-04-24) and becomes NaN.

US only for now: the SEC XBRL share counts are in the database from 2009.
India has no share-count source loaded (NSE shareholding patterns would be
the free one), so Indian rows get NaN, which LightGBM handles.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

# Weighted-average basic shares first: ASC 260 makes filers restate the prior-year
# comparative for splits inside the same 10-Q/10-K, so the latest version of the
# year-ago period is already split-consistent. Period-end balance counts are the
# fallback for filers that do not tag the weighted average.
SHARE_TAGS = ["WeightedAverageNumberOfSharesOutstandingBasic", "CommonStockSharesOutstanding"]
ISSUANCE_COLS = ["issuance_12m", "issuance_36m"]

# (lag in days, tolerance in days) for each output column
_LAGS = {"issuance_12m": (365, 60), "issuance_36m": (1095, 90)}
_STALE_DAYS = 548          # latest share count must describe a period this recent
_SPLIT_RATIOS = np.array([1.5, 2, 2.5, 3, 4, 5, 6, 7, 8, 10, 15, 20, 25, 30, 40, 50, 100], float)
SPLIT_LOGS = np.r_[np.log(_SPLIT_RATIOS), -np.log(_SPLIT_RATIOS)]
SPLIT_TOL = 0.04           # |log ratio - log split| below this counts as a split
MAX_ABS_LOG = np.log(10.0)


def remove_split(x: float) -> float:
    """Strip a standard split ratio from a log share-count change; NaN if implausible."""
    if not np.isfinite(x):
        return np.nan
    d = np.abs(x - SPLIT_LOGS)
    j = int(np.argmin(d))
    if d[j] < SPLIT_TOL:
        x = x - SPLIT_LOGS[j]
    return x if abs(x) <= MAX_ABS_LOG else np.nan


def _symbol_issuance(dates: np.ndarray, facts: pd.DataFrame) -> dict:
    """Issuance columns for one symbol on each of `dates` (datetime64 array)."""
    out = {c: np.full(len(dates), np.nan) for c in ISSUANCE_COLS}
    if facts.empty:
        return out
    pe = facts["period_end"].to_numpy("datetime64[ns]")
    fl = facts["filed"].to_numpy("datetime64[ns]")
    val = facts["value"].to_numpy(float)
    # negative duration so that, after sorting ascending, the shortest period is last
    if "period_start" in facts.columns:
        dur = (facts["period_end"] - pd.to_datetime(facts["period_start"])).dt.days.fillna(0).to_numpy(float)
    else:
        dur = np.zeros(len(facts))
    neg_dur = -dur
    stale = np.timedelta64(_STALE_DAYS, "D")
    for k, t in enumerate(dates):
        vis = fl <= t
        if not vis.any():
            continue
        vpe, vfl, vval, vnd = pe[vis], fl[vis], val[vis], neg_dur[vis]
        # latest filed version of each visible period (shortest duration on ties)
        order = np.lexsort((vnd, vfl, vpe))
        vpe, vfl, vval = vpe[order], vfl[order], vval[order]
        last_of_pe = np.r_[vpe[1:] != vpe[:-1], True]
        vpe, vval = vpe[last_of_pe], vval[last_of_pe]
        p1, s1 = vpe[-1], vval[-1]
        if t - p1 > stale or not s1 > 0:
            continue
        for col, (lag, tol) in _LAGS.items():
            target = p1 - np.timedelta64(lag, "D")
            gap = np.abs(vpe - target)
            j = int(np.argmin(gap))
            if gap[j] > np.timedelta64(tol, "D") or not vval[j] > 0:
                continue
            out[col][k] = remove_split(np.log(s1 / vval[j]))
    return out


def issuance_features(facts: pd.DataFrame, grid: pd.DataFrame) -> pd.DataFrame:
    """Share-issuance features for every (symbol, date) in `grid`.

    facts: long fundamentals rows [symbol, tag, value, period_end, filed], optional period_start.
    grid:  [symbol, date].
    The first tag in SHARE_TAGS that a symbol reports is used for it.
    """
    g = grid[["symbol", "date"]].drop_duplicates().copy()
    g["date"] = pd.to_datetime(g["date"])
    empty = g.assign(**{c: np.nan for c in ISSUANCE_COLS})
    if facts.empty or g.empty:
        return empty
    f = facts[facts["tag"].isin(SHARE_TAGS)].copy()
    f["period_end"] = pd.to_datetime(f["period_end"])
    f["filed"] = pd.to_datetime(f["filed"])
    f["tag_rank"] = f["tag"].map({t: i for i, t in enumerate(SHARE_TAGS)})
    best = f.groupby("symbol")["tag_rank"].transform("min")
    f = f[f["tag_rank"] == best]
    f_by = {s: d for s, d in f.groupby("symbol", sort=False)}
    parts = []
    for sym, sub in g.groupby("symbol", sort=False):
        if sym not in f_by:
            continue
        dates = np.sort(sub["date"].to_numpy("datetime64[ns]"))
        vals = _symbol_issuance(dates, f_by[sym])
        parts.append(pd.DataFrame({"symbol": sym, "date": pd.to_datetime(dates), **vals}))
    if not parts:
        return empty
    got = pd.concat(parts, ignore_index=True)
    return g.merge(got, on=["symbol", "date"], how="left")


def winsorise_by_date(df: pd.DataFrame, cols: list[str], lo: float = 0.01, hi: float = 0.99) -> pd.DataFrame:
    """Clip each column at its lo/hi quantile within each market-date cross-section.

    Call on the WHOLE market (after chunks are joined), not on a symbol chunk.
    Uses only that date's cross-section, so it is backward-looking.
    """
    out = df.copy()
    keys = ["market", "date"] if "market" in out.columns else ["date"]
    for c in cols:
        if c not in out.columns:
            continue
        grp = out.groupby(keys, observed=True)[c]
        out[c] = out[c].clip(grp.transform(lambda s: s.quantile(lo)), grp.transform(lambda s: s.quantile(hi)))
    return out
