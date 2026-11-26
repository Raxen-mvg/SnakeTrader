# Paper trading report

Updated 2026-11-26 13:44 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,551 | +12.78% | 0 | - | 237 |
| unified | 223,126 | +11.56% | 0 | - | 236 |
| oracle | 213,074 | +6.54% | 0 | - | 233 |
| intramonth | 210,150 | +5.08% | 0 | - | 235 |
| random_hold | 209,171 | +4.59% | 13 | 69% | 1,037 |
| intraweek | 207,637 | +3.82% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,437 | +0.22% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit | 199,714 | -0.14% | 2 | 50% | 345 |
| snake_abs_exit_conv | 199,107 | -0.45% | 2 | 50% | 345 |
| snake_abs | 197,553 | -1.22% | 1 | 100% | 255 |
| snake_abs_conv | 197,339 | -1.33% | 1 | 100% | 255 |
| snake_viper_wild | 192,158 | -3.92% | 16 | 50% | 2,827 |
| snake_anaconda | 191,156 | -4.42% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,894 | -5.55% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,208 | -16.90% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,442 (-5.78%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,625 | +0.82% |
| gold | +1,611 | +0.98% |
| intraweek | +894 | +0.43% |
| benchmark | +528 | +0.23% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -321 | -0.15% |
| oracle | -721 | -0.34% |
| unified | -973 | -0.43% |
| intramonth | -1,544 | -0.73% |
| snake_abs_exit | -2,542 | -1.26% |
| snake_abs | -2,597 | -1.30% |
| snake_abs_conv | -2,633 | -1.32% |
| snake_abs_exit_conv | -2,869 | -1.42% |
| snake_anaconda | -3,397 | -1.75% |
| snake_viper_tick | -5,283 | -2.72% |
| snake_viper_wild | -5,386 | -2.73% |

Average per day so far: benchmark Rs +623, unified Rs +564, oracle Rs +319, intramonth Rs +248, random_hold Rs +224, intraweek Rs +186, nifty_calls Rs +45, benchmark_smallcap Rs +12, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_abs_exit Rs -8, snake_abs_exit_conv Rs -24, snake_abs Rs -63, snake_abs_conv Rs -70, snake_viper_wild Rs -238, snake_anaconda Rs -246, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -370, gold Rs -824

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.