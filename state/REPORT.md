# Paper trading report

Updated 2026-11-23 14:34 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,020 | +12.01% | 0 | - | 236 |
| benchmark | 222,208 | +11.10% | 0 | - | 237 |
| intramonth | 212,086 | +6.04% | 0 | - | 235 |
| intraweek | 212,052 | +6.03% | 40 | 55% | 4,400 |
| oracle | 211,979 | +5.99% | 0 | - | 233 |
| random_hold | 208,660 | +4.33% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,044 | +3.52% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,319 | +3.16% | 2 | 50% | 345 |
| snake_abs | 204,990 | +2.50% | 1 | 100% | 255 |
| snake_abs_conv | 204,809 | +2.40% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,124 | +0.56% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,775 | -0.11% | 0 | - | 237 |
| snake_anaconda | 198,024 | -0.99% | 3 | 33% | 374 |
| snake_viper_tick | 197,693 | -1.15% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,479 | -15.26% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,154 (-4.92%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,430 | +0.85% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -297 | -0.14% |
| oracle | -499 | -0.23% |
| snake_abs | -930 | -0.45% |
| snake_abs_conv | -974 | -0.47% |
| benchmark_smallcap | -1,132 | -0.56% |
| snake_abs_exit | -1,518 | -0.73% |
| snake_viper_tick | -1,679 | -0.84% |
| snake_viper_wild | -1,705 | -0.84% |
| snake_anaconda | -1,882 | -0.94% |
| random_hold | -2,100 | -1.00% |
| unified | -2,161 | -0.96% |
| intramonth | -2,918 | -1.36% |
| benchmark | -2,930 | -1.30% |
| intraweek | -3,660 | -1.70% |

Average per day so far: unified Rs +616, benchmark Rs +569, intramonth Rs +310, intraweek Rs +309, oracle Rs +307, random_hold Rs +222, snake_abs_exit Rs +196, snake_abs_exit_conv Rs +176, snake_abs Rs +135, snake_abs_conv Rs +134, nifty_calls Rs +47, snake_viper_wild Rs +36, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -6, snake_anaconda Rs -58, snake_viper_tick Rs -82, snake_nonews Rs -300, snake Rs -320, gold Rs -783

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.