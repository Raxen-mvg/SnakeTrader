# Paper trading report

Updated 2026-11-16 09:45 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,724 | +10.36% | 0 | - | 237 |
| unified | 218,790 | +9.39% | 0 | - | 236 |
| snake_abs_exit | 214,644 | +7.32% | 2 | 50% | 345 |
| intraweek | 214,440 | +7.22% | 35 | 54% | 3,851 |
| oracle | 213,493 | +6.75% | 0 | - | 233 |
| snake_abs_exit_conv | 213,405 | +6.70% | 2 | 50% | 345 |
| snake_abs | 210,465 | +5.23% | 1 | 100% | 255 |
| snake_abs_conv | 210,292 | +5.15% | 1 | 100% | 255 |
| intramonth | 209,930 | +4.96% | 0 | - | 235 |
| random_hold | 207,588 | +3.79% | 10 | 70% | 733 |
| snake_anaconda | 204,619 | +2.31% | 3 | 33% | 374 |
| snake_viper_wild | 203,368 | +1.68% | 14 | 50% | 2,496 |
| benchmark_smallcap | 202,017 | +1.01% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 199,889 | -0.06% | 13 | 46% | 2,299 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 182,302 | -8.85% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,149 (-4.43%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,385 | +0.63% |
| oracle | +396 | +0.19% |
| random_hold | +362 | +0.17% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intramonth | -127 | -0.06% |
| unified | -231 | -0.10% |
| snake_anaconda | -273 | -0.13% |
| benchmark_smallcap | -852 | -0.42% |
| snake_viper_tick | -1,366 | -0.68% |
| snake_viper_wild | -1,390 | -0.68% |
| gold | -1,693 | -0.92% |
| intraweek | -1,705 | -0.79% |
| snake_abs_conv | -2,075 | -0.98% |
| snake_abs | -2,075 | -0.98% |
| snake_abs_exit | -2,341 | -1.08% |
| snake_abs_exit_conv | -2,977 | -1.38% |

Average per day so far: benchmark Rs +610, unified Rs +553, snake_abs_exit Rs +472, snake_abs_exit_conv Rs +432, intraweek Rs +425, oracle Rs +397, snake_abs_conv Rs +332, snake_abs Rs +327, intramonth Rs +292, random_hold Rs +223, snake_anaconda Rs +159, snake_viper_wild Rs +130, benchmark_smallcap Rs +67, nifty_calls Rs +54, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -5, snake_nonews Rs -347, snake Rs -368, gold Rs -521

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.