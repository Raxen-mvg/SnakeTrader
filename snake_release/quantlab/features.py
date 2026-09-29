"""Feature engineering and labels — the part where lookahead bias creeps in.

Every feature here is computed from data that was observable at the close of
the feature date, and every one is cross-sectionally ranked WITHIN a market on
each date. Two reasons for the ranking:

1. It makes US and Indian stocks comparable without fighting over currency,
   inflation, or the fact that Indian equities have had structurally higher
   nominal returns.
2. It absorbs regime shifts. A 6-month return of +30% meant something very
   different in April 2020 than in April 2023. Its RANK among peers is stable.

The factors included are the ones with documented out-of-sample premia across
markets and decades — value, quality, momentum, low volatility, size. That is
not the same as a promise they will work in your holding period. Value
underperformed for most of 2010-2020. Momentum crashes violently and
occasionally (April 2009, Feb 2021). These are long-horizon tendencies with
brutal interim drawdowns, not rules.

LOOKAHEAD CHECKLIST — every one of these has burned someone:
  * Returns use shift() so today's own return is never a feature for today.
  * Fundamentals join on `filed <= date`, never period_end (fundamentals.py).
  * Labels are strictly forward-looking and the validation split embargoes the
    label horizon (validation.py).
  * Cross-sectional ranks use only that date's cross-section — no full-sample
    statistics anywhere.
"""

from __future__ import annotations

import logging

import numpy as np
import pandas as pd

from .config import Config
from .db import DB
from .fundamentals import fundamentals_asof
from .share_issuance import ISSUANCE_COLS, SHARE_TAGS, issuance_features, winsorise_by_date

log = logging.getLogger("quantlab.features")

FUNDAMENTAL_TAGS = [
    "Revenues", "NetIncomeLoss", "GrossProfit", "OperatingIncomeLoss",
    "Assets", "AssetsCurrent", "Liabilities", "LiabilitiesCurrent",
    "StockholdersEquity", "CashAndCashEquivalentsAtCarryingValue",
    "LongTermDebt", "NetCashProvidedByUsedInOperatingActivities",
    "EarningsPerShareDiluted", "InventoryNet",
    "WeightedAverageNumberOfDilutedSharesOutstanding",
    "CommonStockSharesOutstanding",
]


