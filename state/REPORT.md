# Paper trading report

Updated 2026-11-13 11:46 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,223 | +10.11% | 0 | - | 236 |
| benchmark | 219,369 | +9.69% | 0 | - | 237 |
| snake_abs_exit_conv | 216,365 | +8.18% | 2 | 50% | 345 |
| snake_abs_exit | 216,313 | +8.16% | 2 | 50% | 345 |
| intraweek | 215,977 | +7.99% | 30 | 53% | 3,302 |
| oracle | 213,147 | +6.57% | 0 | - | 233 |
| snake_abs | 212,515 | +6.26% | 1 | 100% | 255 |
| snake_abs_conv | 212,343 | +6.17% | 1 | 100% | 255 |
| intramonth | 210,917 | +5.46% | 0 | - | 235 |
| random_hold | 207,183 | +3.59% | 10 | 70% | 733 |
| snake_viper_wild | 205,789 | +2.89% | 14 | 50% | 2,496 |
| snake_anaconda | 204,613 | +2.31% | 3 | 33% | 374 |
| benchmark_smallcap | 202,959 | +1.48% | 0 | - | 237 |
| snake_viper_tick | 202,269 | +1.13% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,831 | -8.08% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,834 (-4.08%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,319 | +0.61% |
| snake_viper_wild | +496 | +0.24% |
| snake_viper_tick | +487 | +0.24% |
| oracle | +31 | +0.01% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| benchmark_smallcap | -247 | -0.12% |
| unified | -473 | -0.21% |
| intramonth | -676 | -0.32% |
| random_hold | -871 | -0.42% |
| snake_abs_exit | -1,130 | -0.52% |
| benchmark | -1,178 | -0.53% |
| snake_anaconda | -1,314 | -0.64% |
| gold | -1,480 | -0.80% |
| snake_abs_exit_conv | -2,309 | -1.06% |
| snake_abs_conv | -3,192 | -1.48% |
| snake_abs | -3,196 | -1.48% |

Average per day so far: unified Rs +613, benchmark Rs +587, snake_abs_exit_conv Rs +546, snake_abs_exit Rs +544, intraweek Rs +484, snake_abs_conv Rs +411, snake_abs Rs +404, oracle Rs +398, intramonth Rs +331, snake_viper_wild Rs +232, random_hold Rs +218, snake_anaconda Rs +165, snake_viper_tick Rs +103, benchmark_smallcap Rs +102, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -490

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.