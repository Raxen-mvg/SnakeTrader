# Paper trading report

Updated 2026-11-17 12:36 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 222,139 | +11.07% | 0 | - | 237 |
| unified | 221,743 | +10.87% | 0 | - | 236 |
| snake_abs_exit | 214,120 | +7.06% | 2 | 50% | 345 |
| intraweek | 212,915 | +6.46% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 212,376 | +6.19% | 2 | 50% | 345 |
| oracle | 212,284 | +6.14% | 0 | - | 233 |
| intramonth | 211,622 | +5.81% | 0 | - | 235 |
| snake_abs | 209,282 | +4.64% | 1 | 100% | 255 |
| snake_abs_conv | 209,133 | +4.57% | 1 | 100% | 255 |
| snake_viper_wild | 207,551 | +3.77% | 14 | 50% | 2,496 |
| random_hold | 207,545 | +3.77% | 10 | 70% | 733 |
| snake_anaconda | 204,838 | +2.42% | 3 | 33% | 374 |
| snake_viper_tick | 204,002 | +2.00% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,468 | +0.73% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,382 | -9.31% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,097 (-4.45%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,058 | +0.94% |
| intraweek | +1,649 | +0.78% |
| snake_viper_wild | +1,406 | +0.68% |
| snake_viper_tick | +1,383 | +0.68% |
| benchmark_smallcap | +639 | +0.32% |
| gold | +427 | +0.24% |
| unified | +305 | +0.14% |
| oracle | +261 | +0.12% |
| intramonth | +4 | +0.00% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| random_hold | -248 | -0.12% |
| snake_anaconda | -265 | -0.13% |
| snake_abs_exit | -289 | -0.14% |
| snake_abs_exit_conv | -842 | -0.40% |
| snake_abs | -852 | -0.41% |
| snake_abs_conv | -857 | -0.41% |

Average per day so far: benchmark Rs +633, unified Rs +621, snake_abs_exit Rs +441, snake_abs_exit_conv Rs +387, intraweek Rs +369, oracle Rs +351, intramonth Rs +332, snake_abs_conv Rs +285, snake_abs Rs +281, snake_viper_wild Rs +280, random_hold Rs +216, snake_viper_tick Rs +167, snake_anaconda Rs +161, nifty_calls Rs +52, benchmark_smallcap Rs +47, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -532

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.