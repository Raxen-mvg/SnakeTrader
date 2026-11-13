# Paper trading report

Updated 2026-11-13 13:25 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,173 | +10.09% | 0 | - | 236 |
| benchmark | 219,461 | +9.73% | 0 | - | 237 |
| snake_abs_exit | 216,565 | +8.28% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,255 | +8.13% | 2 | 50% | 345 |
| intraweek | 215,794 | +7.90% | 30 | 53% | 3,302 |
| oracle | 213,020 | +6.51% | 0 | - | 233 |
| snake_abs | 212,076 | +6.04% | 1 | 100% | 255 |
| snake_abs_conv | 211,906 | +5.95% | 1 | 100% | 255 |
| intramonth | 210,848 | +5.42% | 0 | - | 235 |
| random_hold | 207,173 | +3.59% | 10 | 70% | 733 |
| snake_viper_wild | 205,464 | +2.73% | 14 | 50% | 2,496 |
| snake_anaconda | 204,325 | +2.16% | 3 | 33% | 374 |
| benchmark_smallcap | 202,813 | +1.41% | 0 | - | 237 |
| snake_viper_tick | 201,949 | +0.97% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,979 | -8.01% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,725 (-4.14%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,136 | +0.53% |
| snake_viper_wild | +171 | +0.08% |
| snake_viper_tick | +168 | +0.08% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -96 | -0.04% |
| benchmark_smallcap | -392 | -0.19% |
| unified | -524 | -0.24% |
| intramonth | -746 | -0.35% |
| snake_abs_exit | -878 | -0.40% |
| random_hold | -881 | -0.42% |
| benchmark | -1,086 | -0.49% |
| gold | -1,332 | -0.72% |
| snake_anaconda | -1,603 | -0.78% |
| snake_abs_exit_conv | -2,419 | -1.11% |
| snake_abs_conv | -3,629 | -1.68% |
| snake_abs | -3,636 | -1.69% |

Average per day so far: unified Rs +611, benchmark Rs +590, snake_abs_exit Rs +552, snake_abs_exit_conv Rs +542, intraweek Rs +479, snake_abs_conv Rs +397, oracle Rs +395, snake_abs Rs +390, intramonth Rs +329, snake_viper_wild Rs +219, random_hold Rs +217, snake_anaconda Rs +154, benchmark_smallcap Rs +97, snake_viper_tick Rs +89, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -485

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.