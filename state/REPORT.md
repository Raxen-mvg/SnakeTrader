# Paper trading report

Updated 2026-11-23 15:30 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,285 | +12.14% | 0 | - | 236 |
| benchmark | 221,473 | +10.74% | 0 | - | 237 |
| intramonth | 212,751 | +6.38% | 0 | - | 235 |
| oracle | 212,342 | +6.17% | 0 | - | 233 |
| intraweek | 211,619 | +5.81% | 40 | 55% | 4,400 |
| random_hold | 208,426 | +4.21% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,495 | +3.75% | 2 | 50% | 345 |
| snake_abs_exit_conv | 207,046 | +3.52% | 2 | 50% | 345 |
| snake_abs | 205,461 | +2.73% | 1 | 100% | 255 |
| snake_abs_conv | 205,303 | +2.65% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,124 | +0.56% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,979 | -0.51% | 0 | - | 237 |
| snake_anaconda | 198,703 | -0.65% | 3 | 33% | 374 |
| snake_viper_tick | 197,693 | -1.15% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,430 | -15.29% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,288 (-4.86%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,381 | +0.82% |
| snake_abs_exit_conv | +429 | +0.21% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -136 | -0.06% |
| snake_abs | -459 | -0.22% |
| snake_abs_conv | -480 | -0.23% |
| snake_abs_exit | -1,067 | -0.51% |
| snake_anaconda | -1,202 | -0.60% |
| snake_viper_tick | -1,679 | -0.84% |
| snake_viper_wild | -1,705 | -0.84% |
| unified | -1,897 | -0.84% |
| benchmark_smallcap | -1,928 | -0.96% |
| intramonth | -2,253 | -1.05% |
| random_hold | -2,333 | -1.11% |
| benchmark | -3,664 | -1.63% |
| intraweek | -4,093 | -1.90% |

Average per day so far: unified Rs +623, benchmark Rs +551, intramonth Rs +327, oracle Rs +316, intraweek Rs +298, random_hold Rs +216, snake_abs_exit Rs +208, snake_abs_exit_conv Rs +196, snake_abs Rs +148, snake_abs_conv Rs +147, nifty_calls Rs +47, snake_viper_wild Rs +36, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -29, snake_anaconda Rs -38, snake_viper_tick Rs -82, snake_nonews Rs -300, snake Rs -320, gold Rs -784

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.