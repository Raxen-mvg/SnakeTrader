# Paper trading report

Updated 2026-11-13 13:40 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,507 | +10.25% | 0 | - | 236 |
| benchmark | 219,477 | +9.74% | 0 | - | 237 |
| snake_abs_exit | 216,696 | +8.35% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,453 | +8.23% | 2 | 50% | 345 |
| intraweek | 216,018 | +8.01% | 30 | 53% | 3,302 |
| oracle | 213,245 | +6.62% | 0 | - | 233 |
| snake_abs | 212,359 | +6.18% | 1 | 100% | 255 |
| snake_abs_conv | 212,192 | +6.10% | 1 | 100% | 255 |
| intramonth | 211,153 | +5.58% | 0 | - | 235 |
| random_hold | 207,351 | +3.67% | 10 | 70% | 733 |
| snake_viper_wild | 205,714 | +2.86% | 14 | 50% | 2,496 |
| snake_anaconda | 204,621 | +2.31% | 3 | 33% | 374 |
| benchmark_smallcap | 202,724 | +1.36% | 0 | - | 237 |
| snake_viper_tick | 202,195 | +1.10% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,897 | -8.05% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,945 (-4.03%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,360 | +0.63% |
| snake_viper_wild | +421 | +0.20% |
| snake_viper_tick | +414 | +0.20% |
| oracle | +130 | +0.06% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -190 | -0.09% |
| intramonth | -440 | -0.21% |
| benchmark_smallcap | -482 | -0.24% |
| random_hold | -703 | -0.34% |
| snake_abs_exit | -747 | -0.34% |
| benchmark | -1,071 | -0.49% |
| snake_anaconda | -1,306 | -0.63% |
| gold | -1,414 | -0.76% |
| snake_abs_exit_conv | -2,221 | -1.02% |
| snake_abs_conv | -3,343 | -1.55% |
| snake_abs | -3,352 | -1.55% |

Average per day so far: unified Rs +621, benchmark Rs +590, snake_abs_exit Rs +557, snake_abs_exit_conv Rs +548, intraweek Rs +485, snake_abs_conv Rs +406, oracle Rs +401, snake_abs Rs +399, intramonth Rs +338, snake_viper_wild Rs +229, random_hold Rs +223, snake_anaconda Rs +165, snake_viper_tick Rs +100, benchmark_smallcap Rs +94, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -488

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.