# Paper trading report

Updated 2026-11-16 15:30 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,438 | +10.72% | 0 | - | 236 |
| benchmark | 220,081 | +10.04% | 0 | - | 237 |
| snake_abs_exit | 214,409 | +7.21% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,217 | +6.61% | 2 | 50% | 345 |
| oracle | 212,023 | +6.01% | 0 | - | 233 |
| intramonth | 211,619 | +5.81% | 0 | - | 235 |
| intraweek | 211,266 | +5.63% | 35 | 54% | 3,851 |
| snake_abs | 210,134 | +5.07% | 1 | 100% | 255 |
| snake_abs_conv | 209,990 | +5.00% | 1 | 100% | 255 |
| random_hold | 207,793 | +3.90% | 10 | 70% | 733 |
| snake_viper_wild | 206,144 | +3.07% | 14 | 50% | 2,496 |
| snake_anaconda | 205,103 | +2.55% | 3 | 33% | 374 |
| snake_viper_tick | 202,620 | +1.31% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,829 | +0.41% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,954 | -9.52% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,783 (-4.61%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +2,417 | +1.10% |
| intramonth | +1,562 | +0.74% |
| snake_viper_wild | +1,387 | +0.68% |
| snake_viper_tick | +1,365 | +0.68% |
| benchmark | +742 | +0.34% |
| random_hold | +567 | +0.27% |
| snake_anaconda | +211 | +0.10% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -1,075 | -0.50% |
| benchmark_smallcap | -2,040 | -1.01% |
| snake_abs_conv | -2,377 | -1.12% |
| snake_abs | -2,406 | -1.13% |
| snake_abs_exit | -2,576 | -1.19% |
| gold | -3,041 | -1.65% |
| snake_abs_exit_conv | -3,164 | -1.46% |
| intraweek | -4,879 | -2.26% |

Average per day so far: unified Rs +631, benchmark Rs +591, snake_abs_exit Rs +465, snake_abs_exit_conv Rs +426, oracle Rs +354, intramonth Rs +342, intraweek Rs +331, snake_abs_conv Rs +322, snake_abs Rs +317, snake_viper_wild Rs +236, random_hold Rs +229, snake_anaconda Rs +176, snake_viper_tick Rs +114, nifty_calls Rs +54, benchmark_smallcap Rs +28, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -347, snake Rs -368, gold Rs -560

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.