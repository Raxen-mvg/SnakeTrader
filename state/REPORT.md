# Paper trading report

Updated 2026-11-27 15:04 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,004 | +12.00% | 0 | - | 236 |
| benchmark | 223,661 | +11.83% | 0 | - | 237 |
| oracle | 212,064 | +6.03% | 0 | - | 233 |
| intramonth | 211,491 | +5.75% | 0 | - | 235 |
| random_hold | 211,358 | +5.68% | 13 | 69% | 1,037 |
| intraweek | 208,057 | +4.03% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 206,636 | +3.32% | 2 | 50% | 345 |
| snake_abs_exit | 204,382 | +2.19% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,681 | +0.84% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,834 | -0.08% | 1 | 100% | 255 |
| snake_abs_conv | 199,647 | -0.18% | 1 | 100% | 255 |
| snake_anaconda | 193,282 | -3.36% | 3 | 33% | 374 |
| snake_viper_wild | 192,610 | -3.69% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,338 | -5.33% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,909 | -14.54% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,214 (-5.39%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +6,239 | +3.11% |
| gold | +4,916 | +2.96% |
| snake_abs_exit | +3,305 | +1.64% |
| random_hold | +2,764 | +1.32% |
| snake_abs | +1,282 | +0.65% |
| snake_abs_conv | +1,280 | +0.65% |
| intraweek | +1,009 | +0.49% |
| snake_anaconda | +986 | +0.51% |
| intramonth | +957 | +0.46% |
| unified | +925 | +0.41% |
| benchmark_smallcap | +841 | +0.42% |
| snake_viper_wild | +405 | +0.21% |
| snake_viper_tick | +397 | +0.21% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -171 | -0.08% |
| benchmark | -2,326 | -1.03% |

Average per day so far: unified Rs +572, benchmark Rs +563, oracle Rs +287, intramonth Rs +274, random_hold Rs +270, intraweek Rs +192, snake_abs_exit_conv Rs +170, snake_abs_exit Rs +112, benchmark_smallcap Rs +44, nifty_calls Rs +44, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -4, snake_abs_conv Rs -9, snake_anaconda Rs -182, snake_viper_wild Rs -217, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -344, gold Rs -693

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.