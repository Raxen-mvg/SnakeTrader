"""How SNAKE turns predictions into rupees, and how its book is walked forward in a backtest.

The same two functions serve the backtest and the live account, so the rule that is measured is the
rule that trades:

  calibrate   what the top decile of each horizon's prediction actually paid, measured only on rows
              before the date in question. This converts a predicted rank into an expected return.
  expected    for every name, the best expected return across horizons.

The backtest ledger is the one validated on 2026-09-29 after the first daily simulator produced
nonsense: one ledger of cash plus the current value of each holding, every holding aged and sellable
whether or not it is in that day's liquid universe, and a canary that refuses to report anything
compounding above sixty percent a year or drawing down past minus one hundred percent.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from .model import HORIZONS

ACCOUNT = 200_000.0
TOP_K = 6
DISASTER_STOP = -0.25
CREDIBLE_CAGR = 0.60

BUY_PCT = 0.001 + 0.00015 + 0.0000297 + 0.000001 + 0.0015
SELL_PCT = 0.001 + 0.0000297 + 0.000001 + 0.0015
DP_FEE = 15.93
ETF_BUY = 0.0005 + 0.0000297 + 0.000001 + 0.00015      # slippage, exchange, SEBI, stamp
ETF_SELL = 0.0005 + 0.0000297 + 0.000001 + 0.00001     # slippage, exchange, SEBI, STT


def round_trip(ticket: float) -> float:
    return BUY_PCT + SELL_PCT + DP_FEE / max(ticket, 1.0)


def calibrate(rows: pd.DataFrame) -> dict[int, float]:
    """Top-decile realised forward return per horizon, from the rows given (all in the past)."""
    cal = {}
    for h in HORIZONS:
        p, r = f"p{h}", f"fwd_ret_{h}"
        if p not in rows.columns or r not in rows.columns:
            cal[h] = 0.0
            continue
        s = rows[[p, r]].dropna()
        if len(s) < 5_000:
            cal[h] = 0.0
            continue
        top = s[s[p] >= s[p].quantile(0.90)]
        cal[h] = float(top[r].clip(-0.5, 1.0).mean())
    return cal


def expected(day: pd.DataFrame, cal: dict[int, float]) -> pd.Series:
    """Best expected return across horizons for every name on one date."""
    best = None
    for h in HORIZONS:
        p = f"p{h}"
        if p not in day.columns:
            continue
        e = (day[p].rank(pct=True) - 0.5) * 2.0 * cal.get(h, 0.0)
        best = e if best is None else np.maximum(best, e)
    return best if best is not None else pd.Series(0.0, index=day.index)


def simulate(d: pd.DataFrame, min_names: int = 50, market_filter: str = "",
             filter_names: int = 3, sizing_power: float = 0.0, size_lo: float = 0.5,
             size_hi: float = 1.6, max_weight: float = 0.30, take_profit: float = 0.0,
             rotate_margin: float = 0.0, rotate_max: int = 1,
             sleeve: pd.DataFrame | None = None,
             first_session: bool = False, trace: list | None = None,
             exit_policy=None, exact_timing: bool = False,
             vol_power: float = 0.0, meta: pd.Series | None = None, meta_min: float = 0.0,
             meta_power: float = 0.0, start_date=None, extra_cost: float = 0.0,
             skip_entry_move: float = 0.0, entry_gate: pd.Series | None = None,
             gate_min: float = 0.0, gate_fill_next: bool = False) -> tuple[dict, pd.DataFrame]:
    """Walk Rs 2 lakh forward a session at a time, the model choosing when to sell.

    market_filter caps how many names may be HELD when the market looks weak, using only columns
    known on the day (snake/calendar.py): "" none; "trend" when the equal-weight market is below
    its 200-session average; "trend_breadth" when it is below trend AND under half of stocks are
    above their own 50-session average. Existing holdings are never force-sold by the filter;
    it only stops new buying above filter_names.

    sizing_power > 0 sizes each new buy by conviction instead of equally: the standard ticket times
    (its expected return / the average expected return of the book plus today's buys) ** power,
    clipped to [size_lo, size_hi] times the standard ticket and to max_weight of the account. A name
    the model expects 1.5x the average from gets roughly 1.5x the money at power 1.

    take_profit > 0 sells a holding once its gain reaches take_profit times the return the model
    expected when it was bought ("sell when it has made what it was bought for").

    rotate_margin > 0 swaps the weakest holding for the best name not held, at most rotate_max a
    day, when the newcomer's expected return beats the holding's by more than the whole cost of
    switching (the sale, the purchase, the depository charge) plus rotate_margin.

    sleeve parks idle cash in an exchange-traded fund instead of leaving it at zero: a frame with
    columns date, r1 (the fund's return over the same session a stock's fwd_ret_1 covers) and
    switch (True when the sleeve changes fund that day, which costs a round trip). Money moves
    in and out only as the stock book needs it, paying ETF charges each way.

    Take-profit is a resting limit order at the target price: when a close reaches the target the
    sale is credited AT the target, never at the higher close. Crediting the close would let the
    rule sell at a price it could only have known afterwards.

    first_session=True credits a new holding with its first session's return (fwd_ret_1 on the day
    it is bought: close after entry to the next close). Without it every trade silently skips that
    session, which matters more the more often a rule trades.

    trace, if a list, receives one row per held position per session (its state before the exit
    decision, plus the day's best names not held) - the training data for snake/exit_model.py.

    exit_policy, if given, is called once a session as exit_policy(dt, positions, fresh) with the
    held positions' states and the best names not held, and returns the symbols to sell; it adds to
    the usual exits rather than replacing the disaster stop.

    exact_timing=True is the honest clock, and what every comparison from 2026-10-01 uses. A row
    dated t carries what is known at t's close; a sale or purchase decided on it executes at the
    NEXT close. A holding's value before t's update already runs to that next close, so a sale the
    model decides is credited at it - not a session later, which also counted that session twice
    when the cash went straight into a new name. Resting orders (the disaster stop, take-profit)
    are checked against the later close: the stop fills at that close, the take-profit at its
    target. New names earn from their entry close (first_session).
    """
    if exact_timing:
        first_session = True
    BUY, SELL = BUY_PCT + extra_cost, SELL_PCT + extra_cost
    # entry_gate (snake/entry_timing.py, ANACONDA): the deepest dip expected after buying each
    # (symbol, date). A name whose expected dip is below -gate_min is not bought today - it waits,
    # and is bought on a later day when the dip has passed, if SNAKE still ranks it.
    # Audit knobs (2026-10-02): extra_cost is added to the slippage on EVERY buy and sell (small
    # companies cost more to trade than the 0.15% assumed); skip_entry_move > 0 refuses a purchase
    # whose entry session rose by at least that much (an entry_move column), because a stock locked
    # at its upper price band has no sellers and the fill is fiction.
    # start_date: begin with Rs 2 lakh on this date, while calibrating on everything before it, so the
    # same history can be walked from many starting points and a result judged across them.
    # meta (snake/meta_label.py): P(the pick pays after costs) per (symbol, date). Picks below
    # meta_min are skipped; meta_power > 0 scales stakes by (P / the day's average P) ** meta_power.
    # vol_power > 0 also scales each stake by (the day's median volatility / the stock's own) ** power,
    # within the same bounds as conviction: calmer names get more, wilder names less. Needs a vol_21d
    # column (the stock's 21-session volatility, known at the day's close).
    dates = list(pd.DatetimeIndex(sorted(d["date"].unique())))
    by_date = {dt: g.set_index("symbol") for dt, g in d.groupby("date", sort=False)}
    # Calibrate only on stocks the account could have bought: the least-traded names move far
    # more, and letting them set the scale would overstate what a tradable pick is worth.
    cal_src = d[d["tradable"].astype(bool)] if "tradable" in d.columns else d
    cal_by_year = {y: calibrate(cal_src[cal_src["date"] < pd.Timestamp(f"{y}-01-01")])
                   for y in sorted({dt.year for dt in dates})}

    cash, book, path, holds, rets = ACCOUNT, {}, [], [], []
    sl_val = 0.0
    sl = sleeve.set_index("date") if sleeve is not None else None
    for dt in dates:
        if start_date is not None and dt < pd.Timestamp(start_date):
            continue
        day = by_date.get(dt)
        if day is None or len(day) < min_names:
            continue
        if sl is not None and sl_val > 0 and dt in sl.index:
            row = sl.loc[dt]
            sl_val *= 1.0 + (float(row["r1"]) if pd.notna(row["r1"]) else 0.0)
            if bool(row["switch"]):
                sl_val *= 1.0 - ETF_BUY - ETF_SELL
        exp_all = expected(day, cal_by_year[dt.year])
        fresh = None
        if trace is not None or exit_policy is not None:
            pool = exp_all[~exp_all.index.isin(book)].dropna()
            if "tradable" in day.columns:
                pool = pool[pool.index.isin(day.index[day["tradable"].astype(bool)])]
            fresh = pool.nlargest(3)
        policy_sells: set = set()
        if exit_policy is not None and book:
            states = []
            for sym, pos in book.items():
                states.append({"symbol": sym, "entry": pos["entry_date"], "age": pos["age"] + 1,
                               "expected": float(exp_all.get(sym, pos["expected"])),
                               "entry_exp": pos["entry_exp"]})
            policy_sells = set(exit_policy(dt, states, fresh))
        for sym in list(book):
            pos = book[sym]
            pos["age"] += 1
            pre = pos["value"]
            pos["pre_value"] = pre
            if sym in day.index:
                r1 = day.at[sym, "fwd_ret_1"]
                if pd.notna(r1):
                    pos["value"] *= 1.0 + float(r1)
                pos["expected"] = float(exp_all.get(sym, 0.0))
                pos["stale"] = 0
            else:
                pos["stale"] += 1
            if exact_timing:
                decided = (sym in policy_sells or pos["stale"] > 10
                           or pos["expected"] <= (pre * SELL + DP_FEE) / max(pre, 1.0))
                post_ret = pos["value"] / pos["ticket"] - 1.0
                tp = take_profit > 0 and post_ret >= take_profit * pos.get("entry_exp", np.inf)
                if trace is not None and fresh is not None:
                    trace.append({"symbol": sym, "entry": pos["entry_date"], "date": dt,
                                  "age": pos["age"], "expected": pos["expected"],
                                  "entry_exp": pos["entry_exp"],
                                  "fresh_exp": float(fresh.mean()) if len(fresh) else 0.0,
                                  "fresh_syms": ",".join(fresh.index)})
                if decided:
                    fill = pre                                  # executes at the next close
                elif post_ret <= DISASTER_STOP:
                    fill = pos["value"]                         # the stop fills at that close
                elif tp:
                    fill = pos["ticket"] * (1.0 + take_profit * pos["entry_exp"])
                else:
                    continue
                cash += fill - (fill * SELL + DP_FEE)
                holds.append(pos["age"])
                rets.append(fill / pos["ticket"] - 1.0)
                del book[sym]
                continue
            ret = pos["value"] / pos["ticket"] - 1.0
            exit_cost = pos["value"] * SELL + DP_FEE
            if trace is not None and fresh is not None:
                trace.append({"symbol": sym, "entry": pos["entry_date"], "date": dt,
                              "age": pos["age"], "expected": pos["expected"],
                              "entry_exp": pos["entry_exp"], "fresh_exp": float(fresh.mean()) if len(fresh) else 0.0,
                              "fresh_syms": ",".join(fresh.index)})
            hit = take_profit > 0 and ret >= take_profit * pos.get("entry_exp", np.inf)
            if hit:                                   # the resting limit order fills at the target
                pos["value"] = pos["ticket"] * (1.0 + take_profit * pos["entry_exp"])
                ret = pos["value"] / pos["ticket"] - 1.0
                exit_cost = pos["value"] * SELL + DP_FEE
            leave = (hit or sym in policy_sells or ret <= DISASTER_STOP
                     or pos["expected"] <= exit_cost / max(pos["value"], 1.0) or pos["stale"] > 10)
            if leave:
                cash += pos["value"] - exit_cost
                holds.append(pos["age"])
                rets.append(ret)
                del book[sym]
        cap = TOP_K
        if market_filter and ("mkt_above_200" in day.columns or "mkt_weak" in day.columns):
            m = day.iloc[0]
            weak = pd.notna(m.get("mkt_above_200")) and m.get("mkt_above_200") < 0
            if market_filter == "flag":
                weak = bool(m.get("mkt_weak", False))
            if market_filter == "trend_breadth":
                weak = weak and pd.notna(m.get("mkt_breadth_50")) and m["mkt_breadth_50"] < 0.5
            if weak:
                cap = filter_names
        if rotate_margin > 0 and len(book) >= cap:
            pool = exp_all[~exp_all.index.isin(book)].dropna()
            if "tradable" in day.columns:
                pool = pool[pool.index.isin(day.index[day["tradable"].astype(bool)])]
            for best_sym, best_exp in pool.nlargest(rotate_max).items():
                worst = min(book, key=lambda k: book[k]["expected"])
                wv = book[worst]["pre_value"] if exact_timing else book[worst]["value"]
                switch = SELL + DP_FEE / max(wv, 1.0) + BUY
                if best_exp - book[worst]["expected"] <= switch + rotate_margin:
                    break
                cash += wv - (wv * SELL + DP_FEE)
                holds.append(book[worst]["age"])
                rets.append(wv / book[worst]["ticket"] - 1.0)
                del book[worst]
        free = cap - len(book)
        if sl is not None and free > 0 and sl_val > 0:
            wealth_now = cash + sl_val + sum(p["value"] for p in book.values())
            need = min(sl_val, max(0.0, free * wealth_now / TOP_K * (1 + BUY) - cash))
            if need > 0:
                sl_val -= need
                cash += need * (1.0 - ETF_SELL) - DP_FEE
        if free > 0 and cash > 1_000:
            wealth = cash + sl_val + sum(p["value"] for p in book.values())
            ticket = min(wealth / TOP_K, cash / max(TOP_K - len(book), 1))
            if ticket > 500:
                cand = exp_all[~exp_all.index.isin(book)].dropna()
                # A table built with every stock marks which ones the account could actually
                # trade that day; everything else can be held and marked, but never bought.
                if "tradable" in day.columns:
                    cand = cand[cand.index.isin(day.index[day["tradable"].astype(bool)])]
                cand = cand[cand > (round_trip(ticket) + 2 * extra_cost)]
                pm = None
                if meta is not None:
                    pm = pd.Series([meta.get((x, dt), np.nan) for x in cand.index], index=cand.index)
                    if meta_min > 0:
                        cand = cand[pm.fillna(1.0) >= meta_min]
                if entry_gate is not None and gate_fill_next:
                    # Fill the slot with the best name NOT expected to dip, instead of waiting.
                    gv0 = pd.Series([entry_gate.get((x, dt), np.nan) for x in cand.index], index=cand.index)
                    cand = cand[~(gv0 < -gate_min).fillna(False)]
                chosen = cand.nlargest(free)
                ref = np.mean([p["expected"] for p in book.values()] + list(chosen.values))                     if len(chosen) else 0.0
                if entry_gate is not None:
                    gv = pd.Series([entry_gate.get((x, dt), np.nan) for x in chosen.index], index=chosen.index)
                    chosen = chosen[~(gv < -gate_min).fillna(False)]
                if skip_entry_move > 0 and "entry_move" in day.columns:
                    mv = day["entry_move"].reindex(chosen.index)
                    chosen = chosen[~(mv >= skip_entry_move).fillna(False)]
                for sym in chosen.index:
                    size = ticket
                    mult = 1.0
                    if sizing_power > 0 and ref > 0:
                        mult *= (chosen[sym] / ref) ** sizing_power
                    if meta_power > 0 and pm is not None and pd.notna(pm.get(sym)):
                        avg_p = float(pm.reindex(chosen.index).mean())
                        if avg_p > 0:
                            mult *= (float(pm[sym]) / avg_p) ** meta_power
                    if vol_power > 0 and "vol_21d" in day.columns and pd.notna(day.at[sym, "vol_21d"]):
                        mult *= (float(day["vol_21d"].median()) / max(float(day.at[sym, "vol_21d"]), 1e-4)) ** vol_power
                    if mult != 1.0:
                        mult = float(np.clip(mult, size_lo, size_hi))
                        size = min(ticket * mult, max_weight * wealth, cash / (1 + BUY))
                    if size < 500 or cash < size * (1 + BUY):
                        break
                    cash -= size * (1 + BUY)
                    book[sym] = {"age": 0, "ticket": size, "value": size,
                                 "expected": float(cand[sym]), "entry_exp": float(cand[sym]),
                                 "stale": 0, "entry_date": dt}
                    if first_session and sym in day.index and pd.notna(day.at[sym, "fwd_ret_1"]):
                        book[sym]["value"] *= 1.0 + float(day.at[sym, "fwd_ret_1"])
        if sl is not None and cash > 7_000:
            park = cash - 2_000
            sl_val += park * (1.0 - ETF_BUY)
            cash -= park
        path.append({"date": dt, "wealth": cash + sl_val + sum(p["value"] for p in book.values()),
                     "names": len(book)})

    w = pd.DataFrame(path, columns=["date", "wealth", "names"])
    if w.empty:
        return {"final": ACCOUNT, "cagr": 0.0, "worst_drawdown": 0.0, "trades": 0,
                "median_hold": np.nan, "win_rate": np.nan, "invested": 0.0,
                "years": 0.0, "credible": False}, w
    years = (w["date"].iloc[-1] - w["date"].iloc[0]).days / 365.25
    final = float(w["wealth"].iloc[-1])
    h, r = pd.Series(holds, dtype=float), pd.Series(rets, dtype=float)
    s = {"final": final,
         "cagr": (final / ACCOUNT) ** (1 / years) - 1 if final > 0 and years > 0 else -1.0,
         "worst_drawdown": float((w["wealth"] / w["wealth"].cummax() - 1).min()),
         "trades": int(len(h)), "median_hold": float(h.median()) if len(h) else np.nan,
         "win_rate": float((r > 0).mean()) if len(r) else np.nan,
         "invested": float((w["names"] / TOP_K).mean()), "years": years}
    s["credible"] = bool(s["cagr"] <= CREDIBLE_CAGR and s["worst_drawdown"] >= -1.0)
    return s, w
