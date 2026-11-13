# Paper trading report

Updated 2026-11-13 11:52 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,299 | +10.15% | 0 | - | 236 |
| benchmark | 219,385 | +9.69% | 0 | - | 237 |
| snake_abs_exit_conv | 216,370 | +8.19% | 2 | 50% | 345 |
| snake_abs_exit | 216,308 | +8.15% | 2 | 50% | 345 |
| intraweek | 215,749 | +7.88% | 30 | 53% | 3,302 |
| oracle | 213,297 | +6.65% | 0 | - | 233 |
| snake_abs | 212,237 | +6.12% | 1 | 100% | 255 |
| snake_abs_conv | 212,069 | +6.03% | 1 | 100% | 255 |
| intramonth | 210,946 | +5.47% | 0 | - | 235 |
| random_hold | 207,172 | +3.59% | 10 | 70% | 733 |
| snake_viper_wild | 205,673 | +2.84% | 14 | 50% | 2,496 |
| snake_anaconda | 204,576 | +2.29% | 3 | 33% | 374 |
| benchmark_smallcap | 203,026 | +1.51% | 0 | - | 237 |
| snake_viper_tick | 202,155 | +1.08% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,979 | -8.01% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,813 (-4.09%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,091 | +0.51% |
| snake_viper_wild | +380 | +0.18% |
| snake_viper_tick | +373 | +0.18% |
| oracle | +181 | +0.09% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| benchmark_smallcap | -179 | -0.09% |
| unified | -397 | -0.18% |
| intramonth | -647 | -0.31% |
| random_hold | -882 | -0.42% |
| snake_abs_exit | -1,134 | -0.52% |
| benchmark | -1,163 | -0.53% |
| gold | -1,332 | -0.72% |
| snake_anaconda | -1,351 | -0.66% |
| snake_abs_exit_conv | -2,304 | -1.05% |
| snake_abs_conv | -3,466 | -1.61% |
| snake_abs | -3,474 | -1.61% |

Average per day so far: unified Rs +615, benchmark Rs +587, snake_abs_exit_conv Rs +546, snake_abs_exit Rs +544, intraweek Rs +477, oracle Rs +403, snake_abs_conv Rs +402, snake_abs Rs +395, intramonth Rs +332, snake_viper_wild Rs +227, random_hold Rs +217, snake_anaconda Rs +163, benchmark_smallcap Rs +104, snake_viper_tick Rs +98, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -485

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.