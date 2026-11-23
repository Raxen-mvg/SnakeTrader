# Paper trading report

Updated 2026-11-23 10:13 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,940 | +12.47% | 0 | - | 236 |
| benchmark | 223,608 | +11.80% | 0 | - | 237 |
| intramonth | 212,923 | +6.46% | 0 | - | 235 |
| intraweek | 212,916 | +6.46% | 40 | 55% | 4,400 |
| oracle | 211,153 | +5.58% | 0 | - | 233 |
| random_hold | 209,990 | +5.00% | 12 | 75% | 1,009 |
| snake_abs_exit | 208,339 | +4.17% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,757 | +3.38% | 2 | 50% | 345 |
| snake_abs | 205,488 | +2.74% | 1 | 100% | 255 |
| snake_abs_conv | 205,341 | +2.67% | 1 | 100% | 255 |
| snake_viper_wild | 204,120 | +2.06% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 200,636 | +0.32% | 15 | 47% | 2,625 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,517 | -0.24% | 0 | - | 237 |
| snake_anaconda | 199,472 | -0.26% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,430 | -15.29% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,749 (-4.63%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,381 | +0.82% |
| snake_viper_wild | +1,291 | +0.64% |
| snake_viper_tick | +1,264 | +0.63% |
| snake_abs_exit_conv | +140 | +0.07% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_abs_exit | -224 | -0.11% |
| snake_abs | -432 | -0.21% |
| snake_anaconda | -433 | -0.22% |
| snake_abs_conv | -442 | -0.21% |
| random_hold | -770 | -0.36% |
| unified | -1,241 | -0.55% |
| oracle | -1,325 | -0.62% |
| benchmark_smallcap | -1,390 | -0.69% |
| benchmark | -1,530 | -0.68% |
| intramonth | -2,081 | -0.97% |
| intraweek | -2,796 | -1.30% |

Average per day so far: unified Rs +639, benchmark Rs +605, intramonth Rs +331, intraweek Rs +331, oracle Rs +286, random_hold Rs +256, snake_abs_exit Rs +232, snake_abs_exit_conv Rs +188, snake_abs_conv Rs +148, snake_abs Rs +148, snake_viper_wild Rs +133, nifty_calls Rs +47, snake_viper_tick Rs +23, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, benchmark_smallcap Rs -14, snake_anaconda Rs -16, snake_nonews Rs -300, snake Rs -320, gold Rs -784

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.