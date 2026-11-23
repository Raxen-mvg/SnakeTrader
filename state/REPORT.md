# Paper trading report

Updated 2026-11-23 13:10 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,918 | +11.96% | 0 | - | 236 |
| benchmark | 222,514 | +11.26% | 0 | - | 237 |
| intraweek | 212,286 | +6.14% | 40 | 55% | 4,400 |
| intramonth | 212,127 | +6.06% | 0 | - | 235 |
| oracle | 211,639 | +5.82% | 0 | - | 233 |
| random_hold | 208,915 | +4.46% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,022 | +3.51% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,620 | +2.81% | 2 | 50% | 345 |
| snake_abs | 204,473 | +2.24% | 1 | 100% | 255 |
| snake_abs_conv | 204,311 | +2.15% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,894 | +0.45% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,215 | -0.39% | 0 | - | 237 |
| snake_anaconda | 198,035 | -0.98% | 3 | 33% | 374 |
| snake_viper_tick | 197,467 | -1.27% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,055 | -14.97% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,083 (-4.96%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,006 | +1.19% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -840 | -0.40% |
| snake_abs_exit_conv | -997 | -0.48% |
| snake_abs | -1,446 | -0.70% |
| snake_abs_conv | -1,472 | -0.71% |
| snake_abs_exit | -1,540 | -0.74% |
| benchmark_smallcap | -1,693 | -0.84% |
| random_hold | -1,844 | -0.88% |
| snake_anaconda | -1,871 | -0.94% |
| snake_viper_tick | -1,905 | -0.95% |
| snake_viper_wild | -1,935 | -0.95% |
| unified | -2,264 | -1.00% |
| benchmark | -2,624 | -1.17% |
| intramonth | -2,877 | -1.34% |
| intraweek | -3,427 | -1.59% |

Average per day so far: unified Rs +613, benchmark Rs +577, intraweek Rs +315, intramonth Rs +311, oracle Rs +298, random_hold Rs +229, snake_abs_exit Rs +195, snake_abs_exit_conv Rs +156, snake_abs Rs +121, snake_abs_conv Rs +120, nifty_calls Rs +47, snake_viper_wild Rs +29, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -22, snake_anaconda Rs -58, snake_viper_tick Rs -90, snake_nonews Rs -300, snake Rs -320, gold Rs -768

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.