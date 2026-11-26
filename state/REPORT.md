# Paper trading report

Updated 2026-11-26 14:52 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,979 | +12.99% | 0 | - | 237 |
| unified | 223,050 | +11.53% | 0 | - | 236 |
| oracle | 212,576 | +6.29% | 0 | - | 233 |
| intramonth | 210,365 | +5.18% | 0 | - | 235 |
| random_hold | 208,892 | +4.45% | 13 | 69% | 1,037 |
| intraweek | 207,414 | +3.71% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,818 | +0.41% | 0 | - | 237 |
| snake_abs_exit | 200,111 | +0.06% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit_conv | 199,511 | -0.24% | 2 | 50% | 345 |
| snake_abs | 197,832 | -1.08% | 1 | 100% | 255 |
| snake_abs_conv | 197,623 | -1.19% | 1 | 100% | 255 |
| snake_viper_wild | 192,239 | -3.88% | 16 | 50% | 2,827 |
| snake_anaconda | 191,503 | -4.25% | 3 | 33% | 374 |
| snake_viper_tick | 188,974 | -5.51% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,175 | -16.91% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,359 (-5.82%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,007 | +1.01% |
| gold | +1,578 | +0.96% |
| benchmark | +956 | +0.42% |
| intraweek | +671 | +0.32% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -601 | -0.29% |
| unified | -1,050 | -0.47% |
| oracle | -1,219 | -0.57% |
| intramonth | -1,328 | -0.63% |
| snake_abs_exit | -2,145 | -1.06% |
| snake_abs | -2,318 | -1.16% |
| snake_abs_conv | -2,349 | -1.18% |
| snake_abs_exit_conv | -2,465 | -1.22% |
| snake_anaconda | -3,050 | -1.57% |
| snake_viper_tick | -5,203 | -2.68% |
| snake_viper_wild | -5,304 | -2.69% |

Average per day so far: benchmark Rs +634, unified Rs +562, oracle Rs +307, intramonth Rs +253, random_hold Rs +217, intraweek Rs +181, nifty_calls Rs +45, benchmark_smallcap Rs +22, snake_abs_exit Rs +3, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_abs_exit_conv Rs -13, snake_abs Rs -56, snake_abs_conv Rs -63, snake_viper_wild Rs -235, snake_anaconda Rs -236, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -368, gold Rs -825

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.