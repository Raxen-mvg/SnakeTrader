# Paper trading report

Updated 2026-11-13 14:10 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,855 | +10.43% | 0 | - | 236 |
| benchmark | 219,063 | +9.53% | 0 | - | 237 |
| snake_abs_exit | 216,336 | +8.17% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,126 | +8.06% | 2 | 50% | 345 |
| intraweek | 216,067 | +8.03% | 30 | 53% | 3,302 |
| oracle | 213,071 | +6.54% | 0 | - | 233 |
| snake_abs | 212,248 | +6.12% | 1 | 100% | 255 |
| snake_abs_conv | 212,082 | +6.04% | 1 | 100% | 255 |
| intramonth | 211,320 | +5.66% | 0 | - | 235 |
| random_hold | 207,199 | +3.60% | 10 | 70% | 733 |
| snake_viper_wild | 205,600 | +2.80% | 14 | 50% | 2,496 |
| snake_anaconda | 204,376 | +2.19% | 3 | 33% | 374 |
| benchmark_smallcap | 202,477 | +1.24% | 0 | - | 237 |
| snake_viper_tick | 202,084 | +1.04% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,946 | -8.03% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,968 (-4.02%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,409 | +0.66% |
| snake_viper_wild | +307 | +0.15% |
| snake_viper_tick | +303 | +0.15% |
| unified | +158 | +0.07% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -44 | -0.02% |
| intramonth | -273 | -0.13% |
| benchmark_smallcap | -729 | -0.36% |
| random_hold | -855 | -0.41% |
| snake_abs_exit | -1,106 | -0.51% |
| gold | -1,365 | -0.74% |
| benchmark | -1,484 | -0.67% |
| snake_anaconda | -1,551 | -0.75% |
| snake_abs_exit_conv | -2,548 | -1.17% |
| snake_abs_conv | -3,453 | -1.60% |
| snake_abs | -3,463 | -1.60% |

Average per day so far: unified Rs +632, benchmark Rs +578, snake_abs_exit Rs +545, snake_abs_exit_conv Rs +538, intraweek Rs +487, snake_abs_conv Rs +403, oracle Rs +396, snake_abs Rs +395, intramonth Rs +343, snake_viper_wild Rs +224, random_hold Rs +218, snake_anaconda Rs +156, snake_viper_tick Rs +95, benchmark_smallcap Rs +85, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -486

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.