# Paper trading report

Updated 2026-11-20 12:01 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,117 | +13.06% | 0 | - | 236 |
| benchmark | 223,500 | +11.75% | 0 | - | 237 |
| intramonth | 215,085 | +7.54% | 0 | - | 235 |
| intraweek | 214,303 | +7.15% | 35 | 54% | 3,851 |
| oracle | 212,607 | +6.30% | 0 | - | 233 |
| snake_abs_exit | 209,966 | +4.98% | 2 | 50% | 345 |
| random_hold | 208,957 | +4.48% | 11 | 73% | 979 |
| snake_abs_exit_conv | 207,967 | +3.98% | 2 | 50% | 345 |
| snake_abs | 207,030 | +3.52% | 1 | 100% | 255 |
| snake_abs_conv | 206,895 | +3.45% | 1 | 100% | 255 |
| snake_viper_wild | 206,127 | +3.06% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,608 | +1.30% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,093 | +0.55% | 3 | 33% | 374 |
| benchmark_smallcap | 200,762 | +0.38% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,783 | -16.61% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,005 (-4.00%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,502 | +0.67% |
| intraweek | +1,414 | +0.66% |
| benchmark | +1,125 | +0.51% |
| intramonth | +1,077 | +0.50% |
| oracle | +518 | +0.24% |
| random_hold | +504 | +0.24% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -706 | -0.35% |
| snake_viper_tick | -1,369 | -0.67% |
| snake_viper_wild | -1,396 | -0.67% |
| snake_abs | -1,949 | -0.93% |
| snake_abs_conv | -1,965 | -0.94% |
| snake_anaconda | -2,370 | -1.17% |
| snake_abs_exit_conv | -3,098 | -1.47% |
| snake_abs_exit | -3,385 | -1.59% |
| gold | -7,990 | -4.57% |

Average per day so far: unified Rs +687, benchmark Rs +618, intramonth Rs +397, intraweek Rs +376, oracle Rs +332, snake_abs_exit Rs +285, random_hold Rs +236, snake_abs_exit_conv Rs +228, snake_viper_wild Rs +204, snake_abs_conv Rs +197, snake_abs Rs +195, snake_viper_tick Rs +97, nifty_calls Rs +48, snake_anaconda Rs +33, benchmark_smallcap Rs +22, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -874

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.