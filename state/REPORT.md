# Paper trading report

Updated 2026-11-17 10:45 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,859 | +10.93% | 0 | - | 236 |
| benchmark | 221,489 | +10.74% | 0 | - | 237 |
| snake_abs_exit | 215,492 | +7.75% | 2 | 50% | 345 |
| intraweek | 213,690 | +6.84% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 213,680 | +6.84% | 2 | 50% | 345 |
| oracle | 212,290 | +6.14% | 0 | - | 233 |
| intramonth | 211,731 | +5.87% | 0 | - | 235 |
| snake_abs | 210,123 | +5.06% | 1 | 100% | 255 |
| snake_abs_conv | 209,974 | +4.99% | 1 | 100% | 255 |
| random_hold | 208,183 | +4.09% | 10 | 70% | 733 |
| snake_viper_wild | 206,924 | +3.46% | 14 | 50% | 2,496 |
| snake_anaconda | 205,619 | +2.81% | 3 | 33% | 374 |
| snake_viper_tick | 203,386 | +1.69% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,062 | +1.03% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,415 | -9.29% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,331 (-4.33%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,424 | +1.15% |
| benchmark | +1,408 | +0.64% |
| benchmark_smallcap | +1,233 | +0.61% |
| snake_abs_exit | +1,082 | +0.51% |
| snake_viper_wild | +780 | +0.38% |
| snake_viper_tick | +766 | +0.38% |
| snake_anaconda | +516 | +0.25% |
| snake_abs_exit_conv | +462 | +0.22% |
| gold | +460 | +0.25% |
| unified | +421 | +0.19% |
| random_hold | +390 | +0.19% |
| oracle | +267 | +0.13% |
| intramonth | +112 | +0.05% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs | -11 | -0.01% |
| snake_abs_conv | -16 | -0.01% |

Average per day so far: unified Rs +625, benchmark Rs +614, snake_abs_exit Rs +484, snake_abs_exit_conv Rs +427, intraweek Rs +391, oracle Rs +351, intramonth Rs +335, snake_abs_conv Rs +312, snake_abs Rs +307, snake_viper_wild Rs +256, random_hold Rs +234, snake_anaconda Rs +187, snake_viper_tick Rs +141, benchmark_smallcap Rs +67, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -531

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.