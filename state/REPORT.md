# Paper trading report

Updated 2026-11-19 15:11 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,624 | +12.31% | 0 | - | 236 |
| benchmark | 222,407 | +11.20% | 0 | - | 237 |
| intramonth | 214,042 | +7.02% | 0 | - | 235 |
| snake_abs_exit | 213,370 | +6.68% | 2 | 50% | 345 |
| intraweek | 212,785 | +6.39% | 35 | 54% | 3,851 |
| oracle | 212,069 | +6.04% | 0 | - | 233 |
| snake_abs_exit_conv | 211,099 | +5.55% | 2 | 50% | 345 |
| snake_abs | 208,846 | +4.42% | 1 | 100% | 255 |
| snake_abs_conv | 208,725 | +4.36% | 1 | 100% | 255 |
| random_hold | 208,390 | +4.20% | 10 | 70% | 733 |
| snake_viper_wild | 207,614 | +3.81% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,066 | +2.03% | 15 | 47% | 2,625 |
| snake_anaconda | 203,446 | +1.72% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,479 | +0.74% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,937 | -12.53% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,966 (-4.02%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,152 | +1.08% |
| benchmark | +2,111 | +0.96% |
| unified | +2,012 | +0.90% |
| intramonth | +1,768 | +0.83% |
| random_hold | +1,458 | +0.70% |
| oracle | +1,273 | +0.60% |
| intraweek | +946 | +0.45% |
| snake_viper_wild | +575 | +0.28% |
| snake_viper_tick | +563 | +0.28% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -591 | -0.28% |
| snake_abs_conv | -600 | -0.29% |
| snake_abs_exit | -662 | -0.31% |
| snake_anaconda | -955 | -0.47% |
| snake_abs_exit_conv | -1,285 | -0.60% |
| gold | -2,384 | -1.34% |

Average per day so far: unified Rs +666, benchmark Rs +606, snake_abs_exit Rs +393, intramonth Rs +380, intraweek Rs +346, snake_abs_exit_conv Rs +326, oracle Rs +326, snake_viper_wild Rs +263, snake_abs_conv Rs +257, snake_abs Rs +253, random_hold Rs +227, snake_viper_tick Rs +156, snake_anaconda Rs +108, nifty_calls Rs +50, benchmark_smallcap Rs +45, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -677

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.