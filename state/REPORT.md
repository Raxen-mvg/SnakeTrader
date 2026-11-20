# Paper trading report

Updated 2026-11-20 12:07 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,191 | +13.10% | 0 | - | 236 |
| benchmark | 223,554 | +11.78% | 0 | - | 237 |
| intramonth | 215,149 | +7.57% | 0 | - | 235 |
| intraweek | 214,462 | +7.23% | 35 | 54% | 3,851 |
| oracle | 212,651 | +6.33% | 0 | - | 233 |
| snake_abs_exit | 209,851 | +4.93% | 2 | 50% | 345 |
| random_hold | 208,748 | +4.37% | 11 | 73% | 979 |
| snake_abs_exit_conv | 207,922 | +3.96% | 2 | 50% | 345 |
| snake_abs | 207,041 | +3.52% | 1 | 100% | 255 |
| snake_abs_conv | 206,905 | +3.45% | 1 | 100% | 255 |
| snake_viper_wild | 206,180 | +3.09% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,660 | +1.33% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,105 | +0.55% | 3 | 33% | 374 |
| benchmark_smallcap | 200,672 | +0.34% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,520 | -16.74% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,019 (-3.99%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,576 | +0.70% |
| intraweek | +1,573 | +0.74% |
| benchmark | +1,178 | +0.53% |
| intramonth | +1,141 | +0.53% |
| oracle | +562 | +0.27% |
| random_hold | +295 | +0.14% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -796 | -0.40% |
| snake_viper_tick | -1,317 | -0.65% |
| snake_viper_wild | -1,343 | -0.65% |
| snake_abs | -1,939 | -0.93% |
| snake_abs_conv | -1,955 | -0.94% |
| snake_anaconda | -2,358 | -1.16% |
| snake_abs_exit_conv | -3,142 | -1.49% |
| snake_abs_exit | -3,500 | -1.64% |
| gold | -8,253 | -4.72% |

Average per day so far: unified Rs +689, benchmark Rs +620, intramonth Rs +399, intraweek Rs +381, oracle Rs +333, snake_abs_exit Rs +281, random_hold Rs +230, snake_abs_exit_conv Rs +226, snake_viper_wild Rs +206, snake_abs_conv Rs +197, snake_abs Rs +196, snake_viper_tick Rs +99, nifty_calls Rs +48, snake_anaconda Rs +33, benchmark_smallcap Rs +20, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -881

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.