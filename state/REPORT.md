# Paper trading report

Updated 2026-11-19 14:37 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,025 | +12.01% | 0 | - | 236 |
| benchmark | 222,376 | +11.19% | 0 | - | 237 |
| snake_abs_exit | 213,628 | +6.81% | 2 | 50% | 345 |
| intramonth | 213,554 | +6.78% | 0 | - | 235 |
| oracle | 212,067 | +6.03% | 0 | - | 233 |
| intraweek | 212,034 | +6.02% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,343 | +5.67% | 2 | 50% | 345 |
| snake_abs | 209,162 | +4.58% | 1 | 100% | 255 |
| snake_abs_conv | 209,043 | +4.52% | 1 | 100% | 255 |
| random_hold | 208,033 | +4.02% | 10 | 70% | 733 |
| snake_viper_wild | 207,662 | +3.83% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,113 | +2.06% | 15 | 47% | 2,625 |
| snake_anaconda | 203,835 | +1.92% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,907 | +0.45% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,200 | -12.40% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,604 (-4.20%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,081 | +0.94% |
| benchmark_smallcap | +1,581 | +0.79% |
| unified | +1,414 | +0.64% |
| intramonth | +1,280 | +0.60% |
| oracle | +1,271 | +0.60% |
| random_hold | +1,100 | +0.53% |
| snake_viper_wild | +623 | +0.30% |
| snake_viper_tick | +610 | +0.30% |
| intraweek | +194 | +0.09% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -274 | -0.13% |
| snake_abs_conv | -281 | -0.13% |
| snake_abs_exit | -403 | -0.19% |
| snake_anaconda | -566 | -0.28% |
| snake_abs_exit_conv | -1,041 | -0.49% |
| gold | -2,121 | -1.20% |

Average per day so far: unified Rs +649, benchmark Rs +605, snake_abs_exit Rs +401, intramonth Rs +366, snake_abs_exit_conv Rs +334, oracle Rs +326, intraweek Rs +325, snake_abs_conv Rs +266, snake_viper_wild Rs +264, snake_abs Rs +262, random_hold Rs +217, snake_viper_tick Rs +158, snake_anaconda Rs +120, nifty_calls Rs +50, benchmark_smallcap Rs +27, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -670

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.