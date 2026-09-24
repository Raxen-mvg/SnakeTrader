#!/usr/bin/env python3
"""The single Rs 50,000 account: sleeves stay in their lanes and it is flat intraday by the close.

Run:  python tests/test_oracle_account.py
"""

from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from papertrade import strategies as S  # noqa: E402
from papertrade.broker import Account  # noqa: E402
from papertrade.market import IST  # noqa: E402

ok = True


def check(name, cond, detail=""):
    global ok
    ok &= bool(cond)
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  - {detail}" if detail else ""))


def ctx(t, prices, picks, ranks, intraday=None):
    c = S.Ctx(t, prices, picks, ranks, {})
    if intraday is not None:
        c.intraday_picks = intraday
    return c


def main() -> int:
    names = list("ABCDEFGHIJ")
    prices = {s: 100.0 for s in names} | {S.GOLD_SYMBOL: 60.0}
    picks = [{"symbol": s, "rank_pct": 1 - i / 100, "score": 1 - i / 100} for i, s in enumerate(names)]
    ranks = {p["symbol"]: p["rank_pct"] for p in picks}

    print("\n[SLEEVES]")
    acc = Account("oracle", 50_000, 50_000)
    t = dt.datetime(2026, 9, 25, 10, 30, tzinfo=IST)
    hot = [{"symbol": "H", "score": 0.61}, {"symbol": "I", "score": 0.58}]
    S.oracle(acc, ctx(t, prices, picks, ranks, hot))
    eq = acc.equity(prices)
    core, hedge, trade = (S._sleeve(acc, ctx(t, prices, picks, ranks), k) for k in ("core", "hedge", "trade"))
    print(f"  core Rs {core:,.0f}  hedge Rs {hedge:,.0f}  intraday Rs {trade:,.0f}  cash Rs {acc.cash:,.0f}")
    check("core sleeve is near its 75% target", core <= 0.80 * eq, f"{100 * core / eq:.1f}%")
    check("gold hedge is bought and stays near 10%", 0.05 * eq <= hedge <= 0.15 * eq, f"{100 * hedge / eq:.1f}%")
    check("intraday sleeve never exceeds its 15% cap", trade <= 0.16 * eq, f"{100 * trade / eq:.1f}%")
    check("at most eight core names", len([1 for s, p in acc.positions.items()
                                           if p.product != "intraday" and s != S.GOLD_SYMBOL]) <= S.ORACLE_NAMES)
    check("cash is put to work", acc.cash < 0.15 * eq, f"Rs {acc.cash:,.0f} idle")

    print("\n[LOW CONFIDENCE IS IGNORED]")
    acc2 = Account("oracle", 50_000, 50_000)
    S.oracle(acc2, ctx(t, prices, picks, ranks, [{"symbol": "H", "score": 0.50}]))
    check("a 50% intraday call is below the 55% floor and is not taken",
          not any(p.product == "intraday" for p in acc2.positions.values()))

    print("\n[FLAT BY THE CLOSE]")
    late = dt.datetime(2026, 9, 25, 15, 10, tzinfo=IST)
    S.oracle(acc, ctx(late, prices, picks, ranks, hot))
    check("no intraday position survives the close",
          not any(p.product == "intraday" for p in acc.positions.values()))
    check("the core book is still held", len(acc.positions) > 0, f"{len(acc.positions)} positions")

    print("\n[EXIT ON RANK]")
    fallen = dict(ranks)
    held_core = [s for s, p in acc.positions.items() if p.product != "intraday" and s != S.GOLD_SYMBOL]
    fallen[held_core[0]] = 0.30
    S.oracle(acc, ctx(late + dt.timedelta(days=1), prices, picks, fallen, []))
    check("a name that falls out of the top 25% is sold", held_core[0] not in acc.positions)
    check("gold is never sold for ranking", S.GOLD_SYMBOL in acc.positions)

    print("\nRESULT:", "ORACLE ACCOUNT TESTS PASSED" if ok else "FAILURES ABOVE")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
