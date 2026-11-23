# Paper trading report

Updated 2026-11-23 09:31 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,515 | +12.26% | 0 | - | 236 |
| benchmark | 223,990 | +11.99% | 0 | - | 237 |
| intraweek | 213,331 | +6.67% | 40 | 55% | 4,400 |
| intramonth | 212,245 | +6.12% | 0 | - | 235 |
| oracle | 211,069 | +5.53% | 0 | - | 233 |
| random_hold | 210,803 | +5.40% | 12 | 75% | 1,009 |
| snake_abs_exit | 208,452 | +4.23% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,819 | +3.41% | 2 | 50% | 345 |
| snake_abs | 205,495 | +2.75% | 1 | 100% | 255 |
| snake_abs_conv | 205,356 | +2.68% | 1 | 100% | 255 |
| snake_viper_wild | 203,357 | +1.68% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 199,889 | -0.06% | 15 | 47% | 2,625 |
| benchmark_smallcap | 199,843 | -0.08% | 0 | - | 237 |
| snake_anaconda | 199,596 | -0.20% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,233 | -15.38% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,756 (-4.62%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,184 | +0.70% |
| snake_viper_wild | +528 | +0.26% |
| snake_viper_tick | +517 | +0.26% |
| snake_abs_exit_conv | +202 | +0.10% |
| random_hold | +43 | +0.02% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs_exit | -110 | -0.05% |
| snake_anaconda | -310 | -0.15% |
| snake_abs | -425 | -0.21% |
| snake_abs_conv | -427 | -0.21% |
| benchmark_smallcap | -1,065 | -0.53% |
| benchmark | -1,148 | -0.51% |
| oracle | -1,410 | -0.66% |
| unified | -1,666 | -0.74% |
| intraweek | -2,381 | -1.10% |
| intramonth | -2,759 | -1.28% |

Average per day so far: unified Rs +629, benchmark Rs +615, intraweek Rs +342, intramonth Rs +314, oracle Rs +284, random_hold Rs +277, snake_abs_exit Rs +235, snake_abs_exit_conv Rs +189, snake_abs_conv Rs +149, snake_abs Rs +149, snake_viper_wild Rs +108, nifty_calls Rs +47, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, snake_viper_tick Rs -4, benchmark_smallcap Rs -4, snake_anaconda Rs -12, snake_nonews Rs -300, snake Rs -320, gold Rs -789

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.