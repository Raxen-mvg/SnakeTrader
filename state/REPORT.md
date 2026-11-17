# Paper trading report

Updated 2026-11-17 15:25 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,672 | +10.84% | 0 | - | 237 |
| unified | 221,453 | +10.73% | 0 | - | 236 |
| intraweek | 213,344 | +6.67% | 35 | 54% | 3,851 |
| snake_abs_exit | 213,075 | +6.54% | 2 | 50% | 345 |
| oracle | 212,559 | +6.28% | 0 | - | 233 |
| intramonth | 211,592 | +5.80% | 0 | - | 235 |
| snake_abs_exit_conv | 211,534 | +5.77% | 2 | 50% | 345 |
| snake_viper_wild | 209,159 | +4.58% | 14 | 50% | 2,496 |
| random_hold | 208,383 | +4.19% | 10 | 70% | 733 |
| snake_abs | 208,299 | +4.15% | 1 | 100% | 255 |
| snake_abs_conv | 208,161 | +4.08% | 1 | 100% | 255 |
| snake_viper_tick | 205,585 | +2.79% | 13 | 46% | 2,299 |
| snake_anaconda | 204,020 | +2.01% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,067 | +0.03% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,823 | -9.59% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,176 (-4.41%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,015 | +1.46% |
| snake_viper_tick | +2,965 | +1.46% |
| intraweek | +2,078 | +0.98% |
| benchmark | +1,591 | +0.72% |
| random_hold | +589 | +0.28% |
| oracle | +536 | +0.25% |
| unified | +15 | +0.01% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intramonth | -27 | -0.01% |
| gold | -132 | -0.07% |
| benchmark_smallcap | -762 | -0.38% |
| snake_anaconda | -1,082 | -0.53% |
| snake_abs_exit | -1,335 | -0.62% |
| snake_abs_exit_conv | -1,683 | -0.79% |
| snake_abs_conv | -1,829 | -0.87% |
| snake_abs | -1,835 | -0.87% |

Average per day so far: benchmark Rs +619, unified Rs +613, snake_abs_exit Rs +409, intraweek Rs +381, snake_abs_exit_conv Rs +360, oracle Rs +359, snake_viper_wild Rs +339, intramonth Rs +331, snake_abs_conv Rs +255, snake_abs Rs +251, random_hold Rs +240, snake_viper_tick Rs +233, snake_anaconda Rs +134, nifty_calls Rs +52, benchmark_smallcap Rs +2, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -548

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.