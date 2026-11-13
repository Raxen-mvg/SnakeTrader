# Paper trading report

Updated 2026-11-13 10:34 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,595 | +10.30% | 0 | - | 236 |
| benchmark | 219,966 | +9.98% | 0 | - | 237 |
| snake_abs_exit_conv | 216,970 | +8.48% | 2 | 50% | 345 |
| snake_abs_exit | 216,569 | +8.28% | 2 | 50% | 345 |
| intraweek | 216,219 | +8.11% | 30 | 53% | 3,302 |
| oracle | 213,691 | +6.84% | 0 | - | 233 |
| snake_abs | 213,178 | +6.59% | 1 | 100% | 255 |
| snake_abs_conv | 213,011 | +6.51% | 1 | 100% | 255 |
| intramonth | 211,427 | +5.71% | 0 | - | 235 |
| random_hold | 207,299 | +3.65% | 10 | 70% | 733 |
| snake_viper_wild | 206,723 | +3.36% | 14 | 50% | 2,496 |
| snake_anaconda | 205,165 | +2.58% | 3 | 33% | 374 |
| benchmark_smallcap | 203,587 | +1.79% | 0 | - | 237 |
| snake_viper_tick | 203,188 | +1.59% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,440 | -7.78% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,193 (-3.90%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,561 | +0.73% |
| snake_viper_wild | +1,431 | +0.70% |
| snake_viper_tick | +1,406 | +0.70% |
| oracle | +575 | +0.27% |
| benchmark_smallcap | +381 | +0.19% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -102 | -0.05% |
| intramonth | -166 | -0.08% |
| benchmark | -581 | -0.26% |
| random_hold | -755 | -0.36% |
| snake_anaconda | -762 | -0.37% |
| gold | -871 | -0.47% |
| snake_abs_exit | -874 | -0.40% |
| snake_abs_exit_conv | -1,704 | -0.78% |
| snake_abs_conv | -2,524 | -1.17% |
| snake_abs | -2,533 | -1.17% |

Average per day so far: unified Rs +624, benchmark Rs +605, snake_abs_exit_conv Rs +566, snake_abs_exit Rs +552, intraweek Rs +491, snake_abs_conv Rs +434, snake_abs Rs +425, oracle Rs +415, intramonth Rs +346, snake_viper_wild Rs +269, random_hold Rs +221, snake_anaconda Rs +184, snake_viper_tick Rs +145, benchmark_smallcap Rs +124, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -472

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.