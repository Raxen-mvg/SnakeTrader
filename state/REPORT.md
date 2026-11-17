# Paper trading report

Updated 2026-11-17 11:34 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,152 | +11.08% | 0 | - | 236 |
| benchmark | 221,902 | +10.95% | 0 | - | 237 |
| snake_abs_exit | 215,501 | +7.75% | 2 | 50% | 345 |
| intraweek | 213,905 | +6.95% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 213,536 | +6.77% | 2 | 50% | 345 |
| oracle | 212,490 | +6.25% | 0 | - | 233 |
| intramonth | 212,157 | +6.08% | 0 | - | 235 |
| snake_abs | 210,041 | +5.02% | 1 | 100% | 255 |
| snake_abs_conv | 209,892 | +4.95% | 1 | 100% | 255 |
| random_hold | 207,929 | +3.96% | 10 | 70% | 733 |
| snake_viper_wild | 207,641 | +3.82% | 14 | 50% | 2,496 |
| snake_anaconda | 205,528 | +2.76% | 3 | 33% | 374 |
| snake_viper_tick | 204,091 | +2.05% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,185 | +1.09% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,365 | -9.32% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,534 (-4.23%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,640 | +1.25% |
| benchmark | +1,821 | +0.83% |
| snake_viper_wild | +1,497 | +0.73% |
| snake_viper_tick | +1,471 | +0.73% |
| benchmark_smallcap | +1,356 | +0.68% |
| snake_abs_exit | +1,092 | +0.51% |
| unified | +715 | +0.32% |
| intramonth | +538 | +0.25% |
| oracle | +468 | +0.22% |
| snake_anaconda | +425 | +0.21% |
| gold | +411 | +0.23% |
| snake_abs_exit_conv | +318 | +0.15% |
| random_hold | +135 | +0.07% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs | -93 | -0.04% |
| snake_abs_conv | -97 | -0.05% |

Average per day so far: unified Rs +633, benchmark Rs +626, snake_abs_exit Rs +484, snake_abs_exit_conv Rs +423, intraweek Rs +397, oracle Rs +357, intramonth Rs +347, snake_abs_conv Rs +309, snake_abs Rs +304, snake_viper_wild Rs +283, random_hold Rs +227, snake_anaconda Rs +184, snake_viper_tick Rs +170, benchmark_smallcap Rs +70, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -532

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.