# ---------------------------------------------------------------------------
# Price-derived features
# ---------------------------------------------------------------------------
def price_features(px: pd.DataFrame, bm: pd.DataFrame | None = None) -> pd.DataFrame:
    """Momentum, volatility, liquidity, reversal features from the price panel.

    px: [symbol, market, date, adj_close, close, volume]
    """
    if px.empty:
        return pd.DataFrame()

    df = px.sort_values(["symbol", "date"]).copy()
    df["date"] = pd.to_datetime(df["date"])
    g = df.groupby("symbol", observed=True, sort=False)

    df["ret_1d"] = g["adj_close"].pct_change()

    # --- Momentum -----------------------------------------------------------
    # 12-1 momentum: the classic. The most recent month is EXCLUDED because
    # short-term reversal works against you there; Jegadeesh-Titman found the
    # skip-month formulation is what actually carries the premium.
    for name, lb in (("mom_1m", 21), ("mom_3m", 63), ("mom_6m", 126), ("mom_12m", 252)):
        df[name] = g["adj_close"].transform(lambda s, lb=lb: s / s.shift(lb) - 1.0)
    df["mom_12_1"] = g["adj_close"].transform(
        lambda s: s.shift(21) / s.shift(252) - 1.0)

    # Short-term reversal: last week's move tends to partially reverse.
    df["reversal_5d"] = g["adj_close"].transform(lambda s: s / s.shift(5) - 1.0)

    # --- Volatility ---------------------------------------------------------
    # Low-volatility anomaly: low-vol stocks have historically delivered
    # similar or better risk-adjusted returns than high-vol ones, which
    # contradicts CAPM and has persisted anyway.
    df["vol_21d"] = g["ret_1d"].transform(
        lambda s: s.shift(1).rolling(21, min_periods=15).std() * np.sqrt(252))
    df["vol_63d"] = g["ret_1d"].transform(
        lambda s: s.shift(1).rolling(63, min_periods=40).std() * np.sqrt(252))
    df["vol_252d"] = g["ret_1d"].transform(
        lambda s: s.shift(1).rolling(252, min_periods=150).std() * np.sqrt(252))
    # Volatility trend: rising vol often precedes trouble.
    df["vol_ratio"] = df["vol_21d"] / df["vol_252d"].replace(0, np.nan)

    # Downside deviation, and worst single day in the last quarter.
    df["downside_vol_63d"] = g["ret_1d"].transform(
        lambda s: s.shift(1).where(s.shift(1) < 0).rolling(63, min_periods=20).std()
        * np.sqrt(252))
    df["max_drawdown_1d_63"] = g["ret_1d"].transform(
        lambda s: s.shift(1).rolling(63, min_periods=20).min())

    # --- Trend / position ---------------------------------------------------
    df["ma_50"] = g["adj_close"].transform(
        lambda s: s.shift(1).rolling(50, min_periods=30).mean())
    df["ma_200"] = g["adj_close"].transform(
        lambda s: s.shift(1).rolling(200, min_periods=120).mean())
    df["px_to_ma50"] = df["adj_close"] / df["ma_50"] - 1.0
    df["px_to_ma200"] = df["adj_close"] / df["ma_200"] - 1.0
    # Proximity to 52-week high — momentum in a bounded form, often stronger
    # than raw momentum (George & Hwang).
    df["high_52w"] = g["adj_close"].transform(
        lambda s: s.shift(1).rolling(252, min_periods=150).max())
    df["pct_of_52w_high"] = df["adj_close"] / df["high_52w"]

    # --- Liquidity ----------------------------------------------------------
    df["turnover"] = df["close"] * df["volume"]
    df["log_turnover_21d"] = np.log1p(
        g["turnover"].transform(lambda s: s.shift(1).rolling(21, min_periods=10).mean()))
    # Amihud illiquidity: |return| per unit of turnover. High = your own order
    # moves the price. A crucial control: many "anomalies" are just illiquidity
    # premia you cannot actually harvest.
    illiq = df["ret_1d"].abs() / df["turnover"].replace(0, np.nan)
    df["amihud_21d"] = (illiq.groupby(df["symbol"], observed=True)
                        .transform(lambda s: s.shift(1).rolling(21, min_periods=10).mean()))
    df["volume_trend"] = (
        g["volume"].transform(lambda s: s.shift(1).rolling(21, min_periods=10).mean())
        / g["volume"].transform(lambda s: s.shift(1).rolling(252, min_periods=120).mean())
    )

    # --- Market-relative ----------------------------------------------------
    if bm is not None and not bm.empty:
        b = bm.sort_values("date").copy()
        b["date"] = pd.to_datetime(b["date"])
        b["mkt_ret"] = b["adj_close"].pct_change()
        b["mkt_mom_126"] = b["adj_close"] / b["adj_close"].shift(126) - 1.0
        df = df.merge(b[["date", "mkt_ret", "mkt_mom_126"]], on="date", how="left")
        df["beta_252d"] = _rolling_beta(df, 252, 150)
        # Idiosyncratic volatility — the part not explained by the market.
        df["idio_vol_63d"] = _idio_vol(df, 63, 40)
        # Relative strength vs the index.
        df["rel_mom_126"] = df["mom_6m"] - df["mkt_mom_126"]

    # --- Behavioural ----------------------------------------------------------
    # Lottery demand (Bali, Cakici & Whitelaw 2011): stocks with extreme recent
    # up-days are bid up by lottery-seeking investors and subsequently lag.
    df["max_ret_21d"] = g["ret_1d"].transform(lambda s: s.shift(1).rolling(21, min_periods=15).max())
    # Skewness of daily returns: positively skewed stocks are overpriced
    # (Boyer, Mitton & Vorkink 2010).
    df["skew_63d"] = g["ret_1d"].transform(lambda s: s.shift(1).rolling(63, min_periods=40).skew())
    # Capital-gains overhang (Grinblatt & Han 2005): price vs a volume-weighted
    # reference price. The disposition effect makes holders with gains sell too
    # early, which delays price discovery and produces momentum.
    pv = df["adj_close"] * df["volume"]
    ref = (pv.groupby(df["symbol"], observed=True).transform(lambda s: s.shift(1).rolling(252, min_periods=120).sum())
           / g["volume"].transform(lambda s: s.shift(1).rolling(252, min_periods=120).sum()).replace(0, np.nan))
    df["cg_overhang"] = df["adj_close"] / ref - 1.0
    # Attention: abnormal volume spike in the last week vs the last year.
    df["attention_5d"] = (g["volume"].transform(lambda s: s.shift(1).rolling(5, min_periods=3).mean())
                          / g["volume"].transform(lambda s: s.shift(1).rolling(252, min_periods=120).median()
                                                  ).replace(0, np.nan))
    # Seasonality (Heston & Sadka 2008): a stock's return in the same calendar
    # month in prior years predicts its return this month.
    df["seasonal_same_month"] = g["adj_close"].transform(
        lambda s: (s.shift(252 - 21) / s.shift(252) - 1.0 + s.shift(504 - 21) / s.shift(504) - 1.0) / 2.0)

    # --- Nonlinear dynamics -------------------------------------------------
    # Complexity measures capture structure that moments and autocorrelation
    # miss: how predictable a stock's return sequence currently is, and whether
    # it sits in a trending or a mean-reverting phase. The DFA exponent is the
    # economically useful one — it says which of momentum or reversal deserves
    # trust for THIS name right now, instead of assuming one globally.
    from quant_math.chaos import dfa_alpha, rolling_permutation_entropy

    def _pe(s: pd.Series) -> pd.Series:
        v = rolling_permutation_entropy(s.shift(1).to_numpy(dtype=float),
                                        window=252, order=4, min_periods=120)
        return pd.Series(v, index=s.index)

    def _dfa(s: pd.Series, window: int = 252, step: int = 21) -> pd.Series:
        a = s.shift(1).to_numpy(dtype=float)
        out = np.full(len(a), np.nan)
        for i in range(window - 1, len(a), step):      # monthly, held between
            out[i] = dfa_alpha(a[i - window + 1: i + 1])
        return pd.Series(out, index=s.index).ffill()

    df["perm_entropy_252d"] = g["ret_1d"].transform(_pe)
    df["dfa_alpha_252d"] = g["ret_1d"].transform(_dfa)

    drop = ["ma_50", "ma_200", "high_52w", "turnover", "mkt_mom_126"]
    return df.drop(columns=[c for c in drop if c in df.columns])


