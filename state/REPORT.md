# Paper trading report

Updated 2026-11-17 09:21 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,274 | +11.14% | 0 | - | 236 |
| benchmark | 221,030 | +10.52% | 0 | - | 237 |
| snake_abs_exit | 213,538 | +6.77% | 2 | 50% | 345 |
| snake_abs_exit_conv | 212,860 | +6.43% | 2 | 50% | 345 |
| intraweek | 212,785 | +6.39% | 35 | 54% | 3,851 |
| intramonth | 212,679 | +6.34% | 0 | - | 235 |
| oracle | 212,349 | +6.17% | 0 | - | 233 |
| snake_abs | 209,619 | +4.81% | 1 | 100% | 255 |
| snake_abs_conv | 209,459 | +4.73% | 1 | 100% | 255 |
| random_hold | 207,701 | +3.85% | 10 | 70% | 733 |
| snake_viper_wild | 206,108 | +3.05% | 14 | 50% | 2,496 |
| snake_anaconda | 204,825 | +2.41% | 3 | 33% | 374 |
| snake_viper_tick | 202,583 | +1.29% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,490 | +0.74% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,431 | -9.28% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,414 (-4.29%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,520 | +0.72% |
| intramonth | +1,061 | +0.50% |
| benchmark | +949 | +0.43% |
| unified | +836 | +0.38% |
| benchmark_smallcap | +661 | +0.33% |
| gold | +477 | +0.26% |
| oracle | +326 | +0.15% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_viper_wild | -37 | -0.02% |
| snake_viper_tick | -37 | -0.02% |
| random_hold | -92 | -0.04% |
| snake_anaconda | -278 | -0.14% |
| snake_abs_exit_conv | -357 | -0.17% |
| snake_abs | -514 | -0.24% |
| snake_abs_conv | -531 | -0.25% |
| snake_abs_exit | -871 | -0.41% |

Average per day so far: unified Rs +636, benchmark Rs +601, snake_abs_exit Rs +423, snake_abs_exit_conv Rs +402, intraweek Rs +365, intramonth Rs +362, oracle Rs +353, snake_abs_conv Rs +296, snake_abs Rs +291, snake_viper_wild Rs +226, random_hold Rs +220, snake_anaconda Rs +161, snake_viper_tick Rs +108, nifty_calls Rs +52, benchmark_smallcap Rs +48, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -531

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.