# Paper trading report

Updated 2026-11-13 12:19 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,945 | +9.97% | 0 | - | 236 |
| benchmark | 218,926 | +9.46% | 0 | - | 237 |
| snake_abs_exit_conv | 216,218 | +8.11% | 2 | 50% | 345 |
| snake_abs_exit | 216,138 | +8.07% | 2 | 50% | 345 |
| intraweek | 215,402 | +7.70% | 30 | 53% | 3,302 |
| oracle | 212,900 | +6.45% | 0 | - | 233 |
| snake_abs | 212,471 | +6.24% | 1 | 100% | 255 |
| snake_abs_conv | 212,300 | +6.15% | 1 | 100% | 255 |
| intramonth | 210,632 | +5.32% | 0 | - | 235 |
| random_hold | 207,012 | +3.51% | 10 | 70% | 733 |
| snake_viper_wild | 205,497 | +2.75% | 14 | 50% | 2,496 |
| snake_anaconda | 204,677 | +2.34% | 3 | 33% | 374 |
| benchmark_smallcap | 202,387 | +1.19% | 0 | - | 237 |
| snake_viper_tick | 201,982 | +0.99% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,387 | -8.31% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,530 (-4.23%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +744 | +0.35% |
| snake_viper_wild | +205 | +0.10% |
| snake_viper_tick | +201 | +0.10% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -216 | -0.10% |
| unified | -752 | -0.34% |
| benchmark_smallcap | -818 | -0.40% |
| intramonth | -961 | -0.45% |
| random_hold | -1,041 | -0.50% |
| snake_anaconda | -1,250 | -0.61% |
| snake_abs_exit | -1,305 | -0.60% |
| benchmark | -1,622 | -0.73% |
| gold | -1,923 | -1.04% |
| snake_abs_exit_conv | -2,456 | -1.12% |
| snake_abs_conv | -3,235 | -1.50% |
| snake_abs | -3,240 | -1.50% |

Average per day so far: unified Rs +604, benchmark Rs +574, snake_abs_exit_conv Rs +541, snake_abs_exit Rs +538, intraweek Rs +467, snake_abs_conv Rs +410, snake_abs Rs +402, oracle Rs +391, intramonth Rs +322, snake_viper_wild Rs +220, random_hold Rs +212, snake_anaconda Rs +167, snake_viper_tick Rs +90, benchmark_smallcap Rs +82, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -503

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.