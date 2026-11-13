# Paper trading report

Updated 2026-11-13 15:19 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 219,385 | +9.69% | 0 | - | 237 |
| unified | 218,637 | +9.32% | 0 | - | 236 |
| snake_abs_exit | 217,027 | +8.51% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,461 | +8.23% | 2 | 50% | 345 |
| intraweek | 216,090 | +8.04% | 30 | 53% | 3,302 |
| oracle | 212,990 | +6.50% | 0 | - | 233 |
| snake_abs | 212,650 | +6.33% | 1 | 100% | 255 |
| snake_abs_conv | 212,477 | +6.24% | 1 | 100% | 255 |
| intramonth | 209,844 | +4.92% | 0 | - | 235 |
| random_hold | 207,231 | +3.62% | 10 | 70% | 733 |
| snake_anaconda | 204,950 | +2.48% | 3 | 33% | 374 |
| snake_viper_wild | 204,594 | +2.30% | 14 | 50% | 2,496 |
| benchmark_smallcap | 202,466 | +1.23% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,094 | +0.55% | 13 | 46% | 2,299 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,831 | -8.08% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,440 (-4.28%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,432 | +0.67% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -126 | -0.06% |
| snake_abs_exit | -416 | -0.19% |
| snake_viper_tick | -688 | -0.34% |
| snake_viper_wild | -699 | -0.34% |
| benchmark_smallcap | -740 | -0.36% |
| random_hold | -822 | -0.40% |
| snake_anaconda | -977 | -0.47% |
| benchmark | -1,163 | -0.53% |
| gold | -1,480 | -0.80% |
| intramonth | -1,750 | -0.83% |
| unified | -2,060 | -0.93% |
| snake_abs_exit_conv | -2,213 | -1.01% |
| snake_abs_conv | -3,058 | -1.42% |
| snake_abs | -3,062 | -1.42% |

Average per day so far: benchmark Rs +587, snake_abs_exit Rs +568, unified Rs +565, snake_abs_exit_conv Rs +549, intraweek Rs +488, snake_abs_conv Rs +416, snake_abs Rs +408, oracle Rs +394, intramonth Rs +298, random_hold Rs +219, snake_viper_wild Rs +184, snake_anaconda Rs +177, benchmark_smallcap Rs +85, nifty_calls Rs +56, snake_viper_tick Rs +50, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -490

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.