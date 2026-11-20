# Paper trading report

Updated 2026-11-20 09:35 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,002 | +12.50% | 0 | - | 236 |
| benchmark | 222,139 | +11.07% | 0 | - | 237 |
| intramonth | 214,360 | +7.18% | 0 | - | 235 |
| intraweek | 213,604 | +6.80% | 35 | 54% | 3,851 |
| oracle | 213,084 | +6.54% | 0 | - | 233 |
| snake_abs_exit | 211,118 | +5.56% | 2 | 50% | 345 |
| snake_abs_exit_conv | 208,931 | +4.46% | 2 | 50% | 345 |
| random_hold | 208,454 | +4.23% | 11 | 73% | 979 |
| snake_abs | 207,394 | +3.70% | 1 | 100% | 255 |
| snake_abs_conv | 207,257 | +3.63% | 1 | 100% | 255 |
| snake_viper_wild | 206,611 | +3.31% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,084 | +1.54% | 15 | 47% | 2,625 |
| snake_anaconda | 201,896 | +0.95% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,224 | +0.11% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,273 | -16.86% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,788 (-4.11%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| oracle | +995 | +0.47% |
| intraweek | +715 | +0.34% |
| unified | +387 | +0.17% |
| intramonth | +352 | +0.17% |
| random_hold | +1 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -237 | -0.11% |
| snake_viper_tick | -893 | -0.44% |
| snake_viper_wild | -912 | -0.44% |
| benchmark_smallcap | -1,244 | -0.62% |
| snake_anaconda | -1,568 | -0.77% |
| snake_abs | -1,586 | -0.76% |
| snake_abs_conv | -1,603 | -0.77% |
| snake_abs_exit_conv | -2,134 | -1.01% |
| snake_abs_exit | -2,233 | -1.05% |
| gold | -8,499 | -4.86% |

Average per day so far: unified Rs +658, benchmark Rs +583, intramonth Rs +378, intraweek Rs +358, oracle Rs +344, snake_abs_exit Rs +318, snake_abs_exit_conv Rs +255, random_hold Rs +222, snake_viper_wild Rs +220, snake_abs_conv Rs +207, snake_abs Rs +205, snake_viper_tick Rs +114, snake_anaconda Rs +57, nifty_calls Rs +48, benchmark_smallcap Rs +7, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -888

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.