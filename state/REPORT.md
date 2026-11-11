# Paper trading report

Updated 2026-11-11 11:49 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,420 | +10.71% | 0 | - | 237 |
| unified | 220,681 | +10.34% | 0 | - | 236 |
| snake_abs_exit_conv | 216,590 | +8.29% | 2 | 50% | 345 |
| snake_abs_exit | 215,239 | +7.62% | 2 | 50% | 345 |
| intraweek | 214,349 | +7.17% | 30 | 53% | 3,302 |
| snake_abs | 212,982 | +6.49% | 1 | 100% | 255 |
| snake_abs_conv | 212,830 | +6.42% | 1 | 100% | 255 |
| oracle | 212,172 | +6.09% | 0 | - | 233 |
| intramonth | 211,803 | +5.90% | 0 | - | 235 |
| random_hold | 206,938 | +3.47% | 9 | 67% | 709 |
| snake_anaconda | 203,224 | +1.61% | 3 | 33% | 374 |
| benchmark_smallcap | 201,905 | +0.95% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,771 | +0.89% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 198,341 | -0.83% | 9 | 44% | 1,639 |
| gold | 189,914 | -5.04% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,473 (-4.26%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,681 | +2.21% |
| snake_viper_wild | +4,341 | +2.20% |
| snake_viper_tick | +4,264 | +2.20% |
| snake_anaconda | +3,758 | +1.88% |
| benchmark_smallcap | +3,733 | +1.88% |
| snake_abs_conv | +3,352 | +1.60% |
| snake_abs | +3,336 | +1.59% |
| benchmark | +3,328 | +1.53% |
| snake_abs_exit | +3,255 | +1.54% |
| oracle | +2,254 | +1.07% |
| random_hold | +1,977 | +0.96% |
| intramonth | +1,193 | +0.57% |
| unified | +934 | +0.42% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -193 | -0.09% |
| gold | -2,219 | -1.16% |

Average per day so far: benchmark Rs +691, unified Rs +667, snake_abs_exit_conv Rs +592, snake_abs_exit Rs +544, intraweek Rs +463, snake_abs_conv Rs +458, snake_abs Rs +448, oracle Rs +393, intramonth Rs +381, random_hold Rs +224, snake_anaconda Rs +124, snake_viper_wild Rs +77, benchmark_smallcap Rs +71, nifty_calls Rs +59, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -83, gold Rs -325, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.