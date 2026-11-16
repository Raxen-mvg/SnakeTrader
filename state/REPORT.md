# Paper trading report

Updated 2026-11-16 15:19 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,512 | +10.76% | 0 | - | 236 |
| benchmark | 220,035 | +10.02% | 0 | - | 237 |
| snake_abs_exit | 215,267 | +7.63% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,951 | +6.97% | 2 | 50% | 345 |
| oracle | 212,003 | +6.00% | 0 | - | 233 |
| intramonth | 211,696 | +5.85% | 0 | - | 235 |
| snake_abs | 211,264 | +5.63% | 1 | 100% | 255 |
| snake_abs_conv | 211,113 | +5.56% | 1 | 100% | 255 |
| intraweek | 210,947 | +5.47% | 35 | 54% | 3,851 |
| random_hold | 207,764 | +3.88% | 10 | 70% | 733 |
| snake_viper_wild | 206,035 | +3.02% | 14 | 50% | 2,496 |
| snake_anaconda | 205,810 | +2.90% | 3 | 33% | 374 |
| snake_viper_tick | 202,512 | +1.26% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,064 | +0.53% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,954 | -9.52% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,757 (-4.62%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +2,492 | +1.14% |
| intramonth | +1,639 | +0.78% |
| snake_viper_wild | +1,278 | +0.62% |
| snake_viper_tick | +1,258 | +0.62% |
| snake_anaconda | +918 | +0.45% |
| benchmark | +696 | +0.32% |
| random_hold | +538 | +0.26% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -1,095 | -0.51% |
| snake_abs_conv | -1,253 | -0.59% |
| snake_abs | -1,276 | -0.60% |
| snake_abs_exit | -1,718 | -0.79% |
| benchmark_smallcap | -1,805 | -0.89% |
| snake_abs_exit_conv | -2,430 | -1.12% |
| gold | -3,041 | -1.65% |
| intraweek | -5,198 | -2.40% |

Average per day so far: unified Rs +633, benchmark Rs +589, snake_abs_exit Rs +492, snake_abs_exit_conv Rs +450, snake_abs_conv Rs +358, oracle Rs +353, snake_abs Rs +352, intramonth Rs +344, intraweek Rs +322, snake_viper_wild Rs +232, random_hold Rs +228, snake_anaconda Rs +200, snake_viper_tick Rs +109, nifty_calls Rs +54, benchmark_smallcap Rs +35, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -347, snake Rs -368, gold Rs -560

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.