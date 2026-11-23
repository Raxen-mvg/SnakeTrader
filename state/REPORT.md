# Paper trading report

Updated 2026-11-23 11:03 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,306 | +12.15% | 0 | - | 236 |
| benchmark | 223,041 | +11.52% | 0 | - | 237 |
| intramonth | 212,450 | +6.22% | 0 | - | 235 |
| intraweek | 212,351 | +6.17% | 40 | 55% | 4,400 |
| oracle | 211,149 | +5.58% | 0 | - | 233 |
| random_hold | 209,718 | +4.86% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,720 | +3.36% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,774 | +2.89% | 2 | 50% | 345 |
| snake_abs | 204,072 | +2.04% | 1 | 100% | 255 |
| snake_abs_conv | 203,917 | +1.96% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,265 | +0.13% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,080 | -0.46% | 0 | - | 237 |
| snake_anaconda | 197,720 | -1.14% | 3 | 33% | 374 |
| snake_viper_tick | 196,851 | -1.57% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,808 | -15.10% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,181 (-4.91%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,759 | +1.05% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -842 | -0.41% |
| random_hold | -1,041 | -0.49% |
| oracle | -1,329 | -0.63% |
| benchmark_smallcap | -1,827 | -0.91% |
| snake_abs_exit | -1,842 | -0.88% |
| snake_abs | -1,848 | -0.90% |
| snake_abs_conv | -1,866 | -0.91% |
| unified | -1,876 | -0.83% |
| benchmark | -2,096 | -0.93% |
| snake_anaconda | -2,185 | -1.09% |
| snake_viper_tick | -2,520 | -1.26% |
| intramonth | -2,554 | -1.19% |
| snake_viper_wild | -2,564 | -1.26% |
| intraweek | -3,361 | -1.56% |

Average per day so far: unified Rs +623, benchmark Rs +591, intramonth Rs +319, intraweek Rs +317, oracle Rs +286, random_hold Rs +249, snake_abs_exit Rs +187, snake_abs_exit_conv Rs +160, snake_abs Rs +110, snake_abs_conv Rs +109, nifty_calls Rs +47, snake_viper_wild Rs +9, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -26, snake_anaconda Rs -67, snake_viper_tick Rs -112, snake_nonews Rs -300, snake Rs -320, gold Rs -774

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.