def event_features(events: pd.DataFrame, grid: pd.DataFrame) -> pd.DataFrame:
    """News-shock features from the abnormal-return event library.

    For every (symbol, grid date) uses only events dated strictly before it:
    the signed size of the latest shock, its post-event drift so far, how long
    ago it was, and how often the stock has been shocked. This is what lets
    the model learn over-reaction (reversal) vs under-reaction (drift) by
    event profile, in every market, whether or not a headline is available.
    """
    if events.empty or grid.empty:
        return pd.DataFrame(columns=["symbol", "date"])
    ev = events[["symbol", "date", "std_abnormal", "car", "volume_z"]].copy()
    ev["date"] = pd.to_datetime(ev["date"])
    ev = ev.sort_values("date")
    g = grid[["symbol", "date"]].copy()
    g["date"] = pd.to_datetime(g["date"])
    g = g.sort_values("date")
    # strictly before: shift the event one day so a same-day event is excluded
    ev["avail"] = ev["date"] + pd.Timedelta(days=1)
    last = pd.merge_asof(g, ev.rename(columns={"date": "ev_date"}), left_on="date", right_on="avail",
                         by="symbol", direction="backward")
    last["days_since_event"] = (last["date"] - last["ev_date"]).dt.days
    recent = last["days_since_event"] <= 126
    last["last_shock_sar"] = last["std_abnormal"].where(recent)
    last["last_shock_car"] = last["car"].where(recent)
    last["last_shock_volz"] = last["volume_z"].where(recent)
    last["days_since_event"] = last["days_since_event"].clip(upper=756)

    # Event frequency over the past year, vectorised: running event count per
    # symbol, looked up at t and at t-365d.
    ev = ev.sort_values(["avail"])
    ev["k"] = ev.groupby("symbol").cumcount() + 1
    kk = ev[["symbol", "avail", "k"]]
    now = pd.merge_asof(last[["symbol", "date"]].reset_index(), kk, left_on="date",
                        right_on="avail", by="symbol", direction="backward")
    then = last[["symbol", "date"]].reset_index()
    then["date"] = then["date"] - pd.Timedelta(days=365)
    then = pd.merge_asof(then.sort_values("date"), kk, left_on="date", right_on="avail",
                         by="symbol", direction="backward").set_index("index")
    now = now.set_index("index")
    last["events_365d"] = (now["k"].fillna(0) - then["k"].reindex(now.index).fillna(0)).astype(int)
    return last[["symbol", "date", "last_shock_sar", "last_shock_car", "last_shock_volz",
                 "days_since_event", "events_365d"]]


