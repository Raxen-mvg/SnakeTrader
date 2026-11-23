# Paper trading report

Updated 2026-11-23 13:01 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,938 | +11.97% | 0 | - | 236 |
| benchmark | 222,498 | +11.25% | 0 | - | 237 |
| intraweek | 212,481 | +6.24% | 40 | 55% | 4,400 |
| intramonth | 211,983 | +5.99% | 0 | - | 235 |
| oracle | 211,711 | +5.86% | 0 | - | 233 |
| random_hold | 209,102 | +4.55% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,869 | +3.43% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,571 | +2.79% | 2 | 50% | 345 |
| snake_abs | 204,429 | +2.21% | 1 | 100% | 255 |
| snake_abs_conv | 204,268 | +2.13% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,966 | +0.48% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,349 | -0.33% | 0 | - | 237 |
| snake_anaconda | 198,062 | -0.97% | 3 | 33% | 374 |
| snake_viper_tick | 197,538 | -1.23% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,334 | -14.83% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,126 (-4.94%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,285 | +1.36% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -768 | -0.36% |
| snake_abs_exit_conv | -1,045 | -0.51% |
| snake_abs | -1,491 | -0.72% |
| snake_abs_conv | -1,515 | -0.74% |
| benchmark_smallcap | -1,558 | -0.78% |
| random_hold | -1,657 | -0.79% |
| snake_abs_exit | -1,693 | -0.81% |
| snake_viper_tick | -1,834 | -0.92% |
| snake_anaconda | -1,843 | -0.92% |
| snake_viper_wild | -1,863 | -0.92% |
| unified | -2,244 | -0.99% |
| benchmark | -2,639 | -1.17% |
| intramonth | -3,021 | -1.41% |
| intraweek | -3,231 | -1.50% |

Average per day so far: unified Rs +614, benchmark Rs +577, intraweek Rs +320, intramonth Rs +307, oracle Rs +300, random_hold Rs +233, snake_abs_exit Rs +191, snake_abs_exit_conv Rs +155, snake_abs Rs +120, snake_abs_conv Rs +119, nifty_calls Rs +47, snake_viper_wild Rs +31, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -19, snake_anaconda Rs -57, snake_viper_tick Rs -88, snake_nonews Rs -300, snake Rs -320, gold Rs -761

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.