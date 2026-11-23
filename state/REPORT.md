# Paper trading report

Updated 2026-11-23 14:43 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,202 | +12.10% | 0 | - | 236 |
| benchmark | 221,909 | +10.96% | 0 | - | 237 |
| oracle | 212,164 | +6.08% | 0 | - | 233 |
| intramonth | 212,147 | +6.07% | 0 | - | 235 |
| intraweek | 212,018 | +6.01% | 40 | 55% | 4,400 |
| random_hold | 208,617 | +4.31% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,224 | +3.61% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,622 | +3.31% | 2 | 50% | 345 |
| snake_abs | 205,229 | +2.62% | 1 | 100% | 255 |
| snake_abs_conv | 205,051 | +2.53% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,364 | +0.68% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,764 | -0.12% | 0 | - | 237 |
| snake_anaconda | 198,272 | -0.86% | 3 | 33% | 374 |
| snake_viper_tick | 197,928 | -1.04% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,709 | -15.14% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,242 (-4.88%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,660 | +0.99% |
| snake_abs_exit_conv | +6 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -314 | -0.15% |
| snake_abs | -691 | -0.34% |
| snake_abs_conv | -732 | -0.36% |
| benchmark_smallcap | -1,143 | -0.57% |
| snake_abs_exit | -1,338 | -0.64% |
| snake_viper_tick | -1,444 | -0.72% |
| snake_viper_wild | -1,465 | -0.72% |
| snake_anaconda | -1,634 | -0.82% |
| unified | -1,979 | -0.88% |
| random_hold | -2,142 | -1.02% |
| intramonth | -2,857 | -1.33% |
| benchmark | -3,228 | -1.43% |
| intraweek | -3,694 | -1.71% |

Average per day so far: unified Rs +621, benchmark Rs +562, oracle Rs +312, intramonth Rs +311, intraweek Rs +308, random_hold Rs +221, snake_abs_exit Rs +201, snake_abs_exit_conv Rs +184, snake_abs Rs +141, snake_abs_conv Rs +140, nifty_calls Rs +47, snake_viper_wild Rs +44, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -7, snake_anaconda Rs -51, snake_viper_tick Rs -74, snake_nonews Rs -300, snake Rs -320, gold Rs -777

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.