def _rolling_beta(df: pd.DataFrame, window: int, min_periods: int) -> pd.Series:
    """Rolling beta via covariance ratio. Excludes the current day."""
    out = pd.Series(index=df.index, dtype=float)
    for sym, idx in df.groupby("symbol", observed=True, sort=False).groups.items():
        sub = df.loc[idx]
        r = sub["ret_1d"].shift(1)
        m = sub["mkt_ret"].shift(1)
        cov = r.rolling(window, min_periods=min_periods).cov(m)
        var = m.rolling(window, min_periods=min_periods).var()
        out.loc[idx] = (cov / var.replace(0, np.nan)).clip(-4, 4)
    return out


def _idio_vol(df: pd.DataFrame, window: int, min_periods: int) -> pd.Series:
    out = pd.Series(index=df.index, dtype=float)
    for sym, idx in df.groupby("symbol", observed=True, sort=False).groups.items():
        sub = df.loc[idx]
        r = sub["ret_1d"].shift(1)
        m = sub["mkt_ret"].shift(1)
        cov = r.rolling(window, min_periods=min_periods).cov(m)
        var = m.rolling(window, min_periods=min_periods).var()
        beta = (cov / var.replace(0, np.nan)).clip(-4, 4)
        resid = r - beta * m
        out.loc[idx] = resid.rolling(window, min_periods=min_periods).std() * np.sqrt(252)
    return out


