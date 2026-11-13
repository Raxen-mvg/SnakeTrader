# Paper trading report

Updated 2026-11-13 13:04 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,977 | +9.99% | 0 | - | 236 |
| benchmark | 219,354 | +9.68% | 0 | - | 237 |
| snake_abs_exit | 216,929 | +8.46% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,665 | +8.33% | 2 | 50% | 345 |
| intraweek | 215,541 | +7.77% | 30 | 53% | 3,302 |
| oracle | 212,922 | +6.46% | 0 | - | 233 |
| snake_abs | 212,642 | +6.32% | 1 | 100% | 255 |
| snake_abs_conv | 212,473 | +6.24% | 1 | 100% | 255 |
| intramonth | 210,642 | +5.32% | 0 | - | 235 |
| random_hold | 207,197 | +3.60% | 10 | 70% | 733 |
| snake_viper_wild | 205,691 | +2.85% | 14 | 50% | 2,496 |
| snake_anaconda | 204,801 | +2.40% | 3 | 33% | 374 |
| benchmark_smallcap | 202,690 | +1.34% | 0 | - | 237 |
| snake_viper_tick | 202,173 | +1.09% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,012 | -7.99% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,617 (-4.19%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +883 | +0.41% |
| snake_viper_wild | +398 | +0.19% |
| snake_viper_tick | +391 | +0.19% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -193 | -0.09% |
| snake_abs_exit | -514 | -0.24% |
| benchmark_smallcap | -516 | -0.25% |
| unified | -720 | -0.33% |
| random_hold | -857 | -0.41% |
| intramonth | -951 | -0.45% |
| snake_anaconda | -1,126 | -0.55% |
| benchmark | -1,193 | -0.54% |
| gold | -1,299 | -0.70% |
| snake_abs_exit_conv | -2,009 | -0.92% |
| snake_abs_conv | -3,062 | -1.42% |
| snake_abs | -3,070 | -1.42% |

Average per day so far: unified Rs +605, benchmark Rs +586, snake_abs_exit Rs +564, snake_abs_exit_conv Rs +555, intraweek Rs +471, snake_abs_conv Rs +416, snake_abs Rs +408, oracle Rs +392, intramonth Rs +322, snake_viper_wild Rs +228, random_hold Rs +218, snake_anaconda Rs +171, snake_viper_tick Rs +99, benchmark_smallcap Rs +93, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -484

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.