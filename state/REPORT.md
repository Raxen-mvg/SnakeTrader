# Paper trading report

Updated 2026-11-25 14:33 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,732 | +12.37% | 0 | - | 237 |
| unified | 224,404 | +12.20% | 0 | - | 236 |
| oracle | 212,777 | +6.39% | 0 | - | 233 |
| intramonth | 211,903 | +5.95% | 0 | - | 235 |
| random_hold | 209,746 | +4.87% | 12 | 75% | 1,009 |
| intraweek | 207,130 | +3.56% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,514 | +0.76% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,195 | +0.60% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,860 | -0.07% | 1 | 100% | 255 |
| snake_abs_conv | 199,655 | -0.17% | 1 | 100% | 255 |
| benchmark_smallcap | 198,878 | -0.56% | 0 | - | 237 |
| snake_viper_wild | 197,702 | -1.15% | 16 | 50% | 2,827 |
| snake_viper_tick | 194,332 | -2.83% | 15 | 47% | 2,625 |
| snake_anaconda | 193,243 | -3.38% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,073 | -17.46% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,941 (-5.53%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,259 | +1.47% |
| random_hold | +1,320 | +0.63% |
| oracle | +435 | +0.20% |
| unified | +119 | +0.05% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -101 | -0.05% |
| intramonth | -849 | -0.40% |
| snake_viper_tick | -3,361 | -1.70% |
| snake_viper_wild | -3,423 | -1.70% |
| gold | -4,357 | -2.57% |
| intraweek | -4,489 | -2.12% |
| snake_anaconda | -5,460 | -2.75% |
| snake_abs | -5,601 | -2.73% |
| snake_abs_conv | -5,648 | -2.75% |
| snake_abs_exit_conv | -5,850 | -2.83% |
| snake_abs_exit | -5,981 | -2.88% |

Average per day so far: benchmark Rs +618, unified Rs +610, oracle Rs +319, intramonth Rs +298, random_hold Rs +244, intraweek Rs +178, nifty_calls Rs +46, snake_abs_exit Rs +41, snake_abs_exit_conv Rs +32, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -4, snake_abs_conv Rs -9, benchmark_smallcap Rs -31, snake_viper_wild Rs -72, snake_anaconda Rs -193, snake_viper_tick Rs -195, snake_nonews Rs -292, snake Rs -311, gold Rs -873

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.