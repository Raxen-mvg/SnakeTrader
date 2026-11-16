# Paper trading report

Updated 2026-11-16 14:25 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,431 | +10.22% | 0 | - | 236 |
| benchmark | 219,905 | +9.95% | 0 | - | 237 |
| snake_abs_exit | 213,474 | +6.74% | 2 | 50% | 345 |
| snake_abs_exit_conv | 212,250 | +6.12% | 2 | 50% | 345 |
| oracle | 211,042 | +5.52% | 0 | - | 233 |
| intramonth | 210,949 | +5.47% | 0 | - | 235 |
| intraweek | 210,867 | +5.43% | 35 | 54% | 3,851 |
| snake_abs | 209,596 | +4.80% | 1 | 100% | 255 |
| snake_abs_conv | 209,432 | +4.72% | 1 | 100% | 255 |
| random_hold | 207,509 | +3.75% | 10 | 70% | 733 |
| snake_viper_wild | 205,400 | +2.70% | 14 | 50% | 2,496 |
| snake_anaconda | 203,903 | +1.95% | 3 | 33% | 374 |
| snake_viper_tick | 201,887 | +0.94% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,280 | +0.14% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,300 | -9.35% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,156 (-4.92%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,411 | +0.64% |
| intramonth | +892 | +0.42% |
| snake_viper_wild | +643 | +0.31% |
| snake_viper_tick | +632 | +0.31% |
| benchmark | +566 | +0.26% |
| random_hold | +283 | +0.14% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_anaconda | -989 | -0.48% |
| oracle | -2,055 | -0.96% |
| benchmark_smallcap | -2,590 | -1.28% |
| gold | -2,696 | -1.47% |
| snake_abs_conv | -2,935 | -1.38% |
| snake_abs | -2,944 | -1.39% |
| snake_abs_exit | -3,511 | -1.62% |
| snake_abs_exit_conv | -4,131 | -1.91% |
| intraweek | -5,278 | -2.44% |

Average per day so far: unified Rs +601, benchmark Rs +585, snake_abs_exit Rs +435, snake_abs_exit_conv Rs +395, oracle Rs +325, intramonth Rs +322, intraweek Rs +320, snake_abs_conv Rs +304, snake_abs Rs +300, random_hold Rs +221, snake_viper_wild Rs +208, snake_anaconda Rs +135, snake_viper_tick Rs +82, nifty_calls Rs +54, benchmark_smallcap Rs +9, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -347, snake Rs -368, gold Rs -550

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.