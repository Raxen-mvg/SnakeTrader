# Paper trading report

Updated 2026-11-13 14:16 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,434 | +10.22% | 0 | - | 236 |
| benchmark | 218,956 | +9.48% | 0 | - | 237 |
| snake_abs_exit | 216,397 | +8.20% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,237 | +8.12% | 2 | 50% | 345 |
| intraweek | 215,437 | +7.72% | 30 | 53% | 3,302 |
| oracle | 213,068 | +6.53% | 0 | - | 233 |
| snake_abs | 212,337 | +6.17% | 1 | 100% | 255 |
| snake_abs_conv | 212,171 | +6.09% | 1 | 100% | 255 |
| intramonth | 210,977 | +5.49% | 0 | - | 235 |
| random_hold | 207,009 | +3.50% | 10 | 70% | 733 |
| snake_viper_wild | 205,570 | +2.79% | 14 | 50% | 2,496 |
| snake_anaconda | 204,559 | +2.28% | 3 | 33% | 374 |
| benchmark_smallcap | 202,309 | +1.15% | 0 | - | 237 |
| snake_viper_tick | 202,055 | +1.03% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,864 | -8.07% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,691 (-4.15%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +779 | +0.36% |
| snake_viper_wild | +277 | +0.14% |
| snake_viper_tick | +273 | +0.14% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -47 | -0.02% |
| unified | -263 | -0.12% |
| intramonth | -616 | -0.29% |
| benchmark_smallcap | -897 | -0.44% |
| random_hold | -1,044 | -0.50% |
| snake_abs_exit | -1,046 | -0.48% |
| snake_anaconda | -1,369 | -0.67% |
| gold | -1,447 | -0.78% |
| benchmark | -1,591 | -0.72% |
| snake_abs_exit_conv | -2,437 | -1.11% |
| snake_abs_conv | -3,364 | -1.56% |
| snake_abs | -3,374 | -1.56% |

Average per day so far: unified Rs +619, benchmark Rs +574, snake_abs_exit Rs +547, snake_abs_exit_conv Rs +541, intraweek Rs +468, snake_abs_conv Rs +406, snake_abs Rs +398, oracle Rs +396, intramonth Rs +333, snake_viper_wild Rs +223, random_hold Rs +212, snake_anaconda Rs +163, snake_viper_tick Rs +93, benchmark_smallcap Rs +80, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -489

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.