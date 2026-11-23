# Paper trading report

Updated 2026-11-23 14:49 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,096 | +12.05% | 0 | - | 236 |
| benchmark | 221,909 | +10.96% | 0 | - | 237 |
| oracle | 212,292 | +6.15% | 0 | - | 233 |
| intraweek | 212,120 | +6.06% | 40 | 55% | 4,400 |
| intramonth | 211,937 | +5.97% | 0 | - | 235 |
| random_hold | 208,941 | +4.47% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,268 | +3.63% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,581 | +3.29% | 2 | 50% | 345 |
| snake_abs | 205,071 | +2.54% | 1 | 100% | 255 |
| snake_abs_conv | 204,896 | +2.45% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,374 | +0.69% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,977 | -0.01% | 0 | - | 237 |
| snake_anaconda | 198,312 | -0.84% | 3 | 33% | 374 |
| snake_viper_tick | 197,937 | -1.03% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,972 | -15.01% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,275 (-4.86%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,923 | +1.15% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -35 | -0.02% |
| oracle | -186 | -0.09% |
| snake_abs | -849 | -0.41% |
| snake_abs_conv | -887 | -0.43% |
| benchmark_smallcap | -930 | -0.46% |
| snake_abs_exit | -1,294 | -0.62% |
| snake_viper_tick | -1,435 | -0.72% |
| snake_viper_wild | -1,455 | -0.72% |
| snake_anaconda | -1,594 | -0.80% |
| random_hold | -1,818 | -0.86% |
| unified | -2,086 | -0.92% |
| intramonth | -3,068 | -1.43% |
| benchmark | -3,228 | -1.43% |
| intraweek | -3,592 | -1.67% |

Average per day so far: unified Rs +618, benchmark Rs +562, oracle Rs +315, intraweek Rs +311, intramonth Rs +306, random_hold Rs +229, snake_abs_exit Rs +202, snake_abs_exit_conv Rs +183, snake_abs Rs +137, snake_abs_conv Rs +136, nifty_calls Rs +47, snake_viper_wild Rs +44, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -1, snake_anaconda Rs -50, snake_viper_tick Rs -74, snake_nonews Rs -300, snake Rs -320, gold Rs -770

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.