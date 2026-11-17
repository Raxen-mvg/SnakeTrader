# Paper trading report

Updated 2026-11-17 14:21 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,963 | +10.98% | 0 | - | 237 |
| unified | 221,733 | +10.87% | 0 | - | 236 |
| snake_abs_exit | 213,929 | +6.96% | 2 | 50% | 345 |
| intraweek | 213,670 | +6.83% | 35 | 54% | 3,851 |
| oracle | 212,451 | +6.22% | 0 | - | 233 |
| snake_abs_exit_conv | 212,396 | +6.20% | 2 | 50% | 345 |
| intramonth | 211,631 | +5.82% | 0 | - | 235 |
| snake_viper_wild | 210,080 | +5.04% | 14 | 50% | 2,496 |
| snake_abs | 209,139 | +4.57% | 1 | 100% | 255 |
| snake_abs_conv | 209,008 | +4.50% | 1 | 100% | 255 |
| random_hold | 207,797 | +3.90% | 10 | 70% | 733 |
| snake_viper_tick | 206,491 | +3.25% | 13 | 46% | 2,299 |
| snake_anaconda | 204,624 | +2.31% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,233 | +0.62% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,905 | -9.55% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,258 (-4.37%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,935 | +1.91% |
| snake_viper_tick | +3,871 | +1.91% |
| intraweek | +2,404 | +1.14% |
| benchmark | +1,882 | +0.85% |
| oracle | +428 | +0.20% |
| benchmark_smallcap | +404 | +0.20% |
| unified | +295 | +0.13% |
| intramonth | +12 | +0.01% |
| random_hold | +4 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold | -49 | -0.03% |
| snake_anaconda | -479 | -0.23% |
| snake_abs_exit | -480 | -0.22% |
| snake_abs_exit_conv | -822 | -0.39% |
| snake_abs_conv | -982 | -0.47% |
| snake_abs | -995 | -0.47% |

Average per day so far: benchmark Rs +628, unified Rs +621, snake_abs_exit Rs +435, intraweek Rs +391, snake_abs_exit_conv Rs +387, snake_viper_wild Rs +373, oracle Rs +356, intramonth Rs +332, snake_abs_conv Rs +281, snake_abs Rs +277, snake_viper_tick Rs +270, random_hold Rs +223, snake_anaconda Rs +154, nifty_calls Rs +52, benchmark_smallcap Rs +40, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -546

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.