# Paper trading report

Updated 2026-11-18 12:07 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,015 | +11.51% | 0 | - | 236 |
| benchmark | 220,073 | +10.04% | 0 | - | 237 |
| intraweek | 213,839 | +6.92% | 35 | 54% | 3,851 |
| intramonth | 212,895 | +6.45% | 0 | - | 235 |
| snake_abs_exit | 212,668 | +6.33% | 2 | 50% | 345 |
| oracle | 212,401 | +6.20% | 0 | - | 233 |
| snake_abs_exit_conv | 210,975 | +5.49% | 2 | 50% | 345 |
| snake_abs | 207,896 | +3.95% | 1 | 100% | 255 |
| snake_abs_conv | 207,763 | +3.88% | 1 | 100% | 255 |
| random_hold | 207,377 | +3.69% | 10 | 70% | 733 |
| snake_viper_wild | 206,900 | +3.45% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,367 | +1.68% | 15 | 47% | 2,625 |
| snake_anaconda | 203,068 | +1.53% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,327 | -0.34% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,173 | -11.41% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,500 (-4.25%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,576 | +0.71% |
| intramonth | +1,353 | +0.64% |
| intraweek | +516 | +0.24% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -85 | -0.04% |
| snake_abs_exit | -474 | -0.22% |
| snake_abs_exit_conv | -599 | -0.28% |
| snake_abs_conv | -657 | -0.32% |
| snake_abs | -662 | -0.32% |
| snake_anaconda | -987 | -0.48% |
| random_hold | -1,056 | -0.51% |
| benchmark_smallcap | -1,244 | -0.62% |
| benchmark | -1,530 | -0.69% |
| snake_viper_tick | -2,470 | -1.20% |
| snake_viper_wild | -2,515 | -1.20% |
| gold | -3,551 | -1.97% |

Average per day so far: unified Rs +639, benchmark Rs +558, intraweek Rs +384, snake_abs_exit Rs +384, intramonth Rs +358, oracle Rs +344, snake_abs_exit_conv Rs +333, snake_viper_wild Rs +246, snake_abs_conv Rs +235, snake_abs Rs +232, random_hold Rs +205, snake_viper_tick Rs +135, snake_anaconda Rs +99, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -21, snake_nonews Rs -326, snake Rs -347, gold Rs -634

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.