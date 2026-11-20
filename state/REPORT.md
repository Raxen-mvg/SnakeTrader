# Paper trading report

Updated 2026-11-20 10:37 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,415 | +12.71% | 0 | - | 236 |
| benchmark | 222,904 | +11.45% | 0 | - | 237 |
| intramonth | 214,363 | +7.18% | 0 | - | 235 |
| intraweek | 213,692 | +6.85% | 35 | 54% | 3,851 |
| oracle | 212,642 | +6.32% | 0 | - | 233 |
| snake_abs_exit | 210,283 | +5.14% | 2 | 50% | 345 |
| random_hold | 209,076 | +4.54% | 11 | 73% | 979 |
| snake_abs_exit_conv | 207,809 | +3.90% | 2 | 50% | 345 |
| snake_abs | 206,797 | +3.40% | 1 | 100% | 255 |
| snake_abs_conv | 206,659 | +3.33% | 1 | 100% | 255 |
| snake_viper_wild | 205,792 | +2.90% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,283 | +1.14% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,732 | +0.37% | 3 | 33% | 374 |
| benchmark_smallcap | 200,336 | +0.17% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,172 | -17.41% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,688 (-4.16%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +803 | +0.38% |
| unified | +800 | +0.36% |
| random_hold | +623 | +0.30% |
| oracle | +553 | +0.26% |
| benchmark | +528 | +0.24% |
| intramonth | +355 | +0.17% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -1,132 | -0.56% |
| snake_viper_tick | -1,694 | -0.83% |
| snake_viper_wild | -1,731 | -0.83% |
| snake_abs | -2,183 | -1.04% |
| snake_abs_conv | -2,201 | -1.05% |
| snake_anaconda | -2,731 | -1.34% |
| snake_abs_exit | -3,068 | -1.44% |
| snake_abs_exit_conv | -3,256 | -1.54% |
| gold | -9,601 | -5.49% |

Average per day so far: unified Rs +669, benchmark Rs +603, intramonth Rs +378, intraweek Rs +360, oracle Rs +333, snake_abs_exit Rs +294, random_hold Rs +239, snake_abs_exit_conv Rs +223, snake_viper_wild Rs +193, snake_abs_conv Rs +190, snake_abs Rs +189, snake_viper_tick Rs +85, nifty_calls Rs +48, snake_anaconda Rs +22, benchmark_smallcap Rs +10, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -917

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.