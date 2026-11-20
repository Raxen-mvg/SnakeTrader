# Paper trading report

Updated 2026-11-20 14:09 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,387 | +13.19% | 0 | - | 236 |
| benchmark | 224,610 | +12.30% | 0 | - | 237 |
| intraweek | 215,875 | +7.94% | 35 | 54% | 3,851 |
| intramonth | 215,270 | +7.63% | 0 | - | 235 |
| oracle | 212,797 | +6.40% | 0 | - | 233 |
| random_hold | 210,497 | +5.25% | 11 | 73% | 979 |
| snake_abs_exit | 208,781 | +4.39% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,843 | +3.42% | 2 | 50% | 345 |
| snake_abs | 205,962 | +2.98% | 1 | 100% | 255 |
| snake_abs_conv | 205,832 | +2.92% | 1 | 100% | 255 |
| snake_viper_wild | 203,407 | +1.70% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,177 | +0.59% | 0 | - | 237 |
| snake_anaconda | 200,120 | +0.06% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 199,939 | -0.03% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,115 | -15.94% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,150 (-3.92%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,986 | +1.40% |
| benchmark | +2,234 | +1.00% |
| random_hold | +2,044 | +0.98% |
| unified | +1,772 | +0.79% |
| intramonth | +1,262 | +0.59% |
| oracle | +709 | +0.33% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -291 | -0.14% |
| snake_abs | -3,018 | -1.44% |
| snake_abs_conv | -3,028 | -1.45% |
| snake_anaconda | -3,343 | -1.64% |
| snake_viper_tick | -4,038 | -1.98% |
| snake_viper_wild | -4,116 | -1.98% |
| snake_abs_exit_conv | -4,221 | -2.00% |
| snake_abs_exit | -4,570 | -2.14% |
| gold | -6,658 | -3.81% |

Average per day so far: unified Rs +694, benchmark Rs +648, intraweek Rs +418, intramonth Rs +402, oracle Rs +337, random_hold Rs +276, snake_abs_exit Rs +251, snake_abs_exit_conv Rs +196, snake_abs_conv Rs +167, snake_abs Rs +166, snake_viper_wild Rs +114, nifty_calls Rs +48, benchmark_smallcap Rs +35, snake_anaconda Rs +4, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -2, snake_nonews Rs -308, snake Rs -328, gold Rs -839

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.