# Paper trading report

Updated 2026-11-23 13:04 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,632 | +11.82% | 0 | - | 236 |
| benchmark | 222,445 | +11.22% | 0 | - | 237 |
| intraweek | 212,598 | +6.30% | 40 | 55% | 4,400 |
| intramonth | 211,799 | +5.90% | 0 | - | 235 |
| oracle | 211,662 | +5.83% | 0 | - | 233 |
| random_hold | 209,254 | +4.63% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,989 | +3.49% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,680 | +2.84% | 2 | 50% | 345 |
| snake_abs | 204,506 | +2.25% | 1 | 100% | 255 |
| snake_abs_conv | 204,345 | +2.17% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,019 | +0.51% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,237 | -0.38% | 0 | - | 237 |
| snake_anaconda | 198,139 | -0.93% | 3 | 33% | 374 |
| snake_viper_tick | 197,589 | -1.21% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,170 | -14.91% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,090 (-4.96%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,121 | +1.26% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -817 | -0.38% |
| snake_abs_exit_conv | -936 | -0.45% |
| snake_abs | -1,414 | -0.69% |
| snake_abs_conv | -1,438 | -0.70% |
| random_hold | -1,505 | -0.71% |
| snake_abs_exit | -1,573 | -0.75% |
| benchmark_smallcap | -1,670 | -0.83% |
| snake_anaconda | -1,766 | -0.88% |
| snake_viper_tick | -1,782 | -0.89% |
| snake_viper_wild | -1,811 | -0.89% |
| unified | -2,549 | -1.13% |
| benchmark | -2,693 | -1.20% |
| intraweek | -3,114 | -1.44% |
| intramonth | -3,206 | -1.49% |

Average per day so far: unified Rs +606, benchmark Rs +576, intraweek Rs +323, intramonth Rs +303, oracle Rs +299, random_hold Rs +237, snake_abs_exit Rs +194, snake_abs_exit_conv Rs +158, snake_abs Rs +122, snake_abs_conv Rs +121, nifty_calls Rs +47, snake_viper_wild Rs +33, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -22, snake_anaconda Rs -55, snake_viper_tick Rs -86, snake_nonews Rs -300, snake Rs -320, gold Rs -765

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.