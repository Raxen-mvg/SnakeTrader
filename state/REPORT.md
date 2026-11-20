# Paper trading report

Updated 2026-11-20 10:24 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,544 | +12.77% | 0 | - | 236 |
| benchmark | 222,720 | +11.36% | 0 | - | 237 |
| intramonth | 214,442 | +7.22% | 0 | - | 235 |
| intraweek | 213,409 | +6.71% | 35 | 54% | 3,851 |
| oracle | 212,829 | +6.42% | 0 | - | 233 |
| snake_abs_exit | 210,298 | +5.15% | 2 | 50% | 345 |
| random_hold | 208,565 | +4.28% | 11 | 73% | 979 |
| snake_abs_exit_conv | 207,791 | +3.90% | 2 | 50% | 345 |
| snake_abs | 206,674 | +3.34% | 1 | 100% | 255 |
| snake_abs_conv | 206,539 | +3.27% | 1 | 100% | 255 |
| snake_viper_wild | 205,629 | +2.81% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,123 | +1.06% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,772 | +0.39% | 3 | 33% | 374 |
| benchmark_smallcap | 200,313 | +0.16% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,468 | -17.27% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,647 (-4.18%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +928 | +0.41% |
| oracle | +740 | +0.35% |
| intraweek | +520 | +0.24% |
| intramonth | +434 | +0.20% |
| benchmark | +344 | +0.15% |
| random_hold | +112 | +0.05% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -1,155 | -0.57% |
| snake_viper_tick | -1,854 | -0.91% |
| snake_viper_wild | -1,894 | -0.91% |
| snake_abs | -2,306 | -1.10% |
| snake_abs_conv | -2,321 | -1.11% |
| snake_anaconda | -2,691 | -1.32% |
| snake_abs_exit | -3,053 | -1.43% |
| snake_abs_exit_conv | -3,274 | -1.55% |
| gold | -9,305 | -5.32% |

Average per day so far: unified Rs +672, benchmark Rs +598, intramonth Rs +380, intraweek Rs +353, oracle Rs +338, snake_abs_exit Rs +294, random_hold Rs +225, snake_abs_exit_conv Rs +223, snake_viper_wild Rs +188, snake_abs_conv Rs +187, snake_abs Rs +185, snake_viper_tick Rs +79, nifty_calls Rs +48, snake_anaconda Rs +23, benchmark_smallcap Rs +9, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -909

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.