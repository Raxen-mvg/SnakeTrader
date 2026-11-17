# Paper trading report

Updated 2026-11-17 12:56 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 222,093 | +11.05% | 0 | - | 237 |
| unified | 221,733 | +10.87% | 0 | - | 236 |
| snake_abs_exit | 214,138 | +7.07% | 2 | 50% | 345 |
| intraweek | 214,074 | +7.04% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 212,427 | +6.21% | 2 | 50% | 345 |
| oracle | 212,365 | +6.18% | 0 | - | 233 |
| intramonth | 211,627 | +5.81% | 0 | - | 235 |
| snake_abs | 209,298 | +4.65% | 1 | 100% | 255 |
| snake_abs_conv | 209,149 | +4.58% | 1 | 100% | 255 |
| snake_viper_wild | 207,667 | +3.83% | 14 | 50% | 2,496 |
| random_hold | 207,627 | +3.81% | 10 | 70% | 733 |
| snake_anaconda | 204,846 | +2.42% | 3 | 33% | 374 |
| snake_viper_tick | 204,116 | +2.06% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,502 | +0.75% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,382 | -9.31% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,294 (-4.35%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,808 | +1.33% |
| benchmark | +2,012 | +0.91% |
| snake_viper_wild | +1,522 | +0.74% |
| snake_viper_tick | +1,497 | +0.74% |
| benchmark_smallcap | +673 | +0.34% |
| gold | +427 | +0.24% |
| oracle | +342 | +0.16% |
| unified | +295 | +0.13% |
| intramonth | +8 | +0.00% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| random_hold | -166 | -0.08% |
| snake_anaconda | -257 | -0.12% |
| snake_abs_exit | -272 | -0.13% |
| snake_abs_exit_conv | -790 | -0.37% |
| snake_abs | -836 | -0.40% |
| snake_abs_conv | -840 | -0.40% |

Average per day so far: benchmark Rs +631, unified Rs +621, snake_abs_exit Rs +442, intraweek Rs +402, snake_abs_exit_conv Rs +388, oracle Rs +353, intramonth Rs +332, snake_abs_conv Rs +286, snake_viper_wild Rs +284, snake_abs Rs +282, random_hold Rs +218, snake_viper_tick Rs +172, snake_anaconda Rs +162, nifty_calls Rs +52, benchmark_smallcap Rs +48, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -532

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.