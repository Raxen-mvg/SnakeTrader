# Paper trading report

Updated 2026-11-13 14:13 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,652 | +10.33% | 0 | - | 236 |
| benchmark | 219,056 | +9.53% | 0 | - | 237 |
| snake_abs_exit | 216,396 | +8.20% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,172 | +8.09% | 2 | 50% | 345 |
| intraweek | 215,880 | +7.94% | 30 | 53% | 3,302 |
| oracle | 213,013 | +6.51% | 0 | - | 233 |
| snake_abs | 212,269 | +6.13% | 1 | 100% | 255 |
| snake_abs_conv | 212,102 | +6.05% | 1 | 100% | 255 |
| intramonth | 211,139 | +5.57% | 0 | - | 235 |
| random_hold | 207,146 | +3.57% | 10 | 70% | 733 |
| snake_viper_wild | 205,508 | +2.75% | 14 | 50% | 2,496 |
| snake_anaconda | 204,390 | +2.19% | 3 | 33% | 374 |
| benchmark_smallcap | 202,454 | +1.23% | 0 | - | 237 |
| snake_viper_tick | 201,993 | +1.00% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,897 | -8.05% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,853 (-4.07%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,222 | +0.57% |
| snake_viper_wild | +215 | +0.10% |
| snake_viper_tick | +212 | +0.10% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -45 | -0.02% |
| oracle | -102 | -0.05% |
| intramonth | -454 | -0.21% |
| benchmark_smallcap | -751 | -0.37% |
| random_hold | -908 | -0.44% |
| snake_abs_exit | -1,047 | -0.48% |
| gold | -1,414 | -0.76% |
| benchmark | -1,492 | -0.68% |
| snake_anaconda | -1,537 | -0.75% |
| snake_abs_exit_conv | -2,502 | -1.14% |
| snake_abs_conv | -3,433 | -1.59% |
| snake_abs | -3,443 | -1.60% |

Average per day so far: unified Rs +626, benchmark Rs +577, snake_abs_exit Rs +547, snake_abs_exit_conv Rs +539, intraweek Rs +481, snake_abs_conv Rs +403, snake_abs Rs +396, oracle Rs +394, intramonth Rs +338, snake_viper_wild Rs +220, random_hold Rs +217, snake_anaconda Rs +157, snake_viper_tick Rs +91, benchmark_smallcap Rs +85, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -488

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.