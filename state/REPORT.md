# Paper trading report

Updated 2026-11-13 11:22 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,552 | +10.28% | 0 | - | 236 |
| benchmark | 219,607 | +9.80% | 0 | - | 237 |
| snake_abs_exit_conv | 216,575 | +8.29% | 2 | 50% | 345 |
| snake_abs_exit | 216,480 | +8.24% | 2 | 50% | 345 |
| intraweek | 216,157 | +8.08% | 30 | 53% | 3,302 |
| oracle | 213,522 | +6.76% | 0 | - | 233 |
| snake_abs | 212,780 | +6.39% | 1 | 100% | 255 |
| snake_abs_conv | 212,611 | +6.31% | 1 | 100% | 255 |
| intramonth | 211,315 | +5.66% | 0 | - | 235 |
| random_hold | 207,067 | +3.53% | 10 | 70% | 733 |
| snake_viper_wild | 206,041 | +3.02% | 14 | 50% | 2,496 |
| snake_anaconda | 204,894 | +2.45% | 3 | 33% | 374 |
| benchmark_smallcap | 203,295 | +1.65% | 0 | - | 237 |
| snake_viper_tick | 202,517 | +1.26% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,650 | -8.18% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,075 (-3.96%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,499 | +0.70% |
| snake_viper_wild | +749 | +0.36% |
| snake_viper_tick | +736 | +0.36% |
| oracle | +406 | +0.19% |
| benchmark_smallcap | +90 | +0.04% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -144 | -0.07% |
| intramonth | -278 | -0.13% |
| benchmark | -941 | -0.43% |
| snake_abs_exit | -962 | -0.44% |
| random_hold | -987 | -0.47% |
| snake_anaconda | -1,033 | -0.50% |
| gold | -1,660 | -0.90% |
| snake_abs_exit_conv | -2,099 | -0.96% |
| snake_abs_conv | -2,924 | -1.36% |
| snake_abs | -2,932 | -1.36% |

Average per day so far: unified Rs +623, benchmark Rs +594, snake_abs_exit_conv Rs +553, snake_abs_exit Rs +549, intraweek Rs +490, snake_abs_conv Rs +420, snake_abs Rs +412, oracle Rs +410, intramonth Rs +343, snake_viper_wild Rs +242, random_hold Rs +214, snake_anaconda Rs +175, snake_viper_tick Rs +114, benchmark_smallcap Rs +114, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -495

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.