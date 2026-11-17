# Paper trading report

Updated 2026-11-17 14:31 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 222,001 | +11.00% | 0 | - | 237 |
| unified | 221,426 | +10.71% | 0 | - | 236 |
| intraweek | 213,580 | +6.79% | 35 | 54% | 3,851 |
| snake_abs_exit | 213,092 | +6.55% | 2 | 50% | 345 |
| oracle | 212,317 | +6.16% | 0 | - | 233 |
| snake_abs_exit_conv | 211,529 | +5.76% | 2 | 50% | 345 |
| intramonth | 211,237 | +5.62% | 0 | - | 235 |
| snake_viper_wild | 209,404 | +4.70% | 14 | 50% | 2,496 |
| snake_abs | 208,319 | +4.16% | 1 | 100% | 255 |
| snake_abs_conv | 208,180 | +4.09% | 1 | 100% | 255 |
| random_hold | 207,802 | +3.90% | 10 | 70% | 733 |
| snake_viper_tick | 205,825 | +2.91% | 13 | 46% | 2,299 |
| snake_anaconda | 203,848 | +1.92% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,221 | +0.61% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,889 | -9.56% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,067 (-4.47%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,259 | +1.58% |
| snake_viper_tick | +3,205 | +1.58% |
| intraweek | +2,314 | +1.09% |
| benchmark | +1,920 | +0.87% |
| benchmark_smallcap | +392 | +0.20% |
| oracle | +294 | +0.14% |
| random_hold | +9 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| unified | -11 | -0.01% |
| gold | -66 | -0.04% |
| intramonth | -382 | -0.18% |
| snake_anaconda | -1,255 | -0.61% |
| snake_abs_exit | -1,317 | -0.61% |
| snake_abs_exit_conv | -1,689 | -0.79% |
| snake_abs_conv | -1,810 | -0.86% |
| snake_abs | -1,815 | -0.86% |

Average per day so far: benchmark Rs +629, unified Rs +612, snake_abs_exit Rs +409, intraweek Rs +388, snake_abs_exit_conv Rs +360, oracle Rs +352, snake_viper_wild Rs +348, intramonth Rs +321, snake_abs_conv Rs +256, snake_abs Rs +252, snake_viper_tick Rs +243, random_hold Rs +223, snake_anaconda Rs +128, nifty_calls Rs +52, benchmark_smallcap Rs +39, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -546

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.