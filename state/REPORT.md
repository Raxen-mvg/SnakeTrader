# Paper trading report

Updated 2026-11-23 11:34 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,430 | +12.21% | 0 | - | 236 |
| benchmark | 223,585 | +11.79% | 0 | - | 237 |
| intraweek | 213,182 | +6.59% | 40 | 55% | 4,400 |
| intramonth | 212,517 | +6.26% | 0 | - | 235 |
| oracle | 211,714 | +5.86% | 0 | - | 233 |
| random_hold | 210,356 | +5.18% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,383 | +3.69% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,307 | +3.15% | 2 | 50% | 345 |
| snake_abs | 204,957 | +2.48% | 1 | 100% | 255 |
| snake_abs_conv | 204,789 | +2.39% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,494 | +0.75% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,753 | -0.12% | 0 | - | 237 |
| snake_anaconda | 198,422 | -0.79% | 3 | 33% | 374 |
| snake_viper_tick | 198,055 | -0.97% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,726 | -15.14% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,637 (-4.68%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,677 | +1.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -310 | -0.15% |
| random_hold | -403 | -0.19% |
| oracle | -765 | -0.36% |
| snake_abs | -963 | -0.47% |
| snake_abs_conv | -994 | -0.48% |
| benchmark_smallcap | -1,155 | -0.57% |
| snake_abs_exit | -1,179 | -0.56% |
| snake_viper_tick | -1,317 | -0.66% |
| snake_viper_wild | -1,335 | -0.66% |
| snake_anaconda | -1,483 | -0.74% |
| benchmark | -1,553 | -0.69% |
| unified | -1,751 | -0.77% |
| intramonth | -2,487 | -1.16% |
| intraweek | -2,531 | -1.17% |

Average per day so far: unified Rs +626, benchmark Rs +605, intraweek Rs +338, intramonth Rs +321, oracle Rs +300, random_hold Rs +266, snake_abs_exit Rs +205, snake_abs_exit_conv Rs +175, snake_abs Rs +134, snake_abs_conv Rs +133, snake_viper_wild Rs +48, nifty_calls Rs +47, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -7, snake_anaconda Rs -46, snake_viper_tick Rs -69, snake_nonews Rs -300, snake Rs -320, gold Rs -776

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.