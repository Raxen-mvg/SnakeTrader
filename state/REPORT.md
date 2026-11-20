# Paper trading report

Updated 2026-11-20 14:20 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,482 | +13.24% | 0 | - | 236 |
| benchmark | 224,724 | +12.36% | 0 | - | 237 |
| intraweek | 215,826 | +7.91% | 35 | 54% | 3,851 |
| intramonth | 215,350 | +7.67% | 0 | - | 235 |
| oracle | 213,121 | +6.56% | 0 | - | 233 |
| random_hold | 210,310 | +5.16% | 11 | 73% | 979 |
| snake_abs_exit | 209,031 | +4.51% | 2 | 50% | 345 |
| snake_abs_exit_conv | 207,168 | +3.58% | 2 | 50% | 345 |
| snake_abs | 206,299 | +3.15% | 1 | 100% | 255 |
| snake_abs_conv | 206,170 | +3.08% | 1 | 100% | 255 |
| snake_viper_wild | 203,549 | +1.77% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,008 | +0.50% | 0 | - | 237 |
| snake_anaconda | 200,645 | +0.32% | 3 | 33% | 374 |
| snake_viper_tick | 200,077 | +0.04% | 15 | 47% | 2,625 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,457 | -16.27% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,255 (-3.87%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,936 | +1.38% |
| benchmark | +2,349 | +1.06% |
| unified | +1,867 | +0.83% |
| random_hold | +1,857 | +0.89% |
| intramonth | +1,342 | +0.63% |
| oracle | +1,032 | +0.49% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -460 | -0.23% |
| snake_abs | -2,681 | -1.28% |
| snake_abs_conv | -2,690 | -1.29% |
| snake_anaconda | -2,819 | -1.39% |
| snake_abs_exit_conv | -3,897 | -1.85% |
| snake_viper_tick | -3,900 | -1.91% |
| snake_viper_wild | -3,974 | -1.92% |
| snake_abs_exit | -4,321 | -2.02% |
| gold | -7,316 | -4.19% |

Average per day so far: unified Rs +697, benchmark Rs +651, intraweek Rs +416, intramonth Rs +404, oracle Rs +345, random_hold Rs +271, snake_abs_exit Rs +258, snake_abs_exit_conv Rs +205, snake_abs_conv Rs +176, snake_abs Rs +175, snake_viper_wild Rs +118, nifty_calls Rs +48, benchmark_smallcap Rs +30, snake_anaconda Rs +20, snake_viper_tick Rs +3, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -856

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.