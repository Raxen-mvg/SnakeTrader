"""Indian retail trading costs, as published by Zerodha and Groww (checked 2026-09-21).

Every paper trade pays exactly what a real order of the same size would, so a
strategy that only works before costs shows up as the loser it is.

Sources: zerodha.com/charges, groww.in/pricing. Statutory items (STT, stamp
duty, SEBI fee, GST) are the same at every broker; brokerage and DP charges
differ.
"""

from __future__ import annotations

from dataclasses import dataclass

STT = {"delivery": (0.001, 0.001), "intraday": (0.0, 0.00025), "option": (0.0, 0.0015)}   # (buy, sell)
STAMP_BUY = {"delivery": 0.00015, "intraday": 0.00003, "option": 0.00003}
NSE_TXN = {"delivery": 0.0000307, "intraday": 0.0000307, "option": 0.0003553}
SEBI = 10 / 1e7            # Rs 10 per crore
GST = 0.18


@dataclass(frozen=True)
class Broker:
    name: str
    dp_charge: float                     # per scrip per delivery sell, before GST where applicable

    def brokerage(self, product: str, value: float) -> float:
        if product == "option":
            return 20.0
        if self.name == "zerodha":
            return 0.0 if product == "delivery" else min(20.0, 0.0003 * value)
        # Groww: Rs 20 or 0.1% per executed order, whichever is lower, minimum Rs 5
        return max(5.0, min(20.0, 0.001 * value))


ZERODHA = Broker("zerodha", dp_charge=15.34)          # Zerodha quotes Rs 15.34 inclusive
GROWW = Broker("groww", dp_charge=16.5 + 3.5)


def order_cost(side: str, product: str, value: float, broker: Broker = ZERODHA) -> dict[str, float]:
    """All charges for one executed order. side 'buy' or 'sell'; value = price x quantity
    (option premium x lot for options)."""
    b = broker.brokerage(product, value)
    stt = value * STT[product][0 if side == "buy" else 1]
    txn = value * NSE_TXN[product]
    sebi = value * SEBI
    stamp = value * STAMP_BUY[product] if side == "buy" else 0.0
    gst = GST * (b + txn + sebi)
    dp = 0.0
    if side == "sell" and product == "delivery":
        dp = broker.dp_charge if broker is ZERODHA else broker.dp_charge * (1 + GST)
        if broker is GROWW and value < 100:
            dp = 0.0
    total = b + stt + txn + sebi + stamp + gst + dp
    return {"brokerage": b, "stt": stt, "exchange": txn, "sebi": sebi, "stamp": stamp,
            "gst": gst, "dp": dp, "total": total}
