# Paper trading report

Updated 2026-11-20 13:06 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,286 | +13.14% | 0 | - | 236 |
| benchmark | 224,472 | +12.24% | 0 | - | 237 |
| intramonth | 215,254 | +7.63% | 0 | - | 235 |
| intraweek | 215,186 | +7.59% | 35 | 54% | 3,851 |
| oracle | 212,598 | +6.30% | 0 | - | 233 |
| random_hold | 209,545 | +4.77% | 11 | 73% | 979 |
| snake_abs_exit | 209,077 | +4.54% | 2 | 50% | 345 |
| snake_abs_exit_conv | 207,068 | +3.53% | 2 | 50% | 345 |
| snake_abs | 206,139 | +3.07% | 1 | 100% | 255 |
| snake_abs_conv | 206,006 | +3.00% | 1 | 100% | 255 |
| snake_viper_wild | 205,195 | +2.60% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,695 | +0.85% | 15 | 47% | 2,625 |
| benchmark_smallcap | 201,064 | +0.53% | 0 | - | 237 |
| snake_anaconda | 200,233 | +0.12% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,109 | -16.95% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,031 (-3.98%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,297 | +1.08% |
| benchmark | +2,096 | +0.94% |
| unified | +1,671 | +0.74% |
| intramonth | +1,246 | +0.58% |
| random_hold | +1,092 | +0.52% |
| oracle | +509 | +0.24% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -404 | -0.20% |
| snake_viper_tick | -2,282 | -1.12% |
| snake_viper_wild | -2,328 | -1.12% |
| snake_abs | -2,841 | -1.36% |
| snake_abs_conv | -2,854 | -1.37% |
| snake_anaconda | -3,231 | -1.59% |
| snake_abs_exit_conv | -3,996 | -1.89% |
| snake_abs_exit | -4,274 | -2.00% |
| gold | -8,664 | -4.96% |

Average per day so far: unified Rs +692, benchmark Rs +644, intramonth Rs +401, intraweek Rs +400, oracle Rs +332, snake_abs_exit Rs +259, random_hold Rs +251, snake_abs_exit_conv Rs +202, snake_viper_wild Rs +173, snake_abs_conv Rs +172, snake_abs Rs +171, snake_viper_tick Rs +63, nifty_calls Rs +48, benchmark_smallcap Rs +31, snake_anaconda Rs +7, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -892

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.