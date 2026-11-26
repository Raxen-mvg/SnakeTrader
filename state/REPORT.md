# Paper trading report

Updated 2026-11-26 13:41 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,352 | +12.68% | 0 | - | 237 |
| unified | 223,205 | +11.60% | 0 | - | 236 |
| oracle | 213,191 | +6.59% | 0 | - | 233 |
| intramonth | 210,282 | +5.14% | 0 | - | 235 |
| random_hold | 209,278 | +4.64% | 13 | 69% | 1,037 |
| intraweek | 207,898 | +3.95% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,425 | +0.21% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit | 199,908 | -0.05% | 2 | 50% | 345 |
| snake_abs_exit_conv | 199,295 | -0.35% | 2 | 50% | 345 |
| snake_abs | 197,719 | -1.14% | 1 | 100% | 255 |
| snake_abs_conv | 197,507 | -1.25% | 1 | 100% | 255 |
| snake_viper_wild | 192,215 | -3.89% | 16 | 50% | 2,827 |
| snake_anaconda | 191,323 | -4.34% | 3 | 33% | 374 |
| snake_viper_tick | 188,951 | -5.53% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,257 | -16.87% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,549 (-5.73%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,660 | +1.01% |
| benchmark_smallcap | +1,614 | +0.81% |
| intraweek | +1,155 | +0.56% |
| benchmark | +329 | +0.15% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -214 | -0.10% |
| oracle | -604 | -0.28% |
| unified | -894 | -0.40% |
| intramonth | -1,411 | -0.67% |
| snake_abs_exit | -2,347 | -1.16% |
| snake_abs | -2,431 | -1.22% |
| snake_abs_conv | -2,465 | -1.23% |
| snake_abs_exit_conv | -2,680 | -1.33% |
| snake_anaconda | -3,230 | -1.66% |
| snake_viper_tick | -5,226 | -2.69% |
| snake_viper_wild | -5,328 | -2.70% |

Average per day so far: benchmark Rs +618, unified Rs +566, oracle Rs +322, intramonth Rs +251, random_hold Rs +226, intraweek Rs +193, nifty_calls Rs +45, benchmark_smallcap Rs +11, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_abs_exit Rs -2, snake_abs_exit_conv Rs -19, snake_abs Rs -58, snake_abs_conv Rs -66, snake_viper_wild Rs -236, snake_anaconda Rs -241, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -368, gold Rs -823

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.