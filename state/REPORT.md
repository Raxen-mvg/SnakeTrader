# Paper trading report

Updated 2026-11-26 09:17 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,474 | +12.74% | 0 | - | 237 |
| unified | 224,454 | +12.23% | 0 | - | 236 |
| oracle | 213,661 | +6.83% | 0 | - | 233 |
| intramonth | 211,751 | +5.88% | 0 | - | 235 |
| random_hold | 210,375 | +5.19% | 12 | 75% | 1,009 |
| intraweek | 207,396 | +3.70% | 40 | 55% | 4,400 |
| snake_abs_exit | 203,380 | +1.69% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,694 | +1.35% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,755 | +0.38% | 1 | 100% | 255 |
| snake_abs_conv | 200,581 | +0.29% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,775 | -0.11% | 0 | - | 237 |
| snake_viper_wild | 197,606 | -1.20% | 16 | 50% | 2,827 |
| snake_anaconda | 195,418 | -2.29% | 3 | 33% | 374 |
| snake_viper_tick | 194,238 | -2.88% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,408 | -16.30% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,397 (-5.30%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,811 | +1.71% |
| snake_abs_exit | +1,125 | +0.56% |
| benchmark_smallcap | +964 | +0.48% |
| random_hold | +883 | +0.42% |
| snake_anaconda | +865 | +0.45% |
| snake_abs_exit_conv | +719 | +0.36% |
| intraweek | +652 | +0.32% |
| snake_abs_conv | +609 | +0.30% |
| snake_abs | +605 | +0.30% |
| benchmark | +451 | +0.20% |
| unified | +354 | +0.16% |
| snake_viper_wild | +62 | +0.03% |
| snake_viper_tick | +61 | +0.03% |
| intramonth | +58 | +0.03% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -134 | -0.06% |

Average per day so far: benchmark Rs +621, unified Rs +596, oracle Rs +333, intramonth Rs +287, random_hold Rs +253, intraweek Rs +180, snake_abs_exit Rs +89, snake_abs_exit_conv Rs +71, nifty_calls Rs +45, snake_abs Rs +19, snake_abs_conv Rs +15, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -6, snake_viper_wild Rs -73, snake_anaconda Rs -127, snake_viper_tick Rs -192, snake_nonews Rs -284, snake Rs -304, gold Rs -795

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.