# ---------------------------------------------------------------------------
# Fundamental features
# ---------------------------------------------------------------------------
def fundamental_features(fund: pd.DataFrame, px: pd.DataFrame) -> pd.DataFrame:
    """Value and quality ratios from point-in-time fundamentals.

    Market cap uses shares outstanding as last reported, which is imperfect
    (buybacks and issuance between filings are invisible) but it is what was
    knowable at the time. A data vendor's "current shares outstanding" applied
    to a historical date is lookahead bias.
    """
    if fund.empty:
        return pd.DataFrame()

    f = fund.copy()
    f["date"] = pd.to_datetime(f["date"])
    p = px[["symbol", "date", "adj_close", "close"]].copy()
    p["date"] = pd.to_datetime(p["date"])
    df = f.merge(p, on=["symbol", "date"], how="left")

    shares = df.get("WeightedAverageNumberOfDilutedSharesOutstanding")
    if shares is None:
        shares = df.get("CommonStockSharesOutstanding")
    if shares is None:
        shares = pd.Series(np.nan, index=df.index)
    df["shares"] = pd.to_numeric(shares, errors="coerce")
    df["market_cap"] = df["close"] * df["shares"]

    def safe(num, den):
        n = pd.to_numeric(df.get(num), errors="coerce") if isinstance(num, str) else num
        d = pd.to_numeric(df.get(den), errors="coerce") if isinstance(den, str) else den
        if n is None or d is None:
            return pd.Series(np.nan, index=df.index)
        return n / d.replace(0, np.nan)

    # --- Value: cheapness. Yields not multiples, so negatives stay ordered.
    # (A P/E of -5 is not "cheaper" than a P/E of 10; an earnings yield of
    # -20% is correctly worse than +10%.)
    df["earnings_yield"] = safe("NetIncomeLoss", "market_cap")
    df["book_to_price"] = safe("StockholdersEquity", "market_cap")
    df["sales_to_price"] = safe("Revenues", "market_cap")
    df["cashflow_yield"] = safe("NetCashProvidedByUsedInOperatingActivities", "market_cap")

    # --- Quality: profitability and balance-sheet strength.
    df["roe"] = safe("NetIncomeLoss", "StockholdersEquity")
    df["roa"] = safe("NetIncomeLoss", "Assets")
    df["gross_margin"] = safe("GrossProfit", "Revenues")
    df["operating_margin"] = safe("OperatingIncomeLoss", "Revenues")
    df["net_margin"] = safe("NetIncomeLoss", "Revenues")
    # Gross profitability scaled by assets — Novy-Marx's measure, which has
    # held up better out of sample than most quality definitions.
    df["gross_profitability"] = safe("GrossProfit", "Assets")
    df["debt_to_equity"] = safe("LongTermDebt", "StockholdersEquity")
    df["current_ratio"] = safe("AssetsCurrent", "LiabilitiesCurrent")
    df["cash_to_assets"] = safe("CashAndCashEquivalentsAtCarryingValue", "Assets")
    # Accruals: earnings not backed by cash. Strongly NEGATIVE predictor —
    # high accruals precede disappointments (Sloan 1996).
    ni = pd.to_numeric(df.get("NetIncomeLoss"), errors="coerce")
    cfo = pd.to_numeric(df.get("NetCashProvidedByUsedInOperatingActivities"),
                        errors="coerce")
    assets = pd.to_numeric(df.get("Assets"), errors="coerce")
    df["accruals"] = (ni - cfo) / assets.replace(0, np.nan)

    df["log_market_cap"] = np.log(df["market_cap"].where(df["market_cap"] > 0))

    keep = ["symbol", "date", "market_cap", "log_market_cap", "earnings_yield",
            "book_to_price", "sales_to_price", "cashflow_yield", "roe", "roa",
            "gross_margin", "operating_margin", "net_margin",
            "gross_profitability", "debt_to_equity", "current_ratio",
            "cash_to_assets", "accruals"]
    return df[[c for c in keep if c in df.columns]]


# ---------------------------------------------------------------------------
# Cross-sectional normalisation + labels
# ---------------------------------------------------------------------------
def cross_sectional_rank(df: pd.DataFrame, cols: list[str],
                         group_cols: list[str] = ["market", "date"],
                         min_group: int = 20) -> pd.DataFrame:
    """Rank each feature within market-date, scaled to [-0.5, 0.5].

    Ranking rather than z-scoring is deliberate: financial cross-sections have
    fat tails, and a single extreme outlier destroys a z-score while barely
    moving a rank.
    """
    out = df.copy()
    sizes = out.groupby(group_cols, observed=True)[cols[0]].transform("size")
    valid = sizes >= min_group
    for c in cols:
        if c not in out.columns:
            continue
        r = out.groupby(group_cols, observed=True)[c].rank(pct=True, na_option="keep")
        out[f"z_{c}"] = (r - 0.5).where(valid)
    return out


