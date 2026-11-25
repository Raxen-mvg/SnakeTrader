# Paper trading report

Updated 2026-11-25 10:03 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,172 | +12.59% | 0 | - | 236 |
| benchmark | 224,610 | +12.30% | 0 | - | 237 |
| intramonth | 212,879 | +6.44% | 0 | - | 235 |
| oracle | 212,827 | +6.41% | 0 | - | 233 |
| random_hold | 209,473 | +4.74% | 12 | 75% | 1,009 |
| intraweek | 208,206 | +4.10% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,969 | +1.48% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,337 | +1.17% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,734 | +0.87% | 1 | 100% | 255 |
| snake_abs_conv | 201,554 | +0.78% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,204 | -0.40% | 0 | - | 237 |
| snake_viper_wild | 198,599 | -0.70% | 16 | 50% | 2,827 |
| snake_viper_tick | 195,220 | -2.39% | 15 | 47% | 2,625 |
| snake_anaconda | 194,731 | -2.63% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,402 | -17.30% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,555 (-5.22%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,137 | +1.42% |
| random_hold | +1,047 | +0.50% |
| unified | +887 | +0.40% |
| oracle | +485 | +0.23% |
| benchmark_smallcap | +224 | +0.11% |
| intramonth | +127 | +0.06% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -2,472 | -1.25% |
| snake_viper_wild | -2,525 | -1.25% |
| intraweek | -3,413 | -1.61% |
| snake_abs | -3,727 | -1.81% |
| snake_abs_conv | -3,749 | -1.83% |
| snake_anaconda | -3,973 | -2.00% |
| gold | -4,028 | -2.38% |
| snake_abs_exit | -4,526 | -2.18% |
| snake_abs_exit_conv | -4,709 | -2.27% |

Average per day so far: unified Rs +629, benchmark Rs +615, intramonth Rs +322, oracle Rs +321, random_hold Rs +237, intraweek Rs +205, snake_abs_exit Rs +80, snake_abs_exit_conv Rs +63, nifty_calls Rs +46, snake_abs Rs +46, snake_abs_conv Rs +42, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -22, snake_viper_wild Rs -44, snake_anaconda Rs -151, snake_viper_tick Rs -165, snake_nonews Rs -292, snake Rs -311, gold Rs -865

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.