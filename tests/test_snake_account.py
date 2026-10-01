#!/usr/bin/env python3
"""SNAKE's account: buys only what beats its round trip, sells only when holding stops paying.

Run:  python tests/test_snake_account.py
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


def ctx(t, prices, snake):
    c = S.Ctx(t, prices, [], {}, {})
    c.snake = snake
    return c


def picks(asof, expected):
    order = sorted(expected, key=lambda s: -expected[s])
    return {"asof": asof, "expected": expected,
            "top": [{"symbol": s, "expected": expected[s], "horizon": 21} for s in order]}


def main() -> int:
    t = dt.datetime(2026, 9, 30, 10, 30, tzinfo=IST)
    names = ["AAA.NS", "BBB.NS", "CCC.NS", "DDD.NS", "EEE.NS", "FFF.NS", "GGG.NS", "HHH.NS"]
    prices = {s: 100.0 for s in names}

    # Seven names clear the round trip comfortably, one does not.
    exp = {s: 0.05 - i * 0.002 for i, s in enumerate(names[:7])}
    exp["HHH.NS"] = 0.001
    acc = Account("snake", 200_000, 200_000)
    S.snake(acc, ctx(t, prices, picks("2026-09-29", exp)))
    check("fills exactly six names from a fresh file", len(acc.positions) == 6,
          f"{sorted(acc.positions)}")
    check("never buys a name expected to earn less than its round trip",
          "HHH.NS" not in acc.positions)
    tickets = [p.qty * p.avg_price for p in acc.positions.values()]
    check("equal tickets near a sixth of Rs 2 lakh", all(30_000 < x < 34_000 for x in tickets),
          f"{[round(x) for x in tickets]}")

    # Same day, second tick: it must not keep buying.
    before = len(acc.positions)
    S.snake(acc, ctx(t.replace(hour=11), prices, picks("2026-09-29", exp)))
    check("one entry decision per day", len(acc.positions) == before)

    # Next day: one holding's expectation collapses below its exit cost -> sold, others kept.
    t2 = t + dt.timedelta(days=1)
    exp2 = dict(exp)
    exp2["AAA.NS"] = 0.0005
    S.snake(acc, ctx(t2, prices, picks("2026-09-30", exp2)))
    check("sells a holding once it no longer beats the cost of leaving",
          "AAA.NS" not in acc.positions)
    check("keeps holdings that still pay", "BBB.NS" in acc.positions)
    check("does not buy back what it sold the same day", "AAA.NS" not in acc.positions)

    # Stale file: holds everything, buys nothing, but the disaster stop still fires.
    acc2 = Account("snake", 200_000, 200_000)
    S.snake(acc2, ctx(t, prices, picks("2026-09-29", exp)))
    held = set(acc2.positions)
    crash = dict(prices)
    victim = sorted(held)[0]
    crash[victim] = 70.0
    t3 = t + dt.timedelta(days=10)
    S.snake(acc2, ctx(t3, crash, picks("2026-09-29", {})))
    check("a stale picks file sells nothing on its own say-so",
          set(acc2.positions) == held - {victim})
    check("the disaster stop fires even when picks are stale", victim not in acc2.positions)

    # No picks at all: nothing happens.
    acc3 = Account("snake", 200_000, 200_000)
    S.snake(acc3, ctx(t, prices, {}))
    check("no picks file, no trades", not acc3.positions and acc3.cash == 200_000)

    # snake_abs_conv stakes by conviction: more on the names it expects most from, within bounds.
    wide = {s: 0.09 - i * 0.012 for i, s in enumerate(names[:6])}
    acc4 = Account("snake_abs_conv", 200_000, 200_000)
    S.snake(acc4, ctx(t, prices, picks("2026-09-29", wide)))
    stake = {s: p.qty * p.avg_price for s, p in acc4.positions.items()}
    check("conviction sizing: the top name gets more than the sixth",
          stake.get("AAA.NS", 0) > stake.get("FFF.NS", 1e9), f"{ {k: round(v) for k, v in stake.items()} }")
    check("conviction sizing: no name above 30% of the account",
          max(stake.values()) <= 0.30 * 200_000 + 1)
    check("conviction sizing: never spends more than the cash", acc4.cash >= 0)
    acc5 = Account("snake_abs", 200_000, 200_000)
    S.snake(acc5, ctx(t, prices, picks("2026-09-29", wide)))
    check("snake_abs itself still stakes equally",
          all(30_000 < p.qty * p.avg_price < 34_000 for p in acc5.positions.values()))
    check("registered in the strategy table", S.STRATEGIES.get("snake") is S.snake)
    print("ALL PASS" if ok else "FAILURES")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
