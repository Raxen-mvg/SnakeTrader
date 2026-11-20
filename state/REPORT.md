# Paper trading report

Updated 2026-11-20 14:13 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,475 | +13.24% | 0 | - | 236 |
| benchmark | 224,610 | +12.30% | 0 | - | 237 |
| intraweek | 215,800 | +7.90% | 35 | 54% | 3,851 |
| intramonth | 215,327 | +7.66% | 0 | - | 235 |
| oracle | 212,767 | +6.38% | 0 | - | 233 |
| random_hold | 210,313 | +5.16% | 11 | 73% | 979 |
| snake_abs_exit | 208,975 | +4.49% | 2 | 50% | 345 |
| snake_abs_exit_conv | 207,046 | +3.52% | 2 | 50% | 345 |
| snake_abs | 206,165 | +3.08% | 1 | 100% | 255 |
| snake_abs_conv | 206,035 | +3.02% | 1 | 100% | 255 |
| snake_viper_wild | 203,551 | +1.77% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,109 | +0.56% | 0 | - | 237 |
| snake_anaconda | 200,325 | +0.16% | 3 | 33% | 374 |
| snake_viper_tick | 200,080 | +0.04% | 15 | 47% | 2,625 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,769 | -16.11% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,178 (-3.91%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,911 | +1.37% |
| benchmark | +2,234 | +1.00% |
| random_hold | +1,860 | +0.89% |
| unified | +1,859 | +0.83% |
| intramonth | +1,319 | +0.62% |
| oracle | +678 | +0.32% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -359 | -0.18% |
| snake_abs | -2,815 | -1.35% |
| snake_abs_conv | -2,825 | -1.35% |
| snake_anaconda | -3,138 | -1.54% |
| snake_viper_tick | -3,897 | -1.91% |
| snake_viper_wild | -3,972 | -1.91% |
| snake_abs_exit_conv | -4,018 | -1.90% |
| snake_abs_exit | -4,376 | -2.05% |
| gold | -7,003 | -4.01% |

Average per day so far: unified Rs +697, benchmark Rs +648, intraweek Rs +416, intramonth Rs +403, oracle Rs +336, random_hold Rs +271, snake_abs_exit Rs +256, snake_abs_exit_conv Rs +201, snake_abs_conv Rs +172, snake_abs Rs +171, snake_viper_wild Rs +118, nifty_calls Rs +48, benchmark_smallcap Rs +33, snake_anaconda Rs +10, snake_viper_tick Rs +3, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -848

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.