# Paper trading report

Updated 2026-11-13 11:16 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,420 | +10.21% | 0 | - | 236 |
| benchmark | 219,553 | +9.78% | 0 | - | 237 |
| snake_abs_exit_conv | 216,627 | +8.31% | 2 | 50% | 345 |
| snake_abs_exit | 216,450 | +8.22% | 2 | 50% | 345 |
| intraweek | 215,974 | +7.99% | 30 | 53% | 3,302 |
| oracle | 213,441 | +6.72% | 0 | - | 233 |
| snake_abs | 212,726 | +6.36% | 1 | 100% | 255 |
| snake_abs_conv | 212,558 | +6.28% | 1 | 100% | 255 |
| intramonth | 211,211 | +5.61% | 0 | - | 235 |
| random_hold | 207,069 | +3.53% | 10 | 70% | 733 |
| snake_viper_wild | 206,169 | +3.08% | 14 | 50% | 2,496 |
| snake_anaconda | 204,839 | +2.42% | 3 | 33% | 374 |
| benchmark_smallcap | 203,138 | +1.57% | 0 | - | 237 |
| snake_viper_tick | 202,643 | +1.32% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,061 | -7.97% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,974 (-4.01%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,316 | +0.61% |
| snake_viper_wild | +876 | +0.43% |
| snake_viper_tick | +861 | +0.43% |
| oracle | +326 | +0.15% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| benchmark_smallcap | -67 | -0.03% |
| unified | -277 | -0.12% |
| intramonth | -383 | -0.18% |
| random_hold | -985 | -0.47% |
| snake_abs_exit | -993 | -0.46% |
| benchmark | -994 | -0.45% |
| snake_anaconda | -1,088 | -0.53% |
| gold | -1,249 | -0.67% |
| snake_abs_exit_conv | -2,047 | -0.94% |
| snake_abs_conv | -2,977 | -1.38% |
| snake_abs | -2,985 | -1.38% |

Average per day so far: unified Rs +619, benchmark Rs +593, snake_abs_exit_conv Rs +554, snake_abs_exit Rs +548, intraweek Rs +484, snake_abs_conv Rs +419, snake_abs Rs +411, oracle Rs +407, intramonth Rs +340, snake_viper_wild Rs +247, random_hold Rs +214, snake_anaconda Rs +173, snake_viper_tick Rs +120, benchmark_smallcap Rs +108, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -483

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.