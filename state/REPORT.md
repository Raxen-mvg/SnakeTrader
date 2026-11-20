# Paper trading report

Updated 2026-11-20 12:59 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,126 | +13.06% | 0 | - | 236 |
| benchmark | 224,204 | +12.10% | 0 | - | 237 |
| intramonth | 215,096 | +7.55% | 0 | - | 235 |
| intraweek | 214,274 | +7.14% | 35 | 54% | 3,851 |
| oracle | 212,470 | +6.24% | 0 | - | 233 |
| snake_abs_exit | 209,039 | +4.52% | 2 | 50% | 345 |
| random_hold | 208,708 | +4.35% | 11 | 73% | 979 |
| snake_abs_exit_conv | 207,036 | +3.52% | 2 | 50% | 345 |
| snake_abs | 206,119 | +3.06% | 1 | 100% | 255 |
| snake_abs_conv | 205,986 | +2.99% | 1 | 100% | 255 |
| snake_viper_wild | 205,099 | +2.55% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,601 | +0.80% | 15 | 47% | 2,625 |
| benchmark_smallcap | 201,020 | +0.51% | 0 | - | 237 |
| snake_anaconda | 200,196 | +0.10% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,240 | -16.88% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,774 (-4.11%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,828 | +0.82% |
| unified | +1,511 | +0.67% |
| intraweek | +1,384 | +0.65% |
| intramonth | +1,088 | +0.51% |
| oracle | +381 | +0.18% |
| random_hold | +255 | +0.12% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -448 | -0.22% |
| snake_viper_tick | -2,376 | -1.17% |
| snake_viper_wild | -2,424 | -1.17% |
| snake_abs | -2,860 | -1.37% |
| snake_abs_conv | -2,874 | -1.38% |
| snake_anaconda | -3,268 | -1.61% |
| snake_abs_exit_conv | -4,029 | -1.91% |
| snake_abs_exit | -4,312 | -2.02% |
| gold | -8,532 | -4.88% |

Average per day so far: unified Rs +688, benchmark Rs +637, intramonth Rs +397, intraweek Rs +376, oracle Rs +328, snake_abs_exit Rs +258, random_hold Rs +229, snake_abs_exit_conv Rs +201, snake_abs_conv Rs +171, snake_abs Rs +170, snake_viper_wild Rs +170, snake_viper_tick Rs +59, nifty_calls Rs +48, benchmark_smallcap Rs +30, snake_anaconda Rs +6, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -888

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.