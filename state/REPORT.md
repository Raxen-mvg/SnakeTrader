# Paper trading report

Updated 2026-11-13 14:19 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,430 | +10.21% | 0 | - | 236 |
| benchmark | 218,956 | +9.48% | 0 | - | 237 |
| snake_abs_exit | 216,339 | +8.17% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,180 | +8.09% | 2 | 50% | 345 |
| intraweek | 215,876 | +7.94% | 30 | 53% | 3,302 |
| oracle | 213,078 | +6.54% | 0 | - | 233 |
| snake_abs | 212,265 | +6.13% | 1 | 100% | 255 |
| snake_abs_conv | 212,099 | +6.05% | 1 | 100% | 255 |
| intramonth | 210,905 | +5.45% | 0 | - | 235 |
| random_hold | 207,009 | +3.50% | 10 | 70% | 733 |
| snake_viper_wild | 205,640 | +2.82% | 14 | 50% | 2,496 |
| snake_anaconda | 204,486 | +2.24% | 3 | 33% | 374 |
| benchmark_smallcap | 202,298 | +1.15% | 0 | - | 237 |
| snake_viper_tick | 202,123 | +1.06% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,897 | -8.05% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,783 (-4.11%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,218 | +0.57% |
| snake_viper_wild | +347 | +0.17% |
| snake_viper_tick | +341 | +0.17% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -38 | -0.02% |
| unified | -266 | -0.12% |
| intramonth | -688 | -0.33% |
| benchmark_smallcap | -908 | -0.45% |
| random_hold | -1,045 | -0.50% |
| snake_abs_exit | -1,103 | -0.51% |
| gold | -1,414 | -0.76% |
| snake_anaconda | -1,441 | -0.70% |
| benchmark | -1,591 | -0.72% |
| snake_abs_exit_conv | -2,494 | -1.14% |
| snake_abs_conv | -3,436 | -1.59% |
| snake_abs | -3,447 | -1.60% |

Average per day so far: unified Rs +619, benchmark Rs +574, snake_abs_exit Rs +545, snake_abs_exit_conv Rs +539, intraweek Rs +481, snake_abs_conv Rs +403, oracle Rs +396, snake_abs Rs +396, intramonth Rs +330, snake_viper_wild Rs +226, random_hold Rs +212, snake_anaconda Rs +160, snake_viper_tick Rs +96, benchmark_smallcap Rs +79, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -488

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.