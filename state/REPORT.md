# Paper trading report

Updated 2026-11-13 15:22 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 219,362 | +9.68% | 0 | - | 237 |
| unified | 218,914 | +9.46% | 0 | - | 236 |
| snake_abs_exit | 217,099 | +8.55% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,587 | +8.29% | 2 | 50% | 345 |
| intraweek | 216,221 | +8.11% | 30 | 53% | 3,302 |
| oracle | 213,121 | +6.56% | 0 | - | 233 |
| snake_abs | 212,788 | +6.39% | 1 | 100% | 255 |
| snake_abs_conv | 212,615 | +6.31% | 1 | 100% | 255 |
| intramonth | 210,003 | +5.00% | 0 | - | 235 |
| random_hold | 207,277 | +3.64% | 10 | 70% | 733 |
| snake_anaconda | 205,102 | +2.55% | 3 | 33% | 374 |
| snake_viper_wild | 204,813 | +2.41% | 14 | 50% | 2,496 |
| benchmark_smallcap | 202,511 | +1.25% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,309 | +0.66% | 13 | 46% | 2,299 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,963 | -8.02% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,575 (-4.21%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,563 | +0.73% |
| oracle | +6 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_abs_exit | -343 | -0.16% |
| snake_viper_tick | -472 | -0.23% |
| snake_viper_wild | -480 | -0.23% |
| benchmark_smallcap | -695 | -0.34% |
| random_hold | -776 | -0.37% |
| snake_anaconda | -825 | -0.40% |
| benchmark | -1,186 | -0.54% |
| gold | -1,348 | -0.73% |
| intramonth | -1,591 | -0.75% |
| unified | -1,783 | -0.81% |
| snake_abs_exit_conv | -2,087 | -0.95% |
| snake_abs_conv | -2,920 | -1.35% |
| snake_abs | -2,924 | -1.35% |

Average per day so far: benchmark Rs +587, unified Rs +573, snake_abs_exit Rs +570, snake_abs_exit_conv Rs +553, intraweek Rs +492, snake_abs_conv Rs +421, snake_abs Rs +413, oracle Rs +398, intramonth Rs +303, random_hold Rs +221, snake_viper_wild Rs +193, snake_anaconda Rs +182, benchmark_smallcap Rs +87, snake_viper_tick Rs +60, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -486

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.