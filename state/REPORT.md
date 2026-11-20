# Paper trading report

Updated 2026-11-20 12:04 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,145 | +13.07% | 0 | - | 236 |
| benchmark | 223,722 | +11.86% | 0 | - | 237 |
| intramonth | 215,080 | +7.54% | 0 | - | 235 |
| intraweek | 214,454 | +7.23% | 35 | 54% | 3,851 |
| oracle | 212,623 | +6.31% | 0 | - | 233 |
| snake_abs_exit | 209,872 | +4.94% | 2 | 50% | 345 |
| random_hold | 208,965 | +4.48% | 11 | 73% | 979 |
| snake_abs_exit_conv | 207,899 | +3.95% | 2 | 50% | 345 |
| snake_abs | 206,997 | +3.50% | 1 | 100% | 255 |
| snake_abs_conv | 206,861 | +3.43% | 1 | 100% | 255 |
| snake_viper_wild | 206,112 | +3.06% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,594 | +1.30% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,060 | +0.53% | 3 | 33% | 374 |
| benchmark_smallcap | 200,751 | +0.38% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,684 | -16.66% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,017 (-3.99%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,564 | +0.73% |
| unified | +1,530 | +0.68% |
| benchmark | +1,346 | +0.60% |
| intramonth | +1,072 | +0.50% |
| oracle | +535 | +0.25% |
| random_hold | +512 | +0.25% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -717 | -0.36% |
| snake_viper_tick | -1,383 | -0.68% |
| snake_viper_wild | -1,410 | -0.68% |
| snake_abs | -1,983 | -0.95% |
| snake_abs_conv | -1,999 | -0.96% |
| snake_anaconda | -2,403 | -1.18% |
| snake_abs_exit_conv | -3,166 | -1.50% |
| snake_abs_exit | -3,479 | -1.63% |
| gold | -8,088 | -4.63% |

Average per day so far: unified Rs +688, benchmark Rs +624, intramonth Rs +397, intraweek Rs +380, oracle Rs +332, snake_abs_exit Rs +282, random_hold Rs +236, snake_abs_exit_conv Rs +226, snake_viper_wild Rs +204, snake_abs_conv Rs +196, snake_abs Rs +194, snake_viper_tick Rs +96, nifty_calls Rs +48, snake_anaconda Rs +32, benchmark_smallcap Rs +22, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -877

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.