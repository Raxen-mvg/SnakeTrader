# Paper trading report

Updated 2026-11-25 11:31 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,040 | +13.02% | 0 | - | 237 |
| unified | 225,046 | +12.52% | 0 | - | 236 |
| intramonth | 212,837 | +6.42% | 0 | - | 235 |
| oracle | 211,833 | +5.92% | 0 | - | 233 |
| random_hold | 210,282 | +5.14% | 12 | 75% | 1,009 |
| intraweek | 208,320 | +4.16% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,173 | +1.09% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,574 | +0.79% | 2 | 50% | 345 |
| snake_abs | 201,555 | +0.78% | 1 | 100% | 255 |
| snake_abs_conv | 201,357 | +0.68% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,439 | -0.28% | 0 | - | 237 |
| snake_viper_wild | 196,377 | -1.81% | 16 | 50% | 2,827 |
| snake_anaconda | 193,712 | -3.14% | 3 | 33% | 374 |
| snake_viper_tick | 193,035 | -3.48% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,432 | -17.78% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,401 (-5.30%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,567 | +2.06% |
| random_hold | +1,856 | +0.89% |
| unified | +761 | +0.34% |
| benchmark_smallcap | +460 | +0.23% |
| intramonth | +86 | +0.04% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| oracle | -509 | -0.24% |
| intraweek | -3,298 | -1.56% |
| snake_abs | -3,905 | -1.90% |
| snake_abs_conv | -3,946 | -1.92% |
| snake_viper_tick | -4,658 | -2.36% |
| snake_viper_wild | -4,747 | -2.36% |
| snake_anaconda | -4,992 | -2.51% |
| gold | -4,998 | -2.95% |
| snake_abs_exit | -5,322 | -2.56% |
| snake_abs_exit_conv | -5,472 | -2.64% |

Average per day so far: benchmark Rs +651, unified Rs +626, intramonth Rs +321, oracle Rs +296, random_hold Rs +257, intraweek Rs +208, snake_abs_exit Rs +59, nifty_calls Rs +46, snake_abs_exit_conv Rs +43, snake_abs Rs +41, snake_abs_conv Rs +37, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -16, snake_viper_wild Rs -113, snake_anaconda Rs -180, snake_viper_tick Rs -240, snake_nonews Rs -292, snake Rs -311, gold Rs -889

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.