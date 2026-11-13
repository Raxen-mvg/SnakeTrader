# Paper trading report

Updated 2026-11-13 10:31 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,706 | +10.35% | 0 | - | 236 |
| benchmark | 219,928 | +9.96% | 0 | - | 237 |
| snake_abs_exit_conv | 216,892 | +8.45% | 2 | 50% | 345 |
| intraweek | 216,595 | +8.30% | 30 | 53% | 3,302 |
| snake_abs_exit | 216,469 | +8.23% | 2 | 50% | 345 |
| oracle | 213,784 | +6.89% | 0 | - | 233 |
| snake_abs | 213,101 | +6.55% | 1 | 100% | 255 |
| snake_abs_conv | 212,934 | +6.47% | 1 | 100% | 255 |
| intramonth | 211,432 | +5.72% | 0 | - | 235 |
| random_hold | 207,341 | +3.67% | 10 | 70% | 733 |
| snake_viper_wild | 206,665 | +3.33% | 14 | 50% | 2,496 |
| snake_anaconda | 205,147 | +2.57% | 3 | 33% | 374 |
| benchmark_smallcap | 203,564 | +1.78% | 0 | - | 237 |
| snake_viper_tick | 203,131 | +1.56% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,440 | -7.78% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,316 (-3.84%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,936 | +0.90% |
| snake_viper_wild | +1,373 | +0.67% |
| snake_viper_tick | +1,349 | +0.67% |
| oracle | +669 | +0.31% |
| benchmark_smallcap | +359 | +0.18% |
| unified | +9 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intramonth | -161 | -0.08% |
| benchmark | -620 | -0.28% |
| random_hold | -713 | -0.34% |
| snake_anaconda | -780 | -0.38% |
| gold | -871 | -0.47% |
| snake_abs_exit | -974 | -0.45% |
| snake_abs_exit_conv | -1,782 | -0.81% |
| snake_abs_conv | -2,601 | -1.21% |
| snake_abs | -2,611 | -1.21% |

Average per day so far: unified Rs +627, benchmark Rs +604, snake_abs_exit_conv Rs +563, snake_abs_exit Rs +549, intraweek Rs +503, snake_abs_conv Rs +431, snake_abs Rs +423, oracle Rs +418, intramonth Rs +346, snake_viper_wild Rs +267, random_hold Rs +222, snake_anaconda Rs +184, snake_viper_tick Rs +142, benchmark_smallcap Rs +123, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -472

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.