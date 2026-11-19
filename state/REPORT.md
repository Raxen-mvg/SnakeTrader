# Paper trading report

Updated 2026-11-19 12:29 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,897 | +11.95% | 0 | - | 236 |
| benchmark | 221,473 | +10.74% | 0 | - | 237 |
| intramonth | 213,562 | +6.78% | 0 | - | 235 |
| snake_abs_exit | 212,767 | +6.38% | 2 | 50% | 345 |
| intraweek | 211,600 | +5.80% | 35 | 54% | 3,851 |
| oracle | 211,060 | +5.53% | 0 | - | 233 |
| snake_abs_exit_conv | 210,831 | +5.42% | 2 | 50% | 345 |
| snake_abs | 208,515 | +4.26% | 1 | 100% | 255 |
| snake_abs_conv | 208,383 | +4.19% | 1 | 100% | 255 |
| random_hold | 207,616 | +3.81% | 10 | 70% | 733 |
| snake_viper_wild | 207,460 | +3.73% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,916 | +1.96% | 15 | 47% | 2,625 |
| snake_anaconda | 202,785 | +1.39% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,638 | +0.32% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,904 | -12.55% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,241 (-4.38%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,312 | +0.66% |
| intramonth | +1,288 | +0.61% |
| unified | +1,286 | +0.58% |
| benchmark | +1,178 | +0.54% |
| random_hold | +683 | +0.33% |
| snake_viper_wild | +421 | +0.20% |
| snake_viper_tick | +413 | +0.20% |
| oracle | +264 | +0.12% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -239 | -0.11% |
| snake_abs | -922 | -0.44% |
| snake_abs_conv | -942 | -0.45% |
| snake_abs_exit | -1,264 | -0.59% |
| snake_abs_exit_conv | -1,552 | -0.73% |
| snake_anaconda | -1,616 | -0.79% |
| gold | -2,417 | -1.36% |

Average per day so far: unified Rs +646, benchmark Rs +580, snake_abs_exit Rs +376, intramonth Rs +367, snake_abs_exit_conv Rs +319, intraweek Rs +314, oracle Rs +299, snake_viper_wild Rs +257, snake_abs_conv Rs +247, snake_abs Rs +243, random_hold Rs +206, snake_viper_tick Rs +151, snake_anaconda Rs +87, nifty_calls Rs +50, benchmark_smallcap Rs +19, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -678

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.