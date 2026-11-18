# Paper trading report

Updated 2026-11-18 15:00 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,484 | +11.24% | 0 | - | 236 |
| benchmark | 220,242 | +10.12% | 0 | - | 237 |
| snake_abs_exit | 214,172 | +7.09% | 2 | 50% | 345 |
| snake_abs_exit_conv | 212,554 | +6.28% | 2 | 50% | 345 |
| intramonth | 212,154 | +6.08% | 0 | - | 235 |
| intraweek | 211,923 | +5.96% | 35 | 54% | 3,851 |
| oracle | 211,068 | +5.53% | 0 | - | 233 |
| snake_abs | 209,604 | +4.80% | 1 | 100% | 255 |
| snake_abs_conv | 209,493 | +4.75% | 1 | 100% | 255 |
| snake_viper_wild | 207,332 | +3.67% | 16 | 50% | 2,827 |
| random_hold | 206,810 | +3.40% | 10 | 70% | 733 |
| snake_anaconda | 204,575 | +2.29% | 3 | 33% | 374 |
| snake_viper_tick | 203,790 | +1.90% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,630 | -0.18% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,255 | -11.37% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,731 (-4.63%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_conv | +1,073 | +0.52% |
| unified | +1,045 | +0.47% |
| snake_abs | +1,045 | +0.50% |
| snake_abs_exit | +1,030 | +0.48% |
| snake_abs_exit_conv | +981 | +0.46% |
| intramonth | +611 | +0.29% |
| snake_anaconda | +520 | +0.26% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| benchmark_smallcap | -942 | -0.47% |
| benchmark | -1,362 | -0.61% |
| intraweek | -1,399 | -0.66% |
| oracle | -1,418 | -0.67% |
| random_hold | -1,622 | -0.78% |
| snake_viper_tick | -2,047 | -0.99% |
| snake_viper_wild | -2,083 | -0.99% |
| gold | -3,469 | -1.92% |

Average per day so far: unified Rs +625, benchmark Rs +562, snake_abs_exit Rs +429, snake_abs_exit_conv Rs +380, intramonth Rs +338, intraweek Rs +331, oracle Rs +307, snake_abs_conv Rs +288, snake_abs Rs +282, snake_viper_wild Rs +262, random_hold Rs +189, snake_viper_tick Rs +152, snake_anaconda Rs +148, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -12, snake_nonews Rs -326, snake Rs -347, gold Rs -632

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.