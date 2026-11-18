# Paper trading report

Updated 2026-11-18 13:41 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,926 | +11.46% | 0 | - | 236 |
| benchmark | 219,660 | +9.83% | 0 | - | 237 |
| intramonth | 212,751 | +6.38% | 0 | - | 235 |
| snake_abs_exit | 212,187 | +6.09% | 2 | 50% | 345 |
| oracle | 212,133 | +6.07% | 0 | - | 233 |
| intraweek | 212,123 | +6.06% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 210,435 | +5.22% | 2 | 50% | 345 |
| snake_abs | 207,471 | +3.74% | 1 | 100% | 255 |
| snake_abs_conv | 207,333 | +3.67% | 1 | 100% | 255 |
| random_hold | 207,085 | +3.54% | 10 | 70% | 733 |
| snake_viper_wild | 206,497 | +3.25% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,972 | +1.49% | 15 | 47% | 2,625 |
| snake_anaconda | 202,605 | +1.30% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,136 | -0.43% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,206 | -11.40% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,092 (-4.45%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,487 | +0.67% |
| intramonth | +1,209 | +0.57% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| oracle | -354 | -0.17% |
| snake_abs_exit | -954 | -0.45% |
| snake_abs_conv | -1,087 | -0.52% |
| snake_abs | -1,087 | -0.52% |
| snake_abs_exit_conv | -1,139 | -0.54% |
| intraweek | -1,199 | -0.56% |
| random_hold | -1,348 | -0.65% |
| benchmark_smallcap | -1,435 | -0.71% |
| snake_anaconda | -1,450 | -0.71% |
| benchmark | -1,943 | -0.88% |
| snake_viper_tick | -2,864 | -1.39% |
| snake_viper_wild | -2,918 | -1.39% |
| gold | -3,518 | -1.95% |

Average per day so far: unified Rs +637, benchmark Rs +546, snake_abs_exit Rs +369, intramonth Rs +354, oracle Rs +337, intraweek Rs +337, snake_abs_exit_conv Rs +316, snake_viper_wild Rs +232, snake_abs_conv Rs +222, snake_abs Rs +220, random_hold Rs +197, snake_viper_tick Rs +119, snake_anaconda Rs +84, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -27, snake_nonews Rs -326, snake Rs -347, gold Rs -633

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.