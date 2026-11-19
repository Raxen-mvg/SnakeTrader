# Paper trading report

Updated 2026-11-19 15:01 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,432 | +12.22% | 0 | - | 236 |
| benchmark | 222,292 | +11.15% | 0 | - | 237 |
| intramonth | 213,926 | +6.96% | 0 | - | 235 |
| snake_abs_exit | 213,473 | +6.74% | 2 | 50% | 345 |
| intraweek | 212,545 | +6.27% | 35 | 54% | 3,851 |
| oracle | 212,437 | +6.22% | 0 | - | 233 |
| snake_abs_exit_conv | 211,184 | +5.59% | 2 | 50% | 345 |
| snake_abs | 208,845 | +4.42% | 1 | 100% | 255 |
| snake_abs_conv | 208,728 | +4.36% | 1 | 100% | 255 |
| random_hold | 208,358 | +4.18% | 10 | 70% | 733 |
| snake_viper_wild | 207,518 | +3.76% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,972 | +1.99% | 15 | 47% | 2,625 |
| snake_anaconda | 203,855 | +1.93% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,423 | +0.71% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,674 | -12.66% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,949 (-4.03%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,096 | +1.05% |
| benchmark | +1,997 | +0.91% |
| unified | +1,820 | +0.82% |
| intramonth | +1,652 | +0.78% |
| oracle | +1,641 | +0.78% |
| random_hold | +1,425 | +0.69% |
| intraweek | +706 | +0.33% |
| snake_viper_wild | +479 | +0.23% |
| snake_viper_tick | +469 | +0.23% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_anaconda | -546 | -0.27% |
| snake_abs_exit | -559 | -0.26% |
| snake_abs | -591 | -0.28% |
| snake_abs_conv | -597 | -0.28% |
| snake_abs_exit_conv | -1,199 | -0.56% |
| gold | -2,647 | -1.49% |

Average per day so far: unified Rs +660, benchmark Rs +602, snake_abs_exit Rs +396, intramonth Rs +376, intraweek Rs +339, oracle Rs +336, snake_abs_exit_conv Rs +329, snake_viper_wild Rs +259, snake_abs_conv Rs +257, snake_abs Rs +253, random_hold Rs +226, snake_viper_tick Rs +153, snake_anaconda Rs +120, nifty_calls Rs +50, benchmark_smallcap Rs +43, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -684

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.