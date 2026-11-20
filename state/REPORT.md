# Paper trading report

Updated 2026-11-20 10:20 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,907 | +12.45% | 0 | - | 236 |
| benchmark | 222,598 | +11.30% | 0 | - | 237 |
| intramonth | 214,087 | +7.04% | 0 | - | 235 |
| intraweek | 213,630 | +6.82% | 35 | 54% | 3,851 |
| oracle | 212,759 | +6.38% | 0 | - | 233 |
| snake_abs_exit | 210,455 | +5.23% | 2 | 50% | 345 |
| random_hold | 208,790 | +4.39% | 11 | 73% | 979 |
| snake_abs_exit_conv | 208,168 | +4.08% | 2 | 50% | 345 |
| snake_abs | 206,785 | +3.39% | 1 | 100% | 255 |
| snake_abs_conv | 206,650 | +3.33% | 1 | 100% | 255 |
| snake_viper_wild | 205,614 | +2.81% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,109 | +1.05% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,882 | +0.44% | 3 | 33% | 374 |
| benchmark_smallcap | 200,269 | +0.13% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,468 | -17.27% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,561 (-4.22%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +741 | +0.35% |
| oracle | +671 | +0.32% |
| random_hold | +337 | +0.16% |
| unified | +292 | +0.13% |
| benchmark | +222 | +0.10% |
| intramonth | +79 | +0.04% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -1,199 | -0.59% |
| snake_viper_tick | -1,868 | -0.92% |
| snake_viper_wild | -1,908 | -0.92% |
| snake_abs | -2,195 | -1.05% |
| snake_abs_conv | -2,210 | -1.06% |
| snake_anaconda | -2,582 | -1.27% |
| snake_abs_exit_conv | -2,896 | -1.37% |
| snake_abs_exit | -2,896 | -1.36% |
| gold | -9,305 | -5.32% |

Average per day so far: unified Rs +655, benchmark Rs +595, intramonth Rs +371, intraweek Rs +359, oracle Rs +336, snake_abs_exit Rs +299, snake_abs_exit_conv Rs +233, random_hold Rs +231, snake_abs_conv Rs +190, snake_abs Rs +188, snake_viper_wild Rs +187, snake_viper_tick Rs +78, nifty_calls Rs +48, snake_anaconda Rs +27, benchmark_smallcap Rs +8, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -909

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.