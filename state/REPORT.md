# Paper trading report

Updated 2026-11-12 14:43 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,729 | +10.37% | 0 | - | 236 |
| benchmark | 220,303 | +10.15% | 0 | - | 237 |
| snake_abs_exit_conv | 218,783 | +9.39% | 2 | 50% | 345 |
| snake_abs_exit | 217,690 | +8.85% | 2 | 50% | 345 |
| snake_abs | 215,698 | +7.85% | 1 | 100% | 255 |
| snake_abs_conv | 215,528 | +7.76% | 1 | 100% | 255 |
| intraweek | 214,439 | +7.22% | 30 | 53% | 3,302 |
| oracle | 212,728 | +6.36% | 0 | - | 233 |
| intramonth | 211,432 | +5.72% | 0 | - | 235 |
| random_hold | 207,834 | +3.92% | 10 | 70% | 733 |
| snake_anaconda | 206,457 | +3.23% | 3 | 33% | 374 |
| snake_viper_wild | 205,785 | +2.89% | 13 | 54% | 2,247 |
| benchmark_smallcap | 202,780 | +1.39% | 0 | - | 237 |
| snake_viper_tick | 202,267 | +1.13% | 12 | 50% | 2,054 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,916 | -7.54% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,864 (-4.07%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +2,334 | +1.14% |
| snake_abs | +2,073 | +0.97% |
| snake_abs_conv | +2,070 | +0.97% |
| benchmark_smallcap | +1,973 | +0.98% |
| snake_abs_exit_conv | +1,631 | +0.75% |
| snake_abs_exit | +1,528 | +0.71% |
| intraweek | +1,306 | +0.61% |
| benchmark | +1,040 | +0.47% |
| unified | +915 | +0.42% |
| oracle | +725 | +0.34% |
| random_hold | +724 | +0.35% |
| intramonth | +436 | +0.21% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -942 | -0.46% |
| snake_viper_wild | -957 | -0.46% |
| gold | -4,669 | -2.46% |

Average per day so far: unified Rs +648, snake_abs_exit_conv Rs +648, benchmark Rs +634, snake_abs_exit Rs +610, snake_abs_conv Rs +535, snake_abs Rs +523, intraweek Rs +451, oracle Rs +398, intramonth Rs +357, random_hold Rs +245, snake_viper_wild Rs +241, snake_anaconda Rs +239, snake_viper_tick Rs +108, benchmark_smallcap Rs +99, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -471

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.