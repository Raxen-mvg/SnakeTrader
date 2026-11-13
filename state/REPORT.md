# Paper trading report

Updated 2026-11-13 11:01 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,348 | +10.17% | 0 | - | 236 |
| benchmark | 219,890 | +9.95% | 0 | - | 237 |
| snake_abs_exit | 217,005 | +8.50% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,975 | +8.49% | 2 | 50% | 345 |
| intraweek | 216,122 | +8.06% | 30 | 53% | 3,302 |
| oracle | 213,575 | +6.79% | 0 | - | 233 |
| snake_abs | 212,807 | +6.40% | 1 | 100% | 255 |
| snake_abs_conv | 212,643 | +6.32% | 1 | 100% | 255 |
| intramonth | 211,135 | +5.57% | 0 | - | 235 |
| random_hold | 207,158 | +3.58% | 10 | 70% | 733 |
| snake_viper_wild | 206,509 | +3.25% | 14 | 50% | 2,496 |
| snake_anaconda | 205,045 | +2.52% | 3 | 33% | 374 |
| benchmark_smallcap | 203,665 | +1.83% | 0 | - | 237 |
| snake_viper_tick | 202,977 | +1.49% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,472 | -7.76% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,048 (-3.98%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,464 | +0.68% |
| snake_viper_wild | +1,216 | +0.59% |
| snake_viper_tick | +1,195 | +0.59% |
| oracle | +460 | +0.22% |
| benchmark_smallcap | +460 | +0.23% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -349 | -0.16% |
| snake_abs_exit | -437 | -0.20% |
| intramonth | -458 | -0.22% |
| benchmark | -658 | -0.30% |
| gold | -838 | -0.45% |
| snake_anaconda | -882 | -0.43% |
| random_hold | -896 | -0.43% |
| snake_abs_exit_conv | -1,699 | -0.78% |
| snake_abs_conv | -2,892 | -1.34% |
| snake_abs | -2,904 | -1.35% |

Average per day so far: unified Rs +617, benchmark Rs +603, snake_abs_exit Rs +567, snake_abs_exit_conv Rs +566, intraweek Rs +489, snake_abs_conv Rs +421, snake_abs Rs +413, oracle Rs +411, intramonth Rs +337, snake_viper_wild Rs +260, random_hold Rs +217, snake_anaconda Rs +180, snake_viper_tick Rs +135, benchmark_smallcap Rs +126, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -471

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.