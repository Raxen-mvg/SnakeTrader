# Paper trading report

Updated 2026-11-25 10:38 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,181 | +12.59% | 0 | - | 236 |
| benchmark | 225,122 | +12.56% | 0 | - | 237 |
| intramonth | 212,876 | +6.44% | 0 | - | 235 |
| oracle | 212,114 | +6.06% | 0 | - | 233 |
| random_hold | 209,208 | +4.60% | 12 | 75% | 1,009 |
| intraweek | 206,862 | +3.43% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,718 | +0.86% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,130 | +0.56% | 2 | 50% | 345 |
| snake_abs | 200,666 | +0.33% | 1 | 100% | 255 |
| snake_abs_conv | 200,476 | +0.24% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,372 | -0.31% | 0 | - | 237 |
| snake_viper_wild | 195,441 | -2.28% | 16 | 50% | 2,827 |
| snake_anaconda | 193,172 | -3.41% | 3 | 33% | 374 |
| snake_viper_tick | 192,118 | -3.94% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,468 | -17.27% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,048 (-5.48%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,649 | +1.65% |
| unified | +896 | +0.40% |
| random_hold | +781 | +0.38% |
| benchmark_smallcap | +392 | +0.20% |
| intramonth | +125 | +0.06% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| oracle | -228 | -0.11% |
| gold | -3,962 | -2.34% |
| intraweek | -4,757 | -2.25% |
| snake_abs | -4,795 | -2.33% |
| snake_abs_conv | -4,827 | -2.35% |
| snake_anaconda | -5,532 | -2.78% |
| snake_viper_tick | -5,574 | -2.82% |
| snake_viper_wild | -5,683 | -2.83% |
| snake_abs_exit | -5,777 | -2.78% |
| snake_abs_exit_conv | -5,916 | -2.86% |

Average per day so far: unified Rs +630, benchmark Rs +628, intramonth Rs +322, oracle Rs +303, random_hold Rs +230, intraweek Rs +172, snake_abs_exit Rs +46, nifty_calls Rs +46, snake_abs_exit_conv Rs +31, snake_abs Rs +18, snake_abs_conv Rs +13, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -17, snake_viper_wild Rs -142, snake_anaconda Rs -195, snake_viper_tick Rs -272, snake_nonews Rs -292, snake Rs -311, gold Rs -863

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.