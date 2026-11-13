# Paper trading report

Updated 2026-11-13 12:55 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,061 | +10.03% | 0 | - | 236 |
| benchmark | 219,247 | +9.62% | 0 | - | 237 |
| snake_abs_exit | 216,876 | +8.44% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,695 | +8.35% | 2 | 50% | 345 |
| intraweek | 215,528 | +7.76% | 30 | 53% | 3,302 |
| oracle | 212,951 | +6.47% | 0 | - | 233 |
| snake_abs | 212,746 | +6.37% | 1 | 100% | 255 |
| snake_abs_conv | 212,576 | +6.29% | 1 | 100% | 255 |
| intramonth | 210,652 | +5.33% | 0 | - | 235 |
| random_hold | 207,150 | +3.58% | 10 | 70% | 733 |
| snake_viper_wild | 205,639 | +2.82% | 14 | 50% | 2,496 |
| snake_anaconda | 204,946 | +2.47% | 3 | 33% | 374 |
| benchmark_smallcap | 202,511 | +1.25% | 0 | - | 237 |
| snake_viper_tick | 202,121 | +1.06% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,486 | -8.26% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,630 (-4.19%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +870 | +0.41% |
| snake_viper_wild | +346 | +0.17% |
| snake_viper_tick | +340 | +0.17% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -165 | -0.08% |
| snake_abs_exit | -567 | -0.26% |
| unified | -636 | -0.29% |
| benchmark_smallcap | -695 | -0.34% |
| random_hold | -904 | -0.43% |
| intramonth | -941 | -0.45% |
| snake_anaconda | -981 | -0.48% |
| benchmark | -1,300 | -0.59% |
| gold | -1,825 | -0.98% |
| snake_abs_exit_conv | -1,979 | -0.91% |
| snake_abs_conv | -2,959 | -1.37% |
| snake_abs | -2,966 | -1.38% |

Average per day so far: unified Rs +608, benchmark Rs +583, snake_abs_exit Rs +563, snake_abs_exit_conv Rs +557, intraweek Rs +471, snake_abs_conv Rs +419, snake_abs Rs +411, oracle Rs +392, intramonth Rs +323, snake_viper_wild Rs +226, random_hold Rs +217, snake_anaconda Rs +177, snake_viper_tick Rs +96, benchmark_smallcap Rs +87, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -500

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.