# Paper trading report

Updated 2026-11-17 12:10 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 222,376 | +11.19% | 0 | - | 237 |
| unified | 222,125 | +11.06% | 0 | - | 236 |
| snake_abs_exit | 214,728 | +7.36% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,013 | +6.51% | 2 | 50% | 345 |
| intraweek | 212,464 | +6.23% | 35 | 54% | 3,851 |
| oracle | 212,290 | +6.14% | 0 | - | 233 |
| intramonth | 211,967 | +5.98% | 0 | - | 235 |
| snake_abs | 209,723 | +4.86% | 1 | 100% | 255 |
| snake_abs_conv | 209,573 | +4.79% | 1 | 100% | 255 |
| random_hold | 207,792 | +3.90% | 10 | 70% | 733 |
| snake_viper_wild | 207,306 | +3.65% | 14 | 50% | 2,496 |
| snake_anaconda | 205,261 | +2.63% | 3 | 33% | 374 |
| snake_viper_tick | 203,762 | +1.88% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,219 | +1.11% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,267 | -9.37% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,220 (-4.39%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,295 | +1.04% |
| benchmark_smallcap | +1,390 | +0.69% |
| intraweek | +1,198 | +0.57% |
| snake_viper_wild | +1,162 | +0.56% |
| snake_viper_tick | +1,142 | +0.56% |
| unified | +688 | +0.31% |
| intramonth | +348 | +0.16% |
| snake_abs_exit | +319 | +0.15% |
| gold | +312 | +0.17% |
| oracle | +267 | +0.13% |
| snake_anaconda | +158 | +0.08% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| random_hold | -1 | -0.00% |
| snake_abs_exit_conv | -205 | -0.10% |
| snake_abs | -411 | -0.20% |
| snake_abs_conv | -417 | -0.20% |

Average per day so far: benchmark Rs +639, unified Rs +632, snake_abs_exit Rs +460, snake_abs_exit_conv Rs +407, intraweek Rs +356, oracle Rs +351, intramonth Rs +342, snake_abs_conv Rs +299, snake_abs Rs +295, snake_viper_wild Rs +271, random_hold Rs +223, snake_anaconda Rs +175, snake_viper_tick Rs +157, benchmark_smallcap Rs +72, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -535

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.