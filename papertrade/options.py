"""Simulated index options, priced from real market inputs.

NSE's live option prices are not free to redistribute, so option trades here
are priced with Black-Scholes from the real index level at that moment and
the index's own recent realised volatility (plus a volatility premium, since
implied volatility usually sits above realised). Every option trade is
labelled SIMULATED in the ledger. Treat option results as indicative only.
"""

from __future__ import annotations

import math

NIFTY_LOT = 75             # contract multiplier; NSE revises this periodically - check before trusting
STRIKE_STEP = 50
RATE = 0.065               # Indian risk-free rate, approx.
VOL_PREMIUM = 1.15         # implied vol typically trades above realised


def _ncdf(x: float) -> float:
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def bs_call(spot: float, strike: float, years: float, vol: float, rate: float = RATE) -> float:
    if years <= 0:
        return max(spot - strike, 0.0)
    v = max(vol, 1e-4) * math.sqrt(years)
    d1 = (math.log(spot / strike) + (rate + 0.5 * vol * vol) * years) / v
    return spot * _ncdf(d1) - strike * math.exp(-rate * years) * _ncdf(d1 - v)


def atm_strike(spot: float) -> float:
    return round(spot / STRIKE_STEP) * STRIKE_STEP


def call_premium(spot: float, strike: float, days_left: float, realised_vol: float) -> float:
    return bs_call(spot, strike, max(days_left, 0.0) / 365.0, realised_vol * VOL_PREMIUM)
