# Paper trading report

Updated 2026-11-13 14:07 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,261 | +10.13% | 0 | - | 236 |
| benchmark | 219,063 | +9.53% | 0 | - | 237 |
| snake_abs_exit | 216,401 | +8.20% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,190 | +8.10% | 2 | 50% | 345 |
| intraweek | 215,847 | +7.92% | 30 | 53% | 3,302 |
| oracle | 212,946 | +6.47% | 0 | - | 233 |
| snake_abs | 212,265 | +6.13% | 1 | 100% | 255 |
| snake_abs_conv | 212,099 | +6.05% | 1 | 100% | 255 |
| intramonth | 210,972 | +5.49% | 0 | - | 235 |
| random_hold | 207,241 | +3.62% | 10 | 70% | 733 |
| snake_viper_wild | 205,757 | +2.88% | 14 | 50% | 2,496 |
| snake_anaconda | 204,397 | +2.20% | 3 | 33% | 374 |
| benchmark_smallcap | 202,410 | +1.21% | 0 | - | 237 |
| snake_viper_tick | 202,238 | +1.12% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,930 | -8.04% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,755 (-4.12%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,189 | +0.55% |
| snake_viper_wild | +464 | +0.23% |
| snake_viper_tick | +456 | +0.23% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -170 | -0.08% |
| unified | -436 | -0.20% |
| intramonth | -622 | -0.29% |
| benchmark_smallcap | -796 | -0.39% |
| random_hold | -813 | -0.39% |
| snake_abs_exit | -1,041 | -0.48% |
| gold | -1,381 | -0.74% |
| benchmark | -1,484 | -0.67% |
| snake_anaconda | -1,530 | -0.74% |
| snake_abs_exit_conv | -2,484 | -1.14% |
| snake_abs_conv | -3,436 | -1.59% |
| snake_abs | -3,446 | -1.60% |

Average per day so far: unified Rs +614, benchmark Rs +578, snake_abs_exit Rs +547, snake_abs_exit_conv Rs +540, intraweek Rs +480, snake_abs_conv Rs +403, snake_abs Rs +396, oracle Rs +392, intramonth Rs +332, snake_viper_wild Rs +230, random_hold Rs +219, snake_anaconda Rs +157, snake_viper_tick Rs +102, benchmark_smallcap Rs +83, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -487

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.