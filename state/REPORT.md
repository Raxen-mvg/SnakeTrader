# Paper trading report

Updated 2026-11-23 11:27 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,222 | +12.11% | 0 | - | 236 |
| benchmark | 223,669 | +11.83% | 0 | - | 237 |
| intraweek | 213,028 | +6.51% | 40 | 55% | 4,400 |
| intramonth | 212,433 | +6.22% | 0 | - | 235 |
| oracle | 211,639 | +5.82% | 0 | - | 233 |
| random_hold | 210,134 | +5.07% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,239 | +3.62% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,291 | +3.15% | 2 | 50% | 345 |
| snake_abs | 204,571 | +2.29% | 1 | 100% | 255 |
| snake_abs_conv | 204,407 | +2.20% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,556 | +0.78% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,663 | -0.17% | 0 | - | 237 |
| snake_anaconda | 198,377 | -0.81% | 3 | 33% | 374 |
| snake_viper_tick | 198,116 | -0.94% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,709 | -15.14% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,502 (-4.75%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,660 | +0.99% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -326 | -0.16% |
| random_hold | -625 | -0.30% |
| oracle | -840 | -0.40% |
| benchmark_smallcap | -1,244 | -0.62% |
| snake_viper_tick | -1,256 | -0.63% |
| snake_viper_wild | -1,273 | -0.63% |
| snake_abs_exit | -1,323 | -0.64% |
| snake_abs | -1,348 | -0.66% |
| snake_abs_conv | -1,375 | -0.67% |
| benchmark | -1,469 | -0.65% |
| snake_anaconda | -1,529 | -0.77% |
| unified | -1,960 | -0.87% |
| intramonth | -2,571 | -1.20% |
| intraweek | -2,684 | -1.24% |

Average per day so far: unified Rs +621, benchmark Rs +607, intraweek Rs +334, intramonth Rs +319, oracle Rs +298, random_hold Rs +260, snake_abs_exit Rs +201, snake_abs_exit_conv Rs +175, snake_abs Rs +124, snake_abs_conv Rs +122, snake_viper_wild Rs +50, nifty_calls Rs +47, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -10, snake_anaconda Rs -48, snake_viper_tick Rs -67, snake_nonews Rs -300, snake Rs -320, gold Rs -777

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.