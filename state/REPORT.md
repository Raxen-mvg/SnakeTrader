# Paper trading report

Updated 2026-11-25 09:49 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,476 | +12.74% | 0 | - | 236 |
| benchmark | 224,357 | +12.18% | 0 | - | 237 |
| intramonth | 212,947 | +6.47% | 0 | - | 235 |
| oracle | 212,891 | +6.45% | 0 | - | 233 |
| intraweek | 210,697 | +5.35% | 40 | 55% | 4,400 |
| random_hold | 209,895 | +4.95% | 12 | 75% | 1,009 |
| snake_abs_exit | 202,784 | +1.39% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,209 | +1.10% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,463 | +0.73% | 1 | 100% | 255 |
| snake_abs_conv | 201,273 | +0.64% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,461 | -0.27% | 0 | - | 237 |
| snake_viper_wild | 199,262 | -0.37% | 16 | 50% | 2,827 |
| snake_viper_tick | 195,869 | -2.06% | 15 | 47% | 2,625 |
| snake_anaconda | 194,481 | -2.76% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,797 | -17.10% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,928 (-5.04%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,884 | +1.30% |
| random_hold | +1,468 | +0.70% |
| unified | +1,191 | +0.53% |
| oracle | +549 | +0.26% |
| benchmark_smallcap | +482 | +0.24% |
| intramonth | +196 | +0.09% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -922 | -0.44% |
| snake_viper_tick | -1,824 | -0.92% |
| snake_viper_wild | -1,862 | -0.93% |
| gold | -3,633 | -2.14% |
| snake_abs | -3,998 | -1.95% |
| snake_abs_conv | -4,030 | -1.96% |
| snake_anaconda | -4,223 | -2.12% |
| snake_abs_exit | -4,711 | -2.27% |
| snake_abs_exit_conv | -4,837 | -2.34% |

Average per day so far: unified Rs +637, benchmark Rs +609, intramonth Rs +324, oracle Rs +322, intraweek Rs +267, random_hold Rs +247, snake_abs_exit Rs +75, snake_abs_exit_conv Rs +60, nifty_calls Rs +46, snake_abs Rs +38, snake_abs_conv Rs +34, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -15, snake_viper_wild Rs -23, snake_viper_tick Rs -142, snake_anaconda Rs -158, snake_nonews Rs -292, snake Rs -311, gold Rs -855

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.