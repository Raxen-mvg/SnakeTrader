# Paper trading report

Updated 2026-11-23 10:35 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,685 | +12.34% | 0 | - | 236 |
| benchmark | 223,508 | +11.75% | 0 | - | 237 |
| intraweek | 212,962 | +6.48% | 40 | 55% | 4,400 |
| intramonth | 212,628 | +6.31% | 0 | - | 235 |
| oracle | 211,274 | +5.64% | 0 | - | 233 |
| random_hold | 209,846 | +4.92% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,586 | +3.79% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,636 | +3.32% | 2 | 50% | 345 |
| snake_abs | 204,880 | +2.44% | 1 | 100% | 255 |
| snake_abs_conv | 204,730 | +2.37% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,951 | +0.48% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,585 | -0.21% | 0 | - | 237 |
| snake_anaconda | 198,503 | -0.75% | 3 | 33% | 374 |
| snake_viper_tick | 197,523 | -1.24% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,430 | -15.29% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,532 (-4.73%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,381 | +0.82% |
| snake_abs_exit_conv | +20 | +0.01% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -913 | -0.43% |
| snake_abs_exit | -976 | -0.47% |
| snake_abs | -1,040 | -0.51% |
| snake_abs_conv | -1,053 | -0.51% |
| oracle | -1,205 | -0.57% |
| benchmark_smallcap | -1,323 | -0.66% |
| snake_anaconda | -1,403 | -0.70% |
| unified | -1,497 | -0.66% |
| benchmark | -1,629 | -0.72% |
| snake_viper_tick | -1,848 | -0.93% |
| snake_viper_wild | -1,878 | -0.93% |
| intramonth | -2,376 | -1.10% |
| intraweek | -2,751 | -1.27% |

Average per day so far: unified Rs +633, benchmark Rs +603, intraweek Rs +332, intramonth Rs +324, oracle Rs +289, random_hold Rs +252, snake_abs_exit Rs +211, snake_abs_exit_conv Rs +184, snake_abs Rs +132, snake_abs_conv Rs +131, nifty_calls Rs +47, snake_viper_wild Rs +31, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -12, snake_anaconda Rs -44, snake_viper_tick Rs -88, snake_nonews Rs -300, snake Rs -320, gold Rs -784

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.