def make_labels(px: pd.DataFrame, horizon: int = 21, entry_lag: int = 0) -> pd.DataFrame:
    """Forward returns and the cross-sectional rank target.

    Three labels:
      fwd_ret        — raw forward return over the horizon
      fwd_excess     — forward return minus that date's cross-sectional mean
                       (i.e. relative to the market), the honest target
      fwd_rank       — cross-sectional percentile of fwd_excess, in [0, 1]

    fwd_rank is what the model trains on. Predicting relative rank is a far
    better-posed problem than predicting price level or absolute return: it
    strips out the market factor, which nobody can forecast, and leaves the
    cross-sectional question, which is where documented edge lives.
    """
    df = px.sort_values(["symbol", "date"]).copy()
    df["date"] = pd.to_datetime(df["date"])
    g = df.groupby("symbol", observed=True, sort=False)

    # Forward return. shift(-h) looks into the FUTURE on purpose - that is the
    # label. The embargo in validation.py is what stops it leaking into
    # training.
    #
    # entry_lag exists because the features are built from day t's close, and nobody
    # can buy at a close they are still using to decide. With entry_lag = 1 the trade
    # is bought at the NEXT session's close and held for the same number of sessions,
    # which is a price that can actually be obtained. Verified 2026-09-22 to cost
    # almost nothing in accuracy; the embargo must grow by the same number of days.
    df["fwd_ret"] = g["adj_close"].transform(
        lambda s: s.shift(-(horizon + entry_lag)) / s.shift(-entry_lag) - 1.0)

    gc = ["market", "date"] if "market" in df.columns else ["date"]
    df["fwd_excess"] = df["fwd_ret"] - df.groupby(gc, observed=True)["fwd_ret"].transform("mean")
    df["fwd_rank"] = df.groupby(gc, observed=True)["fwd_excess"].rank(pct=True)
    return df[["symbol", "date", "fwd_ret", "fwd_excess", "fwd_rank"]]


FEATURE_COLS_PRICE = [
    "mom_1m", "mom_3m", "mom_6m", "mom_12m", "mom_12_1", "reversal_5d",
    "vol_21d", "vol_63d", "vol_252d", "vol_ratio", "downside_vol_63d",
    "max_drawdown_1d_63", "px_to_ma50", "px_to_ma200", "pct_of_52w_high",
    "log_turnover_21d", "amihud_21d", "volume_trend", "beta_252d",
    "idio_vol_63d", "rel_mom_126",
    # behavioural
    "max_ret_21d", "skew_63d", "cg_overhang", "attention_5d", "seasonal_same_month",
    # nonlinear dynamics
    "perm_entropy_252d", "dfa_alpha_252d",
]
FEATURE_COLS_EVENT = [
    "last_shock_sar", "last_shock_car", "last_shock_volz", "days_since_event", "events_365d",
]
# Net share issuance (share_issuance.py). Built only when features.share_issuance
# is true; feature_list picks the columns up whenever they exist.
FEATURE_COLS_ISSUANCE = list(ISSUANCE_COLS)
FEATURE_COLS_FUND = [
    "log_market_cap", "earnings_yield", "book_to_price", "sales_to_price",
    "cashflow_yield", "roe", "roa", "gross_margin", "operating_margin",
    "net_margin", "gross_profitability", "debt_to_equity", "current_ratio",
    "cash_to_assets", "accruals",
]


