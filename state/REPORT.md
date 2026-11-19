# Paper trading report

Updated 2026-11-19 10:35 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,898 | +11.95% | 0 | - | 236 |
| benchmark | 220,525 | +10.26% | 0 | - | 237 |
| snake_abs_exit | 213,490 | +6.75% | 2 | 50% | 345 |
| intramonth | 213,482 | +6.74% | 0 | - | 235 |
| intraweek | 211,877 | +5.94% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,718 | +5.86% | 2 | 50% | 345 |
| oracle | 210,956 | +5.48% | 0 | - | 233 |
| snake_abs | 209,264 | +4.63% | 1 | 100% | 255 |
| snake_abs_conv | 209,142 | +4.57% | 1 | 100% | 255 |
| snake_viper_wild | 207,720 | +3.86% | 16 | 50% | 2,827 |
| random_hold | 207,713 | +3.86% | 10 | 70% | 733 |
| snake_viper_tick | 204,170 | +2.08% | 15 | 47% | 2,625 |
| snake_anaconda | 203,430 | +1.72% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,235 | +0.12% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,789 | -12.61% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,266 (-4.37%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,287 | +0.58% |
| intramonth | +1,208 | +0.57% |
| benchmark_smallcap | +908 | +0.46% |
| random_hold | +780 | +0.38% |
| snake_viper_wild | +680 | +0.33% |
| snake_viper_tick | +666 | +0.33% |
| benchmark | +229 | +0.10% |
| oracle | +160 | +0.08% |
| intraweek | +37 | +0.02% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -172 | -0.08% |
| snake_abs_conv | -183 | -0.09% |
| snake_abs_exit | -542 | -0.25% |
| snake_abs_exit_conv | -665 | -0.31% |
| snake_anaconda | -971 | -0.47% |
| gold | -2,532 | -1.43% |

Average per day so far: unified Rs +646, benchmark Rs +555, snake_abs_exit Rs +397, intramonth Rs +364, snake_abs_exit_conv Rs +345, intraweek Rs +321, oracle Rs +296, snake_abs_conv Rs +269, snake_viper_wild Rs +266, snake_abs Rs +265, random_hold Rs +208, snake_viper_tick Rs +160, snake_anaconda Rs +107, nifty_calls Rs +50, benchmark_smallcap Rs +7, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -681

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.