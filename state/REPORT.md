# Paper trading report

Updated 2026-11-23 12:02 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,383 | +12.19% | 0 | - | 236 |
| benchmark | 222,858 | +11.43% | 0 | - | 237 |
| intraweek | 213,186 | +6.59% | 40 | 55% | 4,400 |
| intramonth | 212,395 | +6.20% | 0 | - | 235 |
| oracle | 211,689 | +5.84% | 0 | - | 233 |
| random_hold | 209,956 | +4.98% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,159 | +3.58% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,095 | +3.05% | 2 | 50% | 345 |
| snake_abs | 204,803 | +2.40% | 1 | 100% | 255 |
| snake_abs_conv | 204,634 | +2.32% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,331 | +0.67% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,517 | -0.24% | 0 | - | 237 |
| snake_anaconda | 198,118 | -0.94% | 3 | 33% | 374 |
| snake_viper_tick | 197,895 | -1.05% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,874 | -15.06% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,509 (-4.75%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,825 | +1.09% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -522 | -0.25% |
| oracle | -790 | -0.37% |
| random_hold | -803 | -0.38% |
| snake_abs | -1,117 | -0.54% |
| snake_abs_conv | -1,149 | -0.56% |
| benchmark_smallcap | -1,390 | -0.69% |
| snake_abs_exit | -1,403 | -0.67% |
| snake_viper_tick | -1,477 | -0.74% |
| snake_viper_wild | -1,499 | -0.74% |
| snake_anaconda | -1,787 | -0.89% |
| unified | -1,799 | -0.80% |
| benchmark | -2,280 | -1.01% |
| intraweek | -2,526 | -1.17% |
| intramonth | -2,610 | -1.21% |

Average per day so far: unified Rs +625, benchmark Rs +586, intraweek Rs +338, intramonth Rs +318, oracle Rs +300, random_hold Rs +255, snake_abs_exit Rs +199, snake_abs_exit_conv Rs +169, snake_abs Rs +130, snake_abs_conv Rs +129, nifty_calls Rs +47, snake_viper_wild Rs +43, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -14, snake_anaconda Rs -55, snake_viper_tick Rs -75, snake_nonews Rs -300, snake Rs -320, gold Rs -772

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.