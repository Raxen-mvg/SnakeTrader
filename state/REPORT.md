# Paper trading report

Updated 2026-11-13 13:13 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,006 | +10.00% | 0 | - | 236 |
| benchmark | 219,385 | +9.69% | 0 | - | 237 |
| snake_abs_exit | 216,756 | +8.38% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,332 | +8.17% | 2 | 50% | 345 |
| intraweek | 215,647 | +7.82% | 30 | 53% | 3,302 |
| oracle | 212,911 | +6.46% | 0 | - | 233 |
| snake_abs | 212,170 | +6.08% | 1 | 100% | 255 |
| snake_abs_conv | 212,000 | +6.00% | 1 | 100% | 255 |
| intramonth | 210,592 | +5.30% | 0 | - | 235 |
| random_hold | 207,020 | +3.51% | 10 | 70% | 733 |
| snake_viper_wild | 205,518 | +2.76% | 14 | 50% | 2,496 |
| snake_anaconda | 204,363 | +2.18% | 3 | 33% | 374 |
| benchmark_smallcap | 202,690 | +1.34% | 0 | - | 237 |
| snake_viper_tick | 202,003 | +1.00% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,848 | -8.08% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,599 (-4.20%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +989 | +0.46% |
| snake_viper_wild | +226 | +0.11% |
| snake_viper_tick | +221 | +0.11% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -204 | -0.10% |
| benchmark_smallcap | -516 | -0.25% |
| snake_abs_exit | -687 | -0.32% |
| unified | -691 | -0.31% |
| intramonth | -1,001 | -0.47% |
| random_hold | -1,034 | -0.50% |
| benchmark | -1,163 | -0.53% |
| gold | -1,463 | -0.79% |
| snake_anaconda | -1,565 | -0.76% |
| snake_abs_exit_conv | -2,342 | -1.07% |
| snake_abs_conv | -3,535 | -1.64% |
| snake_abs | -3,542 | -1.64% |

Average per day so far: unified Rs +606, benchmark Rs +587, snake_abs_exit Rs +559, snake_abs_exit_conv Rs +544, intraweek Rs +474, snake_abs_conv Rs +400, snake_abs Rs +393, oracle Rs +391, intramonth Rs +321, snake_viper_wild Rs +221, random_hold Rs +213, snake_anaconda Rs +156, benchmark_smallcap Rs +93, snake_viper_tick Rs +91, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -489

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.