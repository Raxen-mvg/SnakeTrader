# Paper trading report

Updated 2026-11-23 14:25 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,123 | +12.06% | 0 | - | 236 |
| benchmark | 222,276 | +11.14% | 0 | - | 237 |
| intramonth | 212,236 | +6.12% | 0 | - | 235 |
| intraweek | 212,219 | +6.11% | 40 | 55% | 4,400 |
| oracle | 211,899 | +5.95% | 0 | - | 233 |
| random_hold | 208,791 | +4.40% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,275 | +3.64% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,536 | +3.27% | 2 | 50% | 345 |
| snake_abs | 205,004 | +2.50% | 1 | 100% | 255 |
| snake_abs_conv | 204,829 | +2.41% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,239 | +0.62% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,652 | -0.17% | 0 | - | 237 |
| snake_anaconda | 198,279 | -0.86% | 3 | 33% | 374 |
| snake_viper_tick | 197,805 | -1.10% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,528 | -15.24% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,235 (-4.88%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,480 | +0.88% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -80 | -0.04% |
| oracle | -580 | -0.27% |
| snake_abs | -916 | -0.45% |
| snake_abs_conv | -954 | -0.46% |
| benchmark_smallcap | -1,256 | -0.62% |
| snake_abs_exit | -1,287 | -0.62% |
| snake_viper_tick | -1,566 | -0.79% |
| snake_viper_wild | -1,590 | -0.78% |
| snake_anaconda | -1,627 | -0.81% |
| random_hold | -1,968 | -0.93% |
| unified | -2,058 | -0.91% |
| intramonth | -2,768 | -1.29% |
| benchmark | -2,861 | -1.27% |
| intraweek | -3,493 | -1.62% |

Average per day so far: unified Rs +619, benchmark Rs +571, intramonth Rs +314, intraweek Rs +313, oracle Rs +305, random_hold Rs +225, snake_abs_exit Rs +202, snake_abs_exit_conv Rs +182, snake_abs Rs +135, snake_abs_conv Rs +134, nifty_calls Rs +47, snake_viper_wild Rs +40, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -10, snake_anaconda Rs -51, snake_viper_tick Rs -78, snake_nonews Rs -300, snake Rs -320, gold Rs -781

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.