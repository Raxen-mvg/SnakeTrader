# Paper trading report

Updated 2026-11-19 11:36 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,742 | +11.87% | 0 | - | 236 |
| benchmark | 221,106 | +10.55% | 0 | - | 237 |
| snake_abs_exit | 213,492 | +6.75% | 2 | 50% | 345 |
| intramonth | 213,250 | +6.62% | 0 | - | 235 |
| intraweek | 211,805 | +5.90% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,620 | +5.81% | 2 | 50% | 345 |
| oracle | 211,105 | +5.55% | 0 | - | 233 |
| snake_abs | 209,027 | +4.51% | 1 | 100% | 255 |
| snake_abs_conv | 208,905 | +4.45% | 1 | 100% | 255 |
| random_hold | 207,696 | +3.85% | 10 | 70% | 733 |
| snake_viper_wild | 207,427 | +3.71% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,883 | +1.94% | 15 | 47% | 2,625 |
| snake_anaconda | 203,279 | +1.64% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,448 | +0.22% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,184 | -12.41% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,207 (-4.40%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,131 | +0.51% |
| benchmark_smallcap | +1,121 | +0.56% |
| intramonth | +977 | +0.46% |
| benchmark | +811 | +0.37% |
| random_hold | +764 | +0.37% |
| snake_viper_wild | +387 | +0.19% |
| snake_viper_tick | +380 | +0.19% |
| oracle | +309 | +0.15% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -34 | -0.02% |
| snake_abs | -410 | -0.20% |
| snake_abs_conv | -420 | -0.20% |
| snake_abs_exit | -539 | -0.25% |
| snake_abs_exit_conv | -763 | -0.36% |
| snake_anaconda | -1,123 | -0.55% |
| gold | -2,137 | -1.21% |

Average per day so far: unified Rs +642, benchmark Rs +570, snake_abs_exit Rs +397, intramonth Rs +358, snake_abs_exit_conv Rs +342, intraweek Rs +319, oracle Rs +300, snake_abs_conv Rs +262, snake_abs Rs +258, snake_viper_wild Rs +256, random_hold Rs +208, snake_viper_tick Rs +149, snake_anaconda Rs +102, nifty_calls Rs +50, benchmark_smallcap Rs +14, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -671

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.