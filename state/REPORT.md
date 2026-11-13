# Paper trading report

Updated 2026-11-13 13:43 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,505 | +10.25% | 0 | - | 236 |
| benchmark | 219,285 | +9.64% | 0 | - | 237 |
| snake_abs_exit | 216,589 | +8.29% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,214 | +8.11% | 2 | 50% | 345 |
| intraweek | 215,978 | +7.99% | 30 | 53% | 3,302 |
| oracle | 213,174 | +6.59% | 0 | - | 233 |
| snake_abs | 212,248 | +6.12% | 1 | 100% | 255 |
| snake_abs_conv | 212,080 | +6.04% | 1 | 100% | 255 |
| intramonth | 211,110 | +5.55% | 0 | - | 235 |
| random_hold | 207,272 | +3.64% | 10 | 70% | 733 |
| snake_viper_wild | 205,598 | +2.80% | 14 | 50% | 2,496 |
| snake_anaconda | 204,467 | +2.23% | 3 | 33% | 374 |
| benchmark_smallcap | 202,511 | +1.25% | 0 | - | 237 |
| snake_viper_tick | 202,081 | +1.04% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,848 | -8.08% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,894 (-4.05%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,320 | +0.61% |
| snake_viper_wild | +305 | +0.15% |
| snake_viper_tick | +300 | +0.15% |
| oracle | +58 | +0.03% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -191 | -0.09% |
| intramonth | -483 | -0.23% |
| benchmark_smallcap | -695 | -0.34% |
| random_hold | -782 | -0.38% |
| snake_abs_exit | -854 | -0.39% |
| benchmark | -1,262 | -0.57% |
| snake_anaconda | -1,460 | -0.71% |
| gold | -1,463 | -0.79% |
| snake_abs_exit_conv | -2,460 | -1.12% |
| snake_abs_conv | -3,455 | -1.60% |
| snake_abs | -3,463 | -1.60% |

Average per day so far: unified Rs +621, benchmark Rs +584, snake_abs_exit Rs +553, snake_abs_exit_conv Rs +540, intraweek Rs +484, snake_abs_conv Rs +403, oracle Rs +399, snake_abs Rs +395, intramonth Rs +337, snake_viper_wild Rs +224, random_hold Rs +220, snake_anaconda Rs +160, snake_viper_tick Rs +95, benchmark_smallcap Rs +87, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -489

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.