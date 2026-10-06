"""Paper accounts: cash, positions and a ledger, saved as plain JSON between runs.

Whole shares only (NSE equity has no fractional shares), so Rs 50,000 cannot
buy a Rs 30,000 stock twice and a Rs 90,000 stock not at all, exactly as in a
real account. Options trade in whole lots.
"""

from __future__ import annotations

import datetime as dt
import json
import math
from dataclasses import asdict, dataclass, field
from pathlib import Path

from .market import at_circuit_limit  # noqa: F401
from .costs import ZERODHA, Broker, order_cost
from .market import slippage


@dataclass
class Position:
    symbol: str
    qty: int
    avg_price: float
    opened: str
    product: str                       # delivery | intraday | option
    exit_on: str | None = None         # ISO date to close on (holding-period strategies)
    meta: dict = field(default_factory=dict)


@dataclass
class Account:
    name: str
    cash: float
    start_cash: float
    positions: dict[str, Position] = field(default_factory=dict)
    ledger: list[dict] = field(default_factory=list)
    equity_curve: list[dict] = field(default_factory=list)
    memo: dict = field(default_factory=dict)          # strategy's own notes between runs

    # --- orders -------------------------------------------------------------------
    def buy(self, symbol: str, budget: float, price: float, t: dt.datetime, product: str,
            *, slippage_bps: float = 10.0, lot: int = 1, broker: Broker = ZERODHA,
            exit_on: str | None = None, meta: dict | None = None, reason: str = "") -> bool:
        # A stock frozen at its upper circuit has buyers and no sellers: the order
        # would sit in the queue unfilled. Pretending otherwise is exactly how an
        # earlier backtest invented an edge out of prices nobody could trade at.
        if at_circuit_limit(symbol) == "upper":
            self.memo.setdefault("blocked_fills", []).append(
                {"time": t.isoformat(), "symbol": symbol, "side": "BUY", "why": "upper circuit"})
            return False
        fill = slippage(price, "buy", slippage_bps)
        units = math.floor(min(budget, self.cash) / (fill * lot)) * lot
        while units > 0:
            c = order_cost("buy", product, units * fill, broker)["total"]
            if units * fill + c <= self.cash:
                break
            units -= lot
        if units <= 0:
            return False
        value = units * fill
        cost = order_cost("buy", product, value, broker)
        self.cash -= value + cost["total"]
        if symbol in self.positions:
            p = self.positions[symbol]
            p.avg_price = (p.avg_price * p.qty + value) / (p.qty + units)
            p.qty += units
        else:
            self.positions[symbol] = Position(symbol, units, fill, t.isoformat(), product, exit_on, meta or {})
        self.ledger.append({"time": t.isoformat(), "side": "BUY", "symbol": symbol, "qty": units,
                            "price": round(fill, 4), "value": round(value, 2), "costs": round(cost["total"], 2),
                            "product": product, "reason": reason})
        return True

    def sell(self, symbol: str, price: float, t: dt.datetime, *, slippage_bps: float = 10.0,
             broker: Broker = ZERODHA, reason: str = "", qty: int | None = None) -> float | None:
        """Sell the whole position, or only qty units of it (a trim)."""
        p = self.positions.get(symbol)
        if not p:
            return None
        units = p.qty if qty is None else max(0, min(int(qty), p.qty))
        if units <= 0:
            return None
        if at_circuit_limit(symbol) == "lower":      # sellers only; no one to sell to
            self.memo.setdefault("blocked_fills", []).append(
                {"time": t.isoformat(), "symbol": symbol, "side": "SELL", "why": "lower circuit"})
            return None
        fill = slippage(price, "sell", slippage_bps)
        value = units * fill
        cost = order_cost("sell", p.product, value, broker)
        self.cash += value - cost["total"]
        pnl = value - cost["total"] - units * p.avg_price
        self.ledger.append({"time": t.isoformat(), "side": "SELL", "symbol": symbol, "qty": units,
                            "price": round(fill, 4), "value": round(value, 2), "costs": round(cost["total"], 2),
                            "product": p.product, "pnl": round(pnl, 2), "reason": reason})
        if units >= p.qty:
            del self.positions[symbol]
        else:
            p.qty -= units
        return pnl

    def apply_split(self, symbol: str, ratio: float, ex_date: str) -> bool:
        """A split or bonus issue: the holding becomes ratio x the shares at 1/ratio the price.

        Without this a 2-for-1 split reads as a 50% crash: on 2026-10-06 BLSE.NS split and the
        SNAKE accounts sold it at their disaster stop. Applied once per ex-date, and only to a
        position opened before the ex-date (one bought on or after it already paid the new price)."""
        p = self.positions.get(symbol)
        if not p or p.product == "option" or ratio <= 0 or ratio == 1:
            return False
        if ex_date in p.meta.get("splits", []) or p.opened[:10] >= ex_date:
            return False
        old = p.qty
        p.qty = int(math.floor(p.qty * ratio + 1e-9))       # fractions are paid out in cash; ignored
        p.avg_price /= ratio
        if "last_price" in p.meta:
            p.meta["last_price"] /= ratio
        p.meta.setdefault("splits", []).append(ex_date)
        self.memo.setdefault("corporate_actions", []).append(
            {"symbol": symbol, "ex_date": ex_date, "ratio": ratio, "qty_before": old, "qty_after": p.qty})
        return True

    # --- valuation ------------------------------------------------------------------
    def equity(self, prices: dict[str, float]) -> float:
        held = 0.0
        for s, p in self.positions.items():
            px = prices.get(s, p.meta.get("last_price", p.avg_price))
            held += p.qty * px
        return self.cash + held

    def mark(self, prices: dict[str, float], t: dt.datetime) -> float:
        for s, p in self.positions.items():
            if s in prices:
                p.meta["last_price"] = prices[s]
        e = self.equity(prices)
        self.equity_curve.append({"time": t.isoformat(), "equity": round(e, 2)})
        return e

    # --- persistence ----------------------------------------------------------------
    def to_json(self) -> dict:
        d = asdict(self)
        d["positions"] = {k: asdict(v) for k, v in self.positions.items()}
        return d

    @classmethod
    def from_json(cls, d: dict) -> "Account":
        a = cls(d["name"], d["cash"], d["start_cash"], {}, d.get("ledger", []),
                d.get("equity_curve", []), d.get("memo", {}))
        a.positions = {k: Position(**v) for k, v in d.get("positions", {}).items()}
        return a


def load_accounts(path: Path, names: list[str], start_cash: float) -> dict[str, Account]:
    data = json.loads(path.read_text()) if path.exists() else {}
    return {n: Account.from_json(data[n]) if n in data else Account(n, start_cash, start_cash)
            for n in names}


def save_accounts(path: Path, accounts: dict[str, Account]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps({k: v.to_json() for k, v in accounts.items()}, indent=1))
    tmp.replace(path)
