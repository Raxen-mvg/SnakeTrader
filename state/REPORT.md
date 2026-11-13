# Paper trading report

Updated 2026-11-13 12:10 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,234 | +10.12% | 0 | - | 236 |
| benchmark | 219,209 | +9.60% | 0 | - | 237 |
| snake_abs_exit | 216,306 | +8.15% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,244 | +8.12% | 2 | 50% | 345 |
| intraweek | 215,413 | +7.71% | 30 | 53% | 3,302 |
| oracle | 212,877 | +6.44% | 0 | - | 233 |
| snake_abs | 212,452 | +6.23% | 1 | 100% | 255 |
| snake_abs_conv | 212,281 | +6.14% | 1 | 100% | 255 |
| intramonth | 210,842 | +5.42% | 0 | - | 235 |
| random_hold | 207,179 | +3.59% | 10 | 70% | 733 |
| snake_viper_wild | 205,613 | +2.81% | 14 | 50% | 2,496 |
| snake_anaconda | 204,627 | +2.31% | 3 | 33% | 374 |
| benchmark_smallcap | 202,589 | +1.29% | 0 | - | 237 |
| snake_viper_tick | 202,096 | +1.05% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,634 | -8.18% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,621 (-4.19%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +755 | +0.35% |
| snake_viper_wild | +321 | +0.16% |
| snake_viper_tick | +315 | +0.16% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -238 | -0.11% |
| unified | -462 | -0.21% |
| benchmark_smallcap | -617 | -0.30% |
| intramonth | -751 | -0.35% |
| random_hold | -875 | -0.42% |
| snake_abs_exit | -1,136 | -0.52% |
| snake_anaconda | -1,300 | -0.63% |
| benchmark | -1,339 | -0.61% |
| gold | -1,677 | -0.91% |
| snake_abs_exit_conv | -2,430 | -1.11% |
| snake_abs_conv | -3,254 | -1.51% |
| snake_abs | -3,259 | -1.51% |

Average per day so far: unified Rs +613, benchmark Rs +582, snake_abs_exit Rs +544, snake_abs_exit_conv Rs +541, intraweek Rs +467, snake_abs_conv Rs +409, snake_abs Rs +402, oracle Rs +390, intramonth Rs +329, snake_viper_wild Rs +225, random_hold Rs +218, snake_anaconda Rs +165, snake_viper_tick Rs +95, benchmark_smallcap Rs +89, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -496

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.