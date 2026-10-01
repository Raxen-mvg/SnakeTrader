"""One tick of the paper trader: quote, let every strategy act, mark, save.

Run every ~15 minutes during NSE hours (GitHub Actions cron or the laptop).
State lives in state/: accounts.json (the truth), and derived files for a
frontend: summary.json, trades.csv, equity.csv, REPORT.md.

Usage:  python -m papertrade.engine            (acts only while the market is open)
        python -m papertrade.engine --force    (act now regardless, for testing)
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import logging
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

from .broker import load_accounts, save_accounts
from .market import IST, latest_prices, now_ist, session_open
from .strategies import ALWAYS_QUOTE, STRATEGIES, TOP_N, Ctx, option_marks

log = logging.getLogger("papertrade")
# Raised from Rs 50,000 on 2026-09-28: the owner's real account starts at Rs 2 lakh, and
# account size is not a detail here. The fixed Rs 15.93 depository fee on every sell is
# 0.32% of a Rs 5,000 position and 0.03% of a Rs 50,000 one, so the same strategy that
# loses money small can make it larger. Simulating the wrong size answers the wrong
# question. The four days of Rs 50,000 history are archived beside the state files.
START_CASH = 200_000.0
ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "state"


def not_companies() -> set[str]:
    """ETFs, index and liquid funds: they are not stocks and must never be traded.
    Written from the database by tools/export_picks.py; a name-based guard as backstop."""
    f = STATE / "not_companies.json"
    listed = set(json.loads(f.read_text())) if f.exists() else set()
    return listed


FUND_WORDS = re.compile(r"(ETF|BEES|LIQUID|LIQID|BETA|NEXT50|NIFTY|SENSEX|GOLD|SILVER|GILT|GSEC|IETF)", re.I)


def is_company(symbol: str, blocked: set[str]) -> bool:
    return symbol not in blocked and not FUND_WORDS.search(symbol.split(".")[0])


def load_picks() -> tuple[list[dict], dict[str, float], str]:
    f = STATE / "picks_IN.json"
    if not f.exists():
        return [], {}, "none"
    d = json.loads(f.read_text())
    blocked = not_companies()
    picks = [p for p in d.get("top", []) if is_company(p["symbol"], blocked)]
    ranks = {k: v for k, v in d.get("ranks", {}).items() if is_company(k, blocked)}
    return picks, ranks, d.get("asof", "unknown")


def intraday_model_picks(t: dt.datetime) -> list[dict] | None:
    """None when no intraday model is trained; [] before 10:20; else today's picks,
    scored once and cached in state/intraday_picks.json."""
    model = STATE / "intraday_model.txt"
    if not model.exists():
        return None
    if t.time() < dt.time(10, 20):
        return []
    cache = STATE / "intraday_picks.json"
    if cache.exists():
        c = json.loads(cache.read_text())
        if c.get("date") == t.date().isoformat():
            return c["top"]
    from .intraday_model import live_picks
    blocked = not_companies()
    universe = [s for s in json.loads((STATE / "intraday_universe.json").read_text())
                if is_company(s, blocked)]
    try:
        top = [p for p in live_picks(model, universe) if is_company(p["symbol"], blocked)]
    except Exception as exc:
        log.warning("intraday model scoring failed: %s", exc)
        return []
    cache.write_text(json.dumps({"date": t.date().isoformat(), "time": t.isoformat(), "top": top}, indent=1))
    return top


def allocator(accounts: dict, names: list[str], lookback: int = 20, switch_cost: float = 0.002) -> pd.DataFrame:
    """Virtual combined account: Rs 50,000 spread across the strategies, re-weighted each
    day toward those with the best recent risk-adjusted returns (equal weight until
    there is enough history). Pays switch_cost on the fraction moved."""
    series = {}
    for n in names:
        ec = pd.DataFrame(accounts[n].equity_curve)
        if ec.empty:
            continue
        ec["time"] = pd.to_datetime(ec["time"], format="ISO8601")
        series[n] = ec.set_index("time")["equity"].resample("D").last().dropna()
    if not series:
        return pd.DataFrame()
    eq = pd.DataFrame(series).ffill().fillna(START_CASH)
    rets = eq.pct_change().fillna(0.0)
    value, w_prev, rows = START_CASH, None, []
    for i, (day, r) in enumerate(rets.iterrows()):
        hist = rets.iloc[max(0, i - lookback):i]
        if len(hist) >= 5:
            sharpe = hist.mean() / hist.std().replace(0, np.nan)
            score = sharpe.clip(lower=0).fillna(0)
            w = score / score.sum() if score.sum() > 0 else pd.Series(1 / len(r), index=r.index)
        else:
            w = pd.Series(1 / len(r), index=r.index)
        moved = 0.0 if w_prev is None else float((w - w_prev).abs().sum() / 2)
        value *= (1 + float((w * r).sum())) * (1 - moved * switch_cost)
        rows.append({"date": day.date().isoformat(), "equity": round(value, 2),
                     **{f"w_{k}": round(float(v), 3) for k, v in w.items()}})
        w_prev = w
    return pd.DataFrame(rows)


BIG_MOVE = 0.02          # a position or an account moving this much in a day is worth flagging


def write_alerts(accounts: dict, prices: dict, t: dt.datetime) -> list[str]:
    """Append anything worth a human's attention to state/alerts.jsonl: trades since the
    last tick, positions moving more than 2%, and accounts up or down more than 2% today."""
    f = STATE / "alerts.jsonl"
    seen = set()
    if f.exists():
        for line in f.read_text(encoding="utf-8").splitlines():
            try:
                seen.add(json.loads(line)["id"])
            except Exception:
                pass
    out = []
    for name, a in accounts.items():
        for x in a.ledger:
            key = f"{x['time']}|{name}|{x['side']}|{x['symbol']}"
            if key in seen:
                continue
            pnl = f", P&L Rs {x['pnl']:+,.0f}" if "pnl" in x else ""
            out.append({"id": key, "time": x["time"], "kind": "trade", "strategy": name,
                        "text": f"{name}: {x['side']} {x['qty']} {x['symbol']} at {x['price']:,.2f}"
                                f" ({x['reason']}){pnl}"})
        for s, p in a.positions.items():
            if s not in prices:
                continue
            move = prices[s] / p.avg_price - 1
            if abs(move) >= BIG_MOVE:
                key = f"{t.date()}|{name}|{s}|{round(move, 2)}"
                if key not in seen:
                    out.append({"id": key, "time": t.isoformat(), "kind": "move", "strategy": name,
                                "text": f"{name}: {s} is {100 * move:+.1f}% since entry"})
        if a.equity_curve:
            today = [e for e in a.equity_curve if e["time"][:10] == t.date().isoformat()]
            if today:
                day_move = a.equity_curve[-1]["equity"] / today[0]["equity"] - 1
                if abs(day_move) >= BIG_MOVE:
                    key = f"{t.date()}|{name}|day|{round(day_move, 2)}"
                    if key not in seen:
                        out.append({"id": key, "time": t.isoformat(), "kind": "account", "strategy": name,
                                    "text": f"{name} account {100 * day_move:+.1f}% today "
                                            f"(Rs {a.equity_curve[-1]['equity']:,.0f})"})
    if out:
        with f.open("a", encoding="utf-8") as fh:
            for o in out:
                fh.write(json.dumps(o) + "\n")
    return [o["text"] for o in out]


# The owner's target for every account: +10% by the end of October 2026. It is MEASURED and shown,
# never fed to the strategies: a deadline that made a rule take bigger bets would lower the money
# it is expected to make, which is the opposite of the point.
GOAL = {"target_pct": 10.0, "by": "2026-10-31"}


def write_reports(accounts: dict, prices: dict, t: dt.datetime, picks_asof: str) -> None:
    rows, trades, curves = [], [], []
    for n, a in accounts.items():
        eq = a.equity_curve[-1]["equity"] if a.equity_curve else a.cash
        sells = [x for x in a.ledger if x["side"] == "SELL"]
        wins = [x for x in sells if x.get("pnl", 0) > 0]
        rows.append({"strategy": n, "equity": round(eq, 2), "return_pct": round(100 * (eq / a.start_cash - 1), 3),
                     "cash": round(a.cash, 2), "open_positions": len(a.positions),
                     "closed_trades": len(sells), "win_rate_pct": round(100 * len(wins) / len(sells), 1) if sells else None,
                     "costs_paid": round(sum(x["costs"] for x in a.ledger), 2),
                     "goal_progress_pct": round(100 * (eq / a.start_cash - 1) / GOAL["target_pct"] * 100, 1),
                     "positions": [{"symbol": p.symbol, "qty": p.qty, "avg_price": round(p.avg_price, 2),
                                    "last": round(p.meta.get("last_price", p.avg_price), 2),
                                    "exit_on": p.exit_on} for p in a.positions.values()]})
        trades += [{"strategy": n, **x} for x in a.ledger]
        curves += [{"strategy": n, **x} for x in a.equity_curve]
    # Per-day profit for every account: what Rs 50,000 made each day, in rupees and percent.
    daily = []
    for n, a in accounts.items():
        ec = pd.DataFrame(a.equity_curve)
        if ec.empty:
            continue
        # Timestamps are ISO but not all carry microseconds, so the format must be inferred.
        ec["day"] = pd.to_datetime(ec["time"], format="ISO8601").dt.date
        g = ec.groupby("day")["equity"]
        d = pd.DataFrame({"strategy": n, "open": g.first(), "close": g.last()}).reset_index()
        prev = d["close"].shift(1).fillna(a.start_cash)
        d["profit_rs"] = (d["close"] - prev).round(2)
        d["profit_pct"] = (100 * (d["close"] / prev - 1)).round(3)
        daily.append(d)
    if daily:
        dd = pd.concat(daily, ignore_index=True)
        dd.to_csv(STATE / "daily_profit.csv", index=False)

    alloc = allocator(accounts, [n for n in accounts if n != "benchmark"])
    summary = {"updated": t.isoformat(), "picks_asof": picks_asof, "start_cash": START_CASH,
               "goal": GOAL,
               "strategies": sorted(rows, key=lambda r: -r["return_pct"]),
               "combined": alloc.tail(1).to_dict("records")[0] if not alloc.empty else None}
    (STATE / "summary.json").write_text(json.dumps(summary, indent=1))
    pd.DataFrame(trades).to_csv(STATE / "trades.csv", index=False)
    pd.DataFrame(curves).to_csv(STATE / "equity.csv", index=False)
    if not alloc.empty:
        alloc.to_csv(STATE / "combined.csv", index=False)
    lines = [f"# Paper trading report", "", f"Updated {t:%Y-%m-%d %H:%M} IST. Model picks as of {picks_asof}. "
             f"Each strategy started with Rs {START_CASH:,.0f} of fake money. Costs are Zerodha's published charges. "
             f"Goal: +{GOAL['target_pct']:.0f}% by {GOAL['by']} (tracked, not traded on).", "",
             "| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |", "|:---|---:|---:|---:|---:|---:|"]
    for r in summary["strategies"]:
        wr = f"{r['win_rate_pct']:.0f}%" if r["win_rate_pct"] is not None else "-"
        lines.append(f"| {r['strategy']} | {r['equity']:,.0f} | {r['return_pct']:+.2f}% | {r['closed_trades']} | {wr} | {r['costs_paid']:,.0f} |")
    if summary["combined"]:
        c = summary["combined"]
        lines += ["", f"Combined allocator (virtual): Rs {c['equity']:,.0f} ({100 * (c['equity'] / START_CASH - 1):+.2f}%)."]
    if daily:
        last = dd[dd["day"] == dd["day"].max()].sort_values("profit_rs", ascending=False)
        lines += ["", f"Profit on {dd['day'].max()}:", "", "| Strategy | Rs | % |", "|:---|---:|---:|"]
        lines += [f"| {r.strategy} | {r.profit_rs:+,.0f} | {r.profit_pct:+.2f}% |" for r in last.itertuples()]
        avg = dd.groupby("strategy")["profit_rs"].mean().sort_values(ascending=False)
        lines += ["", "Average per day so far: " + ", ".join(f"{k} Rs {v:+,.0f}" for k, v in avg.items())]
    lines += ["", "Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices."]
    (STATE / "REPORT.md").write_text("\n".join(lines), encoding="utf-8")


# Each SNAKE account trades from its own picks file. Two versions run side by side from
# 2026-09-30 so real money decides between them: "snake" is trained with Indian exchange news,
# "snake_nonews" is the same network trained without it. A third, "snake_abs", joined on
# 2026-09-30: a network trained to predict each stock's own return, with the results calendar and
# market state as inputs, which made the most money on both seed pairs in backtest.
SNAKE_FILES = {"snake": "picks_snake.json", "snake_nonews": "picks_snake_nonews.json",
               "snake_abs": "picks_snake_abs.json",
               # the same absolute-return picks, staked by conviction - a fourth arm of the race
               "snake_abs_conv": "picks_snake_abs.json",
               # and two that also sell on the trained exit model, equal and conviction staked
               "snake_abs_exit": "picks_snake_abs.json",
               "snake_abs_exit_conv": "picks_snake_abs.json"}


def load_snake_picks(file: str = "picks_snake.json") -> dict:
    """A SNAKE picks file, with the same company filter as the main list applied."""
    f = STATE / file
    if not f.exists():
        return {}
    try:
        d = json.loads(f.read_text())
    except (json.JSONDecodeError, OSError):
        return {}
    blocked = not_companies()
    d["top"] = [p for p in d.get("top", []) if is_company(p["symbol"], blocked)]
    d["expected"] = {k: v for k, v in d.get("expected", {}).items() if is_company(k, blocked)}
    return d


def tick(force: bool = False) -> int:
    t = now_ist()
    if not force and not session_open(t):
        log.info("market closed at %s; nothing to do", t)
        return 0
    STATE.mkdir(exist_ok=True)
    # Two clocks drive this (the research laptop and GitHub Actions, whose schedule is
    # unreliable). Whichever arrives second within 10 minutes stands down.
    summ = STATE / "summary.json"
    if not force and summ.exists():
        last = dt.datetime.fromisoformat(json.loads(summ.read_text())["updated"])
        if (t - last).total_seconds() < 150:          # ticks are 3 minutes apart
            log.info("ticked %s ago by the other runner; skipping", t - last)
            return 0
    accounts = load_accounts(STATE / "accounts.json", list(STRATEGIES), START_CASH)
    picks, ranks, asof = load_picks()
    intraday_picks = intraday_model_picks(t)
    held = {s for a in accounts.values() for s, p in a.positions.items() if p.product != "option"}
    want = set(ALWAYS_QUOTE) | held | {p["symbol"] for p in picks[: TOP_N * 3]}
    want |= {p["symbol"] for p in (intraday_picks or [])}
    snake_picks = {n: load_snake_picks(f) for n, f in SNAKE_FILES.items()}
    for sp in snake_picks.values():
        want |= {p["symbol"] for p in sp.get("top", [])[:15]}
    prices = latest_prices(sorted(want), asof=t)
    if not prices:
        log.warning("no prices returned (holiday, outage or rate limit); skipping this tick")
        return 0
    blocked = not_companies()
    for name, a in accounts.items():
        if name in ("gold", "gold_trend", "benchmark"):     # these hold ETFs on purpose
            continue
        for s in [x for x in a.positions if not is_company(x, blocked)]:
            if s in prices:
                a.sell(s, prices[s], t, reason="not a company (fund or ETF); exited")
    first = {}
    for name, fn in STRATEGIES.items():
        a = accounts[name]
        ctx = Ctx(t, prices, picks, ranks, first)
        if intraday_picks is not None:
            ctx.intraday_picks = intraday_picks
        ctx.snake = snake_picks.get(name, {})
        try:
            fn(a, ctx)
        except Exception as exc:                   # one strategy failing must not stop the others
            log.exception("%s failed: %s", name, exc)
            a.memo["last_error"] = f"{t.isoformat()} {exc}"
        a.mark({**prices, **option_marks(a, ctx)}, t)
    save_accounts(STATE / "accounts.json", accounts)
    for line in write_alerts(accounts, prices, t):
        log.info("ALERT %s", line)
    write_reports(accounts, prices, t, asof)
    log.info("tick done at %s: %d prices, picks as of %s", t.strftime("%H:%M"), len(prices), asof)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true", help="act even if the market is closed (testing)")
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    return tick(force=args.force)


if __name__ == "__main__":
    sys.exit(main())
