# Paper trading report

Updated 2026-11-23 12:43 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,147 | +12.07% | 0 | - | 236 |
| benchmark | 222,598 | +11.30% | 0 | - | 237 |
| intraweek | 212,252 | +6.13% | 40 | 55% | 4,400 |
| intramonth | 212,235 | +6.12% | 0 | - | 235 |
| oracle | 211,928 | +5.96% | 0 | - | 233 |
| random_hold | 208,811 | +4.41% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,905 | +3.45% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,794 | +2.90% | 2 | 50% | 345 |
| snake_abs | 204,346 | +2.17% | 1 | 100% | 255 |
| snake_abs_conv | 204,186 | +2.09% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,913 | +0.46% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,562 | -0.22% | 0 | - | 237 |
| snake_anaconda | 198,114 | -0.94% | 3 | 33% | 374 |
| snake_viper_tick | 197,486 | -1.26% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,334 | -14.83% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,168 (-4.92%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,285 | +1.36% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -551 | -0.26% |
| snake_abs_exit_conv | -822 | -0.40% |
| benchmark_smallcap | -1,345 | -0.67% |
| snake_abs | -1,574 | -0.77% |
| snake_abs_conv | -1,597 | -0.78% |
| snake_abs_exit | -1,658 | -0.80% |
| snake_anaconda | -1,792 | -0.90% |
| snake_viper_tick | -1,886 | -0.95% |
| snake_viper_wild | -1,916 | -0.94% |
| random_hold | -1,949 | -0.93% |
| unified | -2,034 | -0.90% |
| benchmark | -2,540 | -1.13% |
| intramonth | -2,769 | -1.29% |
| intraweek | -3,460 | -1.60% |

Average per day so far: unified Rs +619, benchmark Rs +579, intraweek Rs +314, intramonth Rs +314, oracle Rs +306, random_hold Rs +226, snake_abs_exit Rs +192, snake_abs_exit_conv Rs +161, snake_abs Rs +117, snake_abs_conv Rs +116, nifty_calls Rs +47, snake_viper_wild Rs +29, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -13, snake_anaconda Rs -55, snake_viper_tick Rs -90, snake_nonews Rs -300, snake Rs -320, gold Rs -761

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.