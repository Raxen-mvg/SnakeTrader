# Paper trading report

Updated 2026-11-13 10:43 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,350 | +10.18% | 0 | - | 236 |
| benchmark | 219,966 | +9.98% | 0 | - | 237 |
| snake_abs_exit | 217,201 | +8.60% | 2 | 50% | 345 |
| snake_abs_exit_conv | 217,187 | +8.59% | 2 | 50% | 345 |
| intraweek | 216,400 | +8.20% | 30 | 53% | 3,302 |
| oracle | 213,650 | +6.83% | 0 | - | 233 |
| snake_abs | 213,204 | +6.60% | 1 | 100% | 255 |
| snake_abs_conv | 213,035 | +6.52% | 1 | 100% | 255 |
| intramonth | 211,178 | +5.59% | 0 | - | 235 |
| random_hold | 207,350 | +3.67% | 10 | 70% | 733 |
| snake_viper_wild | 206,770 | +3.38% | 14 | 50% | 2,496 |
| snake_anaconda | 205,114 | +2.56% | 3 | 33% | 374 |
| benchmark_smallcap | 203,699 | +1.85% | 0 | - | 237 |
| snake_viper_tick | 203,233 | +1.62% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,440 | -7.78% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,173 (-3.91%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,742 | +0.81% |
| snake_viper_wild | +1,477 | +0.72% |
| snake_viper_tick | +1,452 | +0.72% |
| oracle | +535 | +0.25% |
| benchmark_smallcap | +493 | +0.24% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_abs_exit | -242 | -0.11% |
| unified | -347 | -0.16% |
| intramonth | -415 | -0.20% |
| benchmark | -581 | -0.26% |
| random_hold | -704 | -0.34% |
| snake_anaconda | -813 | -0.40% |
| gold | -871 | -0.47% |
| snake_abs_exit_conv | -1,487 | -0.68% |
| snake_abs_conv | -2,500 | -1.16% |
| snake_abs | -2,507 | -1.16% |

Average per day so far: unified Rs +617, benchmark Rs +605, snake_abs_exit Rs +573, snake_abs_exit_conv Rs +573, intraweek Rs +497, snake_abs_conv Rs +435, snake_abs Rs +426, oracle Rs +414, intramonth Rs +339, snake_viper_wild Rs +271, random_hold Rs +223, snake_anaconda Rs +183, snake_viper_tick Rs +147, benchmark_smallcap Rs +128, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -472

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.