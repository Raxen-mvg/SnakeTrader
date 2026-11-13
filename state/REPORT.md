# Paper trading report

Updated 2026-11-13 15:07 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 219,385 | +9.69% | 0 | - | 237 |
| unified | 218,943 | +9.47% | 0 | - | 236 |
| snake_abs_exit | 217,044 | +8.52% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,381 | +8.19% | 2 | 50% | 345 |
| intraweek | 216,111 | +8.05% | 30 | 53% | 3,302 |
| oracle | 212,808 | +6.40% | 0 | - | 233 |
| snake_abs | 212,474 | +6.24% | 1 | 100% | 255 |
| snake_abs_conv | 212,301 | +6.15% | 1 | 100% | 255 |
| intramonth | 210,001 | +5.00% | 0 | - | 235 |
| random_hold | 207,110 | +3.56% | 10 | 70% | 733 |
| snake_viper_wild | 205,021 | +2.51% | 14 | 50% | 2,496 |
| snake_anaconda | 204,710 | +2.35% | 3 | 33% | 374 |
| benchmark_smallcap | 203,026 | +1.51% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,515 | +0.76% | 13 | 46% | 2,299 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,996 | -8.00% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,476 (-4.26%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,453 | +0.68% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| benchmark_smallcap | -179 | -0.09% |
| snake_viper_tick | -267 | -0.13% |
| snake_viper_wild | -271 | -0.13% |
| oracle | -307 | -0.14% |
| snake_abs_exit | -399 | -0.18% |
| random_hold | -944 | -0.45% |
| benchmark | -1,163 | -0.53% |
| snake_anaconda | -1,217 | -0.59% |
| gold | -1,315 | -0.71% |
| intramonth | -1,592 | -0.75% |
| unified | -1,753 | -0.80% |
| snake_abs_exit_conv | -2,293 | -1.05% |
| snake_abs_conv | -3,234 | -1.50% |
| snake_abs | -3,237 | -1.50% |

Average per day so far: benchmark Rs +587, unified Rs +574, snake_abs_exit Rs +568, snake_abs_exit_conv Rs +546, intraweek Rs +488, snake_abs_conv Rs +410, snake_abs Rs +402, oracle Rs +388, intramonth Rs +303, random_hold Rs +215, snake_viper_wild Rs +201, snake_anaconda Rs +168, benchmark_smallcap Rs +104, snake_viper_tick Rs +69, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -485

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.