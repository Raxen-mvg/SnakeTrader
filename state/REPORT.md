# Paper trading report

Updated 2026-11-19 14:40 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,185 | +12.09% | 0 | - | 236 |
| benchmark | 222,330 | +11.16% | 0 | - | 237 |
| intramonth | 213,733 | +6.87% | 0 | - | 235 |
| snake_abs_exit | 213,553 | +6.78% | 2 | 50% | 345 |
| intraweek | 211,977 | +5.99% | 35 | 54% | 3,851 |
| oracle | 211,715 | +5.86% | 0 | - | 233 |
| snake_abs_exit_conv | 211,258 | +5.63% | 2 | 50% | 345 |
| snake_abs | 209,080 | +4.54% | 1 | 100% | 255 |
| snake_abs_conv | 208,961 | +4.48% | 1 | 100% | 255 |
| random_hold | 208,092 | +4.05% | 10 | 70% | 733 |
| snake_viper_wild | 207,561 | +3.78% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,015 | +2.01% | 15 | 47% | 2,625 |
| snake_anaconda | 203,572 | +1.79% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,896 | +0.45% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,184 | -12.41% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,592 (-4.20%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,035 | +0.92% |
| unified | +1,573 | +0.71% |
| benchmark_smallcap | +1,569 | +0.79% |
| intramonth | +1,460 | +0.69% |
| random_hold | +1,159 | +0.56% |
| oracle | +919 | +0.44% |
| snake_viper_wild | +522 | +0.25% |
| snake_viper_tick | +511 | +0.25% |
| intraweek | +138 | +0.07% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -356 | -0.17% |
| snake_abs_conv | -364 | -0.17% |
| snake_abs_exit | -479 | -0.22% |
| snake_anaconda | -829 | -0.41% |
| snake_abs_exit_conv | -1,125 | -0.53% |
| gold | -2,137 | -1.21% |

Average per day so far: unified Rs +654, benchmark Rs +604, snake_abs_exit Rs +399, intramonth Rs +371, snake_abs_exit_conv Rs +331, intraweek Rs +324, oracle Rs +317, snake_abs_conv Rs +264, snake_viper_wild Rs +261, snake_abs Rs +259, random_hold Rs +219, snake_viper_tick Rs +154, snake_anaconda Rs +112, nifty_calls Rs +50, benchmark_smallcap Rs +27, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -671

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.