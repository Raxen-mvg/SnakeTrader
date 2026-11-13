# Paper trading report

Updated 2026-11-13 12:16 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,965 | +9.98% | 0 | - | 236 |
| benchmark | 219,002 | +9.50% | 0 | - | 237 |
| snake_abs_exit_conv | 216,317 | +8.16% | 2 | 50% | 345 |
| snake_abs_exit | 216,280 | +8.14% | 2 | 50% | 345 |
| intraweek | 215,376 | +7.69% | 30 | 53% | 3,302 |
| oracle | 212,922 | +6.46% | 0 | - | 233 |
| snake_abs | 212,550 | +6.28% | 1 | 100% | 255 |
| snake_abs_conv | 212,379 | +6.19% | 1 | 100% | 255 |
| intramonth | 210,605 | +5.30% | 0 | - | 235 |
| random_hold | 207,019 | +3.51% | 10 | 70% | 733 |
| snake_viper_wild | 205,561 | +2.78% | 14 | 50% | 2,496 |
| snake_anaconda | 204,773 | +2.39% | 3 | 33% | 374 |
| benchmark_smallcap | 202,432 | +1.22% | 0 | - | 237 |
| snake_viper_tick | 202,045 | +1.02% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,486 | -8.26% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,535 (-4.23%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +718 | +0.33% |
| snake_viper_wild | +268 | +0.13% |
| snake_viper_tick | +263 | +0.13% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -194 | -0.09% |
| unified | -732 | -0.33% |
| benchmark_smallcap | -773 | -0.38% |
| intramonth | -988 | -0.47% |
| random_hold | -1,035 | -0.50% |
| snake_anaconda | -1,154 | -0.56% |
| snake_abs_exit | -1,162 | -0.54% |
| benchmark | -1,545 | -0.70% |
| gold | -1,825 | -0.98% |
| snake_abs_exit_conv | -2,357 | -1.08% |
| snake_abs_conv | -3,156 | -1.46% |
| snake_abs | -3,162 | -1.47% |

Average per day so far: unified Rs +605, benchmark Rs +576, snake_abs_exit_conv Rs +544, snake_abs_exit Rs +543, intraweek Rs +466, snake_abs_conv Rs +413, snake_abs Rs +405, oracle Rs +392, intramonth Rs +321, snake_viper_wild Rs +222, random_hold Rs +213, snake_anaconda Rs +170, snake_viper_tick Rs +93, benchmark_smallcap Rs +84, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -500

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.