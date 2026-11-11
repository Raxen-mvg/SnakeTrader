# Paper trading report

Updated 2026-11-11 11:55 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,297 | +10.65% | 0 | - | 237 |
| unified | 220,759 | +10.38% | 0 | - | 236 |
| snake_abs_exit_conv | 216,641 | +8.32% | 2 | 50% | 345 |
| snake_abs_exit | 215,327 | +7.66% | 2 | 50% | 345 |
| intraweek | 214,288 | +7.14% | 30 | 53% | 3,302 |
| snake_abs | 213,038 | +6.52% | 1 | 100% | 255 |
| snake_abs_conv | 212,886 | +6.44% | 1 | 100% | 255 |
| oracle | 212,060 | +6.03% | 0 | - | 233 |
| intramonth | 211,845 | +5.92% | 0 | - | 235 |
| random_hold | 206,947 | +3.47% | 9 | 67% | 709 |
| snake_anaconda | 203,248 | +1.62% | 3 | 33% | 374 |
| snake_viper_wild | 202,086 | +1.04% | 10 | 50% | 1,825 |
| benchmark_smallcap | 201,894 | +0.95% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 198,650 | -0.68% | 9 | 44% | 1,639 |
| gold | 189,815 | -5.09% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,473 (-4.26%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,732 | +2.23% |
| snake_viper_wild | +4,656 | +2.36% |
| snake_viper_tick | +4,573 | +2.36% |
| snake_anaconda | +3,782 | +1.90% |
| benchmark_smallcap | +3,722 | +1.88% |
| snake_abs_conv | +3,408 | +1.63% |
| snake_abs | +3,391 | +1.62% |
| snake_abs_exit | +3,343 | +1.58% |
| benchmark | +3,205 | +1.47% |
| oracle | +2,141 | +1.02% |
| random_hold | +1,986 | +0.97% |
| intramonth | +1,236 | +0.59% |
| unified | +1,012 | +0.46% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -254 | -0.12% |
| gold | -2,318 | -1.21% |

Average per day so far: benchmark Rs +687, unified Rs +670, snake_abs_exit_conv Rs +594, snake_abs_exit Rs +547, intraweek Rs +461, snake_abs_conv Rs +460, snake_abs Rs +450, oracle Rs +389, intramonth Rs +382, random_hold Rs +224, snake_anaconda Rs +125, snake_viper_wild Rs +91, benchmark_smallcap Rs +70, nifty_calls Rs +59, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -67, gold Rs -329, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.