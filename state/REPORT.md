# Paper trading report

Updated 2026-11-13 10:19 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,632 | +10.32% | 0 | - | 236 |
| benchmark | 219,905 | +9.95% | 0 | - | 237 |
| snake_abs_exit_conv | 216,970 | +8.48% | 2 | 50% | 345 |
| snake_abs_exit | 216,550 | +8.28% | 2 | 50% | 345 |
| intraweek | 215,942 | +7.97% | 30 | 53% | 3,302 |
| oracle | 213,910 | +6.96% | 0 | - | 233 |
| snake_abs | 213,102 | +6.55% | 1 | 100% | 255 |
| snake_abs_conv | 212,934 | +6.47% | 1 | 100% | 255 |
| intramonth | 211,105 | +5.55% | 0 | - | 235 |
| random_hold | 207,405 | +3.70% | 10 | 70% | 733 |
| snake_viper_wild | 206,642 | +3.32% | 14 | 50% | 2,496 |
| snake_anaconda | 205,182 | +2.59% | 3 | 33% | 374 |
| benchmark_smallcap | 203,688 | +1.84% | 0 | - | 237 |
| snake_viper_tick | 203,107 | +1.55% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,275 | -7.86% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,133 (-3.93%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +1,349 | +0.66% |
| snake_viper_tick | +1,326 | +0.66% |
| intraweek | +1,284 | +0.60% |
| oracle | +794 | +0.37% |
| benchmark_smallcap | +482 | +0.24% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -64 | -0.03% |
| intramonth | -488 | -0.23% |
| benchmark | -643 | -0.29% |
| random_hold | -649 | -0.31% |
| snake_anaconda | -746 | -0.36% |
| snake_abs_exit | -892 | -0.41% |
| gold | -1,036 | -0.56% |
| snake_abs_exit_conv | -1,704 | -0.78% |
| snake_abs_conv | -2,601 | -1.21% |
| snake_abs | -2,610 | -1.21% |

Average per day so far: unified Rs +625, benchmark Rs +603, snake_abs_exit_conv Rs +566, snake_abs_exit Rs +552, intraweek Rs +483, snake_abs_conv Rs +431, snake_abs Rs +423, oracle Rs +422, intramonth Rs +337, snake_viper_wild Rs +266, random_hold Rs +224, snake_anaconda Rs +185, snake_viper_tick Rs +141, benchmark_smallcap Rs +127, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -477

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.