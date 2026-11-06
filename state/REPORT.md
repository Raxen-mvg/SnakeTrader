# Paper trading report

Updated 2026-11-06 09:35 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,600 | +7.30% | 0 | - | 236 |
| benchmark | 214,137 | +7.07% | 0 | - | 237 |
| snake_abs_exit_conv | 210,652 | +5.33% | 1 | 100% | 255 |
| snake_abs_exit | 210,413 | +5.21% | 1 | 100% | 260 |
| intraweek | 209,907 | +4.95% | 25 | 48% | 2,757 |
| snake_abs | 207,580 | +3.79% | 1 | 100% | 255 |
| snake_abs_conv | 207,423 | +3.71% | 1 | 100% | 255 |
| intramonth | 206,646 | +3.32% | 0 | - | 235 |
| oracle | 204,403 | +2.20% | 0 | - | 233 |
| random_hold | 203,648 | +1.82% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,860 | -1.07% | 3 | 33% | 374 |
| snake_viper_wild | 197,283 | -1.36% | 3 | 33% | 702 |
| benchmark_smallcap | 195,258 | -2.37% | 0 | - | 237 |
| snake_viper_tick | 193,936 | -3.03% | 2 | 0% | 532 |
| gold | 190,177 | -4.91% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,543 (-6.23%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +489 | +0.23% |
| benchmark | +367 | +0.17% |
| oracle | +331 | +0.16% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -675 | -0.33% |
| intramonth | -1,303 | -0.63% |
| unified | -1,383 | -0.64% |
| benchmark_smallcap | -3,430 | -1.73% |
| gold | -4,044 | -2.08% |
| snake_abs | -4,108 | -1.94% |
| snake_abs_conv | -4,122 | -1.95% |
| snake_abs_exit_conv | -4,152 | -1.93% |
| snake_abs_exit | -4,246 | -1.98% |
| snake_anaconda | -4,619 | -2.28% |
| snake_viper_tick | -7,202 | -3.58% |
| snake_viper_wild | -7,373 | -3.60% |

Average per day so far: unified Rs +503, benchmark Rs +487, snake_abs_exit_conv Rs +410, snake_abs_exit Rs +401, intraweek Rs +342, snake_abs_conv Rs +285, snake_abs Rs +281, intramonth Rs +229, oracle Rs +152, random_hold Rs +126, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -89, snake_viper_wild Rs -129, benchmark_smallcap Rs -190, snake_viper_tick Rs -337, gold Rs -339, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.