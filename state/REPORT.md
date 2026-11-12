# Paper trading report

Updated 2026-11-12 15:07 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,456 | +10.23% | 0 | - | 237 |
| unified | 220,436 | +10.22% | 0 | - | 236 |
| snake_abs_exit_conv | 218,937 | +9.47% | 2 | 50% | 345 |
| snake_abs_exit | 217,713 | +8.86% | 2 | 50% | 345 |
| snake_abs | 216,011 | +8.01% | 1 | 100% | 255 |
| snake_abs_conv | 215,841 | +7.92% | 1 | 100% | 255 |
| intraweek | 214,496 | +7.25% | 30 | 53% | 3,302 |
| oracle | 212,823 | +6.41% | 0 | - | 233 |
| intramonth | 211,418 | +5.71% | 0 | - | 235 |
| random_hold | 207,804 | +3.90% | 10 | 70% | 733 |
| snake_anaconda | 205,810 | +2.90% | 3 | 33% | 374 |
| snake_viper_wild | 205,724 | +2.86% | 13 | 54% | 2,247 |
| benchmark_smallcap | 202,993 | +1.50% | 0 | - | 237 |
| snake_viper_tick | 202,207 | +1.10% | 12 | 50% | 2,054 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 185,229 | -7.39% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,879 (-4.06%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs | +2,386 | +1.12% |
| snake_abs_conv | +2,383 | +1.12% |
| benchmark_smallcap | +2,186 | +1.09% |
| snake_abs_exit_conv | +1,786 | +0.82% |
| snake_anaconda | +1,687 | +0.83% |
| snake_abs_exit | +1,551 | +0.72% |
| intraweek | +1,363 | +0.64% |
| benchmark | +1,193 | +0.54% |
| oracle | +820 | +0.39% |
| random_hold | +693 | +0.34% |
| unified | +622 | +0.28% |
| intramonth | +421 | +0.20% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -1,002 | -0.49% |
| snake_viper_wild | -1,018 | -0.49% |
| gold | -4,357 | -2.30% |

Average per day so far: snake_abs_exit_conv Rs +653, benchmark Rs +639, unified Rs +639, snake_abs_exit Rs +611, snake_abs_conv Rs +546, snake_abs Rs +534, intraweek Rs +453, oracle Rs +401, intramonth Rs +357, random_hold Rs +244, snake_viper_wild Rs +239, snake_anaconda Rs +215, benchmark_smallcap Rs +107, snake_viper_tick Rs +105, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -462

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.