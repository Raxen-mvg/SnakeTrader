# Paper trading report

Updated 2026-11-17 15:16 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,746 | +10.87% | 0 | - | 236 |
| benchmark | 221,695 | +10.85% | 0 | - | 237 |
| intraweek | 213,447 | +6.72% | 35 | 54% | 3,851 |
| snake_abs_exit | 213,442 | +6.72% | 2 | 50% | 345 |
| oracle | 212,726 | +6.36% | 0 | - | 233 |
| snake_abs_exit_conv | 211,872 | +5.94% | 2 | 50% | 345 |
| intramonth | 211,806 | +5.90% | 0 | - | 235 |
| snake_viper_wild | 209,468 | +4.73% | 14 | 50% | 2,496 |
| snake_abs | 208,604 | +4.30% | 1 | 100% | 255 |
| snake_abs_conv | 208,469 | +4.23% | 1 | 100% | 255 |
| random_hold | 208,308 | +4.15% | 10 | 70% | 733 |
| snake_viper_tick | 205,888 | +2.94% | 13 | 46% | 2,299 |
| snake_anaconda | 204,326 | +2.16% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,235 | +0.12% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,806 | -9.60% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,335 (-4.33%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,323 | +1.61% |
| snake_viper_tick | +3,268 | +1.61% |
| intraweek | +2,181 | +1.03% |
| benchmark | +1,614 | +0.73% |
| oracle | +703 | +0.33% |
| random_hold | +514 | +0.25% |
| unified | +308 | +0.14% |
| intramonth | +187 | +0.09% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -148 | -0.08% |
| benchmark_smallcap | -594 | -0.30% |
| snake_anaconda | -777 | -0.38% |
| snake_abs_exit | -968 | -0.45% |
| snake_abs_exit_conv | -1,345 | -0.63% |
| snake_abs_conv | -1,521 | -0.72% |
| snake_abs | -1,530 | -0.73% |

Average per day so far: unified Rs +621, benchmark Rs +620, snake_abs_exit Rs +420, intraweek Rs +384, snake_abs_exit_conv Rs +371, oracle Rs +364, snake_viper_wild Rs +351, intramonth Rs +337, snake_abs_conv Rs +265, snake_abs Rs +261, snake_viper_tick Rs +245, random_hold Rs +237, snake_anaconda Rs +144, nifty_calls Rs +52, benchmark_smallcap Rs +8, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -548

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.