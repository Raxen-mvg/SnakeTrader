# Paper trading report

Updated 2026-11-13 09:40 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,650 | +10.32% | 0 | - | 236 |
| benchmark | 219,706 | +9.85% | 0 | - | 237 |
| snake_abs_exit_conv | 217,288 | +8.64% | 2 | 50% | 345 |
| snake_abs_exit | 216,786 | +8.39% | 2 | 50% | 345 |
| intraweek | 215,224 | +7.61% | 30 | 53% | 3,302 |
| snake_abs | 214,356 | +7.18% | 1 | 100% | 255 |
| snake_abs_conv | 214,180 | +7.09% | 1 | 100% | 255 |
| oracle | 213,570 | +6.79% | 0 | - | 233 |
| intramonth | 211,795 | +5.90% | 0 | - | 235 |
| random_hold | 207,840 | +3.92% | 10 | 70% | 733 |
| snake_viper_wild | 205,933 | +2.97% | 14 | 50% | 2,496 |
| snake_anaconda | 203,925 | +1.96% | 3 | 33% | 374 |
| benchmark_smallcap | 203,194 | +1.60% | 0 | - | 237 |
| snake_viper_tick | 202,413 | +1.21% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,588 | -7.71% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,073 (-3.96%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +640 | +0.31% |
| snake_viper_tick | +631 | +0.31% |
| intraweek | +566 | +0.26% |
| oracle | +454 | +0.21% |
| intramonth | +202 | +0.10% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| benchmark_smallcap | -11 | -0.01% |
| unified | -46 | -0.02% |
| random_hold | -214 | -0.10% |
| snake_abs_exit | -656 | -0.30% |
| gold | -723 | -0.39% |
| benchmark | -842 | -0.38% |
| snake_abs_conv | -1,355 | -0.63% |
| snake_abs | -1,356 | -0.63% |
| snake_abs_exit_conv | -1,386 | -0.63% |
| snake_anaconda | -2,002 | -0.97% |

Average per day so far: unified Rs +626, benchmark Rs +597, snake_abs_exit_conv Rs +576, snake_abs_exit Rs +560, snake_abs_conv Rs +473, snake_abs Rs +463, intraweek Rs +461, oracle Rs +411, intramonth Rs +357, random_hold Rs +238, snake_viper_wild Rs +237, snake_anaconda Rs +140, benchmark_smallcap Rs +110, snake_viper_tick Rs +110, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.