# Paper trading report

Updated 2026-11-17 12:46 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 222,009 | +11.00% | 0 | - | 237 |
| unified | 221,735 | +10.87% | 0 | - | 236 |
| snake_abs_exit | 214,161 | +7.08% | 2 | 50% | 345 |
| intraweek | 213,877 | +6.94% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 212,428 | +6.21% | 2 | 50% | 345 |
| oracle | 212,224 | +6.11% | 0 | - | 233 |
| intramonth | 211,674 | +5.84% | 0 | - | 235 |
| snake_abs | 209,258 | +4.63% | 1 | 100% | 255 |
| snake_abs_conv | 209,110 | +4.55% | 1 | 100% | 255 |
| snake_viper_wild | 207,647 | +3.82% | 14 | 50% | 2,496 |
| random_hold | 207,567 | +3.78% | 10 | 70% | 733 |
| snake_anaconda | 204,771 | +2.39% | 3 | 33% | 374 |
| snake_viper_tick | 204,097 | +2.05% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,524 | +0.76% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,365 | -9.32% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,236 (-4.38%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,611 | +1.24% |
| benchmark | +1,928 | +0.88% |
| snake_viper_wild | +1,503 | +0.73% |
| snake_viper_tick | +1,478 | +0.73% |
| benchmark_smallcap | +695 | +0.35% |
| gold | +411 | +0.23% |
| unified | +298 | +0.13% |
| oracle | +201 | +0.10% |
| intramonth | +55 | +0.03% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| random_hold | -226 | -0.11% |
| snake_abs_exit | -249 | -0.12% |
| snake_anaconda | -331 | -0.16% |
| snake_abs_exit_conv | -790 | -0.37% |
| snake_abs | -876 | -0.42% |
| snake_abs_conv | -880 | -0.42% |

Average per day so far: benchmark Rs +629, unified Rs +621, snake_abs_exit Rs +443, intraweek Rs +396, snake_abs_exit_conv Rs +388, oracle Rs +349, intramonth Rs +334, snake_abs_conv Rs +285, snake_viper_wild Rs +283, snake_abs Rs +281, random_hold Rs +216, snake_viper_tick Rs +171, snake_anaconda Rs +159, nifty_calls Rs +52, benchmark_smallcap Rs +49, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -532

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.