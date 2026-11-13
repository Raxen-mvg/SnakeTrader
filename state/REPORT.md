# Paper trading report

Updated 2026-11-13 15:01 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,008 | +10.00% | 0 | - | 236 |
| benchmark | 219,316 | +9.66% | 0 | - | 237 |
| snake_abs_exit | 217,438 | +8.72% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,932 | +8.47% | 2 | 50% | 345 |
| intraweek | 216,176 | +8.09% | 30 | 53% | 3,302 |
| oracle | 213,280 | +6.64% | 0 | - | 233 |
| snake_abs | 213,065 | +6.53% | 1 | 100% | 255 |
| snake_abs_conv | 212,896 | +6.45% | 1 | 100% | 255 |
| intramonth | 210,830 | +5.42% | 0 | - | 235 |
| random_hold | 207,101 | +3.55% | 10 | 70% | 733 |
| snake_anaconda | 205,361 | +2.68% | 3 | 33% | 374 |
| snake_viper_wild | 205,100 | +2.55% | 14 | 50% | 2,496 |
| benchmark_smallcap | 202,959 | +1.48% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,592 | +0.80% | 13 | 46% | 2,299 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,864 | -8.07% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,900 (-4.05%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,518 | +0.71% |
| oracle | +165 | +0.08% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_abs_exit | -4 | -0.00% |
| snake_viper_tick | -190 | -0.09% |
| snake_viper_wild | -193 | -0.09% |
| benchmark_smallcap | -247 | -0.12% |
| snake_anaconda | -566 | -0.28% |
| unified | -689 | -0.31% |
| intramonth | -763 | -0.36% |
| random_hold | -953 | -0.46% |
| benchmark | -1,232 | -0.56% |
| gold | -1,447 | -0.78% |
| snake_abs_exit_conv | -1,742 | -0.80% |
| snake_abs_conv | -2,639 | -1.23% |
| snake_abs | -2,646 | -1.23% |

Average per day so far: unified Rs +606, benchmark Rs +585, snake_abs_exit Rs +581, snake_abs_exit_conv Rs +564, intraweek Rs +490, snake_abs_conv Rs +430, snake_abs Rs +421, oracle Rs +402, intramonth Rs +328, random_hold Rs +215, snake_viper_wild Rs +204, snake_anaconda Rs +191, benchmark_smallcap Rs +102, snake_viper_tick Rs +72, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -489

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.