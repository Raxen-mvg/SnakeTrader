# Paper trading report

Updated 2026-11-13 12:52 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,901 | +9.95% | 0 | - | 236 |
| benchmark | 219,194 | +9.60% | 0 | - | 237 |
| snake_abs_exit | 216,837 | +8.42% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,775 | +8.39% | 2 | 50% | 345 |
| intraweek | 215,516 | +7.76% | 30 | 53% | 3,302 |
| oracle | 212,878 | +6.44% | 0 | - | 233 |
| snake_abs | 212,870 | +6.43% | 1 | 100% | 255 |
| snake_abs_conv | 212,701 | +6.35% | 1 | 100% | 255 |
| intramonth | 210,500 | +5.25% | 0 | - | 235 |
| random_hold | 206,954 | +3.48% | 10 | 70% | 733 |
| snake_viper_wild | 205,621 | +2.81% | 14 | 50% | 2,496 |
| snake_anaconda | 205,067 | +2.53% | 3 | 33% | 374 |
| benchmark_smallcap | 202,499 | +1.25% | 0 | - | 237 |
| snake_viper_tick | 202,104 | +1.05% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,486 | -8.26% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,558 (-4.22%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +858 | +0.40% |
| snake_viper_wild | +328 | +0.16% |
| snake_viper_tick | +323 | +0.16% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -238 | -0.11% |
| snake_abs_exit | -606 | -0.28% |
| benchmark_smallcap | -706 | -0.35% |
| unified | -796 | -0.36% |
| snake_anaconda | -860 | -0.42% |
| intramonth | -1,093 | -0.52% |
| random_hold | -1,099 | -0.53% |
| benchmark | -1,354 | -0.61% |
| gold | -1,825 | -0.98% |
| snake_abs_exit_conv | -1,899 | -0.87% |
| snake_abs_conv | -2,834 | -1.31% |
| snake_abs | -2,842 | -1.32% |

Average per day so far: unified Rs +603, benchmark Rs +582, snake_abs_exit Rs +561, snake_abs_exit_conv Rs +559, intraweek Rs +470, snake_abs_conv Rs +423, snake_abs Rs +415, oracle Rs +390, intramonth Rs +318, snake_viper_wild Rs +225, random_hold Rs +211, snake_anaconda Rs +181, snake_viper_tick Rs +96, benchmark_smallcap Rs +86, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -500

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.