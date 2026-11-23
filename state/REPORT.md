# Paper trading report

Updated 2026-11-23 13:52 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,675 | +11.84% | 0 | - | 236 |
| benchmark | 222,292 | +11.15% | 0 | - | 237 |
| intraweek | 212,259 | +6.13% | 40 | 55% | 4,400 |
| intramonth | 211,876 | +5.94% | 0 | - | 235 |
| oracle | 211,376 | +5.69% | 0 | - | 233 |
| random_hold | 208,897 | +4.45% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,877 | +3.44% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,676 | +2.84% | 2 | 50% | 345 |
| snake_abs | 204,618 | +2.31% | 1 | 100% | 255 |
| snake_abs_conv | 204,446 | +2.22% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,831 | +0.42% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,327 | -0.34% | 0 | - | 237 |
| snake_anaconda | 197,796 | -1.10% | 3 | 33% | 374 |
| snake_viper_tick | 197,406 | -1.30% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,233 | -15.38% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,972 (-5.01%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,184 | +0.70% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -940 | -0.46% |
| oracle | -1,103 | -0.52% |
| snake_abs | -1,302 | -0.63% |
| snake_abs_conv | -1,337 | -0.65% |
| benchmark_smallcap | -1,581 | -0.79% |
| snake_abs_exit | -1,685 | -0.81% |
| random_hold | -1,863 | -0.88% |
| snake_viper_tick | -1,966 | -0.99% |
| snake_viper_wild | -1,998 | -0.98% |
| snake_anaconda | -2,110 | -1.05% |
| unified | -2,507 | -1.11% |
| benchmark | -2,846 | -1.26% |
| intramonth | -3,128 | -1.46% |
| intraweek | -3,454 | -1.60% |

Average per day so far: unified Rs +607, benchmark Rs +572, intraweek Rs +314, intramonth Rs +305, oracle Rs +292, random_hold Rs +228, snake_abs_exit Rs +191, snake_abs_exit_conv Rs +158, snake_abs Rs +125, snake_abs_conv Rs +123, nifty_calls Rs +47, snake_viper_wild Rs +27, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -19, snake_anaconda Rs -65, snake_viper_tick Rs -93, snake_nonews Rs -300, snake Rs -320, gold Rs -789

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.