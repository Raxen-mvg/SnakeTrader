# Paper trading report

Updated 2026-11-13 12:01 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,092 | +10.05% | 0 | - | 236 |
| benchmark | 219,385 | +9.69% | 0 | - | 237 |
| snake_abs_exit_conv | 216,691 | +8.35% | 2 | 50% | 345 |
| snake_abs_exit | 216,633 | +8.32% | 2 | 50% | 345 |
| intraweek | 215,662 | +7.83% | 30 | 53% | 3,302 |
| oracle | 213,198 | +6.60% | 0 | - | 233 |
| snake_abs | 212,638 | +6.32% | 1 | 100% | 255 |
| snake_abs_conv | 212,471 | +6.24% | 1 | 100% | 255 |
| intramonth | 210,706 | +5.35% | 0 | - | 235 |
| random_hold | 207,087 | +3.54% | 10 | 70% | 733 |
| snake_viper_wild | 205,693 | +2.85% | 14 | 50% | 2,496 |
| snake_anaconda | 205,046 | +2.52% | 3 | 33% | 374 |
| benchmark_smallcap | 202,768 | +1.38% | 0 | - | 237 |
| snake_viper_tick | 202,175 | +1.09% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,700 | -8.15% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,719 (-4.14%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,004 | +0.47% |
| snake_viper_wild | +400 | +0.20% |
| snake_viper_tick | +393 | +0.20% |
| oracle | +83 | +0.04% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| benchmark_smallcap | -437 | -0.21% |
| unified | -605 | -0.27% |
| snake_abs_exit | -810 | -0.37% |
| snake_anaconda | -881 | -0.43% |
| intramonth | -887 | -0.42% |
| random_hold | -967 | -0.47% |
| benchmark | -1,163 | -0.53% |
| gold | -1,611 | -0.87% |
| snake_abs_exit_conv | -1,983 | -0.91% |
| snake_abs_conv | -3,064 | -1.42% |
| snake_abs | -3,073 | -1.43% |

Average per day so far: unified Rs +609, benchmark Rs +587, snake_abs_exit_conv Rs +556, snake_abs_exit Rs +554, intraweek Rs +475, snake_abs_conv Rs +416, snake_abs Rs +408, oracle Rs +400, intramonth Rs +324, snake_viper_wild Rs +228, random_hold Rs +215, snake_anaconda Rs +180, snake_viper_tick Rs +99, benchmark_smallcap Rs +95, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -494

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.