# Paper trading report

Updated 2026-11-23 09:21 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,446 | +13.22% | 0 | - | 236 |
| benchmark | 225,344 | +12.67% | 0 | - | 237 |
| intraweek | 216,653 | +8.33% | 35 | 54% | 3,851 |
| intramonth | 214,966 | +7.48% | 0 | - | 235 |
| oracle | 212,969 | +6.48% | 0 | - | 233 |
| random_hold | 212,178 | +6.09% | 11 | 73% | 979 |
| snake_abs_exit | 208,851 | +4.43% | 2 | 50% | 345 |
| snake_abs_exit_conv | 207,343 | +3.67% | 2 | 50% | 345 |
| snake_abs | 206,678 | +3.34% | 1 | 100% | 255 |
| snake_abs_conv | 206,527 | +3.26% | 1 | 100% | 255 |
| snake_viper_wild | 204,111 | +2.06% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,818 | +0.41% | 0 | - | 237 |
| snake_viper_tick | 200,627 | +0.31% | 15 | 47% | 2,625 |
| snake_anaconda | 200,004 | +0.00% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,838 | -15.58% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,452 (-3.77%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| random_hold | +1,419 | +0.67% |
| snake_viper_wild | +1,282 | +0.63% |
| snake_viper_tick | +1,255 | +0.63% |
| intraweek | +941 | +0.44% |
| gold | +789 | +0.47% |
| snake_abs | +758 | +0.37% |
| snake_abs_conv | +744 | +0.36% |
| snake_abs_exit_conv | +726 | +0.35% |
| oracle | +490 | +0.23% |
| snake_abs_exit | +289 | +0.14% |
| unified | +264 | +0.12% |
| benchmark | +207 | +0.09% |
| snake_anaconda | +99 | +0.05% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intramonth | -38 | -0.02% |
| benchmark_smallcap | -90 | -0.04% |

Average per day so far: unified Rs +678, benchmark Rs +650, intraweek Rs +427, intramonth Rs +384, oracle Rs +333, random_hold Rs +312, snake_abs_exit Rs +246, snake_abs_exit_conv Rs +204, snake_abs_conv Rs +181, snake_abs Rs +180, snake_viper_wild Rs +133, nifty_calls Rs +47, benchmark_smallcap Rs +23, snake_viper_tick Rs +22, snake_anaconda Rs +0, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -300, snake Rs -320, gold Rs -799

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.