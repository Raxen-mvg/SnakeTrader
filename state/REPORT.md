# Paper trading report

Updated 2026-11-11 12:01 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,374 | +10.69% | 0 | - | 237 |
| unified | 220,497 | +10.25% | 0 | - | 236 |
| snake_abs_exit_conv | 216,817 | +8.41% | 2 | 50% | 345 |
| snake_abs_exit | 215,388 | +7.69% | 2 | 50% | 345 |
| intraweek | 214,343 | +7.17% | 30 | 53% | 3,302 |
| snake_abs | 213,212 | +6.61% | 1 | 100% | 255 |
| snake_abs_conv | 213,062 | +6.53% | 1 | 100% | 255 |
| oracle | 211,995 | +6.00% | 0 | - | 233 |
| intramonth | 211,546 | +5.77% | 0 | - | 235 |
| random_hold | 206,880 | +3.44% | 9 | 67% | 709 |
| snake_anaconda | 203,418 | +1.71% | 3 | 33% | 374 |
| benchmark_smallcap | 201,905 | +0.95% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,780 | +0.89% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 198,349 | -0.82% | 9 | 44% | 1,639 |
| gold | 189,799 | -5.10% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,394 (-4.30%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,908 | +2.32% |
| snake_viper_wild | +4,350 | +2.20% |
| snake_viper_tick | +4,273 | +2.20% |
| snake_anaconda | +3,951 | +1.98% |
| benchmark_smallcap | +3,733 | +1.88% |
| snake_abs_conv | +3,584 | +1.71% |
| snake_abs | +3,565 | +1.70% |
| snake_abs_exit | +3,404 | +1.61% |
| benchmark | +3,282 | +1.50% |
| oracle | +2,076 | +0.99% |
| random_hold | +1,920 | +0.94% |
| intramonth | +937 | +0.45% |
| unified | +750 | +0.34% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -199 | -0.09% |
| gold | -2,334 | -1.22% |

Average per day so far: benchmark Rs +689, unified Rs +661, snake_abs_exit_conv Rs +601, snake_abs_exit Rs +550, snake_abs_conv Rs +466, intraweek Rs +463, snake_abs Rs +456, oracle Rs +387, intramonth Rs +372, random_hold Rs +222, snake_anaconda Rs +131, snake_viper_wild Rs +77, benchmark_smallcap Rs +71, nifty_calls Rs +59, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -83, gold Rs -329, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.