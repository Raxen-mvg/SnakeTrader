# Paper trading report

Updated 2026-11-23 15:04 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,103 | +12.05% | 0 | - | 236 |
| benchmark | 221,550 | +10.78% | 0 | - | 237 |
| oracle | 212,287 | +6.14% | 0 | - | 233 |
| intramonth | 211,858 | +5.93% | 0 | - | 235 |
| intraweek | 211,751 | +5.88% | 40 | 55% | 4,400 |
| random_hold | 208,545 | +4.27% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,326 | +3.66% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,708 | +3.35% | 2 | 50% | 345 |
| snake_abs | 205,441 | +2.72% | 1 | 100% | 255 |
| snake_abs_conv | 205,264 | +2.63% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,316 | +0.66% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,439 | -0.28% | 0 | - | 237 |
| snake_anaconda | 198,556 | -0.72% | 3 | 33% | 374 |
| snake_viper_tick | 197,881 | -1.06% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,430 | -15.29% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,169 (-4.92%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,381 | +0.82% |
| snake_abs_exit_conv | +92 | +0.04% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -192 | -0.09% |
| snake_abs | -479 | -0.23% |
| snake_abs_conv | -519 | -0.25% |
| snake_abs_exit | -1,236 | -0.59% |
| snake_anaconda | -1,350 | -0.68% |
| benchmark_smallcap | -1,469 | -0.73% |
| snake_viper_tick | -1,491 | -0.75% |
| snake_viper_wild | -1,513 | -0.75% |
| unified | -2,078 | -0.92% |
| random_hold | -2,215 | -1.05% |
| intramonth | -3,146 | -1.46% |
| benchmark | -3,588 | -1.59% |
| intraweek | -3,961 | -1.84% |

Average per day so far: unified Rs +618, benchmark Rs +553, oracle Rs +315, intramonth Rs +304, intraweek Rs +301, random_hold Rs +219, snake_abs_exit Rs +204, snake_abs_exit_conv Rs +186, snake_abs Rs +147, snake_abs_conv Rs +146, nifty_calls Rs +47, snake_viper_wild Rs +42, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -16, snake_anaconda Rs -42, snake_viper_tick Rs -76, snake_nonews Rs -300, snake Rs -320, gold Rs -784

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.