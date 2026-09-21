#!/usr/bin/env python3
"""Paper trader: costs match the published schedule, accounts behave like real ones,
strategies enter and exit when they should. Offline (no network).

Run:  python tests/test_papertrade.py
"""

from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from papertrade import strategies as S  # noqa: E402
from papertrade.broker import Account  # noqa: E402
from papertrade.costs import GROWW, ZERODHA, order_cost  # noqa: E402
from papertrade.market import IST  # noqa: E402
from papertrade.options import bs_call  # noqa: E402

ok = True


def check(name, cond, detail=""):
    global ok
    ok &= bool(cond)
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  - {detail}" if detail else ""))


def at(y, m, d, hh, mm):
    return dt.datetime(y, m, d, hh, mm, tzinfo=IST)


def main() -> int:
    print("\n[COSTS] Rs 10,000 order")
    b = order_cost("buy", "delivery", 10_000, ZERODHA)
    check("Zerodha delivery buy: zero brokerage, 0.1% STT, 0.015% stamp",
          b["brokerage"] == 0 and abs(b["stt"] - 10) < 1e-9 and abs(b["stamp"] - 1.5) < 1e-9, f"total Rs {b['total']:.2f}")
    s = order_cost("sell", "delivery", 10_000, ZERODHA)
    check("delivery sell pays DP Rs 15.34", abs(s["dp"] - 15.34) < 1e-9, f"total Rs {s['total']:.2f}")
    i = order_cost("sell", "intraday", 10_000, ZERODHA)
    check("Zerodha intraday: 0.03% brokerage (Rs 3) and 0.025% STT on the sell",
          abs(i["brokerage"] - 3) < 1e-9 and abs(i["stt"] - 2.5) < 1e-9)
    g = order_cost("buy", "delivery", 10_000, GROWW)
    check("Groww: Rs 20 or 0.1%, whichever lower -> Rs 10", abs(g["brokerage"] - 10) < 1e-9)
    check("Groww minimum Rs 5 applies to tiny orders", order_cost("buy", "delivery", 1_000, GROWW)["brokerage"] == 5)

    print("\n[ACCOUNT] whole shares, cash never negative")
    a = Account("t", 50_000, 50_000)
    t0 = at(2026, 9, 22, 9, 30)
    a.buy("X.NS", 50_000, 30_000, t0, "delivery")
    check("Rs 50k buys one Rs 30k share, not 1.66", a.positions["X.NS"].qty == 1)
    check("cash stays positive after costs", a.cash > 0, f"cash Rs {a.cash:,.2f}")
    check("a Rs 90k share cannot be bought", not a.buy("Y.NS", 50_000, 90_000, t0, "delivery"))
    pnl = a.sell("X.NS", 30_000, t0)
    check("round trip at the same price loses exactly the costs and slippage", pnl < 0, f"Rs {pnl:,.2f}")

    print("\n[STRATEGIES]")
    picks = [{"symbol": f"S{k}.NS", "score": 1 - k / 10, "rank_pct": 1 - k / 100} for k in range(10)]
    prices = {p["symbol"]: 100.0 for p in picks} | {"NIFTYBEES.NS": 250.0, "GOLDBEES.NS": 60.0, "^NSEI": 25_000.0}
    ranks = {p["symbol"]: p["rank_pct"] for p in picks}

    acc = Account("intraday", 50_000, 50_000)
    S.intraday(acc, S.Ctx(at(2026, 9, 22, 9, 20), prices, picks, ranks, {}))
    check("intraday waits until 09:30", not acc.positions)
    S.intraday(acc, S.Ctx(at(2026, 9, 22, 9, 45), prices, picks, ranks, {}))
    check("intraday buys the top 5 after 09:30", len(acc.positions) == 5)
    S.intraday(acc, S.Ctx(at(2026, 9, 22, 11, 0), prices, picks, ranks, {}))
    check("no second entry the same day", sum(1 for x in acc.ledger if x["side"] == "BUY") == 5)
    S.intraday(acc, S.Ctx(at(2026, 9, 22, 15, 10), prices, picks, ranks, {}))
    check("intraday closes everything before the close", not acc.positions)
    check("intraday uses the intraday cost schedule", all(x["product"] == "intraday" for x in acc.ledger))

    wk = Account("intraweek", 50_000, 50_000)
    S.intraweek(wk, S.Ctx(at(2026, 9, 22, 9, 45), prices, picks, ranks, {}))
    exit_on = next(iter(wk.positions.values())).exit_on
    check("intraweek holds for 5 trading days", exit_on == "2026-09-29", exit_on)
    S.intraweek(wk, S.Ctx(at(2026, 9, 28, 10, 0), prices, picks, ranks, {}))
    check("still held on day 4", len(wk.positions) == 5)
    S.intraweek(wk, S.Ctx(at(2026, 9, 29, 10, 0), prices, picks, ranks, {}))
    check("sold on day 5 and re-entered", sum(1 for x in wk.ledger if x["side"] == "SELL") == 5 and len(wk.positions) == 5)

    mo = Account("intramonth", 50_000, 50_000)
    S.intramonth(mo, S.Ctx(at(2026, 9, 22, 9, 45), prices, picks, ranks, {}))
    held = set(mo.positions)
    ranks2 = dict(ranks)
    ranks2[sorted(held)[0]] = 0.5                     # one name falls out of the top 25%
    S.intramonth(mo, S.Ctx(at(2026, 9, 23, 9, 45), prices, picks, ranks2, {}))
    check("hold-winners sells only the name that fell below the top 25%",
          sum(1 for x in mo.ledger if x["side"] == "SELL") == 1)

    bm = Account("benchmark", 50_000, 50_000)
    S.benchmark(bm, S.Ctx(at(2026, 9, 22, 9, 45), prices, picks, ranks, {}))
    S.benchmark(bm, S.Ctx(at(2026, 9, 23, 9, 45), prices, picks, ranks, {}))
    check("benchmark buys NIFTYBEES once and holds", sum(1 for x in bm.ledger if x["side"] == "BUY") == 1)

    print("\n[OPTIONS] pricing sanity")
    c = bs_call(25_000, 25_000, 7 / 365, 0.14)
    check("7-day ATM Nifty call at 14% vol is priced in a sane range", 100 < c < 250, f"Rs {c:.1f}")

    print("\nRESULT:", "PAPER TRADER TESTS PASSED" if ok else "FAILURES ABOVE")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
