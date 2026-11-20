# Paper trading report

Updated 2026-11-20 12:55 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,892 | +12.95% | 0 | - | 236 |
| benchmark | 224,319 | +12.16% | 0 | - | 237 |
| intramonth | 214,947 | +7.47% | 0 | - | 235 |
| intraweek | 214,245 | +7.12% | 35 | 54% | 3,851 |
| oracle | 212,342 | +6.17% | 0 | - | 233 |
| snake_abs_exit | 209,120 | +4.56% | 2 | 50% | 345 |
| random_hold | 208,828 | +4.41% | 11 | 73% | 979 |
| snake_abs_exit_conv | 207,146 | +3.57% | 2 | 50% | 345 |
| snake_abs | 206,255 | +3.13% | 1 | 100% | 255 |
| snake_abs_conv | 206,121 | +3.06% | 1 | 100% | 255 |
| snake_viper_wild | 205,142 | +2.57% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,644 | +0.82% | 15 | 47% | 2,625 |
| benchmark_smallcap | 201,087 | +0.54% | 0 | - | 237 |
| snake_anaconda | 200,247 | +0.12% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,240 | -16.88% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,732 (-4.13%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,943 | +0.87% |
| intraweek | +1,356 | +0.64% |
| unified | +1,277 | +0.57% |
| intramonth | +939 | +0.44% |
| random_hold | +375 | +0.18% |
| oracle | +253 | +0.12% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -381 | -0.19% |
| snake_viper_tick | -2,333 | -1.14% |
| snake_viper_wild | -2,381 | -1.15% |
| snake_abs | -2,724 | -1.30% |
| snake_abs_conv | -2,739 | -1.31% |
| snake_anaconda | -3,217 | -1.58% |
| snake_abs_exit_conv | -3,919 | -1.86% |
| snake_abs_exit | -4,231 | -1.98% |
| gold | -8,532 | -4.88% |

Average per day so far: unified Rs +681, benchmark Rs +640, intramonth Rs +393, intraweek Rs +375, oracle Rs +325, snake_abs_exit Rs +261, random_hold Rs +232, snake_abs_exit_conv Rs +204, snake_abs_conv Rs +175, snake_abs Rs +174, snake_viper_wild Rs +171, snake_viper_tick Rs +61, nifty_calls Rs +48, benchmark_smallcap Rs +32, snake_anaconda Rs +7, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -888

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.