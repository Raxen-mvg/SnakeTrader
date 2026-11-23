# Paper trading report

Updated 2026-11-23 10:17 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,001 | +12.50% | 0 | - | 236 |
| benchmark | 223,569 | +11.79% | 0 | - | 237 |
| intramonth | 213,012 | +6.51% | 0 | - | 235 |
| intraweek | 213,001 | +6.50% | 40 | 55% | 4,400 |
| oracle | 211,151 | +5.58% | 0 | - | 233 |
| random_hold | 210,071 | +5.04% | 12 | 75% | 1,009 |
| snake_abs_exit | 208,442 | +4.22% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,871 | +3.44% | 2 | 50% | 345 |
| snake_abs | 205,571 | +2.79% | 1 | 100% | 255 |
| snake_abs_conv | 205,425 | +2.71% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,359 | +0.68% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,753 | -0.12% | 0 | - | 237 |
| snake_anaconda | 199,216 | -0.39% | 3 | 33% | 374 |
| snake_viper_tick | 197,923 | -1.04% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,413 | -15.29% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,766 (-4.62%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,365 | +0.81% |
| snake_abs_exit_conv | +254 | +0.12% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -120 | -0.06% |
| snake_abs | -349 | -0.17% |
| snake_abs_conv | -358 | -0.17% |
| random_hold | -689 | -0.33% |
| snake_anaconda | -689 | -0.34% |
| benchmark_smallcap | -1,155 | -0.57% |
| unified | -1,181 | -0.52% |
| oracle | -1,328 | -0.62% |
| snake_viper_tick | -1,449 | -0.73% |
| snake_viper_wild | -1,470 | -0.72% |
| benchmark | -1,568 | -0.70% |
| intramonth | -1,992 | -0.93% |
| intraweek | -2,711 | -1.26% |

Average per day so far: unified Rs +641, benchmark Rs +604, intramonth Rs +334, intraweek Rs +333, oracle Rs +286, random_hold Rs +258, snake_abs_exit Rs +235, snake_abs_exit_conv Rs +191, snake_abs_conv Rs +151, snake_abs Rs +151, nifty_calls Rs +47, snake_viper_wild Rs +44, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -7, snake_anaconda Rs -23, snake_viper_tick Rs -74, snake_nonews Rs -300, snake Rs -320, gold Rs -784

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.