# Paper trading report

Updated 2026-11-23 12:49 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,795 | +11.90% | 0 | - | 236 |
| benchmark | 222,621 | +11.31% | 0 | - | 237 |
| intraweek | 212,173 | +6.09% | 40 | 55% | 4,400 |
| intramonth | 211,875 | +5.94% | 0 | - | 235 |
| oracle | 211,776 | +5.89% | 0 | - | 233 |
| random_hold | 208,701 | +4.35% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,567 | +3.28% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,323 | +2.66% | 2 | 50% | 345 |
| snake_abs | 204,010 | +2.00% | 1 | 100% | 255 |
| snake_abs_conv | 203,844 | +1.92% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,899 | +0.45% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,450 | -0.28% | 0 | - | 237 |
| snake_anaconda | 197,787 | -1.11% | 3 | 33% | 374 |
| snake_viper_tick | 197,472 | -1.26% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,564 | -14.72% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,961 (-5.02%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,515 | +1.50% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -702 | -0.33% |
| snake_abs_exit_conv | -1,293 | -0.63% |
| benchmark_smallcap | -1,457 | -0.72% |
| snake_viper_tick | -1,900 | -0.95% |
| snake_abs | -1,910 | -0.93% |
| snake_viper_wild | -1,931 | -0.95% |
| snake_abs_conv | -1,939 | -0.94% |
| snake_abs_exit | -1,996 | -0.96% |
| random_hold | -2,058 | -0.98% |
| snake_anaconda | -2,119 | -1.06% |
| unified | -2,387 | -1.05% |
| benchmark | -2,517 | -1.12% |
| intramonth | -3,130 | -1.46% |
| intraweek | -3,540 | -1.64% |

Average per day so far: unified Rs +610, benchmark Rs +580, intraweek Rs +312, intramonth Rs +304, oracle Rs +302, random_hold Rs +223, snake_abs_exit Rs +182, snake_abs_exit_conv Rs +148, snake_abs Rs +108, snake_abs_conv Rs +107, nifty_calls Rs +47, snake_viper_wild Rs +29, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -16, snake_anaconda Rs -65, snake_viper_tick Rs -90, snake_nonews Rs -300, snake Rs -320, gold Rs -755

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.