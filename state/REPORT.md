# Paper trading report

Updated 2026-11-13 11:07 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,353 | +10.18% | 0 | - | 236 |
| benchmark | 219,675 | +9.84% | 0 | - | 237 |
| snake_abs_exit_conv | 217,012 | +8.51% | 2 | 50% | 345 |
| snake_abs_exit | 216,980 | +8.49% | 2 | 50% | 345 |
| intraweek | 216,286 | +8.14% | 30 | 53% | 3,302 |
| oracle | 213,499 | +6.75% | 0 | - | 233 |
| snake_abs | 212,918 | +6.46% | 1 | 100% | 255 |
| snake_abs_conv | 212,753 | +6.38% | 1 | 100% | 255 |
| intramonth | 211,092 | +5.55% | 0 | - | 235 |
| random_hold | 207,123 | +3.56% | 10 | 70% | 733 |
| snake_viper_wild | 206,416 | +3.21% | 14 | 50% | 2,496 |
| snake_anaconda | 205,057 | +2.53% | 3 | 33% | 374 |
| benchmark_smallcap | 203,273 | +1.64% | 0 | - | 237 |
| snake_viper_tick | 202,886 | +1.44% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,456 | -7.77% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,060 (-3.97%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,628 | +0.76% |
| snake_viper_wild | +1,123 | +0.55% |
| snake_viper_tick | +1,104 | +0.55% |
| oracle | +384 | +0.18% |
| benchmark_smallcap | +67 | +0.03% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -344 | -0.16% |
| snake_abs_exit | -462 | -0.21% |
| intramonth | -501 | -0.24% |
| gold | -855 | -0.46% |
| snake_anaconda | -870 | -0.42% |
| benchmark | -872 | -0.40% |
| random_hold | -931 | -0.45% |
| snake_abs_exit_conv | -1,662 | -0.76% |
| snake_abs_conv | -2,782 | -1.29% |
| snake_abs | -2,793 | -1.29% |

Average per day so far: unified Rs +617, benchmark Rs +596, snake_abs_exit_conv Rs +567, snake_abs_exit Rs +566, intraweek Rs +494, snake_abs_conv Rs +425, snake_abs Rs +417, oracle Rs +409, intramonth Rs +336, snake_viper_wild Rs +257, random_hold Rs +216, snake_anaconda Rs +181, snake_viper_tick Rs +131, benchmark_smallcap Rs +113, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -471

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.