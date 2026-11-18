# Paper trading report

Updated 2026-11-18 09:21 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,270 | +10.63% | 0 | - | 236 |
| benchmark | 221,030 | +10.52% | 0 | - | 237 |
| snake_abs_exit | 213,141 | +6.57% | 2 | 50% | 345 |
| intraweek | 212,824 | +6.41% | 35 | 54% | 3,851 |
| oracle | 212,383 | +6.19% | 0 | - | 233 |
| snake_abs_exit_conv | 211,496 | +5.75% | 2 | 50% | 345 |
| intramonth | 210,997 | +5.50% | 0 | - | 235 |
| snake_abs | 208,478 | +4.24% | 1 | 100% | 255 |
| snake_abs_conv | 208,332 | +4.17% | 1 | 100% | 255 |
| snake_viper_wild | 207,690 | +3.85% | 14 | 50% | 2,496 |
| random_hold | 207,626 | +3.81% | 10 | 70% | 733 |
| snake_viper_tick | 204,139 | +2.07% | 13 | 46% | 2,299 |
| snake_anaconda | 203,660 | +1.83% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,885 | +0.44% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,190 | -11.40% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,821 (-4.59%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +314 | +0.16% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -1 | -0.00% |
| snake_abs_exit_conv | -77 | -0.04% |
| snake_abs | -80 | -0.04% |
| snake_abs_conv | -87 | -0.04% |
| oracle | -104 | -0.05% |
| unified | -169 | -0.08% |
| snake_anaconda | -395 | -0.19% |
| intraweek | -498 | -0.23% |
| intramonth | -546 | -0.26% |
| benchmark | -574 | -0.26% |
| random_hold | -806 | -0.39% |
| snake_viper_tick | -1,697 | -0.82% |
| snake_viper_wild | -1,725 | -0.82% |
| gold | -3,535 | -1.96% |

Average per day so far: unified Rs +591, benchmark Rs +584, snake_abs_exit Rs +398, intraweek Rs +356, snake_abs_exit_conv Rs +348, oracle Rs +344, intramonth Rs +305, snake_viper_wild Rs +275, snake_abs_conv Rs +252, snake_abs Rs +249, random_hold Rs +212, snake_viper_tick Rs +166, snake_anaconda Rs +118, nifty_calls Rs +51, benchmark_smallcap Rs +28, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -326, snake Rs -347, gold Rs -634

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.