# Paper trading report

Updated 2026-11-25 11:45 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,224 | +13.11% | 0 | - | 237 |
| unified | 225,517 | +12.76% | 0 | - | 236 |
| intramonth | 213,236 | +6.62% | 0 | - | 235 |
| oracle | 212,344 | +6.17% | 0 | - | 233 |
| random_hold | 210,028 | +5.01% | 12 | 75% | 1,009 |
| intraweek | 208,079 | +4.04% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,767 | +1.38% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,208 | +1.10% | 2 | 50% | 345 |
| snake_abs | 201,955 | +0.98% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_conv | 201,763 | +0.88% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,663 | -0.17% | 0 | - | 237 |
| snake_viper_wild | 196,962 | -1.52% | 16 | 50% | 2,827 |
| snake_anaconda | 194,301 | -2.85% | 3 | 33% | 374 |
| snake_viper_tick | 193,608 | -3.20% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,564 | -17.72% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,643 (-5.18%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,751 | +2.15% |
| random_hold | +1,602 | +0.77% |
| unified | +1,232 | +0.55% |
| benchmark_smallcap | +684 | +0.34% |
| intramonth | +484 | +0.23% |
| oracle | +2 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs | -3,506 | -1.71% |
| snake_abs_conv | -3,540 | -1.72% |
| intraweek | -3,540 | -1.67% |
| snake_viper_tick | -4,084 | -2.07% |
| snake_viper_wild | -4,162 | -2.07% |
| snake_anaconda | -4,403 | -2.22% |
| snake_abs_exit | -4,728 | -2.28% |
| snake_abs_exit_conv | -4,837 | -2.34% |
| gold | -4,866 | -2.87% |

Average per day so far: benchmark Rs +656, unified Rs +638, intramonth Rs +331, oracle Rs +309, random_hold Rs +251, intraweek Rs +202, snake_abs_exit Rs +75, snake_abs_exit_conv Rs +60, snake_abs Rs +51, snake_abs_conv Rs +48, nifty_calls Rs +46, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -9, snake_viper_wild Rs -95, snake_anaconda Rs -163, snake_viper_tick Rs -220, snake_nonews Rs -292, snake Rs -311, gold Rs -886

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.