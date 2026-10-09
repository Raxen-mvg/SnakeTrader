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
    # The exit-model accounts sell what the trained exit flags, and only past the minimum age.
    acc6 = Account("snake_abs_exit", 200_000, 200_000)
    S.snake(acc6, ctx(t, prices, picks("2026-09-29", exp)))
    held = sorted(acc6.positions)
    pk = picks("2026-09-30", exp)
    pk["exit_rule"] = {"margin": 0.02, "min_age": 10}
    pk["exit_scores"] = {"snake_abs_exit": {held[0]: {"pred": -0.05, "age": 12},
                                            held[1]: {"pred": 0.01, "age": 12},
                                            held[2]: {"pred": -0.05, "age": 4}}}
    t5 = t + dt.timedelta(days=1)
    S.snake(acc6, ctx(t5, prices, pk))
    check("exit model: sells a holding it says to switch out of", held[0] not in acc6.positions)
    check("exit model: keeps one it says to hold", held[1] in acc6.positions)
    check("exit model: never sells before the minimum age", held[2] in acc6.positions)
    acc7 = Account("snake_abs", 200_000, 200_000)
    S.snake(acc7, ctx(t, prices, picks("2026-09-29", exp)))
    pk2 = dict(pk, exit_scores={"snake_abs": {s: {"pred": -0.5, "age": 50} for s in acc7.positions}})
    S.snake(acc7, ctx(t5, prices, pk2))
    check("accounts without the exit model ignore exit scores", len(acc7.positions) == 6)
    check("buys record the expected return at entry",
          all("entry_exp" in p.meta for p in acc6.positions.values()))
    # ANACONDA waits on names its learned entry flags, keeps the slot, and buys the rest.
    pk3 = picks("2026-09-29", exp)
    pk3["entry_wait"] = {"AAA.NS": 0.004, "BBB.NS": -0.002}
    acc8 = Account("snake_anaconda", 200_000, 200_000)
    S.snake(acc8, ctx(t, prices, pk3))
    check("anaconda: does not buy a name it should wait on", "AAA.NS" not in acc8.positions)
    check("anaconda: buys names it should not wait on", "BBB.NS" in acc8.positions)
    check("anaconda: the waiting name keeps its slot (five bought, not six)", len(acc8.positions) == 5,
          f"{sorted(acc8.positions)}")
    acc9 = Account("snake_abs_exit_conv", 200_000, 200_000)
    S.snake(acc9, ctx(t, prices, pk3))
    check("other accounts ignore the entry signal", "AAA.NS" in acc9.positions)
    # VIPER WILD: three names, big conviction stakes, exit at any age, no disaster stop.
    accw = Account("snake_viper_wild", 200_000, 200_000)
    S.snake(accw, ctx(t, prices, picks("2026-09-29", wide)))
    stakes = {s: p.qty * p.avg_price for s, p in accw.positions.items()}
    check("wild: holds three names, not six", len(accw.positions) == 3, f"{sorted(accw.positions)}")
    check("wild: may stake far above 30% of the account on one name",
          max(stakes.values()) > 0.30 * 200_000, f"{ {k: round(v) for k, v in stakes.items()} }")
    check("wild: never spends more than the cash", accw.cash >= 0)
    hw = sorted(accw.positions)
    pkw = picks("2026-09-30", wide)
    pkw["exit_rule"] = {"margin": 0.02, "min_age": 10}
    pkw["exit_scores"] = {"snake_viper_wild": {hw[0]: {"pred": -0.001, "age": 1}}}
    crash = {s: (px * 0.5 if s == hw[1] else px) for s, px in prices.items()}
    S.snake(accw, ctx(t5, crash, pkw))
    check("wild: the exit model sells at any age and any margin", hw[0] not in accw.positions)
    check("wild: no disaster stop on a 50% fall", hw[1] in accw.positions)
    check("registered in the strategy table", S.STRATEGIES.get("snake") is S.snake)
    print("ALL PASS" if ok else "FAILURES")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
