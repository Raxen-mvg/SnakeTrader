# Paper trading report

Updated 2026-11-20 10:44 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,323 | +12.66% | 0 | - | 236 |
| benchmark | 222,888 | +11.44% | 0 | - | 237 |
| intramonth | 214,229 | +7.12% | 0 | - | 235 |
| intraweek | 213,688 | +6.84% | 35 | 54% | 3,851 |
| oracle | 212,375 | +6.19% | 0 | - | 233 |
| snake_abs_exit | 210,447 | +5.22% | 2 | 50% | 345 |
| random_hold | 209,048 | +4.52% | 11 | 73% | 979 |
| snake_abs_exit_conv | 207,932 | +3.97% | 2 | 50% | 345 |
| snake_abs | 207,036 | +3.52% | 1 | 100% | 255 |
| snake_abs_conv | 206,895 | +3.45% | 1 | 100% | 255 |
| snake_viper_wild | 206,152 | +3.08% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,635 | +1.32% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,724 | +0.36% | 3 | 33% | 374 |
| benchmark_smallcap | 200,336 | +0.17% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,942 | -17.53% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,654 (-4.17%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +799 | +0.38% |
| unified | +708 | +0.32% |
| random_hold | +595 | +0.28% |
| benchmark | +513 | +0.23% |
| oracle | +287 | +0.14% |
| intramonth | +221 | +0.10% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -1,132 | -0.56% |
| snake_viper_tick | -1,342 | -0.66% |
| snake_viper_wild | -1,371 | -0.66% |
| snake_abs | -1,944 | -0.93% |
| snake_abs_conv | -1,965 | -0.94% |
| snake_anaconda | -2,739 | -1.35% |
| snake_abs_exit | -2,904 | -1.36% |
| snake_abs_exit_conv | -3,132 | -1.48% |
| gold | -9,831 | -5.62% |

Average per day so far: unified Rs +666, benchmark Rs +602, intramonth Rs +374, intraweek Rs +360, oracle Rs +326, snake_abs_exit Rs +298, random_hold Rs +238, snake_abs_exit_conv Rs +227, snake_viper_wild Rs +205, snake_abs_conv Rs +197, snake_abs Rs +195, snake_viper_tick Rs +98, nifty_calls Rs +48, snake_anaconda Rs +22, benchmark_smallcap Rs +10, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -923

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.