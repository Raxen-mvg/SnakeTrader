# Paper trading report

Updated 2026-11-23 13:43 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,599 | +11.80% | 0 | - | 236 |
| benchmark | 222,101 | +11.05% | 0 | - | 237 |
| intraweek | 212,076 | +6.04% | 40 | 55% | 4,400 |
| intramonth | 211,799 | +5.90% | 0 | - | 235 |
| oracle | 211,321 | +5.66% | 0 | - | 233 |
| random_hold | 208,760 | +4.38% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,838 | +3.42% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,573 | +2.79% | 2 | 50% | 345 |
| snake_abs | 204,467 | +2.23% | 1 | 100% | 255 |
| snake_abs_conv | 204,297 | +2.15% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,831 | +0.42% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,282 | -0.36% | 0 | - | 237 |
| snake_anaconda | 197,840 | -1.08% | 3 | 33% | 374 |
| snake_viper_tick | 197,406 | -1.30% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,019 | -15.49% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,888 (-5.06%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +970 | +0.58% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -1,043 | -0.51% |
| oracle | -1,157 | -0.55% |
| snake_abs | -1,453 | -0.71% |
| snake_abs_conv | -1,486 | -0.72% |
| benchmark_smallcap | -1,625 | -0.81% |
| snake_abs_exit | -1,724 | -0.83% |
| snake_viper_tick | -1,966 | -0.99% |
| snake_viper_wild | -1,998 | -0.98% |
| random_hold | -2,000 | -0.95% |
| snake_anaconda | -2,066 | -1.03% |
| unified | -2,583 | -1.14% |
| benchmark | -3,037 | -1.35% |
| intramonth | -3,205 | -1.49% |
| intraweek | -3,636 | -1.69% |

Average per day so far: unified Rs +605, benchmark Rs +567, intraweek Rs +310, intramonth Rs +303, oracle Rs +290, random_hold Rs +225, snake_abs_exit Rs +190, snake_abs_exit_conv Rs +155, snake_abs Rs +121, snake_abs_conv Rs +119, nifty_calls Rs +47, snake_viper_wild Rs +27, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -21, snake_anaconda Rs -64, snake_viper_tick Rs -93, snake_nonews Rs -300, snake Rs -320, gold Rs -794

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.