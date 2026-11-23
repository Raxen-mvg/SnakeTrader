# Paper trading report

Updated 2026-11-23 10:56 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,294 | +12.15% | 0 | - | 236 |
| benchmark | 223,279 | +11.64% | 0 | - | 237 |
| intraweek | 212,583 | +6.29% | 40 | 55% | 4,400 |
| intramonth | 212,532 | +6.27% | 0 | - | 235 |
| oracle | 211,113 | +5.56% | 0 | - | 233 |
| random_hold | 209,722 | +4.86% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,758 | +3.38% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,780 | +2.89% | 2 | 50% | 345 |
| snake_abs | 204,208 | +2.10% | 1 | 100% | 255 |
| snake_abs_conv | 204,053 | +2.03% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,097 | +0.05% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,316 | -0.34% | 0 | - | 237 |
| snake_anaconda | 197,710 | -1.15% | 3 | 33% | 374 |
| snake_viper_tick | 196,687 | -1.66% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,660 | -15.17% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,236 (-4.88%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,611 | +0.96% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -836 | -0.41% |
| random_hold | -1,037 | -0.49% |
| oracle | -1,366 | -0.64% |
| benchmark_smallcap | -1,592 | -0.79% |
| snake_abs | -1,712 | -0.83% |
| snake_abs_conv | -1,730 | -0.84% |
| snake_abs_exit | -1,805 | -0.86% |
| benchmark | -1,859 | -0.83% |
| unified | -1,888 | -0.83% |
| snake_anaconda | -2,196 | -1.10% |
| intramonth | -2,473 | -1.15% |
| snake_viper_tick | -2,685 | -1.35% |
| snake_viper_wild | -2,732 | -1.35% |
| intraweek | -3,129 | -1.45% |

Average per day so far: unified Rs +623, benchmark Rs +597, intraweek Rs +323, intramonth Rs +321, oracle Rs +285, random_hold Rs +249, snake_abs_exit Rs +188, snake_abs_exit_conv Rs +161, snake_abs Rs +114, snake_abs_conv Rs +113, nifty_calls Rs +47, snake_viper_wild Rs +3, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -20, snake_anaconda Rs -67, snake_viper_tick Rs -118, snake_nonews Rs -300, snake Rs -320, gold Rs -778

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.