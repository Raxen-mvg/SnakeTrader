# Paper trading report

Updated 2026-11-13 11:04 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,257 | +10.13% | 0 | - | 236 |
| benchmark | 219,767 | +9.88% | 0 | - | 237 |
| snake_abs_exit_conv | 217,022 | +8.51% | 2 | 50% | 345 |
| snake_abs_exit | 217,002 | +8.50% | 2 | 50% | 345 |
| intraweek | 216,161 | +8.08% | 30 | 53% | 3,302 |
| oracle | 213,485 | +6.74% | 0 | - | 233 |
| snake_abs | 212,919 | +6.46% | 1 | 100% | 255 |
| snake_abs_conv | 212,754 | +6.38% | 1 | 100% | 255 |
| intramonth | 211,057 | +5.53% | 0 | - | 235 |
| random_hold | 207,112 | +3.56% | 10 | 70% | 733 |
| snake_viper_wild | 206,428 | +3.21% | 14 | 50% | 2,496 |
| snake_anaconda | 205,057 | +2.53% | 3 | 33% | 374 |
| benchmark_smallcap | 203,486 | +1.74% | 0 | - | 237 |
| snake_viper_tick | 202,897 | +1.45% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,390 | -7.80% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,013 (-3.99%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,503 | +0.70% |
| snake_viper_wild | +1,135 | +0.55% |
| snake_viper_tick | +1,115 | +0.55% |
| oracle | +369 | +0.17% |
| benchmark_smallcap | +280 | +0.14% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -440 | -0.20% |
| snake_abs_exit | -440 | -0.20% |
| intramonth | -536 | -0.25% |
| benchmark | -780 | -0.35% |
| snake_anaconda | -870 | -0.42% |
| gold | -921 | -0.50% |
| random_hold | -942 | -0.45% |
| snake_abs_exit_conv | -1,652 | -0.76% |
| snake_abs_conv | -2,781 | -1.29% |
| snake_abs | -2,792 | -1.29% |

Average per day so far: unified Rs +614, benchmark Rs +599, snake_abs_exit_conv Rs +567, snake_abs_exit Rs +567, intraweek Rs +490, snake_abs_conv Rs +425, snake_abs Rs +417, oracle Rs +409, intramonth Rs +335, snake_viper_wild Rs +257, random_hold Rs +216, snake_anaconda Rs +181, snake_viper_tick Rs +132, benchmark_smallcap Rs +120, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -473

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.