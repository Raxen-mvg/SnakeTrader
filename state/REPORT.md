# Paper trading report

Updated 2026-11-20 11:20 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,725 | +12.86% | 0 | - | 236 |
| benchmark | 222,896 | +11.45% | 0 | - | 237 |
| intramonth | 214,713 | +7.36% | 0 | - | 235 |
| intraweek | 214,218 | +7.11% | 35 | 54% | 3,851 |
| oracle | 212,634 | +6.32% | 0 | - | 233 |
| snake_abs_exit | 210,569 | +5.29% | 2 | 50% | 345 |
| random_hold | 209,099 | +4.55% | 11 | 73% | 979 |
| snake_abs_exit_conv | 208,180 | +4.09% | 2 | 50% | 345 |
| snake_abs | 207,387 | +3.69% | 1 | 100% | 255 |
| snake_abs_conv | 207,249 | +3.62% | 1 | 100% | 255 |
| snake_viper_wild | 206,088 | +3.04% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,571 | +1.28% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,292 | +0.65% | 3 | 33% | 374 |
| benchmark_smallcap | 200,414 | +0.21% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,895 | -17.05% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,942 (-4.03%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,329 | +0.62% |
| unified | +1,110 | +0.49% |
| intramonth | +705 | +0.33% |
| random_hold | +645 | +0.31% |
| oracle | +545 | +0.26% |
| benchmark | +520 | +0.23% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -1,054 | -0.52% |
| snake_viper_tick | -1,406 | -0.69% |
| snake_viper_wild | -1,434 | -0.69% |
| snake_abs | -1,592 | -0.76% |
| snake_abs_conv | -1,611 | -0.77% |
| snake_anaconda | -2,172 | -1.07% |
| snake_abs_exit | -2,782 | -1.30% |
| snake_abs_exit_conv | -2,885 | -1.37% |
| gold | -8,878 | -5.08% |

Average per day so far: unified Rs +677, benchmark Rs +603, intramonth Rs +387, intraweek Rs +374, oracle Rs +332, snake_abs_exit Rs +302, random_hold Rs +239, snake_abs_exit_conv Rs +234, snake_abs_conv Rs +207, snake_abs Rs +205, snake_viper_wild Rs +203, snake_viper_tick Rs +95, nifty_calls Rs +48, snake_anaconda Rs +39, benchmark_smallcap Rs +12, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -897

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.