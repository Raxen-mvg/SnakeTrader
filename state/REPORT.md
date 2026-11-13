# Paper trading report

Updated 2026-11-13 14:25 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,360 | +10.18% | 0 | - | 236 |
| benchmark | 218,895 | +9.45% | 0 | - | 237 |
| snake_abs_exit | 215,926 | +7.96% | 2 | 50% | 345 |
| snake_abs_exit_conv | 215,817 | +7.91% | 2 | 50% | 345 |
| intraweek | 215,783 | +7.89% | 30 | 53% | 3,302 |
| oracle | 212,861 | +6.43% | 0 | - | 233 |
| snake_abs | 212,040 | +6.02% | 1 | 100% | 255 |
| snake_abs_conv | 211,868 | +5.93% | 1 | 100% | 255 |
| intramonth | 210,885 | +5.44% | 0 | - | 235 |
| random_hold | 207,085 | +3.54% | 10 | 70% | 733 |
| snake_viper_wild | 205,157 | +2.58% | 14 | 50% | 2,496 |
| snake_anaconda | 204,177 | +2.09% | 3 | 33% | 374 |
| benchmark_smallcap | 202,241 | +1.12% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,648 | +0.82% | 13 | 46% | 2,299 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,913 | -8.04% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,689 (-4.16%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,125 | +0.52% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_viper_tick | -134 | -0.07% |
| snake_viper_wild | -136 | -0.07% |
| oracle | -254 | -0.12% |
| unified | -336 | -0.15% |
| intramonth | -709 | -0.34% |
| benchmark_smallcap | -964 | -0.47% |
| random_hold | -968 | -0.47% |
| gold | -1,397 | -0.75% |
| snake_abs_exit | -1,516 | -0.70% |
| benchmark | -1,652 | -0.75% |
| snake_anaconda | -1,751 | -0.85% |
| snake_abs_exit_conv | -2,857 | -1.31% |
| snake_abs_conv | -3,667 | -1.70% |
| snake_abs | -3,672 | -1.70% |

Average per day so far: unified Rs +617, benchmark Rs +573, snake_abs_exit Rs +531, snake_abs_exit_conv Rs +527, intraweek Rs +478, snake_abs_conv Rs +396, oracle Rs +390, snake_abs Rs +388, intramonth Rs +330, random_hold Rs +215, snake_viper_wild Rs +206, snake_anaconda Rs +149, benchmark_smallcap Rs +77, snake_viper_tick Rs +75, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -487

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.