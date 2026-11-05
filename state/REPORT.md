# Paper trading report

Updated 2026-11-05 15:04 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 216,182 | +8.09% | 0 | - | 236 |
| snake_abs_exit_conv | 215,161 | +7.58% | 1 | 100% | 255 |
| snake_abs_exit | 215,041 | +7.52% | 1 | 100% | 260 |
| benchmark | 213,884 | +6.94% | 0 | - | 237 |
| snake_abs | 212,037 | +6.02% | 1 | 100% | 255 |
| snake_abs_conv | 211,898 | +5.95% | 1 | 100% | 255 |
| intraweek | 208,949 | +4.47% | 25 | 48% | 2,757 |
| intramonth | 207,968 | +3.98% | 0 | - | 235 |
| snake_viper_wild | 204,554 | +2.28% | 3 | 33% | 702 |
| random_hold | 204,496 | +2.25% | 8 | 62% | 649 |
| oracle | 204,166 | +2.08% | 0 | - | 233 |
| snake_anaconda | 202,913 | +1.46% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,040 | +0.52% | 2 | 0% | 532 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,688 | -0.66% | 0 | - | 237 |
| gold | 194,336 | -2.83% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,450 (-5.28%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,126 | +2.46% |
| gold | +2,943 | +1.54% |
| oracle | +2,373 | +1.18% |
| benchmark_smallcap | +2,018 | +1.03% |
| unified | +1,743 | +0.81% |
| random_hold | +1,188 | +0.58% |
| intramonth | +952 | +0.46% |
| snake_abs_exit_conv | +146 | +0.07% |
| snake_abs_exit | +141 | +0.07% |
| snake_abs_conv | +140 | +0.07% |
| snake_abs | +134 | +0.06% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| intraweek | -749 | -0.36% |
| snake_anaconda | -907 | -0.45% |
| snake_viper_tick | -4,361 | -2.12% |
| snake_viper_wild | -4,476 | -2.14% |

Average per day so far: snake_abs_exit_conv Rs +606, snake_abs_exit Rs +602, unified Rs +578, benchmark Rs +496, snake_abs_conv Rs +476, snake_abs Rs +463, intraweek Rs +320, intramonth Rs +285, snake_viper_wild Rs +228, random_hold Rs +161, oracle Rs +149, snake_anaconda Rs +127, nifty_calls Rs +66, snake_viper_tick Rs +61, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -55, gold Rs -202, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.