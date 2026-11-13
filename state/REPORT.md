# Paper trading report

Updated 2026-11-13 12:58 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,108 | +10.05% | 0 | - | 236 |
| benchmark | 219,270 | +9.63% | 0 | - | 237 |
| snake_abs_exit | 217,046 | +8.52% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,781 | +8.39% | 2 | 50% | 345 |
| intraweek | 215,624 | +7.81% | 30 | 53% | 3,302 |
| oracle | 213,061 | +6.53% | 0 | - | 233 |
| snake_abs | 212,769 | +6.38% | 1 | 100% | 255 |
| snake_abs_conv | 212,599 | +6.30% | 1 | 100% | 255 |
| intramonth | 210,732 | +5.37% | 0 | - | 235 |
| random_hold | 207,284 | +3.64% | 10 | 70% | 733 |
| snake_viper_wild | 205,749 | +2.87% | 14 | 50% | 2,496 |
| snake_anaconda | 204,968 | +2.48% | 3 | 33% | 374 |
| benchmark_smallcap | 202,544 | +1.27% | 0 | - | 237 |
| snake_viper_tick | 202,230 | +1.11% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,470 | -8.27% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,708 (-4.15%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +966 | +0.45% |
| snake_viper_wild | +456 | +0.22% |
| snake_viper_tick | +448 | +0.22% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -55 | -0.03% |
| snake_abs_exit | -397 | -0.18% |
| unified | -589 | -0.27% |
| benchmark_smallcap | -661 | -0.33% |
| random_hold | -770 | -0.37% |
| intramonth | -861 | -0.41% |
| snake_anaconda | -959 | -0.47% |
| benchmark | -1,278 | -0.58% |
| gold | -1,841 | -0.99% |
| snake_abs_exit_conv | -1,893 | -0.86% |
| snake_abs_conv | -2,936 | -1.36% |
| snake_abs | -2,943 | -1.36% |

Average per day so far: unified Rs +609, benchmark Rs +584, snake_abs_exit Rs +568, snake_abs_exit_conv Rs +559, intraweek Rs +473, snake_abs_conv Rs +420, snake_abs Rs +412, oracle Rs +396, intramonth Rs +325, snake_viper_wild Rs +230, random_hold Rs +221, snake_anaconda Rs +177, snake_viper_tick Rs +101, benchmark_smallcap Rs +88, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -501

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.