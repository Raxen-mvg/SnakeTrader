# Paper trading report

Updated 2026-11-19 11:39 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,688 | +11.84% | 0 | - | 236 |
| benchmark | 221,052 | +10.53% | 0 | - | 237 |
| snake_abs_exit | 213,498 | +6.75% | 2 | 50% | 345 |
| intramonth | 213,196 | +6.60% | 0 | - | 235 |
| intraweek | 211,917 | +5.96% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,642 | +5.82% | 2 | 50% | 345 |
| oracle | 211,127 | +5.56% | 0 | - | 233 |
| snake_abs | 209,034 | +4.52% | 1 | 100% | 255 |
| snake_abs_conv | 208,913 | +4.46% | 1 | 100% | 255 |
| random_hold | 207,650 | +3.83% | 10 | 70% | 733 |
| snake_viper_wild | 207,427 | +3.71% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,883 | +1.94% | 15 | 47% | 2,625 |
| snake_anaconda | 203,301 | +1.65% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,493 | +0.25% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,069 | -12.47% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,205 (-4.40%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,166 | +0.58% |
| unified | +1,076 | +0.48% |
| intramonth | +923 | +0.43% |
| benchmark | +757 | +0.34% |
| random_hold | +717 | +0.35% |
| snake_viper_wild | +387 | +0.19% |
| snake_viper_tick | +380 | +0.19% |
| oracle | +331 | +0.16% |
| intraweek | +77 | +0.04% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -403 | -0.19% |
| snake_abs_conv | -412 | -0.20% |
| snake_abs_exit | -534 | -0.25% |
| snake_abs_exit_conv | -742 | -0.35% |
| snake_anaconda | -1,100 | -0.54% |
| gold | -2,252 | -1.27% |

Average per day so far: unified Rs +640, benchmark Rs +569, snake_abs_exit Rs +397, intramonth Rs +357, snake_abs_exit_conv Rs +342, intraweek Rs +322, oracle Rs +301, snake_abs_conv Rs +262, snake_abs Rs +258, snake_viper_wild Rs +256, random_hold Rs +207, snake_viper_tick Rs +149, snake_anaconda Rs +103, nifty_calls Rs +50, benchmark_smallcap Rs +15, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -674

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.