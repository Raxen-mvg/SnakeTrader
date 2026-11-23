# Paper trading report

Updated 2026-11-23 13:13 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,005 | +12.00% | 0 | - | 236 |
| benchmark | 222,483 | +11.24% | 0 | - | 237 |
| intraweek | 212,329 | +6.16% | 40 | 55% | 4,400 |
| intramonth | 212,190 | +6.09% | 0 | - | 235 |
| oracle | 211,786 | +5.89% | 0 | - | 233 |
| random_hold | 208,977 | +4.49% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,013 | +3.51% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,533 | +2.77% | 2 | 50% | 345 |
| snake_abs | 204,477 | +2.24% | 1 | 100% | 255 |
| snake_abs_conv | 204,314 | +2.16% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,894 | +0.45% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,237 | -0.38% | 0 | - | 237 |
| snake_anaconda | 198,104 | -0.95% | 3 | 33% | 374 |
| snake_viper_tick | 197,467 | -1.27% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,104 | -14.95% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,139 (-4.93%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,055 | +1.22% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -693 | -0.33% |
| snake_abs_exit_conv | -1,084 | -0.53% |
| snake_abs | -1,443 | -0.70% |
| snake_abs_conv | -1,469 | -0.71% |
| snake_abs_exit | -1,549 | -0.74% |
| benchmark_smallcap | -1,670 | -0.83% |
| random_hold | -1,783 | -0.85% |
| snake_anaconda | -1,802 | -0.90% |
| snake_viper_tick | -1,905 | -0.95% |
| snake_viper_wild | -1,935 | -0.95% |
| unified | -2,177 | -0.96% |
| benchmark | -2,655 | -1.18% |
| intramonth | -2,815 | -1.31% |
| intraweek | -3,384 | -1.57% |

Average per day so far: unified Rs +616, benchmark Rs +576, intraweek Rs +316, intramonth Rs +313, oracle Rs +302, random_hold Rs +230, snake_abs_exit Rs +195, snake_abs_exit_conv Rs +154, snake_abs Rs +121, snake_abs_conv Rs +120, nifty_calls Rs +47, snake_viper_wild Rs +29, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -22, snake_anaconda Rs -56, snake_viper_tick Rs -90, snake_nonews Rs -300, snake Rs -320, gold Rs -767

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.