# Paper trading report

Updated 2026-11-17 14:14 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,909 | +10.96% | 0 | - | 237 |
| unified | 221,665 | +10.83% | 0 | - | 236 |
| snake_abs_exit | 213,711 | +6.86% | 2 | 50% | 345 |
| intraweek | 213,643 | +6.82% | 35 | 54% | 3,851 |
| oracle | 212,490 | +6.25% | 0 | - | 233 |
| snake_abs_exit_conv | 212,150 | +6.08% | 2 | 50% | 345 |
| intramonth | 211,622 | +5.81% | 0 | - | 235 |
| snake_viper_wild | 209,557 | +4.78% | 14 | 50% | 2,496 |
| snake_abs | 208,912 | +4.46% | 1 | 100% | 255 |
| snake_abs_conv | 208,775 | +4.39% | 1 | 100% | 255 |
| random_hold | 207,687 | +3.84% | 10 | 70% | 733 |
| snake_viper_tick | 205,976 | +2.99% | 13 | 46% | 2,299 |
| snake_anaconda | 204,480 | +2.24% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,165 | +0.58% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,938 | -9.53% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,236 (-4.38%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,413 | +1.66% |
| snake_viper_tick | +3,357 | +1.66% |
| intraweek | +2,377 | +1.12% |
| benchmark | +1,828 | +0.83% |
| oracle | +467 | +0.22% |
| benchmark_smallcap | +336 | +0.17% |
| unified | +227 | +0.10% |
| intramonth | +3 | +0.00% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold | -16 | -0.01% |
| random_hold | -106 | -0.05% |
| snake_anaconda | -622 | -0.30% |
| snake_abs_exit | -698 | -0.33% |
| snake_abs_exit_conv | -1,068 | -0.50% |
| snake_abs_conv | -1,215 | -0.58% |
| snake_abs | -1,222 | -0.58% |

Average per day so far: benchmark Rs +626, unified Rs +619, snake_abs_exit Rs +428, intraweek Rs +390, snake_abs_exit_conv Rs +380, oracle Rs +357, snake_viper_wild Rs +354, intramonth Rs +332, snake_abs_conv Rs +274, snake_abs Rs +270, snake_viper_tick Rs +249, random_hold Rs +220, snake_anaconda Rs +149, nifty_calls Rs +52, benchmark_smallcap Rs +38, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -545

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.