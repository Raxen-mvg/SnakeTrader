# Paper trading report

Updated 2026-11-18 14:10 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,292 | +11.15% | 0 | - | 236 |
| benchmark | 220,142 | +10.07% | 0 | - | 237 |
| snake_abs_exit | 213,847 | +6.92% | 2 | 50% | 345 |
| oracle | 212,199 | +6.10% | 0 | - | 233 |
| intraweek | 212,138 | +6.07% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 212,086 | +6.04% | 2 | 50% | 345 |
| intramonth | 212,009 | +6.00% | 0 | - | 235 |
| snake_abs | 209,014 | +4.51% | 1 | 100% | 255 |
| snake_abs_conv | 208,897 | +4.45% | 1 | 100% | 255 |
| snake_viper_wild | 206,972 | +3.49% | 16 | 50% | 2,827 |
| random_hold | 206,885 | +3.44% | 10 | 70% | 733 |
| snake_anaconda | 204,154 | +2.08% | 3 | 33% | 374 |
| snake_viper_tick | 203,437 | +1.72% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,495 | -0.25% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,074 | -11.46% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,919 (-4.54%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +854 | +0.39% |
| snake_abs_exit | +705 | +0.33% |
| snake_abs_exit_conv | +512 | +0.24% |
| snake_abs_conv | +478 | +0.23% |
| intramonth | +467 | +0.22% |
| snake_abs | +455 | +0.22% |
| snake_anaconda | +99 | +0.05% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -287 | -0.14% |
| benchmark_smallcap | -1,076 | -0.54% |
| intraweek | -1,185 | -0.56% |
| benchmark | -1,461 | -0.66% |
| random_hold | -1,547 | -0.74% |
| snake_viper_tick | -2,399 | -1.17% |
| snake_viper_wild | -2,443 | -1.17% |
| gold | -3,650 | -2.02% |

Average per day so far: unified Rs +619, benchmark Rs +560, snake_abs_exit Rs +420, snake_abs_exit_conv Rs +366, oracle Rs +339, intraweek Rs +337, intramonth Rs +334, snake_abs_conv Rs +270, snake_abs Rs +265, snake_viper_wild Rs +249, random_hold Rs +191, snake_viper_tick Rs +137, snake_anaconda Rs +134, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -16, snake_nonews Rs -326, snake Rs -347, gold Rs -637

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.