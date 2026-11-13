# Paper trading report

Updated 2026-11-13 15:28 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 219,270 | +9.63% | 0 | - | 237 |
| unified | 218,658 | +9.33% | 0 | - | 236 |
| snake_abs_exit | 216,854 | +8.43% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,292 | +8.15% | 2 | 50% | 345 |
| intraweek | 216,040 | +8.02% | 30 | 53% | 3,302 |
| oracle | 213,228 | +6.61% | 0 | - | 233 |
| snake_abs | 212,509 | +6.25% | 1 | 100% | 255 |
| snake_abs_conv | 212,336 | +6.17% | 1 | 100% | 255 |
| intramonth | 209,861 | +4.93% | 0 | - | 235 |
| random_hold | 207,342 | +3.67% | 10 | 70% | 733 |
| snake_anaconda | 204,912 | +2.46% | 3 | 33% | 374 |
| snake_viper_wild | 204,594 | +2.30% | 14 | 50% | 2,496 |
| benchmark_smallcap | 203,138 | +1.57% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,094 | +0.55% | 13 | 46% | 2,299 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,045 | -7.98% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,495 (-4.25%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,382 | +0.64% |
| oracle | +113 | +0.05% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| benchmark_smallcap | -67 | -0.03% |
| snake_abs_exit | -588 | -0.27% |
| snake_viper_tick | -688 | -0.34% |
| snake_viper_wild | -699 | -0.34% |
| random_hold | -712 | -0.34% |
| snake_anaconda | -1,015 | -0.49% |
| gold | -1,266 | -0.68% |
| benchmark | -1,278 | -0.58% |
| intramonth | -1,732 | -0.82% |
| unified | -2,039 | -0.92% |
| snake_abs_exit_conv | -2,382 | -1.09% |
| snake_abs_conv | -3,199 | -1.48% |
| snake_abs | -3,202 | -1.48% |

Average per day so far: benchmark Rs +584, unified Rs +565, snake_abs_exit Rs +562, snake_abs_exit_conv Rs +543, intraweek Rs +486, snake_abs_conv Rs +411, snake_abs Rs +404, oracle Rs +401, intramonth Rs +299, random_hold Rs +222, snake_viper_wild Rs +184, snake_anaconda Rs +175, benchmark_smallcap Rs +108, nifty_calls Rs +56, snake_viper_tick Rs +50, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -483

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.