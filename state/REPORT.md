# Paper trading report

Updated 2026-11-20 10:48 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,311 | +12.66% | 0 | - | 236 |
| benchmark | 222,904 | +11.45% | 0 | - | 237 |
| intramonth | 214,223 | +7.11% | 0 | - | 235 |
| intraweek | 213,637 | +6.82% | 35 | 54% | 3,851 |
| oracle | 212,368 | +6.18% | 0 | - | 233 |
| snake_abs_exit | 210,912 | +5.46% | 2 | 50% | 345 |
| random_hold | 209,047 | +4.52% | 11 | 73% | 979 |
| snake_abs_exit_conv | 208,494 | +4.25% | 2 | 50% | 345 |
| snake_abs | 207,602 | +3.80% | 1 | 100% | 255 |
| snake_abs_conv | 207,462 | +3.73% | 1 | 100% | 255 |
| snake_viper_wild | 207,083 | +3.54% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,547 | +1.77% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,310 | +0.66% | 3 | 33% | 374 |
| benchmark_smallcap | 200,425 | +0.21% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,827 | -17.59% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,782 (-4.11%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +748 | +0.35% |
| unified | +696 | +0.31% |
| random_hold | +594 | +0.28% |
| benchmark | +528 | +0.24% |
| oracle | +279 | +0.13% |
| intramonth | +215 | +0.10% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -430 | -0.21% |
| snake_viper_wild | -440 | -0.21% |
| benchmark_smallcap | -1,043 | -0.52% |
| snake_abs | -1,378 | -0.66% |
| snake_abs_conv | -1,398 | -0.67% |
| snake_anaconda | -2,153 | -1.06% |
| snake_abs_exit | -2,439 | -1.14% |
| snake_abs_exit_conv | -2,571 | -1.22% |
| gold | -9,946 | -5.69% |

Average per day so far: unified Rs +666, benchmark Rs +603, intramonth Rs +374, intraweek Rs +359, oracle Rs +325, snake_abs_exit Rs +312, snake_abs_exit_conv Rs +243, random_hold Rs +238, snake_viper_wild Rs +236, snake_abs_conv Rs +213, snake_abs Rs +211, snake_viper_tick Rs +131, nifty_calls Rs +48, snake_anaconda Rs +40, benchmark_smallcap Rs +13, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -926

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.