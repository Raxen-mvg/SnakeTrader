# Paper trading report

Updated 2026-11-23 11:48 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,336 | +12.17% | 0 | - | 236 |
| benchmark | 223,057 | +11.53% | 0 | - | 237 |
| intraweek | 212,679 | +6.34% | 40 | 55% | 4,400 |
| intramonth | 212,394 | +6.20% | 0 | - | 235 |
| oracle | 211,537 | +5.77% | 0 | - | 233 |
| random_hold | 209,788 | +4.89% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,466 | +3.73% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,485 | +3.24% | 2 | 50% | 345 |
| snake_abs | 204,943 | +2.47% | 1 | 100% | 255 |
| snake_abs_conv | 204,779 | +2.39% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,556 | +0.78% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,551 | -0.22% | 0 | - | 237 |
| snake_anaconda | 198,412 | -0.79% | 3 | 33% | 374 |
| snake_viper_tick | 198,116 | -0.94% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,808 | -15.10% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,438 (-4.78%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,759 | +1.05% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -132 | -0.06% |
| oracle | -942 | -0.44% |
| random_hold | -971 | -0.46% |
| snake_abs | -977 | -0.47% |
| snake_abs_conv | -1,004 | -0.49% |
| snake_abs_exit | -1,096 | -0.53% |
| snake_viper_tick | -1,256 | -0.63% |
| snake_viper_wild | -1,273 | -0.63% |
| benchmark_smallcap | -1,356 | -0.68% |
| snake_anaconda | -1,494 | -0.75% |
| unified | -1,845 | -0.82% |
| benchmark | -2,081 | -0.92% |
| intramonth | -2,611 | -1.21% |
| intraweek | -3,033 | -1.41% |

Average per day so far: unified Rs +624, benchmark Rs +591, intraweek Rs +325, intramonth Rs +318, oracle Rs +296, random_hold Rs +251, snake_abs_exit Rs +207, snake_abs_exit_conv Rs +180, snake_abs Rs +134, snake_abs_conv Rs +133, snake_viper_wild Rs +50, nifty_calls Rs +47, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -13, snake_anaconda Rs -47, snake_viper_tick Rs -67, snake_nonews Rs -300, snake Rs -320, gold Rs -774

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.