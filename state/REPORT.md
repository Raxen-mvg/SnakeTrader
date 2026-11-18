# Paper trading report

Updated 2026-11-18 14:06 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,604 | +11.30% | 0 | - | 236 |
| benchmark | 220,280 | +10.14% | 0 | - | 237 |
| snake_abs_exit | 213,826 | +6.91% | 2 | 50% | 345 |
| intraweek | 212,486 | +6.24% | 35 | 54% | 3,851 |
| oracle | 212,313 | +6.16% | 0 | - | 233 |
| intramonth | 212,310 | +6.16% | 0 | - | 235 |
| snake_abs_exit_conv | 212,074 | +6.04% | 2 | 50% | 345 |
| snake_abs | 209,188 | +4.59% | 1 | 100% | 255 |
| snake_abs_conv | 209,069 | +4.53% | 1 | 100% | 255 |
| random_hold | 207,246 | +3.62% | 10 | 70% | 733 |
| snake_viper_wild | 206,972 | +3.49% | 16 | 50% | 2,827 |
| snake_anaconda | 204,152 | +2.08% | 3 | 33% | 374 |
| snake_viper_tick | 203,437 | +1.72% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,495 | -0.25% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,042 | -11.48% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,137 (-4.43%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,165 | +0.53% |
| intramonth | +768 | +0.36% |
| snake_abs_exit | +685 | +0.32% |
| snake_abs_conv | +649 | +0.31% |
| snake_abs | +630 | +0.30% |
| snake_abs_exit_conv | +500 | +0.24% |
| snake_anaconda | +97 | +0.05% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -173 | -0.08% |
| intraweek | -837 | -0.39% |
| benchmark_smallcap | -1,076 | -0.54% |
| random_hold | -1,186 | -0.57% |
| benchmark | -1,323 | -0.60% |
| snake_viper_tick | -2,399 | -1.17% |
| snake_viper_wild | -2,443 | -1.17% |
| gold | -3,683 | -2.04% |

Average per day so far: unified Rs +628, benchmark Rs +563, snake_abs_exit Rs +419, snake_abs_exit_conv Rs +366, intraweek Rs +347, oracle Rs +342, intramonth Rs +342, snake_abs_conv Rs +275, snake_abs Rs +270, snake_viper_wild Rs +249, random_hold Rs +201, snake_viper_tick Rs +137, snake_anaconda Rs +134, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -16, snake_nonews Rs -326, snake Rs -347, gold Rs -638

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.