"""Results-calendar and market-state features for SNAKE, built so that nothing reads the future.

RESULTS CALENDAR (per stock and date). A company must tell NSE days ahead that its board will meet
to approve results (collect_nse_board_meetings.py). That tells anyone WHEN news is coming, not
whether it is good, so the features are the ones the evidence says lean one way:

  cal_upcoming        1 if a results meeting has been announced and not yet held
  cal_sessions_to     trading sessions until that meeting, capped at 30 and scaled to [0, 1]
                      (1 when none is announced). Stocks tend to drift up into scheduled results
                      - the earnings-announcement premium - whatever the results turn out to be.
  cal_sessions_since  sessions since the last results meeting, capped at 126, scaled
  cal_last_reaction   the stock's move against the market from the close before its last results
                      meeting to two sessions after it. A strong reaction tends to be followed by
                      more of the same (post-earnings drift), and good results tend to be followed
                      by good results.
  cal_reaction_avg4   the mean of the last four such reactions: a track record
  cal_reaction_pos4   the share of the last four that were positive
  cal_peer_reaction   the mean last reaction of the same industry's companies whose results came
                      out in the past 42 sessions: a company still to report tends to follow its
                      peers, because customers, costs and demand are shared
  cal_has_data        1 once the board-meeting archive covers the date, 0 before - so the model can
                      tell "no calendar collected" from "no meeting announced"

Timing rules, the part that matters: a meeting is known only from its known_session (the session
after the intimation, if that came after the close). A reaction is known only once the second session
after the meeting has closed, and is used from the session after that.

MARKET STATE (the same for every stock on a date): the equal-weight Indian market built from every
stock's daily move (the average of moves clipped at 20%, so one bad print cannot swing it) -

  mkt_ret_5, mkt_ret_21, mkt_ret_63   market return over the past week, month and quarter
  mkt_above_200                       the market's level against its 200-session average
  mkt_breadth_50                      share of stocks above their own 50-session average
  mkt_vol_21                          the market's daily volatility over the past month
  mkt_disp_21                         how differently stocks moved over the past month

These are what a market filter needs: a network can learn that picks made in a falling, fragile
market pay less, and the backtest can test holding fewer names when the market is below its trend.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

BM_DB = r"C:\quantlab_data\nse_board_meetings.duckdb"
DAILY_IN = r"C:\quantlab_data\daily_in.duckdb"
CAP_TO, CAP_SINCE, PEER_WINDOW, REACT_AFTER = 30, 126, 42, 2

CAL_COLS = ["cal_has_data", "cal_upcoming", "cal_sessions_to", "cal_sessions_since",
            "cal_last_reaction", "cal_reaction_avg4", "cal_reaction_pos4", "cal_peer_reaction"]
MKT_COLS = ["mkt_ret_5", "mkt_ret_21", "mkt_ret_63", "mkt_above_200", "mkt_breadth_50",
            "mkt_vol_21", "mkt_disp_21"]


def load_prices(db: str = DAILY_IN, table: str = "features_daily") -> pd.DataFrame:
    import duckdb
    con = duckdb.connect(db, read_only=True)
    px = con.execute(f"SELECT symbol, date, adj_close FROM {table}").df()
    con.close()
    px["date"] = pd.to_datetime(px["date"])
    return px.sort_values(["symbol", "date"], ignore_index=True)


def market_features(px: pd.DataFrame) -> pd.DataFrame:
    """One row per date, from a (symbol, date, adj_close) panel."""
    p = px.sort_values(["symbol", "date"])
    g = p.groupby("symbol", sort=False)["adj_close"]
    r = g.pct_change()
    # A split or a bad print inside the panel shows up as an impossible day; it is not a return.
    r = r.where(r.abs() < 0.5)
    ma50 = g.transform(lambda s: s.rolling(50, min_periods=40).mean())
    r21 = g.pct_change(21)
    day = pd.DataFrame({"date": p["date"], "r": r, "above50": (p["adj_close"] > ma50).where(ma50.notna()),
                        "r21": r21.where(r21.abs() < 3)})
    # Each day's move is the average of stock moves clipped at +-20%: a median would sit below the
    # mean every day (returns are skewed) and drift the index into a permanent bear market.
    day["r"] = day["r"].clip(-0.2, 0.2)
    m = day.groupby("date").agg(r=("r", "mean"), breadth=("above50", "mean"),
                                disp=("r21", "std"), n=("r", "count")).sort_index()
    m = m[m["n"] >= 50]
    level = (1 + m["r"].fillna(0)).cumprod()
    out = pd.DataFrame(index=m.index)
    for w in (5, 21, 63):
        out[f"mkt_ret_{w}"] = level / level.shift(w) - 1
    out["mkt_above_200"] = level / level.rolling(200, min_periods=150).mean() - 1
    out["mkt_breadth_50"] = m["breadth"]
    out["mkt_vol_21"] = m["r"].rolling(21, min_periods=15).std()
    out["mkt_disp_21"] = m["disp"]
    return out.reset_index().astype({c: "float32" for c in MKT_COLS})


def _meetings(bm_db: str) -> pd.DataFrame:
    import duckdb
    con = duckdb.connect(bm_db, read_only=True)
    bm = con.execute("""SELECT symbol || '.NS' AS symbol, meeting_date, MIN(known_session) AS known,
                               ANY_VALUE(industry) AS industry
                        FROM board_meetings WHERE is_results GROUP BY 1, 2""").df()
    con.close()
    bm["meeting_date"] = pd.to_datetime(bm["meeting_date"])
    bm["known"] = pd.to_datetime(bm["known"])
    return bm.dropna(subset=["meeting_date", "known"])


def calendar_features(px: pd.DataFrame, bm_db: str = BM_DB,
                      mkt: pd.DataFrame | None = None) -> pd.DataFrame:
    """Per (symbol, date) results-calendar features for every row of the price panel."""
    bm = _meetings(bm_db)
    coverage = bm["known"].min() if len(bm) else pd.Timestamp.max
    p = px[["symbol", "date", "adj_close"]].sort_values(["symbol", "date"], ignore_index=True)
    p["rn"] = p.groupby("symbol", sort=False).cumcount()
    if mkt is None:
        mkt = market_features(px)
    mr = market_daily_returns(px)

    # Each meeting placed on the stock's own trading calendar: the first session on or after it.
    cal = p[["symbol", "date", "rn"]]
    bm = bm[bm["symbol"].isin(set(p["symbol"]))].sort_values("meeting_date")
    mt = pd.merge_asof(bm.sort_values("meeting_date"), cal.sort_values("date"),
                       left_on="meeting_date", right_on="date", by="symbol", direction="forward")
    # A meeting after the panel's last session is exactly the one a live model needs to see
    # coming: place it that many weekdays past the stock's last session.
    last = cal.groupby("symbol").agg(last_date=("date", "max"), last_rn=("rn", "max"))
    ahead = mt["rn"].isna()
    if ahead.any():
        lk = last.reindex(mt.loc[ahead, "symbol"])
        gap = np.busday_count(lk["last_date"].to_numpy().astype("datetime64[D]"),
                              mt.loc[ahead, "meeting_date"].to_numpy().astype("datetime64[D]"))
        mt.loc[ahead, "rn"] = lk["last_rn"].to_numpy() + np.maximum(gap, 1)
    mt = mt.dropna(subset=["rn"])
    mt["m_rn"] = mt["rn"].astype(int)
    kn = pd.merge_asof(mt.drop(columns=["date", "rn"]).sort_values("known"),
                       cal.rename(columns={"date": "k_date", "rn": "k_rn"}).sort_values("k_date"),
                       left_on="known", right_on="k_date", by="symbol", direction="forward")
    mt = kn.dropna(subset=["k_rn"]).copy()
    mt["k_rn"] = mt["k_rn"].astype(int)

    # The reaction: stock minus market, close before the meeting to REACT_AFTER sessions after.
    price = p.set_index(["symbol", "rn"])["adj_close"]
    dates = p.set_index(["symbol", "rn"])["date"]
    idx_b = list(zip(mt["symbol"], mt["m_rn"] - 1))
    idx_a = list(zip(mt["symbol"], mt["m_rn"] + REACT_AFTER))
    pb, pa = price.reindex(idx_b).to_numpy(), price.reindex(idx_a).to_numpy()
    db_, da_ = dates.reindex(idx_b).to_numpy(), dates.reindex(idx_a).to_numpy()
    lvl = (1 + mr.fillna(0)).cumprod()
    mb = lvl.reindex(pd.DatetimeIndex(db_)).to_numpy()
    ma = lvl.reindex(pd.DatetimeIndex(da_)).to_numpy()
    mt["reaction"] = np.clip((pa / pb - 1) - (ma / mb - 1), -0.3, 0.3)
    mt["r_rn"] = mt["m_rn"] + REACT_AFTER + 1          # first session the reaction may be used
    mt["r_date"] = dates.reindex(list(zip(mt["symbol"], mt["r_rn"]))).to_numpy()

    out = p[["symbol", "date", "rn"]].copy()
    # Upcoming: the nearest announced meeting with known <= today < meeting (+ the meeting day).
    up = {s: g for s, g in mt[["symbol", "k_rn", "m_rn"]].groupby("symbol")}
    nxt = np.full(len(out), np.nan)
    for sym, g in out.groupby("symbol", sort=False):
        u = up.get(sym)
        if u is None:
            continue
        rn = g["rn"].to_numpy()
        best = np.full(len(rn), np.inf)
        for k, m in zip(u["k_rn"].to_numpy(), u["m_rn"].to_numpy()):
            live = (rn >= k) & (rn <= m)
            best[live] = np.minimum(best[live], m - rn[live])
        best[np.isinf(best)] = np.nan
        nxt[g.index.to_numpy()] = best
    out["cal_upcoming"] = np.isfinite(nxt).astype("float32")
    out["cal_sessions_to"] = np.where(np.isfinite(nxt), np.minimum(nxt, CAP_TO) / CAP_TO, 1.0)

    # Since the last meeting, and the reaction track record, carried forward from when known.
    last = mt[["symbol", "m_rn"]].rename(columns={"m_rn": "last_m"}).sort_values("last_m")
    out = pd.merge_asof(out.sort_values("rn"), last, left_on="rn", right_on="last_m",
                        by="symbol", direction="backward")
    out["cal_sessions_since"] = (np.minimum(out["rn"] - out["last_m"], CAP_SINCE) / CAP_SINCE).fillna(1.0)

    rx = mt.dropna(subset=["reaction", "r_date"]).sort_values(["symbol", "r_rn"]).copy()
    grp = rx.groupby("symbol")["reaction"]
    rx["avg4"] = grp.transform(lambda s: s.rolling(4, min_periods=1).mean())
    rx["pos4"] = grp.transform(lambda s: (s > 0).astype(float).rolling(4, min_periods=1).mean())
    out = pd.merge_asof(out.sort_values("rn"),
                        rx[["symbol", "r_rn", "reaction", "avg4", "pos4"]].sort_values("r_rn"),
                        left_on="rn", right_on="r_rn", by="symbol", direction="backward")
    out["cal_last_reaction"] = out["reaction"].fillna(0.0)
    out["cal_reaction_avg4"] = out["avg4"].fillna(0.0)
    out["cal_reaction_pos4"] = out["pos4"].fillna(0.5)

    # Peers: same industry, reaction known within the past PEER_WINDOW calendar-trading days.
    ind = bm.groupby("symbol")["industry"].agg(lambda s: s.mode().iat[0] if len(s.mode()) else "")
    rx["industry"] = rx["symbol"].map(ind)
    rx["r_date"] = pd.to_datetime(rx["r_date"])
    daily = (rx.groupby(["industry", "r_date"])["reaction"].agg(["sum", "count"])
             .reset_index().sort_values("r_date"))
    all_dates = pd.DatetimeIndex(sorted(out["date"].unique()))
    peer = {}
    for industry, g in daily.groupby("industry"):
        s = g.set_index("r_date")[["sum", "count"]].reindex(all_dates, fill_value=0)
        roll = s.rolling(PEER_WINDOW, min_periods=1).sum()
        peer[industry] = roll
    out["industry"] = out["symbol"].map(ind)
    vals = np.zeros(len(out), dtype="float32")
    for industry, g in out.groupby("industry"):
        if industry not in peer:
            continue
        roll = peer[industry].reindex(pd.DatetimeIndex(g["date"]))
        sm, ct = roll["sum"].to_numpy(), roll["count"].to_numpy()
        # Leave the stock's own reaction out if it falls inside the window.
        mine = g["reaction"].where((g["rn"] - g["r_rn"]) < PEER_WINDOW).fillna(0).to_numpy()
        has = ((g["rn"] - g["r_rn"]) < PEER_WINDOW).fillna(False).to_numpy()
        sm, ct = sm - mine, ct - has.astype(int)
        vals[g.index.to_numpy()] = np.where(ct > 0, sm / np.maximum(ct, 1), 0.0)
    out["cal_peer_reaction"] = vals

    out["cal_has_data"] = (out["date"] >= coverage).astype("float32")
    for c in CAL_COLS[1:]:
        out[c] = out[c].astype("float32")
        out.loc[out["cal_has_data"] == 0, c] = 0.0
    return out[["symbol", "date"] + CAL_COLS]


def market_daily_returns(px: pd.DataFrame) -> pd.Series:
    p = px.sort_values(["symbol", "date"])
    r = p.groupby("symbol", sort=False)["adj_close"].pct_change()
    r = r.where(r.abs() < 0.5)
    return pd.Series(r.clip(-0.2, 0.2).values, index=p["date"].values).groupby(level=0).mean().sort_index()


def all_features(px: pd.DataFrame, bm_db: str = BM_DB) -> pd.DataFrame:
    """Calendar and market features for every (symbol, date) of the panel."""
    mkt = market_features(px)
    cal = calendar_features(px, bm_db, mkt)
    return cal.merge(mkt, on="date", how="left")
