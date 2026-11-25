# Paper trading report

Updated 2026-11-25 13:19 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,572 | +12.29% | 0 | - | 236 |
| benchmark | 223,852 | +11.93% | 0 | - | 237 |
| oracle | 212,433 | +6.22% | 0 | - | 233 |
| intramonth | 212,318 | +6.16% | 0 | - | 235 |
| random_hold | 209,766 | +4.88% | 12 | 75% | 1,009 |
| intraweek | 208,370 | +4.18% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,378 | +0.69% | 2 | 50% | 345 |
| snake_abs_exit_conv | 200,993 | +0.50% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,567 | -0.22% | 1 | 100% | 255 |
| snake_abs_conv | 199,377 | -0.31% | 1 | 100% | 255 |
| benchmark_smallcap | 198,766 | -0.62% | 0 | - | 237 |
| snake_viper_wild | 196,670 | -1.67% | 16 | 50% | 2,827 |
| snake_viper_tick | 193,321 | -3.34% | 15 | 47% | 2,625 |
| snake_anaconda | 193,096 | -3.45% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,794 | -17.60% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,049 (-5.48%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,379 | +1.07% |
| random_hold | +1,339 | +0.64% |
| unified | +287 | +0.13% |
| oracle | +91 | +0.04% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -213 | -0.11% |
| intramonth | -434 | -0.20% |
| intraweek | -3,249 | -1.53% |
| snake_viper_tick | -4,371 | -2.21% |
| snake_viper_wild | -4,455 | -2.21% |
| gold | -4,636 | -2.74% |
| snake_anaconda | -5,607 | -2.82% |
| snake_abs | -5,894 | -2.87% |
| snake_abs_conv | -5,925 | -2.89% |
| snake_abs_exit_conv | -6,053 | -2.92% |
| snake_abs_exit | -6,117 | -2.95% |

Average per day so far: unified Rs +614, benchmark Rs +596, oracle Rs +311, intramonth Rs +308, random_hold Rs +244, intraweek Rs +209, nifty_calls Rs +46, snake_abs_exit Rs +37, snake_abs_exit_conv Rs +27, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -11, snake_abs_conv Rs -17, benchmark_smallcap Rs -34, snake_viper_wild Rs -104, snake_anaconda Rs -197, snake_viper_tick Rs -230, snake_nonews Rs -292, snake Rs -311, gold Rs -880

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.