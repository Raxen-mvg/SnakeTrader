# Paper trading report

Updated 2026-11-11 12:07 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,282 | +10.64% | 0 | - | 237 |
| unified | 220,493 | +10.25% | 0 | - | 236 |
| snake_abs_exit_conv | 216,434 | +8.22% | 2 | 50% | 345 |
| snake_abs_exit | 215,025 | +7.51% | 2 | 50% | 345 |
| intraweek | 214,260 | +7.13% | 30 | 53% | 3,302 |
| snake_abs | 212,841 | +6.42% | 1 | 100% | 255 |
| snake_abs_conv | 212,686 | +6.34% | 1 | 100% | 255 |
| oracle | 211,912 | +5.96% | 0 | - | 233 |
| intramonth | 211,412 | +5.71% | 0 | - | 235 |
| random_hold | 207,007 | +3.50% | 9 | 67% | 709 |
| snake_anaconda | 203,069 | +1.53% | 3 | 33% | 374 |
| benchmark_smallcap | 201,905 | +0.95% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,778 | +0.89% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 198,347 | -0.83% | 9 | 44% | 1,639 |
| gold | 189,815 | -5.09% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,315 (-4.34%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,525 | +2.13% |
| snake_viper_wild | +4,348 | +2.20% |
| snake_viper_tick | +4,271 | +2.20% |
| benchmark_smallcap | +3,733 | +1.88% |
| snake_anaconda | +3,602 | +1.81% |
| snake_abs_conv | +3,208 | +1.53% |
| snake_abs | +3,195 | +1.52% |
| benchmark | +3,190 | +1.46% |
| snake_abs_exit | +3,041 | +1.44% |
| random_hold | +2,046 | +1.00% |
| oracle | +1,994 | +0.95% |
| intramonth | +802 | +0.38% |
| unified | +746 | +0.34% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -282 | -0.13% |
| gold | -2,318 | -1.21% |

Average per day so far: benchmark Rs +687, unified Rs +661, snake_abs_exit_conv Rs +587, snake_abs_exit Rs +537, intraweek Rs +460, snake_abs_conv Rs +453, snake_abs Rs +443, oracle Rs +384, intramonth Rs +368, random_hold Rs +226, snake_anaconda Rs +118, snake_viper_wild Rs +77, benchmark_smallcap Rs +71, nifty_calls Rs +59, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -83, gold Rs -329, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.