# Paper trading report

Updated 2026-11-20 11:31 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,749 | +12.88% | 0 | - | 236 |
| benchmark | 222,820 | +11.41% | 0 | - | 237 |
| intramonth | 214,758 | +7.38% | 0 | - | 235 |
| intraweek | 214,413 | +7.21% | 35 | 54% | 3,851 |
| oracle | 212,614 | +6.31% | 0 | - | 233 |
| snake_abs_exit | 210,224 | +5.11% | 2 | 50% | 345 |
| random_hold | 209,287 | +4.64% | 11 | 73% | 979 |
| snake_abs_exit_conv | 207,985 | +3.99% | 2 | 50% | 345 |
| snake_abs | 207,657 | +3.83% | 1 | 100% | 255 |
| snake_abs_conv | 207,514 | +3.76% | 1 | 100% | 255 |
| snake_viper_wild | 205,949 | +2.98% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,434 | +1.22% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,249 | +0.62% | 3 | 33% | 374 |
| benchmark_smallcap | 200,414 | +0.21% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,813 | -17.09% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,981 (-4.01%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,524 | +0.72% |
| unified | +1,134 | +0.51% |
| random_hold | +833 | +0.40% |
| intramonth | +750 | +0.35% |
| oracle | +525 | +0.25% |
| benchmark | +444 | +0.20% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -1,054 | -0.52% |
| snake_abs | -1,323 | -0.63% |
| snake_abs_conv | -1,346 | -0.64% |
| snake_viper_tick | -1,543 | -0.76% |
| snake_viper_wild | -1,574 | -0.76% |
| snake_anaconda | -2,214 | -1.09% |
| snake_abs_exit_conv | -3,079 | -1.46% |
| snake_abs_exit | -3,127 | -1.47% |
| gold | -8,960 | -5.13% |

Average per day so far: unified Rs +678, benchmark Rs +601, intramonth Rs +388, intraweek Rs +379, oracle Rs +332, snake_abs_exit Rs +292, random_hold Rs +244, snake_abs_exit_conv Rs +228, snake_abs_conv Rs +215, snake_abs Rs +213, snake_viper_wild Rs +198, snake_viper_tick Rs +90, nifty_calls Rs +48, snake_anaconda Rs +38, benchmark_smallcap Rs +12, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -900

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.