# Paper trading report

Updated 2026-11-18 12:43 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,187 | +11.09% | 0 | - | 236 |
| benchmark | 219,981 | +9.99% | 0 | - | 237 |
| intraweek | 213,170 | +6.58% | 35 | 54% | 3,851 |
| snake_abs_exit | 212,545 | +6.27% | 2 | 50% | 345 |
| intramonth | 212,231 | +6.12% | 0 | - | 235 |
| oracle | 211,639 | +5.82% | 0 | - | 233 |
| snake_abs_exit_conv | 210,711 | +5.36% | 2 | 50% | 345 |
| snake_abs | 207,795 | +3.90% | 1 | 100% | 255 |
| snake_abs_conv | 207,657 | +3.83% | 1 | 100% | 255 |
| random_hold | 206,982 | +3.49% | 10 | 70% | 733 |
| snake_viper_wild | 206,795 | +3.40% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,264 | +1.63% | 15 | 47% | 2,625 |
| snake_anaconda | 202,701 | +1.35% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,181 | -0.41% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 176,976 | -11.51% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,920 (-4.54%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +748 | +0.34% |
| intramonth | +689 | +0.33% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraweek | -153 | -0.07% |
| snake_abs_exit | -597 | -0.28% |
| snake_abs_conv | -762 | -0.37% |
| snake_abs | -763 | -0.37% |
| oracle | -848 | -0.40% |
| snake_abs_exit_conv | -863 | -0.41% |
| snake_anaconda | -1,354 | -0.66% |
| benchmark_smallcap | -1,390 | -0.69% |
| random_hold | -1,451 | -0.70% |
| benchmark | -1,622 | -0.73% |
| snake_viper_tick | -2,573 | -1.25% |
| snake_viper_wild | -2,620 | -1.25% |
| gold | -3,748 | -2.07% |

Average per day so far: unified Rs +616, benchmark Rs +555, snake_abs_exit Rs +380, intraweek Rs +366, intramonth Rs +340, snake_abs_exit_conv Rs +325, oracle Rs +323, snake_viper_wild Rs +243, snake_abs_conv Rs +232, snake_abs Rs +229, random_hold Rs +194, snake_viper_tick Rs +131, snake_anaconda Rs +87, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -26, snake_nonews Rs -326, snake Rs -347, gold Rs -640

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.