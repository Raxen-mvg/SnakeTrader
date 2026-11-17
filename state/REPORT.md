# Paper trading report

Updated 2026-11-17 12:39 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 222,101 | +11.05% | 0 | - | 237 |
| unified | 221,733 | +10.87% | 0 | - | 236 |
| snake_abs_exit | 214,150 | +7.08% | 2 | 50% | 345 |
| intraweek | 213,172 | +6.59% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 212,433 | +6.22% | 2 | 50% | 345 |
| oracle | 212,193 | +6.10% | 0 | - | 233 |
| intramonth | 211,585 | +5.79% | 0 | - | 235 |
| snake_abs | 209,352 | +4.68% | 1 | 100% | 255 |
| snake_abs_conv | 209,203 | +4.60% | 1 | 100% | 255 |
| random_hold | 207,530 | +3.77% | 10 | 70% | 733 |
| snake_viper_wild | 207,493 | +3.75% | 14 | 50% | 2,496 |
| snake_anaconda | 204,874 | +2.44% | 3 | 33% | 374 |
| snake_viper_tick | 203,946 | +1.97% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,401 | +0.70% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,349 | -9.33% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,102 (-4.45%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,020 | +0.92% |
| intraweek | +1,906 | +0.90% |
| snake_viper_wild | +1,348 | +0.65% |
| snake_viper_tick | +1,326 | +0.65% |
| benchmark_smallcap | +572 | +0.28% |
| gold | +395 | +0.22% |
| unified | +296 | +0.13% |
| oracle | +170 | +0.08% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -33 | -0.02% |
| snake_anaconda | -229 | -0.11% |
| snake_abs_exit | -260 | -0.12% |
| random_hold | -264 | -0.13% |
| snake_abs | -782 | -0.37% |
| snake_abs_exit_conv | -784 | -0.37% |
| snake_abs_conv | -787 | -0.38% |

Average per day so far: benchmark Rs +631, unified Rs +621, snake_abs_exit Rs +442, snake_abs_exit_conv Rs +389, intraweek Rs +376, oracle Rs +348, intramonth Rs +331, snake_abs_conv Rs +288, snake_abs Rs +283, snake_viper_wild Rs +278, random_hold Rs +215, snake_viper_tick Rs +164, snake_anaconda Rs +162, nifty_calls Rs +52, benchmark_smallcap Rs +45, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -533

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.