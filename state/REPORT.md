# Paper trading report

Updated 2026-11-23 13:46 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,792 | +11.90% | 0 | - | 236 |
| benchmark | 222,101 | +11.05% | 0 | - | 237 |
| intraweek | 212,199 | +6.10% | 40 | 55% | 4,400 |
| intramonth | 211,979 | +5.99% | 0 | - | 235 |
| oracle | 211,377 | +5.69% | 0 | - | 233 |
| random_hold | 208,871 | +4.43% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,774 | +3.39% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,612 | +2.81% | 2 | 50% | 345 |
| snake_abs | 204,452 | +2.23% | 1 | 100% | 255 |
| snake_abs_conv | 204,281 | +2.14% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,831 | +0.42% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,316 | -0.34% | 0 | - | 237 |
| snake_anaconda | 197,825 | -1.09% | 3 | 33% | 374 |
| snake_viper_tick | 197,406 | -1.30% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,216 | -15.39% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,980 (-5.01%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,167 | +0.69% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -1,004 | -0.49% |
| oracle | -1,101 | -0.52% |
| snake_abs | -1,468 | -0.71% |
| snake_abs_conv | -1,501 | -0.73% |
| benchmark_smallcap | -1,592 | -0.79% |
| snake_abs_exit | -1,788 | -0.86% |
| random_hold | -1,888 | -0.90% |
| snake_viper_tick | -1,966 | -0.99% |
| snake_viper_wild | -1,998 | -0.98% |
| snake_anaconda | -2,081 | -1.04% |
| unified | -2,390 | -1.06% |
| intramonth | -3,025 | -1.41% |
| benchmark | -3,037 | -1.35% |
| intraweek | -3,513 | -1.63% |

Average per day so far: unified Rs +610, benchmark Rs +567, intraweek Rs +313, intramonth Rs +307, oracle Rs +292, random_hold Rs +227, snake_abs_exit Rs +188, snake_abs_exit_conv Rs +156, snake_abs Rs +120, snake_abs_conv Rs +119, nifty_calls Rs +47, snake_viper_wild Rs +27, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -20, snake_anaconda Rs -64, snake_viper_tick Rs -93, snake_nonews Rs -300, snake Rs -320, gold Rs -789

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.