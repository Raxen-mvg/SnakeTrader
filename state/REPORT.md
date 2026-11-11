# Paper trading report

Updated 2026-11-11 12:22 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,991 | +10.50% | 0 | - | 237 |
| unified | 220,778 | +10.39% | 0 | - | 236 |
| snake_abs_exit_conv | 216,228 | +8.11% | 2 | 50% | 345 |
| snake_abs_exit | 215,059 | +7.53% | 2 | 50% | 345 |
| intraweek | 214,100 | +7.05% | 30 | 53% | 3,302 |
| snake_abs | 212,576 | +6.29% | 1 | 100% | 255 |
| snake_abs_conv | 212,421 | +6.21% | 1 | 100% | 255 |
| oracle | 212,131 | +6.07% | 0 | - | 233 |
| intramonth | 211,793 | +5.90% | 0 | - | 235 |
| random_hold | 207,163 | +3.58% | 9 | 67% | 709 |
| snake_anaconda | 202,849 | +1.43% | 3 | 33% | 374 |
| snake_viper_wild | 202,397 | +1.20% | 10 | 50% | 1,825 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,647 | +0.82% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 198,954 | -0.52% | 9 | 44% | 1,639 |
| gold | 189,898 | -5.05% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,413 (-4.29%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +4,967 | +2.52% |
| snake_viper_tick | +4,878 | +2.51% |
| snake_abs_exit_conv | +4,320 | +2.04% |
| benchmark_smallcap | +3,475 | +1.75% |
| snake_anaconda | +3,383 | +1.70% |
| snake_abs_exit | +3,075 | +1.45% |
| snake_abs_conv | +2,943 | +1.41% |
| snake_abs | +2,930 | +1.40% |
| benchmark | +2,899 | +1.33% |
| oracle | +2,212 | +1.05% |
| random_hold | +2,202 | +1.07% |
| intramonth | +1,184 | +0.56% |
| unified | +1,031 | +0.47% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -442 | -0.21% |
| gold | -2,236 | -1.16% |

Average per day so far: benchmark Rs +677, unified Rs +670, snake_abs_exit_conv Rs +580, snake_abs_exit Rs +538, intraweek Rs +455, snake_abs_conv Rs +444, snake_abs Rs +434, oracle Rs +391, intramonth Rs +380, random_hold Rs +231, snake_anaconda Rs +110, snake_viper_wild Rs +104, benchmark_smallcap Rs +61, nifty_calls Rs +59, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -52, gold Rs -326, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.