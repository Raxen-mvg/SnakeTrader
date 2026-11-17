# Paper trading report

Updated 2026-11-17 10:21 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,915 | +10.96% | 0 | - | 236 |
| benchmark | 221,573 | +10.79% | 0 | - | 237 |
| snake_abs_exit | 215,736 | +7.87% | 2 | 50% | 345 |
| snake_abs_exit_conv | 214,335 | +7.17% | 2 | 50% | 345 |
| intraweek | 213,221 | +6.61% | 35 | 54% | 3,851 |
| oracle | 212,508 | +6.25% | 0 | - | 233 |
| intramonth | 211,947 | +5.97% | 0 | - | 235 |
| snake_abs | 210,652 | +5.33% | 1 | 100% | 255 |
| snake_abs_conv | 210,504 | +5.25% | 1 | 100% | 255 |
| random_hold | 208,230 | +4.12% | 10 | 70% | 733 |
| snake_viper_wild | 207,178 | +3.59% | 14 | 50% | 2,496 |
| snake_anaconda | 206,007 | +3.00% | 3 | 33% | 374 |
| snake_viper_tick | 203,636 | +1.82% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,185 | +1.09% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,497 | -9.25% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,375 (-4.31%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,955 | +0.93% |
| benchmark | +1,492 | +0.68% |
| benchmark_smallcap | +1,356 | +0.68% |
| snake_abs_exit | +1,327 | +0.62% |
| snake_abs_exit_conv | +1,117 | +0.52% |
| snake_viper_wild | +1,034 | +0.50% |
| snake_viper_tick | +1,016 | +0.50% |
| snake_anaconda | +904 | +0.44% |
| gold | +543 | +0.30% |
| snake_abs | +518 | +0.25% |
| snake_abs_conv | +514 | +0.24% |
| oracle | +485 | +0.23% |
| unified | +478 | +0.22% |
| random_hold | +437 | +0.21% |
| intramonth | +328 | +0.15% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +626, benchmark Rs +616, snake_abs_exit Rs +492, snake_abs_exit_conv Rs +448, intraweek Rs +378, oracle Rs +357, intramonth Rs +341, snake_abs_conv Rs +328, snake_abs Rs +323, snake_viper_wild Rs +266, random_hold Rs +235, snake_anaconda Rs +200, snake_viper_tick Rs +151, benchmark_smallcap Rs +70, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -529

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.