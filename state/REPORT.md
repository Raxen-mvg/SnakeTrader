# Paper trading report

Updated 2026-11-25 10:56 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,658 | +12.83% | 0 | - | 237 |
| unified | 225,202 | +12.60% | 0 | - | 236 |
| intramonth | 213,003 | +6.50% | 0 | - | 235 |
| oracle | 212,067 | +6.03% | 0 | - | 233 |
| random_hold | 209,916 | +4.96% | 12 | 75% | 1,009 |
| intraweek | 208,584 | +4.29% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,765 | +0.88% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,350 | +0.68% | 2 | 50% | 345 |
| snake_abs | 200,835 | +0.42% | 1 | 100% | 255 |
| snake_abs_conv | 200,646 | +0.32% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,641 | -0.18% | 0 | - | 237 |
| snake_viper_wild | 195,364 | -2.32% | 16 | 50% | 2,827 |
| snake_anaconda | 193,333 | -3.33% | 3 | 33% | 374 |
| snake_viper_tick | 192,043 | -3.98% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,649 | -17.18% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,383 (-5.31%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,185 | +1.89% |
| random_hold | +1,490 | +0.71% |
| unified | +917 | +0.41% |
| benchmark_smallcap | +661 | +0.33% |
| intramonth | +252 | +0.12% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| oracle | -275 | -0.13% |
| intraweek | -3,035 | -1.43% |
| gold | -3,781 | -2.23% |
| snake_abs | -4,626 | -2.25% |
| snake_abs_conv | -4,657 | -2.27% |
| snake_anaconda | -5,371 | -2.70% |
| snake_viper_tick | -5,650 | -2.86% |
| snake_abs_exit_conv | -5,695 | -2.75% |
| snake_abs_exit | -5,730 | -2.76% |
| snake_viper_wild | -5,760 | -2.86% |

Average per day so far: benchmark Rs +641, unified Rs +630, intramonth Rs +325, oracle Rs +302, random_hold Rs +248, intraweek Rs +215, snake_abs_exit Rs +48, nifty_calls Rs +46, snake_abs_exit_conv Rs +36, snake_abs Rs +22, snake_abs_conv Rs +17, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -10, snake_viper_wild Rs -145, snake_anaconda Rs -190, snake_viper_tick Rs -274, snake_nonews Rs -292, snake Rs -311, gold Rs -859

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.