# Paper trading report

Updated 2026-11-13 14:01 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,143 | +10.07% | 0 | - | 236 |
| benchmark | 219,262 | +9.63% | 0 | - | 237 |
| snake_abs_exit | 216,467 | +8.23% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,209 | +8.11% | 2 | 50% | 345 |
| intraweek | 215,991 | +8.00% | 30 | 53% | 3,302 |
| oracle | 213,017 | +6.51% | 0 | - | 233 |
| snake_abs | 212,296 | +6.15% | 1 | 100% | 255 |
| snake_abs_conv | 212,130 | +6.07% | 1 | 100% | 255 |
| intramonth | 210,843 | +5.42% | 0 | - | 235 |
| random_hold | 207,192 | +3.60% | 10 | 70% | 733 |
| snake_viper_wild | 205,766 | +2.88% | 14 | 50% | 2,496 |
| snake_anaconda | 204,521 | +2.26% | 3 | 33% | 374 |
| benchmark_smallcap | 202,466 | +1.23% | 0 | - | 237 |
| snake_viper_tick | 202,248 | +1.12% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,815 | -8.09% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,767 (-4.12%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,333 | +0.62% |
| snake_viper_wild | +474 | +0.23% |
| snake_viper_tick | +466 | +0.23% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -98 | -0.05% |
| unified | -554 | -0.25% |
| benchmark_smallcap | -740 | -0.36% |
| intramonth | -750 | -0.35% |
| random_hold | -861 | -0.41% |
| snake_abs_exit | -976 | -0.45% |
| benchmark | -1,285 | -0.58% |
| snake_anaconda | -1,406 | -0.68% |
| gold | -1,496 | -0.81% |
| snake_abs_exit_conv | -2,465 | -1.13% |
| snake_abs_conv | -3,405 | -1.58% |
| snake_abs | -3,415 | -1.58% |

Average per day so far: unified Rs +610, benchmark Rs +584, snake_abs_exit Rs +549, snake_abs_exit_conv Rs +540, intraweek Rs +485, snake_abs_conv Rs +404, snake_abs Rs +397, oracle Rs +394, intramonth Rs +329, snake_viper_wild Rs +231, random_hold Rs +218, snake_anaconda Rs +161, snake_viper_tick Rs +102, benchmark_smallcap Rs +85, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -490

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.