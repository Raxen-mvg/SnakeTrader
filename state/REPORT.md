# Paper trading report

Updated 2026-11-26 09:21 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,145 | +12.57% | 0 | - | 237 |
| unified | 224,237 | +12.12% | 0 | - | 236 |
| oracle | 214,069 | +7.03% | 0 | - | 233 |
| intramonth | 211,859 | +5.93% | 0 | - | 235 |
| random_hold | 210,377 | +5.19% | 12 | 75% | 1,009 |
| intraweek | 207,465 | +3.73% | 40 | 55% | 4,400 |
| snake_abs_exit | 204,020 | +2.01% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,200 | +1.60% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,893 | +0.45% | 1 | 100% | 255 |
| snake_abs_conv | 200,726 | +0.36% | 1 | 100% | 255 |
| benchmark_smallcap | 200,056 | +0.03% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 197,250 | -1.38% | 16 | 50% | 2,827 |
| snake_anaconda | 195,673 | -2.16% | 3 | 33% | 374 |
| snake_viper_tick | 193,890 | -3.06% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,095 | -16.45% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,504 (-5.25%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,499 | +1.52% |
| snake_abs_exit | +1,764 | +0.87% |
| benchmark_smallcap | +1,244 | +0.63% |
| snake_abs_exit_conv | +1,224 | +0.61% |
| snake_anaconda | +1,120 | +0.57% |
| random_hold | +885 | +0.42% |
| snake_abs_conv | +754 | +0.38% |
| snake_abs | +743 | +0.37% |
| intraweek | +722 | +0.35% |
| oracle | +274 | +0.13% |
| intramonth | +166 | +0.08% |
| unified | +137 | +0.06% |
| benchmark | +122 | +0.05% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -287 | -0.15% |
| snake_viper_wild | -293 | -0.15% |

Average per day so far: benchmark Rs +613, unified Rs +591, oracle Rs +343, intramonth Rs +289, random_hold Rs +253, intraweek Rs +182, snake_abs_exit Rs +106, snake_abs_exit_conv Rs +84, nifty_calls Rs +45, snake_abs Rs +23, snake_abs_conv Rs +19, benchmark_smallcap Rs +2, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_viper_wild Rs -83, snake_anaconda Rs -120, snake_viper_tick Rs -204, snake_nonews Rs -284, snake Rs -304, gold Rs -803

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.