def build_features(cfg: Config, db: DB, *, markets: list[str] | None = None,
                   rebalance_days: int | None = None,
                   liquid_only: bool = True) -> pd.DataFrame:
    """Build the full feature+label table and store it.

    Features are computed daily but SAMPLED every `rebalance_days`. Daily
    samples of a monthly-horizon label are ~95% redundant and they make
    validation look better than it is, because overlapping windows mean
    neighbouring rows share most of their label.
    """
    mcfg = cfg.section("model")
    horizon = int(mcfg.get("horizon_days", 21))
    step = int(rebalance_days or mcfg.get("rebalance_days", 21))
    markets = markets or cfg.markets
    chunk = int(cfg.section("features").get("chunk_symbols", 400))
    from .alpha_features import FEATURE_COLS_ALPHA, alpha_features
    from .context_features import FEATURE_COLS_PROB, probability_features
    fcfg = cfg.section("features")
    with_issuance = bool(fcfg.get("share_issuance", False))
    table = str(fcfg.get("table", "features"))
    # What the branch tests actually earned a place: the alpha formulas and the
    # probability profiles. Fourier cycles, chaos measures and news mood were run on
    # the same folds and did not beat the baseline, so they are not here.
    all_feats = (FEATURE_COLS_PRICE + FEATURE_COLS_FUND + FEATURE_COLS_EVENT
                 + FEATURE_COLS_ALPHA + FEATURE_COLS_PROB)
    if with_issuance:
        all_feats = all_feats + FEATURE_COLS_ISSUANCE

    frames = []
    for market in markets:
        syms = db.symbols(market=market, liquid_only=liquid_only, with_prices=True)
        if not syms:
            log.warning("No symbols for %s (liquid_only=%s)", market, liquid_only)
            continue
        cfg.resources.checkpoint(f"features {market}")
        bsym = benchmark_for(cfg, db, market)
        bm = (db.q("SELECT date, adj_close FROM benchmarks WHERE symbol = ? ORDER BY date", [bsym])
              if bsym else pd.DataFrame())
        # Rebalance grid from the market's own trading calendar, fixed before
        # chunking so every chunk samples the same dates.
        ph = ", ".join("?" for _ in syms)
        cal = db.q(f"SELECT DISTINCT date FROM prices WHERE symbol IN ({ph}) ORDER BY date", syms)
        dates = pd.to_datetime(cal["date"]).to_numpy()
        grid = set(pd.to_datetime(dates[::step]))
        # Always include the latest session: live scoring must use today's
        # cross-section, not the last grid point (up to step-1 days stale).
        # Its labels are NaN (future unknown), so it never enters training.
        grid.add(pd.Timestamp(dates[-1]))
        log.info("Building features for %s: %d symbols, benchmark=%s, %d grid dates",
                 market, len(syms), bsym, len(grid))

        parts = []
        for i in range(0, len(syms), chunk):
            px = db.price_panel(symbols=syms[i:i + chunk], market=market)
            if px.empty:
                continue
            pf = price_features(px, bm)
            pf = pf.merge(alpha_features(px, bm), on=["symbol", "date"], how="left")
            fwd = make_labels(px, horizon=horizon,
                              entry_lag=int(mcfg.get("entry_lag_days", 0)))[["symbol", "date", "fwd_ret"]]
            df = pf.merge(fwd, on=["symbol", "date"], how="left")
            df = df.merge(probability_features(px), on=["symbol", "date"], how="left")
            df = df[df["date"].isin(grid)]
            num = df.select_dtypes("float64").columns
            df[num] = df[num].astype("float32")
            try:
                fund_raw = fundamentals_asof(db, FUNDAMENTAL_TAGS, df[["symbol", "date"]])
                if not fund_raw.empty:
                    df = df.merge(fundamental_features(fund_raw, px), on=["symbol", "date"], how="left")
            except Exception as exc:
                log.debug("  %s chunk %d: fundamentals unavailable (%s)", market, i // chunk, exc)
            if with_issuance:
                chunk_syms = syms[i:i + chunk]
                tl = ", ".join(f"'{t}'" for t in SHARE_TAGS)
                facts = db.q(f"SELECT symbol, tag, value, period_start, period_end, filed FROM fundamentals "
                              f"WHERE tag IN ({tl}) AND symbol IN ({', '.join('?' for _ in chunk_syms)})",
                              chunk_syms)
                iss = issuance_features(facts, df[["symbol", "date"]])
                df = df.merge(iss, on=["symbol", "date"], how="left")
                df[ISSUANCE_COLS] = df[ISSUANCE_COLS].astype("float32")
            parts.append(df)
        if not parts:
            continue
        df = pd.concat(parts, ignore_index=True)
        del parts

        # --- era-neutral tradeability -------------------------------------
        # A fixed cash threshold ("$1m a day") silently deletes history: almost
        # no company traded $1m/day in 1975 nominal dollars, so every firm that
        # lived and died before the modern high-volume era vanishes — taking its
        # bankruptcy with it. That is survivorship bias re-entering through the
        # universe, and it inflated the first backtest badly (equal-weight US
        # universe returned 17.5% a year against a real ~11%).
        # Instead keep the most liquid share of each market ON EACH DATE, which
        # is inflation-proof and era-neutral. The absolute cash floor still
        # applies to live screening, where it belongs.
        pct = float(cfg.section("features").get("min_turnover_percentile", 0.4))
        if pct > 0 and "log_turnover_21d" in df.columns:
            before = len(df)
            liq_rank = df.groupby("date")["log_turnover_21d"].rank(pct=True)
            df = df[liq_rank >= pct]
            log.info("  %s: era-neutral liquidity kept %d/%d rows (top %.0f%% by turnover each date)",
                     market, len(df), before, 100 * (1 - pct))

        if with_issuance:
            df = winsorise_by_date(df, ISSUANCE_COLS)
            log.info("  %s: share issuance available on %.0f%% of rows", market,
                     100 * df["issuance_12m"].notna().mean())

        # Labels need the WHOLE market cross-section on each date.
        df["fwd_excess"] = df["fwd_ret"] - df.groupby("date")["fwd_ret"].transform("mean")
        df["fwd_rank"] = df.groupby("date")["fwd_excess"].rank(pct=True)

        ev = db.q("SELECT symbol, date, std_abnormal, car, volume_z FROM events WHERE market = ?",
                  [market])
        if not ev.empty:
            df = df.merge(event_features(ev, df[["symbol", "date"]]), on=["symbol", "date"], how="left")

        df["market"] = market
        cols = [c for c in all_feats if c in df.columns]
        df = cross_sectional_rank(df, cols)
        for c in cols:   # winsorise raw columns per market
            lo, hi = df[c].quantile([0.001, 0.999])
            df[c] = df[c].clip(lo, hi)
        zc = [f"z_{c}" for c in cols]
        df[zc] = df[zc].astype("float32")
        log.info("  %s: %d symbol-dates, %d features (fundamentals %.0f%%, events %.0f%%)",
                 market, len(df), len(cols),
                 100 * df["earnings_yield"].notna().mean() if "earnings_yield" in df else 0,
                 100 * df["last_shock_sar"].notna().mean() if "last_shock_sar" in df else 0)
        frames.append(df)

    if not frames:
        raise RuntimeError("No features built. Do you have prices? Check `run.py status`.")

    out = pd.concat(frames, ignore_index=True)
    out["date"] = pd.to_datetime(out["date"])
    from .context_features import attach_context
    try:
        out = attach_context(out)          # fear gauges: raw, one value per market-date
    except Exception as exc:
        log.warning("context features unavailable: %s", exc)
    # Experiments write their own table so they never overwrite the live one.
    db.replace_table_from_df(out, table)
    log.info("Features stored in %s: %d rows, %d markets (%s -> %s)", table, len(out), out["market"].nunique(),
             out["date"].min().date(), out["date"].max().date())
    return out


def benchmark_for(cfg: Config, db: DB, market: str) -> str | None:
    """Config benchmark, else the market's index from global_universe, else EW_<market>."""
    sym = cfg.section("prices").get("benchmarks", {}).get(market)
    if not sym:
        from .global_universe import MARKETS
        sym = MARKETS.get(market, (None, None, None))[1]
    have = set(db.q("SELECT DISTINCT symbol FROM benchmarks WHERE market = ?", [market])["symbol"])
    if sym in have:
        return sym
    return f"EW_{market}" if f"EW_{market}" in have else (sym if sym else None)


def feature_list(df: pd.DataFrame, ranked: bool = True) -> list[str]:
    """The model's input columns: the cross-sectionally ranked versions."""
    from .alpha_features import FEATURE_COLS_ALPHA
    from .context_features import FEATURE_COLS_CTX, FEATURE_COLS_PROB
    # Every adopted family is listed; only columns actually present are returned, so a
    # market or a run without one of them simply does not see it.
    base = (FEATURE_COLS_PRICE + FEATURE_COLS_FUND + FEATURE_COLS_EVENT
            + FEATURE_COLS_ALPHA + FEATURE_COLS_PROB + FEATURE_COLS_ISSUANCE)
    if ranked:
        # Context columns stay raw: ranking a value shared by every stock on a date
        # would erase it; the trees combine it with each stock's ranked traits.
        return [f"z_{c}" for c in base if f"z_{c}" in df.columns] + [c for c in FEATURE_COLS_CTX if c in df.columns]
    return [c for c in base if c in df.columns]
