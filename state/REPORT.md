# Paper trading report

Updated 2026-11-23 14:40 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,146 | +12.07% | 0 | - | 236 |
| benchmark | 222,024 | +11.01% | 0 | - | 237 |
| intramonth | 212,132 | +6.07% | 0 | - | 235 |
| intraweek | 212,116 | +6.06% | 40 | 55% | 4,400 |
| oracle | 211,922 | +5.96% | 0 | - | 233 |
| random_hold | 208,684 | +4.34% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,327 | +3.66% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,741 | +3.37% | 2 | 50% | 345 |
| snake_abs | 205,323 | +2.66% | 1 | 100% | 255 |
| snake_abs_conv | 205,145 | +2.57% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,364 | +0.68% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,674 | -0.16% | 0 | - | 237 |
| snake_anaconda | 198,364 | -0.82% | 3 | 33% | 374 |
| snake_viper_tick | 197,928 | -1.04% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,594 | -15.20% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,230 (-4.88%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,545 | +0.92% |
| snake_abs_exit_conv | +124 | +0.06% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -557 | -0.26% |
| snake_abs | -597 | -0.29% |
| snake_abs_conv | -638 | -0.31% |
| benchmark_smallcap | -1,233 | -0.61% |
| snake_abs_exit | -1,235 | -0.59% |
| snake_viper_tick | -1,444 | -0.72% |
| snake_viper_wild | -1,465 | -0.72% |
| snake_anaconda | -1,542 | -0.77% |
| unified | -2,036 | -0.90% |
| random_hold | -2,076 | -0.98% |
| intramonth | -2,872 | -1.34% |
| benchmark | -3,114 | -1.38% |
| intraweek | -3,596 | -1.67% |

Average per day so far: unified Rs +619, benchmark Rs +565, intramonth Rs +311, intraweek Rs +311, oracle Rs +306, random_hold Rs +223, snake_abs_exit Rs +204, snake_abs_exit_conv Rs +187, snake_abs Rs +144, snake_abs_conv Rs +143, nifty_calls Rs +47, snake_viper_wild Rs +44, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -9, snake_anaconda Rs -48, snake_viper_tick Rs -74, snake_nonews Rs -300, snake Rs -320, gold Rs -780

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.