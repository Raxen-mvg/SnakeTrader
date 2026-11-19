# Paper trading report

Updated 2026-11-19 14:25 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,435 | +11.72% | 0 | - | 236 |
| benchmark | 222,322 | +11.16% | 0 | - | 237 |
| snake_abs_exit | 213,414 | +6.71% | 2 | 50% | 345 |
| intramonth | 213,075 | +6.54% | 0 | - | 235 |
| intraweek | 211,781 | +5.89% | 35 | 54% | 3,851 |
| oracle | 211,272 | +5.64% | 0 | - | 233 |
| snake_abs_exit_conv | 211,146 | +5.57% | 2 | 50% | 345 |
| snake_abs | 209,018 | +4.51% | 1 | 100% | 255 |
| snake_abs_conv | 208,898 | +4.45% | 1 | 100% | 255 |
| random_hold | 207,929 | +3.96% | 10 | 70% | 733 |
| snake_viper_wild | 207,595 | +3.80% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,047 | +2.02% | 15 | 47% | 2,625 |
| snake_anaconda | 203,522 | +1.76% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,784 | +0.39% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,003 | -12.50% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,177 (-4.41%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,027 | +0.92% |
| benchmark_smallcap | +1,457 | +0.73% |
| random_hold | +997 | +0.48% |
| unified | +824 | +0.37% |
| intramonth | +802 | +0.38% |
| snake_viper_wild | +555 | +0.27% |
| snake_viper_tick | +544 | +0.27% |
| oracle | +476 | +0.23% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -59 | -0.03% |
| snake_abs | -418 | -0.20% |
| snake_abs_conv | -427 | -0.20% |
| snake_abs_exit | -618 | -0.29% |
| snake_anaconda | -879 | -0.43% |
| snake_abs_exit_conv | -1,237 | -0.58% |
| gold | -2,318 | -1.31% |

Average per day so far: unified Rs +633, benchmark Rs +603, snake_abs_exit Rs +395, intramonth Rs +353, snake_abs_exit_conv Rs +328, intraweek Rs +318, oracle Rs +305, snake_viper_wild Rs +262, snake_abs_conv Rs +262, snake_abs Rs +258, random_hold Rs +214, snake_viper_tick Rs +156, snake_anaconda Rs +110, nifty_calls Rs +50, benchmark_smallcap Rs +24, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -676

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.