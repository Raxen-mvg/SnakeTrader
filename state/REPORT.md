# Paper trading report

Updated 2026-11-17 13:32 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,648 | +10.82% | 0 | - | 236 |
| benchmark | 221,481 | +10.74% | 0 | - | 237 |
| snake_abs_exit | 214,579 | +7.29% | 2 | 50% | 345 |
| intraweek | 213,544 | +6.77% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 212,996 | +6.50% | 2 | 50% | 345 |
| oracle | 212,251 | +6.12% | 0 | - | 233 |
| intramonth | 211,663 | +5.83% | 0 | - | 235 |
| snake_abs | 209,752 | +4.88% | 1 | 100% | 255 |
| snake_abs_conv | 209,614 | +4.81% | 1 | 100% | 255 |
| snake_viper_wild | 209,299 | +4.65% | 14 | 50% | 2,496 |
| random_hold | 207,459 | +3.73% | 10 | 70% | 733 |
| snake_viper_tick | 205,722 | +2.86% | 13 | 46% | 2,299 |
| snake_anaconda | 205,421 | +2.71% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,132 | +0.57% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,234 | -9.38% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,161 (-4.42%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,154 | +1.53% |
| snake_viper_tick | +3,102 | +1.53% |
| intraweek | +2,279 | +1.08% |
| benchmark | +1,400 | +0.64% |
| snake_anaconda | +319 | +0.15% |
| benchmark_smallcap | +303 | +0.15% |
| gold | +279 | +0.15% |
| oracle | +228 | +0.11% |
| unified | +210 | +0.10% |
| snake_abs_exit | +169 | +0.08% |
| intramonth | +45 | +0.02% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_abs_exit_conv | -221 | -0.10% |
| random_hold | -334 | -0.16% |
| snake_abs_conv | -375 | -0.18% |
| snake_abs | -381 | -0.18% |

Average per day so far: unified Rs +619, benchmark Rs +614, snake_abs_exit Rs +456, snake_abs_exit_conv Rs +406, intraweek Rs +387, oracle Rs +350, snake_viper_wild Rs +344, intramonth Rs +333, snake_abs_conv Rs +300, snake_abs Rs +296, snake_viper_tick Rs +238, random_hold Rs +213, snake_anaconda Rs +181, nifty_calls Rs +52, benchmark_smallcap Rs +37, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -536

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.