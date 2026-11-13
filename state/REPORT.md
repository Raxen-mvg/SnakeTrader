# Paper trading report

Updated 2026-11-13 15:04 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,475 | +9.74% | 0 | - | 236 |
| benchmark | 219,262 | +9.63% | 0 | - | 237 |
| snake_abs_exit | 217,124 | +8.56% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,549 | +8.28% | 2 | 50% | 345 |
| intraweek | 216,134 | +8.07% | 30 | 53% | 3,302 |
| oracle | 213,033 | +6.52% | 0 | - | 233 |
| snake_abs | 212,665 | +6.33% | 1 | 100% | 255 |
| snake_abs_conv | 212,492 | +6.25% | 1 | 100% | 255 |
| intramonth | 210,380 | +5.19% | 0 | - | 235 |
| random_hold | 207,028 | +3.51% | 10 | 70% | 733 |
| snake_viper_wild | 204,963 | +2.48% | 14 | 50% | 2,496 |
| snake_anaconda | 204,903 | +2.45% | 3 | 33% | 374 |
| benchmark_smallcap | 202,914 | +1.46% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,457 | +0.73% | 13 | 46% | 2,299 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,864 | -8.07% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,664 (-4.17%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,476 | +0.69% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -82 | -0.04% |
| benchmark_smallcap | -291 | -0.14% |
| snake_abs_exit | -319 | -0.15% |
| snake_viper_tick | -324 | -0.16% |
| snake_viper_wild | -330 | -0.16% |
| snake_anaconda | -1,024 | -0.50% |
| random_hold | -1,026 | -0.49% |
| intramonth | -1,214 | -0.57% |
| unified | -1,221 | -0.55% |
| benchmark | -1,285 | -0.58% |
| gold | -1,447 | -0.78% |
| snake_abs_exit_conv | -2,125 | -0.97% |
| snake_abs_conv | -3,043 | -1.41% |
| snake_abs | -3,046 | -1.41% |

Average per day so far: unified Rs +590, benchmark Rs +584, snake_abs_exit Rs +571, snake_abs_exit_conv Rs +552, intraweek Rs +489, snake_abs_conv Rs +416, snake_abs Rs +409, oracle Rs +395, intramonth Rs +315, random_hold Rs +213, snake_viper_wild Rs +199, snake_anaconda Rs +175, benchmark_smallcap Rs +100, snake_viper_tick Rs +66, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -489

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.