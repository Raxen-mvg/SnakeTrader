# Paper trading report

Updated 2026-11-25 13:23 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,594 | +12.30% | 0 | - | 236 |
| benchmark | 223,776 | +11.89% | 0 | - | 237 |
| oracle | 212,499 | +6.25% | 0 | - | 233 |
| intramonth | 212,317 | +6.16% | 0 | - | 235 |
| random_hold | 209,745 | +4.87% | 12 | 75% | 1,009 |
| intraweek | 208,282 | +4.14% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,307 | +0.65% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,016 | +0.51% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,646 | -0.18% | 1 | 100% | 255 |
| snake_abs_conv | 199,454 | -0.27% | 1 | 100% | 255 |
| benchmark_smallcap | 198,878 | -0.56% | 0 | - | 237 |
| snake_viper_wild | 196,670 | -1.67% | 16 | 50% | 2,827 |
| snake_viper_tick | 193,321 | -3.34% | 15 | 47% | 2,625 |
| snake_anaconda | 193,112 | -3.44% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,695 | -17.65% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,062 (-5.47%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,303 | +1.04% |
| random_hold | +1,319 | +0.63% |
| unified | +308 | +0.14% |
| oracle | +157 | +0.07% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -101 | -0.05% |
| intramonth | -434 | -0.20% |
| intraweek | -3,337 | -1.58% |
| snake_viper_tick | -4,371 | -2.21% |
| snake_viper_wild | -4,455 | -2.21% |
| gold | -4,735 | -2.79% |
| snake_anaconda | -5,591 | -2.81% |
| snake_abs | -5,815 | -2.83% |
| snake_abs_conv | -5,848 | -2.85% |
| snake_abs_exit_conv | -6,030 | -2.91% |
| snake_abs_exit | -6,188 | -2.98% |

Average per day so far: unified Rs +615, benchmark Rs +594, oracle Rs +312, intramonth Rs +308, random_hold Rs +244, intraweek Rs +207, nifty_calls Rs +46, snake_abs_exit Rs +35, snake_abs_exit_conv Rs +27, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -9, snake_abs_conv Rs -15, benchmark_smallcap Rs -31, snake_viper_wild Rs -104, snake_anaconda Rs -197, snake_viper_tick Rs -230, snake_nonews Rs -292, snake Rs -311, gold Rs -883

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.