# Paper trading report

Updated 2026-11-23 13:58 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,784 | +11.89% | 0 | - | 236 |
| benchmark | 222,254 | +11.13% | 0 | - | 237 |
| intraweek | 212,319 | +6.16% | 40 | 55% | 4,400 |
| intramonth | 211,895 | +5.95% | 0 | - | 235 |
| oracle | 211,468 | +5.73% | 0 | - | 233 |
| random_hold | 209,003 | +4.50% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,888 | +3.44% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,620 | +2.81% | 2 | 50% | 345 |
| snake_abs | 204,644 | +2.32% | 1 | 100% | 255 |
| snake_abs_conv | 204,471 | +2.24% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,831 | +0.42% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,484 | -0.26% | 0 | - | 237 |
| snake_anaconda | 197,782 | -1.11% | 3 | 33% | 374 |
| snake_viper_tick | 197,406 | -1.30% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,331 | -15.33% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,034 (-4.98%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,282 | +0.76% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -997 | -0.48% |
| oracle | -1,010 | -0.47% |
| snake_abs | -1,276 | -0.62% |
| snake_abs_conv | -1,312 | -0.64% |
| benchmark_smallcap | -1,424 | -0.71% |
| snake_abs_exit | -1,674 | -0.80% |
| random_hold | -1,756 | -0.83% |
| snake_viper_tick | -1,966 | -0.99% |
| snake_viper_wild | -1,998 | -0.98% |
| snake_anaconda | -2,123 | -1.06% |
| unified | -2,398 | -1.06% |
| benchmark | -2,884 | -1.28% |
| intramonth | -3,109 | -1.45% |
| intraweek | -3,393 | -1.57% |

Average per day so far: unified Rs +610, benchmark Rs +571, intraweek Rs +316, intramonth Rs +305, oracle Rs +294, random_hold Rs +231, snake_abs_exit Rs +191, snake_abs_exit_conv Rs +156, snake_abs Rs +126, snake_abs_conv Rs +124, nifty_calls Rs +47, snake_viper_wild Rs +27, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -15, snake_anaconda Rs -65, snake_viper_tick Rs -93, snake_nonews Rs -300, snake Rs -320, gold Rs -786

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.