# Paper trading report

Updated 2026-11-20 13:30 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,399 | +13.20% | 0 | - | 236 |
| benchmark | 224,204 | +12.10% | 0 | - | 237 |
| intramonth | 215,289 | +7.64% | 0 | - | 235 |
| intraweek | 215,216 | +7.61% | 35 | 54% | 3,851 |
| oracle | 212,596 | +6.30% | 0 | - | 233 |
| random_hold | 209,529 | +4.76% | 11 | 73% | 979 |
| snake_abs_exit | 209,441 | +4.72% | 2 | 50% | 345 |
| snake_abs_exit_conv | 207,426 | +3.71% | 2 | 50% | 345 |
| snake_abs | 206,562 | +3.28% | 1 | 100% | 255 |
| snake_abs_conv | 206,433 | +3.22% | 1 | 100% | 255 |
| snake_viper_wild | 204,079 | +2.04% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,042 | +0.52% | 0 | - | 237 |
| snake_anaconda | 200,708 | +0.35% | 3 | 33% | 374 |
| snake_viper_tick | 200,597 | +0.30% | 15 | 47% | 2,625 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,128 | -16.44% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,085 (-3.96%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,327 | +1.09% |
| benchmark | +1,828 | +0.82% |
| unified | +1,784 | +0.79% |
| intramonth | +1,281 | +0.60% |
| random_hold | +1,076 | +0.52% |
| oracle | +507 | +0.24% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -426 | -0.21% |
| snake_abs | -2,418 | -1.16% |
| snake_abs_conv | -2,427 | -1.16% |
| snake_anaconda | -2,756 | -1.35% |
| snake_viper_tick | -3,380 | -1.66% |
| snake_viper_wild | -3,444 | -1.66% |
| snake_abs_exit_conv | -3,639 | -1.72% |
| snake_abs_exit | -3,910 | -1.83% |
| gold | -7,645 | -4.37% |

Average per day so far: unified Rs +695, benchmark Rs +637, intramonth Rs +402, intraweek Rs +400, oracle Rs +331, snake_abs_exit Rs +270, random_hold Rs +251, snake_abs_exit_conv Rs +212, snake_abs_conv Rs +184, snake_abs Rs +182, snake_viper_wild Rs +136, nifty_calls Rs +48, benchmark_smallcap Rs +31, snake_viper_tick Rs +22, snake_anaconda Rs +21, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -865

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.