# Paper trading report

Updated 2026-11-25 12:41 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,134 | +12.57% | 0 | - | 236 |
| benchmark | 224,816 | +12.41% | 0 | - | 237 |
| intramonth | 213,231 | +6.62% | 0 | - | 235 |
| oracle | 212,765 | +6.38% | 0 | - | 233 |
| random_hold | 209,957 | +4.98% | 12 | 75% | 1,009 |
| intraweek | 208,237 | +4.12% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,293 | +1.15% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,067 | +1.03% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,790 | +0.40% | 1 | 100% | 255 |
| snake_abs_conv | 200,607 | +0.30% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,372 | -0.31% | 0 | - | 237 |
| snake_viper_wild | 196,958 | -1.52% | 16 | 50% | 2,827 |
| snake_anaconda | 194,034 | -2.98% | 3 | 33% | 374 |
| snake_viper_tick | 193,603 | -3.20% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,531 | -17.73% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,527 (-5.24%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,343 | +1.51% |
| random_hold | +1,531 | +0.73% |
| unified | +849 | +0.38% |
| intramonth | +480 | +0.23% |
| oracle | +423 | +0.20% |
| benchmark_smallcap | +392 | +0.20% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -3,382 | -1.60% |
| snake_viper_tick | -4,089 | -2.07% |
| snake_viper_wild | -4,167 | -2.07% |
| snake_anaconda | -4,670 | -2.35% |
| snake_abs | -4,671 | -2.27% |
| snake_abs_conv | -4,696 | -2.29% |
| gold | -4,899 | -2.89% |
| snake_abs_exit_conv | -4,979 | -2.40% |
| snake_abs_exit | -5,202 | -2.51% |

Average per day so far: unified Rs +628, benchmark Rs +620, intramonth Rs +331, oracle Rs +319, random_hold Rs +249, intraweek Rs +206, snake_abs_exit Rs +62, snake_abs_exit_conv Rs +56, nifty_calls Rs +46, snake_abs Rs +21, snake_abs_conv Rs +16, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -17, snake_viper_wild Rs -95, snake_anaconda Rs -170, snake_viper_tick Rs -221, snake_nonews Rs -292, snake Rs -311, gold Rs -887

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.