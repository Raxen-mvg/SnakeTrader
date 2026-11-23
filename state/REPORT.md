# Paper trading report

Updated 2026-11-23 09:35 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,254 | +12.63% | 0 | - | 236 |
| benchmark | 223,279 | +11.64% | 0 | - | 237 |
| intraweek | 213,425 | +6.71% | 40 | 55% | 4,400 |
| intramonth | 212,857 | +6.43% | 0 | - | 235 |
| oracle | 211,175 | +5.59% | 0 | - | 233 |
| random_hold | 210,871 | +5.44% | 12 | 75% | 1,009 |
| snake_abs_exit | 208,377 | +4.19% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,701 | +3.35% | 2 | 50% | 345 |
| snake_abs | 205,505 | +2.75% | 1 | 100% | 255 |
| snake_abs_conv | 205,364 | +2.68% | 1 | 100% | 255 |
| snake_viper_wild | 203,381 | +1.69% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 199,912 | -0.04% | 15 | 47% | 2,625 |
| benchmark_smallcap | 199,585 | -0.21% | 0 | - | 237 |
| snake_anaconda | 199,466 | -0.27% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,937 | -15.53% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,965 (-4.52%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +888 | +0.53% |
| snake_viper_wild | +552 | +0.27% |
| snake_viper_tick | +540 | +0.27% |
| random_hold | +112 | +0.05% |
| snake_abs_exit_conv | +85 | +0.04% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs_exit | -186 | -0.09% |
| snake_abs | -415 | -0.20% |
| snake_abs_conv | -419 | -0.20% |
| snake_anaconda | -439 | -0.22% |
| unified | -928 | -0.41% |
| oracle | -1,304 | -0.61% |
| benchmark_smallcap | -1,323 | -0.66% |
| benchmark | -1,859 | -0.83% |
| intramonth | -2,147 | -1.00% |
| intraweek | -2,287 | -1.06% |

Average per day so far: unified Rs +648, benchmark Rs +597, intraweek Rs +344, intramonth Rs +330, oracle Rs +287, random_hold Rs +279, snake_abs_exit Rs +233, snake_abs_exit_conv Rs +186, snake_abs_conv Rs +149, snake_abs Rs +149, snake_viper_wild Rs +109, nifty_calls Rs +47, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, snake_viper_tick Rs -3, benchmark_smallcap Rs -12, snake_anaconda Rs -16, snake_nonews Rs -300, snake Rs -320, gold Rs -796

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.