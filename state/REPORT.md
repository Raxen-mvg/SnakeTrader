# Paper trading report

Updated 2026-11-13 09:34 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 219,316 | +9.66% | 0 | - | 237 |
| unified | 219,165 | +9.58% | 0 | - | 236 |
| snake_abs_exit_conv | 217,450 | +8.72% | 2 | 50% | 345 |
| snake_abs_exit | 216,824 | +8.41% | 2 | 50% | 345 |
| intraweek | 215,341 | +7.67% | 30 | 53% | 3,302 |
| snake_abs | 214,616 | +7.31% | 1 | 100% | 255 |
| snake_abs_conv | 214,441 | +7.22% | 1 | 100% | 255 |
| oracle | 213,044 | +6.52% | 0 | - | 233 |
| intramonth | 210,673 | +5.34% | 0 | - | 235 |
| random_hold | 207,570 | +3.79% | 10 | 70% | 733 |
| snake_viper_wild | 205,583 | +2.79% | 14 | 50% | 2,496 |
| snake_anaconda | 204,136 | +2.07% | 3 | 33% | 374 |
| benchmark_smallcap | 202,802 | +1.40% | 0 | - | 237 |
| snake_viper_tick | 202,068 | +1.03% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,620 | -7.69% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,597 (-4.20%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +683 | +0.32% |
| snake_viper_wild | +290 | +0.14% |
| snake_viper_tick | +286 | +0.14% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -71 | -0.03% |
| benchmark_smallcap | -404 | -0.20% |
| random_hold | -484 | -0.23% |
| snake_abs_exit | -619 | -0.28% |
| gold | -690 | -0.37% |
| intramonth | -920 | -0.43% |
| snake_abs_conv | -1,094 | -0.51% |
| snake_abs | -1,095 | -0.51% |
| snake_abs_exit_conv | -1,224 | -0.56% |
| benchmark | -1,232 | -0.56% |
| unified | -1,531 | -0.69% |
| snake_anaconda | -1,792 | -0.87% |

Average per day so far: benchmark Rs +585, snake_abs_exit_conv Rs +582, unified Rs +581, snake_abs_exit Rs +561, snake_abs_conv Rs +481, snake_abs Rs +471, intraweek Rs +465, oracle Rs +395, intramonth Rs +323, random_hold Rs +229, snake_viper_wild Rs +223, snake_anaconda Rs +148, benchmark_smallcap Rs +97, snake_viper_tick Rs +94, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -466

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.