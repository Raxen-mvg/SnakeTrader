# Paper trading report

Updated 2026-11-23 13:49 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,653 | +11.83% | 0 | - | 236 |
| benchmark | 222,108 | +11.05% | 0 | - | 237 |
| intraweek | 212,304 | +6.15% | 40 | 55% | 4,400 |
| intramonth | 211,864 | +5.93% | 0 | - | 235 |
| oracle | 211,261 | +5.63% | 0 | - | 233 |
| random_hold | 208,908 | +4.45% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,775 | +3.39% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,538 | +2.77% | 2 | 50% | 345 |
| snake_abs | 204,427 | +2.21% | 1 | 100% | 255 |
| snake_abs_conv | 204,256 | +2.13% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,831 | +0.42% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,316 | -0.34% | 0 | - | 237 |
| snake_anaconda | 197,724 | -1.14% | 3 | 33% | 374 |
| snake_viper_tick | 197,406 | -1.30% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,134 | -15.43% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,939 (-5.03%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,085 | +0.65% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -1,078 | -0.52% |
| oracle | -1,218 | -0.57% |
| snake_abs | -1,493 | -0.72% |
| snake_abs_conv | -1,527 | -0.74% |
| benchmark_smallcap | -1,592 | -0.79% |
| snake_abs_exit | -1,787 | -0.86% |
| random_hold | -1,852 | -0.88% |
| snake_viper_tick | -1,966 | -0.99% |
| snake_viper_wild | -1,998 | -0.98% |
| snake_anaconda | -2,182 | -1.09% |
| unified | -2,529 | -1.12% |
| benchmark | -3,029 | -1.35% |
| intramonth | -3,140 | -1.46% |
| intraweek | -3,408 | -1.58% |

Average per day so far: unified Rs +606, benchmark Rs +567, intraweek Rs +315, intramonth Rs +304, oracle Rs +289, random_hold Rs +228, snake_abs_exit Rs +188, snake_abs_exit_conv Rs +154, snake_abs Rs +120, snake_abs_conv Rs +118, nifty_calls Rs +47, snake_viper_wild Rs +27, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -20, snake_anaconda Rs -67, snake_viper_tick Rs -93, snake_nonews Rs -300, snake Rs -320, gold Rs -791

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.