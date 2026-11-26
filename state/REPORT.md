# Paper trading report

Updated 2026-11-26 14:12 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,260 | +12.63% | 0 | - | 237 |
| unified | 223,287 | +11.64% | 0 | - | 236 |
| oracle | 213,121 | +6.56% | 0 | - | 233 |
| intramonth | 210,532 | +5.27% | 0 | - | 235 |
| random_hold | 209,319 | +4.66% | 13 | 69% | 1,037 |
| intraweek | 207,885 | +3.94% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,381 | +0.19% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit | 199,890 | -0.06% | 2 | 50% | 345 |
| snake_abs_exit_conv | 199,315 | -0.34% | 2 | 50% | 345 |
| snake_abs | 197,635 | -1.18% | 1 | 100% | 255 |
| snake_abs_conv | 197,427 | -1.29% | 1 | 100% | 255 |
| snake_viper_wild | 192,345 | -3.83% | 16 | 50% | 2,827 |
| snake_anaconda | 191,388 | -4.31% | 3 | 33% | 374 |
| snake_viper_tick | 189,077 | -5.46% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,388 | -16.81% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,582 (-5.71%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,792 | +1.09% |
| benchmark_smallcap | +1,569 | +0.79% |
| intraweek | +1,142 | +0.55% |
| benchmark | +237 | +0.10% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -174 | -0.08% |
| oracle | -674 | -0.32% |
| unified | -813 | -0.36% |
| intramonth | -1,161 | -0.55% |
| snake_abs_exit | -2,366 | -1.17% |
| snake_abs | -2,515 | -1.26% |
| snake_abs_conv | -2,545 | -1.27% |
| snake_abs_exit_conv | -2,661 | -1.32% |
| snake_anaconda | -3,165 | -1.63% |
| snake_viper_tick | -5,099 | -2.63% |
| snake_viper_wild | -5,199 | -2.63% |

Average per day so far: benchmark Rs +616, unified Rs +568, oracle Rs +320, intramonth Rs +257, random_hold Rs +227, intraweek Rs +192, nifty_calls Rs +45, benchmark_smallcap Rs +10, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_abs_exit Rs -3, snake_abs_exit_conv Rs -18, snake_abs Rs -61, snake_abs_conv Rs -68, snake_viper_wild Rs -232, snake_anaconda Rs -239, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -364, gold Rs -820

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.