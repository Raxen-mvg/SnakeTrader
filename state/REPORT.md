# Paper trading report

Updated 2026-11-13 12:40 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,033 | +10.02% | 0 | - | 236 |
| benchmark | 219,385 | +9.69% | 0 | - | 237 |
| snake_abs_exit_conv | 216,571 | +8.29% | 2 | 50% | 345 |
| snake_abs_exit | 216,454 | +8.23% | 2 | 50% | 345 |
| intraweek | 216,070 | +8.04% | 30 | 53% | 3,302 |
| oracle | 213,221 | +6.61% | 0 | - | 233 |
| snake_abs | 212,759 | +6.38% | 1 | 100% | 255 |
| snake_abs_conv | 212,590 | +6.29% | 1 | 100% | 255 |
| intramonth | 210,649 | +5.33% | 0 | - | 235 |
| random_hold | 207,256 | +3.63% | 10 | 70% | 733 |
| snake_viper_wild | 205,755 | +2.88% | 14 | 50% | 2,496 |
| snake_anaconda | 204,948 | +2.47% | 3 | 33% | 374 |
| benchmark_smallcap | 202,679 | +1.34% | 0 | - | 237 |
| snake_viper_tick | 202,235 | +1.12% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,700 | -8.15% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,815 (-4.09%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,412 | +0.66% |
| snake_viper_wild | +462 | +0.23% |
| snake_viper_tick | +454 | +0.23% |
| oracle | +105 | +0.05% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| benchmark_smallcap | -527 | -0.26% |
| unified | -663 | -0.30% |
| random_hold | -798 | -0.38% |
| intramonth | -944 | -0.45% |
| snake_anaconda | -979 | -0.47% |
| snake_abs_exit | -989 | -0.46% |
| benchmark | -1,163 | -0.53% |
| gold | -1,611 | -0.87% |
| snake_abs_exit_conv | -2,103 | -0.96% |
| snake_abs_conv | -2,945 | -1.37% |
| snake_abs | -2,952 | -1.37% |

Average per day so far: unified Rs +607, benchmark Rs +587, snake_abs_exit_conv Rs +552, snake_abs_exit Rs +548, intraweek Rs +487, snake_abs_conv Rs +420, snake_abs Rs +412, oracle Rs +401, intramonth Rs +323, snake_viper_wild Rs +230, random_hold Rs +220, snake_anaconda Rs +177, snake_viper_tick Rs +102, benchmark_smallcap Rs +92, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -494

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.