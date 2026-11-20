# Paper trading report

Updated 2026-11-20 12:13 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,304 | +13.15% | 0 | - | 236 |
| benchmark | 223,661 | +11.83% | 0 | - | 237 |
| intramonth | 215,243 | +7.62% | 0 | - | 235 |
| intraweek | 214,679 | +7.34% | 35 | 54% | 3,851 |
| oracle | 212,752 | +6.38% | 0 | - | 233 |
| snake_abs_exit | 209,942 | +4.97% | 2 | 50% | 345 |
| random_hold | 208,823 | +4.41% | 11 | 73% | 979 |
| snake_abs_exit_conv | 208,003 | +4.00% | 2 | 50% | 345 |
| snake_abs | 207,106 | +3.55% | 1 | 100% | 255 |
| snake_abs_conv | 206,970 | +3.48% | 1 | 100% | 255 |
| snake_viper_wild | 206,184 | +3.09% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,665 | +1.33% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,169 | +0.58% | 3 | 33% | 374 |
| benchmark_smallcap | 200,762 | +0.38% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,372 | -16.81% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,111 (-3.94%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,790 | +0.84% |
| unified | +1,689 | +0.75% |
| benchmark | +1,285 | +0.58% |
| intramonth | +1,235 | +0.58% |
| oracle | +663 | +0.31% |
| random_hold | +370 | +0.18% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -706 | -0.35% |
| snake_viper_tick | -1,312 | -0.64% |
| snake_viper_wild | -1,338 | -0.65% |
| snake_abs | -1,874 | -0.90% |
| snake_abs_conv | -1,890 | -0.91% |
| snake_anaconda | -2,295 | -1.13% |
| snake_abs_exit_conv | -3,061 | -1.45% |
| snake_abs_exit | -3,409 | -1.60% |
| gold | -8,401 | -4.81% |

Average per day so far: unified Rs +692, benchmark Rs +623, intramonth Rs +401, intraweek Rs +386, oracle Rs +336, snake_abs_exit Rs +284, random_hold Rs +232, snake_abs_exit_conv Rs +229, snake_viper_wild Rs +206, snake_abs_conv Rs +199, snake_abs Rs +197, snake_viper_tick Rs +99, nifty_calls Rs +48, snake_anaconda Rs +35, benchmark_smallcap Rs +22, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -885

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.