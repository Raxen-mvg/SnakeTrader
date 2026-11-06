# Paper trading report

Updated 2026-11-06 14:19 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 216,156 | +8.08% | 0 | - | 237 |
| unified | 215,202 | +7.60% | 0 | - | 236 |
| snake_abs_exit_conv | 208,855 | +4.43% | 1 | 100% | 255 |
| snake_abs_exit | 208,751 | +4.38% | 1 | 100% | 260 |
| intraweek | 208,676 | +4.34% | 25 | 48% | 2,757 |
| intramonth | 207,450 | +3.73% | 0 | - | 235 |
| snake_abs | 205,834 | +2.92% | 1 | 100% | 255 |
| snake_abs_conv | 205,650 | +2.83% | 1 | 100% | 255 |
| oracle | 205,427 | +2.71% | 0 | - | 233 |
| random_hold | 203,421 | +1.71% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,217 | -1.89% | 3 | 33% | 702 |
| snake_anaconda | 196,069 | -1.97% | 3 | 33% | 374 |
| benchmark_smallcap | 195,314 | -2.34% | 0 | - | 237 |
| snake_viper_tick | 192,889 | -3.56% | 2 | 0% | 532 |
| gold | 191,081 | -4.46% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,140 (-6.43%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,387 | +1.12% |
| oracle | +1,355 | +0.66% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -498 | -0.24% |
| intraweek | -743 | -0.35% |
| unified | -781 | -0.36% |
| random_hold | -902 | -0.44% |
| gold | -3,140 | -1.62% |
| benchmark_smallcap | -3,374 | -1.70% |
| snake_abs | -5,855 | -2.77% |
| snake_abs_conv | -5,895 | -2.79% |
| snake_abs_exit | -5,908 | -2.75% |
| snake_abs_exit_conv | -5,948 | -2.77% |
| snake_anaconda | -6,410 | -3.17% |
| snake_viper_tick | -8,249 | -4.10% |
| snake_viper_wild | -8,439 | -4.12% |

Average per day so far: benchmark Rs +557, unified Rs +524, snake_abs_exit_conv Rs +341, snake_abs_exit Rs +337, intraweek Rs +299, intramonth Rs +257, snake_abs_conv Rs +217, snake_abs Rs +216, oracle Rs +187, random_hold Rs +118, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -164, snake_viper_wild Rs -180, benchmark_smallcap Rs -187, gold Rs -308, snake_viper_tick Rs -395, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.