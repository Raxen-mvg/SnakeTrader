# Paper trading report

Updated 2026-11-04 12:10 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,623 | +6.81% | 0 | - | 236 |
| snake_abs_exit_conv | 209,346 | +4.67% | 1 | 100% | 255 |
| snake_abs_exit | 209,212 | +4.61% | 1 | 100% | 260 |
| intraweek | 207,600 | +3.80% | 25 | 48% | 2,757 |
| benchmark | 207,428 | +3.71% | 0 | - | 237 |
| snake_viper_wild | 207,249 | +3.62% | 3 | 33% | 702 |
| snake_abs | 206,254 | +3.13% | 1 | 100% | 255 |
| snake_abs_conv | 206,101 | +3.05% | 1 | 100% | 255 |
| intramonth | 206,069 | +3.04% | 0 | - | 235 |
| snake_viper_tick | 203,642 | +1.82% | 2 | 0% | 532 |
| random_hold | 202,634 | +1.32% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,188 | +0.59% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 198,040 | -0.98% | 3 | 33% | 361 |
| benchmark_smallcap | 194,675 | -2.66% | 0 | - | 237 |
| gold | 190,687 | -4.66% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,007 (-5.50%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +5,409 | +2.92% |
| snake_abs_exit | +5,198 | +2.55% |
| snake_abs_exit_conv | +5,007 | +2.45% |
| snake_abs_conv | +4,960 | +2.47% |
| snake_abs | +4,945 | +2.46% |
| snake_anaconda | +4,216 | +2.17% |
| intraweek | +2,514 | +1.23% |
| random_hold | +2,165 | +1.08% |
| intramonth | +2,098 | +1.03% |
| benchmark_smallcap | +1,738 | +0.90% |
| unified | +1,622 | +0.77% |
| oracle | +1,199 | +0.60% |
| benchmark | +727 | +0.35% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,525 | -1.70% |
| snake_viper_wild | -3,644 | -1.73% |

Average per day so far: unified Rs +505, snake_abs_exit_conv Rs +389, snake_abs_exit Rs +384, snake_viper_wild Rs +382, intraweek Rs +281, benchmark Rs +275, snake_abs_conv Rs +254, snake_abs Rs +250, snake_viper_tick Rs +228, intramonth Rs +225, random_hold Rs +98, nifty_calls Rs +68, oracle Rs +44, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -89, benchmark_smallcap Rs -232, gold Rs -345, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.