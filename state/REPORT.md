# Paper trading report

Updated 2026-11-13 12:27 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,109 | +10.05% | 0 | - | 236 |
| benchmark | 219,148 | +9.57% | 0 | - | 237 |
| snake_abs_exit_conv | 216,435 | +8.22% | 2 | 50% | 345 |
| snake_abs_exit | 216,375 | +8.19% | 2 | 50% | 345 |
| intraweek | 215,780 | +7.89% | 30 | 53% | 3,302 |
| oracle | 213,149 | +6.57% | 0 | - | 233 |
| snake_abs | 212,681 | +6.34% | 1 | 100% | 255 |
| snake_abs_conv | 212,510 | +6.25% | 1 | 100% | 255 |
| intramonth | 210,672 | +5.34% | 0 | - | 235 |
| random_hold | 207,154 | +3.58% | 10 | 70% | 733 |
| snake_viper_wild | 205,474 | +2.74% | 14 | 50% | 2,496 |
| snake_anaconda | 204,895 | +2.45% | 3 | 33% | 374 |
| benchmark_smallcap | 202,511 | +1.25% | 0 | - | 237 |
| snake_viper_tick | 201,959 | +0.98% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,650 | -8.18% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,728 (-4.14%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,122 | +0.52% |
| snake_viper_wild | +181 | +0.09% |
| snake_viper_tick | +177 | +0.09% |
| oracle | +33 | +0.02% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -588 | -0.27% |
| benchmark_smallcap | -695 | -0.34% |
| random_hold | -900 | -0.43% |
| intramonth | -921 | -0.43% |
| snake_anaconda | -1,032 | -0.50% |
| snake_abs_exit | -1,068 | -0.49% |
| benchmark | -1,400 | -0.64% |
| gold | -1,660 | -0.90% |
| snake_abs_exit_conv | -2,239 | -1.02% |
| snake_abs_conv | -3,025 | -1.40% |
| snake_abs | -3,030 | -1.41% |

Average per day so far: unified Rs +609, benchmark Rs +580, snake_abs_exit_conv Rs +548, snake_abs_exit Rs +546, intraweek Rs +478, snake_abs_conv Rs +417, snake_abs Rs +409, oracle Rs +398, intramonth Rs +323, snake_viper_wild Rs +219, random_hold Rs +217, snake_anaconda Rs +175, snake_viper_tick Rs +89, benchmark_smallcap Rs +87, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -495

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.