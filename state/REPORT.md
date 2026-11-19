# Paper trading report

Updated 2026-11-19 11:22 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,630 | +11.81% | 0 | - | 236 |
| benchmark | 220,877 | +10.44% | 0 | - | 237 |
| snake_abs_exit | 213,724 | +6.86% | 2 | 50% | 345 |
| intramonth | 213,141 | +6.57% | 0 | - | 235 |
| snake_abs_exit_conv | 211,776 | +5.89% | 2 | 50% | 345 |
| intraweek | 211,723 | +5.86% | 35 | 54% | 3,851 |
| oracle | 210,931 | +5.46% | 0 | - | 233 |
| snake_abs | 209,184 | +4.59% | 1 | 100% | 255 |
| snake_abs_conv | 209,064 | +4.53% | 1 | 100% | 255 |
| random_hold | 207,653 | +3.83% | 10 | 70% | 733 |
| snake_viper_wild | 207,417 | +3.71% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,874 | +1.94% | 15 | 47% | 2,625 |
| snake_anaconda | 203,445 | +1.72% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,392 | +0.20% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,348 | -12.33% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,121 (-4.44%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,065 | +0.53% |
| unified | +1,018 | +0.46% |
| intramonth | +868 | +0.41% |
| random_hold | +720 | +0.35% |
| benchmark | +581 | +0.26% |
| snake_viper_wild | +378 | +0.18% |
| snake_viper_tick | +370 | +0.18% |
| oracle | +135 | +0.06% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -116 | -0.06% |
| snake_abs | -253 | -0.12% |
| snake_abs_conv | -261 | -0.12% |
| snake_abs_exit | -308 | -0.14% |
| snake_abs_exit_conv | -607 | -0.29% |
| snake_anaconda | -956 | -0.47% |
| gold | -1,973 | -1.11% |

Average per day so far: unified Rs +639, benchmark Rs +564, snake_abs_exit Rs +404, intramonth Rs +355, snake_abs_exit_conv Rs +346, intraweek Rs +317, oracle Rs +295, snake_abs_conv Rs +267, snake_abs Rs +262, snake_viper_wild Rs +256, random_hold Rs +207, snake_viper_tick Rs +149, snake_anaconda Rs +108, nifty_calls Rs +50, benchmark_smallcap Rs +12, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -666

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.