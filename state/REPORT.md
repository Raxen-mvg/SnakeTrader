# Paper trading report

Updated 2026-11-23 09:52 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,516 | +12.76% | 0 | - | 236 |
| benchmark | 223,959 | +11.98% | 0 | - | 237 |
| intraweek | 213,469 | +6.74% | 40 | 55% | 4,400 |
| intramonth | 213,348 | +6.67% | 0 | - | 235 |
| oracle | 211,748 | +5.87% | 0 | - | 233 |
| random_hold | 210,579 | +5.29% | 12 | 75% | 1,009 |
| snake_abs_exit | 208,278 | +4.14% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,596 | +3.30% | 2 | 50% | 345 |
| snake_abs | 205,868 | +2.93% | 1 | 100% | 255 |
| snake_abs_conv | 205,714 | +2.86% | 1 | 100% | 255 |
| snake_viper_wild | 203,789 | +1.90% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 200,312 | +0.16% | 15 | 47% | 2,625 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,999 | -0.00% | 0 | - | 237 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,475 | -0.26% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,397 | -15.30% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,161 (-4.42%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,348 | +0.80% |
| snake_viper_wild | +960 | +0.47% |
| snake_viper_tick | +940 | +0.47% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs_exit_conv | -21 | -0.01% |
| snake_abs | -52 | -0.03% |
| snake_abs_conv | -68 | -0.03% |
| random_hold | -180 | -0.09% |
| snake_abs_exit | -284 | -0.14% |
| snake_anaconda | -430 | -0.21% |
| unified | -666 | -0.29% |
| oracle | -731 | -0.34% |
| benchmark_smallcap | -908 | -0.45% |
| benchmark | -1,178 | -0.52% |
| intramonth | -1,656 | -0.77% |
| intraweek | -2,243 | -1.04% |

Average per day so far: unified Rs +654, benchmark Rs +614, intraweek Rs +345, intramonth Rs +342, oracle Rs +301, random_hold Rs +271, snake_abs_exit Rs +230, snake_abs_exit_conv Rs +183, snake_abs_conv Rs +159, snake_abs Rs +159, snake_viper_wild Rs +122, nifty_calls Rs +47, snake_viper_tick Rs +11, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, benchmark_smallcap Rs -0, snake_anaconda Rs -15, snake_nonews Rs -300, snake Rs -320, gold Rs -785

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.