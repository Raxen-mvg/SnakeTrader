# Paper trading report

Updated 2026-11-23 14:16 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,969 | +11.98% | 0 | - | 236 |
| benchmark | 221,986 | +10.99% | 0 | - | 237 |
| intraweek | 212,173 | +6.09% | 40 | 55% | 4,400 |
| intramonth | 212,057 | +6.03% | 0 | - | 235 |
| oracle | 211,610 | +5.80% | 0 | - | 233 |
| random_hold | 208,932 | +4.47% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,943 | +3.47% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,249 | +3.12% | 2 | 50% | 345 |
| snake_abs | 204,571 | +2.29% | 1 | 100% | 255 |
| snake_abs_conv | 204,402 | +2.20% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,827 | +0.41% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,271 | -0.36% | 0 | - | 237 |
| snake_anaconda | 197,994 | -1.00% | 3 | 33% | 374 |
| snake_viper_tick | 197,401 | -1.30% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,496 | -15.25% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,082 (-4.96%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,447 | +0.86% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -367 | -0.18% |
| oracle | -868 | -0.41% |
| snake_abs | -1,349 | -0.66% |
| snake_abs_conv | -1,380 | -0.67% |
| snake_abs_exit | -1,620 | -0.78% |
| benchmark_smallcap | -1,637 | -0.81% |
| random_hold | -1,827 | -0.87% |
| snake_anaconda | -1,911 | -0.96% |
| snake_viper_tick | -1,970 | -0.99% |
| snake_viper_wild | -2,003 | -0.99% |
| unified | -2,213 | -0.98% |
| intramonth | -2,947 | -1.37% |
| benchmark | -3,152 | -1.40% |
| intraweek | -3,539 | -1.64% |

Average per day so far: unified Rs +615, benchmark Rs +564, intraweek Rs +312, intramonth Rs +309, oracle Rs +298, random_hold Rs +229, snake_abs_exit Rs +193, snake_abs_exit_conv Rs +174, snake_abs Rs +124, snake_abs_conv Rs +122, nifty_calls Rs +47, snake_viper_wild Rs +27, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -21, snake_anaconda Rs -59, snake_viper_tick Rs -93, snake_nonews Rs -300, snake Rs -320, gold Rs -782

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.