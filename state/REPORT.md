# Paper trading report

Updated 2026-11-26 09:28 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,046 | +12.52% | 0 | - | 237 |
| unified | 224,179 | +12.09% | 0 | - | 236 |
| oracle | 213,916 | +6.96% | 0 | - | 233 |
| intramonth | 211,809 | +5.90% | 0 | - | 235 |
| random_hold | 210,199 | +5.10% | 12 | 75% | 1,009 |
| intraweek | 207,360 | +3.68% | 40 | 55% | 4,400 |
| snake_abs_exit | 203,962 | +1.98% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,404 | +1.70% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,159 | +0.58% | 1 | 100% | 255 |
| snake_abs_conv | 200,992 | +0.50% | 1 | 100% | 255 |
| benchmark_smallcap | 200,235 | +0.12% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,545 | -1.73% | 16 | 50% | 2,827 |
| snake_anaconda | 195,657 | -2.17% | 3 | 33% | 374 |
| snake_viper_tick | 193,199 | -3.40% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,865 | -16.57% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,446 (-5.28%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,269 | +1.38% |
| snake_abs_exit | +1,706 | +0.84% |
| snake_abs_exit_conv | +1,429 | +0.71% |
| benchmark_smallcap | +1,424 | +0.72% |
| snake_anaconda | +1,104 | +0.57% |
| snake_abs_conv | +1,020 | +0.51% |
| snake_abs | +1,010 | +0.50% |
| random_hold | +706 | +0.34% |
| intraweek | +617 | +0.30% |
| oracle | +121 | +0.06% |
| intramonth | +116 | +0.06% |
| unified | +79 | +0.04% |
| benchmark | +23 | +0.01% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -978 | -0.50% |
| snake_viper_wild | -998 | -0.51% |

Average per day so far: benchmark Rs +611, unified Rs +590, oracle Rs +339, intramonth Rs +288, random_hold Rs +249, intraweek Rs +180, snake_abs_exit Rs +104, snake_abs_exit_conv Rs +90, nifty_calls Rs +45, snake_abs Rs +30, snake_abs_conv Rs +26, benchmark_smallcap Rs +6, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_viper_wild Rs -105, snake_anaconda Rs -121, snake_viper_tick Rs -227, snake_nonews Rs -284, snake Rs -304, gold Rs -808

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.