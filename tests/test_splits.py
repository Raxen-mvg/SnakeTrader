"""A split or bonus issue must not read as a crash (BLSE.NS, 2-for-1, 2026-10-06)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from papertrade.broker import Account, Position  # noqa: E402

ok = True


def check(name, cond, extra=""):
    global ok
    ok &= bool(cond)
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}  {extra}")


a = Account("t", 1000.0, 1000.0)
a.positions["X.NS"] = Position("X.NS", 102, 324.5, "2026-09-30T10:21:00+05:30", "delivery", None, {"last_price": 320.0})
before = a.equity({"X.NS": 320.0})
check("split applied", a.apply_split("X.NS", 2.0, "2026-10-06"))
p = a.positions["X.NS"]
check("shares doubled, cost halved", p.qty == 204 and abs(p.avg_price - 162.25) < 1e-9, f"{p.qty} @ {p.avg_price}")
check("value unchanged at the new price", abs(a.equity({"X.NS": 160.0}) - before) < 1e-6)
check("applied once only", not a.apply_split("X.NS", 2.0, "2026-10-06"))
b = Account("t", 1000.0, 1000.0)
b.positions["X.NS"] = Position("X.NS", 10, 160.0, "2026-10-06T10:00:00+05:30", "delivery")
check("bought on the ex-date: untouched", not b.apply_split("X.NS", 2.0, "2026-10-06") and b.positions["X.NS"].qty == 10)
c = Account("t", 1000.0, 1000.0)
c.positions["Y.NS"] = Position("Y.NS", 7, 300.0, "2026-09-01T10:00:00+05:30", "delivery")
c.apply_split("Y.NS", 1.5, "2026-10-06")
check("odd bonus rounds down to whole shares", c.positions["Y.NS"].qty == 10)
print("ALL PASS" if ok else "SOME FAILED")
sys.exit(0 if ok else 1)
