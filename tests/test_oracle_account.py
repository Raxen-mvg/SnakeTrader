#!/usr/bin/env python3
"""The two new Rs 50,000 accounts: money follows expected edge, and nothing trades below its cost.

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
    prices = {s: 100.0 for s in names}
    picks = [{"symbol": s, "rank_pct": 1 - i / 100, "score": 1 - i / 100} for i, s in enumerate(names)]
    ranks = {p["symbol"]: p["rank_pct"] for p in picks}
    t = dt.datetime(2026, 9, 25, 10, 30, tzinfo=IST)

    print()
    print("[WHAT IT REALLY COSTS]")
    check("a small ticket costs more per rupee than a large one",
          S.round_trip_cost(5_000) > S.round_trip_cost(37_500) > 0,
          f"{100 * S.round_trip_cost(5_000):.3f}% vs {100 * S.round_trip_cost(37_500):.3f}%")
    check("the fixed selling charge is what makes small tickets expensive",
          S.round_trip_cost(5_000) - S.round_trip_cost(50_000) > 0.002)
    check("selling alone costs less than a round trip", S.exit_cost(12_500) < S.round_trip_cost(12_500))
    n50, t50 = S.best_book([1.0, 0.99, 0.98, 0.97, 0.95, 0.93, 0.90, 0.87, 0.84, 0.80, 0.77], 50_000)
    n10, t10 = S.best_book([1.0, 0.99, 0.98, 0.97, 0.95, 0.93, 0.90, 0.87, 0.84, 0.80, 0.77], 1_000_000)
    check("a bigger account can afford more names", n10 > n50, f"{n10} vs {n50}")
    check("a small account still diversifies", 3 <= n50 <= 10, f"{n50} names at Rs {t50:,.0f}")
    check("every name in the chosen book pays for itself",
          all(S.core_gross(r) > S.round_trip_cost(t50) for r in [1.0, 0.99, 0.98, 0.97, 0.95,
                                                                 0.93, 0.90, 0.87, 0.84, 0.80, 0.77][:n50]))
    check("a list of mediocre names is mostly refused", S.best_book([0.66, 0.64, 0.62], 50_000)[0] <= 1)

    print()
    print("[WHAT A TRADE IS EXPECTED TO EARN]")
    check("a top-ranked name clears its costs", S.core_edge(0.99) > 0, f"{100 * S.core_edge(0.99):+.4f}%/day")
    check("a middling name does not", S.core_edge(0.55) <= 0, f"{100 * S.core_edge(0.55):+.4f}%/day")
    cut = next(r / 100 for r in range(50, 101) if S.core_edge(r / 100) > 0)
    check("there is a single cut-off and costs put it there",
          0.5 < cut < 0.95 and S.core_edge(cut - 0.01) <= 0 < S.core_edge(cut),
          f"buys from rank {cut:.2f} up")
    check("expected return rises with rank", S.core_edge(0.99) > S.core_edge(0.85) > S.core_edge(0.75))
    check("with nothing measured, no intraday score is tradeable",
          not any(S.intraday_worth_it(x) for x in (0.3, 0.5, 0.55, 0.7, 0.9)))
    import json as _json
    S.CALIBRATION.write_text(_json.dumps({"score": [0.4, 0.6, 0.8],
                                          "expected_net": [-0.01, 0.0, 0.02]}))
    try:
        check("a score measured to lose is refused", not S.intraday_worth_it(0.40))
        check("a score measured to break even is refused", not S.intraday_worth_it(0.60))
        check("a score measured to pay several times the cost is taken", S.intraday_worth_it(0.80))
        check("what it demands is several times the cost",
              S.intraday_edge(0.80) >= S.EDGE_MULTIPLE * S.ROUND_TRIP_INTRADAY)
        check("between measured points it interpolates rather than guessing",
              abs(S.intraday_expected_net(0.70) - 0.01) < 1e-9, str(S.intraday_expected_net(0.70)))
    finally:
        S.CALIBRATION.unlink(missing_ok=True)

    print()
    print("[ORACLE: NO FIXED ALLOCATION]")
    acc = Account("oracle", 50_000, 50_000)
    S.oracle(acc, ctx(t, prices, picks, ranks, [{"symbol": "A", "score": 0.55}]))
    check("the weak intraday call is not funded",
          not any(p.product == "intraday" for p in acc.positions.values()))
    check("cash went into the core book", len(acc.positions) > 0, f"{len(acc.positions)} names")
    # The cap loosens when few names qualify, otherwise a three-name book would be forced to
    # leave a tenth of the account in cash. So the test is against the cap that actually
    # applies, not the headline one.
    held = [p for s_, p in acc.positions.items() if p.product != "intraday"]
    cap = max(S.MAX_NAME_WEIGHT, 1.0 / max(len(held), 1))
    check("no name takes more than the cap that applies to a book this size",
          max(p.qty * 100.0 for p in held) <= (cap + 0.02) * 50_000,
          f"{len(held)} names, cap {cap:.2f}")

    import json as _json
    S.CALIBRATION.write_text(_json.dumps({"score": [0.4, 0.8], "expected_net": [-0.01, 0.02]}))
    try:
        acc2 = Account("oracle", 50_000, 50_000)
        S.oracle(acc2, ctx(t, prices, picks, ranks, [{"symbol": "A", "score": 0.85}]))
        check("a call measured to pay IS funded, ahead of the core book",
              any(p.product == "intraday" for p in acc2.positions.values()))
    finally:
        S.CALIBRATION.unlink(missing_ok=True)

    late = dt.datetime(2026, 9, 25, 15, 10, tzinfo=IST)
    S.oracle(acc2, ctx(late, prices, picks, ranks, []))
    check("nothing intraday is held overnight",
          not any(p.product == "intraday" for p in acc2.positions.values()))

    # Exits, now that a name is held for a minimum period. Three behaviours: one that merely
    # goes quiet early is kept, one that turns actively bad is sold whenever that happens, and
    # a quiet one is let go once the minimum hold has passed.
    quiet = dict(ranks)
    held = [s for s, p in acc.positions.items() if p.product != "intraday"][0]
    quiet[held] = 0.60                                  # below its costs, but not a disaster
    S.oracle(acc, ctx(late + dt.timedelta(days=1), prices, picks, quiet, []))
    check("a name that merely goes quiet is kept while the minimum hold runs",
          held in acc.positions)

    bad = dict(quiet)
    bad[held] = 0.02                                    # actively bad, not merely unexciting
    S.oracle(acc, ctx(late + dt.timedelta(days=2), prices, picks, bad, []))
    check("a name that turns actively bad is sold straight away", held not in acc.positions)

    acc5 = Account("oracle", 50_000, 50_000)
    S.oracle(acc5, ctx(t, prices, picks, ranks, []))
    kept = [s for s, p in acc5.positions.items() if p.product != "intraday"][0]
    later = t + dt.timedelta(days=int(S.MIN_HOLD_SESSIONS * 7 / 5) + 5)
    S.oracle(acc5, ctx(later, prices, picks, {**ranks, kept: 0.60}, []))
    check("once the minimum hold has passed, a quiet name is let go",
          kept not in acc5.positions, f"after about {S.MIN_HOLD_SESSIONS} sessions")

    print()
    print("[STAT ARB]")
    sa_prices = {s: 100.0 for s in S.STATARB_UNIVERSE}
    sa_open = dict(sa_prices)
    acc3 = Account("statarb", 50_000, 50_000)
    S.statarb(acc3, ctx(t, sa_prices, [], {}))
    check("a flat cross-section gives no trades", not acc3.positions)
    was = S.STATARB_ENABLED
    S.STATARB_ENABLED = True                       # measured off; switch on to test the rule
    for i, s in enumerate(S.STATARB_UNIVERSE):
        sa_prices[s] = sa_open[s] * (1 + 0.01)
    laggard = S.STATARB_UNIVERSE[0]
    sa_prices[laggard] = sa_open[laggard] * (1 - 0.05)
    S.statarb(acc3, ctx(t + dt.timedelta(minutes=5), sa_prices, [], {}))
    check("the name far below its peers is bought", laggard in acc3.positions, str(list(acc3.positions)))
    check("it does not buy the whole crowd", len(acc3.positions) <= S.STATARB_MAX_POSITIONS,
          f"{len(acc3.positions)} positions")
    sa_prices[laggard] = sa_open[laggard] * 1.009
    S.statarb(acc3, ctx(t + dt.timedelta(minutes=10), sa_prices, [], {}))
    check("it sells once the gap has closed", laggard not in acc3.positions)
    sa_prices[laggard] = sa_open[laggard] * (1 - 0.05)
    S.statarb(acc3, ctx(late, sa_prices, [], {}))
    check("it is flat before the close", not acc3.positions)
    S.STATARB_ENABLED = was
    acc4 = Account("statarb", 50_000, 50_000)
    S.statarb(acc4, ctx(t + dt.timedelta(minutes=20), sa_prices, [], {}))
    check("with the rule measured to lose, the account does not trade at all",
          not acc4.positions and acc4.cash == 50_000)

    print()
    print("RESULT:", "ACCOUNT TESTS PASSED" if ok else "FAILURES ABOVE")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
