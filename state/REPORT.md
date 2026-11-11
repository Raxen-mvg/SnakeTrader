# Paper trading report

Updated 2026-11-11 14:13 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,312 | +10.16% | 0 | - | 236 |
| benchmark | 220,188 | +10.09% | 0 | - | 237 |
| snake_abs_exit_conv | 216,952 | +8.48% | 2 | 50% | 345 |
| snake_abs_exit | 216,095 | +8.05% | 2 | 50% | 345 |
| snake_abs | 213,978 | +6.99% | 1 | 100% | 255 |
| snake_abs_conv | 213,812 | +6.91% | 1 | 100% | 255 |
| intraweek | 213,303 | +6.65% | 30 | 53% | 3,302 |
| oracle | 211,847 | +5.92% | 0 | - | 233 |
| intramonth | 211,339 | +5.67% | 0 | - | 235 |
| random_hold | 207,086 | +3.54% | 9 | 67% | 709 |
| snake_viper_wild | 205,109 | +2.56% | 10 | 50% | 1,825 |
| snake_anaconda | 203,881 | +1.94% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,610 | +0.81% | 9 | 44% | 1,639 |
| benchmark_smallcap | 201,120 | +0.56% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,717 | -5.14% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,181 (-4.41%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +7,679 | +3.89% |
| snake_viper_tick | +7,533 | +3.88% |
| snake_abs_exit_conv | +5,043 | +2.38% |
| snake_anaconda | +4,414 | +2.21% |
| snake_abs_conv | +4,334 | +2.07% |
| snake_abs | +4,332 | +2.07% |
| snake_abs_exit | +4,111 | +1.94% |
| benchmark_smallcap | +2,948 | +1.49% |
| random_hold | +2,125 | +1.04% |
| benchmark | +2,096 | +0.96% |
| oracle | +1,928 | +0.92% |
| intramonth | +730 | +0.35% |
| unified | +565 | +0.26% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -1,239 | -0.58% |
| gold | -2,417 | -1.26% |

Average per day so far: unified Rs +655, benchmark Rs +651, snake_abs_exit_conv Rs +605, snake_abs_exit Rs +575, snake_abs_conv Rs +493, snake_abs Rs +482, intraweek Rs +429, oracle Rs +382, intramonth Rs +366, random_hold Rs +229, snake_viper_wild Rs +222, snake_anaconda Rs +149, snake_viper_tick Rs +80, nifty_calls Rs +59, benchmark_smallcap Rs +41, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -332, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.