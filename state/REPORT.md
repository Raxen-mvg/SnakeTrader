# Paper trading report

Updated 2026-11-18 13:07 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,916 | +11.46% | 0 | - | 236 |
| benchmark | 219,698 | +9.85% | 0 | - | 237 |
| intramonth | 212,750 | +6.38% | 0 | - | 235 |
| intraweek | 212,695 | +6.35% | 35 | 54% | 3,851 |
| snake_abs_exit | 212,168 | +6.08% | 2 | 50% | 345 |
| oracle | 212,025 | +6.01% | 0 | - | 233 |
| snake_abs_exit_conv | 210,439 | +5.22% | 2 | 50% | 345 |
| snake_abs | 207,602 | +3.80% | 1 | 100% | 255 |
| snake_abs_conv | 207,462 | +3.73% | 1 | 100% | 255 |
| random_hold | 207,090 | +3.54% | 10 | 70% | 733 |
| snake_viper_wild | 206,703 | +3.35% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,174 | +1.59% | 15 | 47% | 2,625 |
| snake_anaconda | 202,591 | +1.30% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,148 | -0.43% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 176,811 | -11.59% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,156 (-4.42%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,477 | +0.67% |
| intramonth | +1,207 | +0.57% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| oracle | -462 | -0.22% |
| intraweek | -628 | -0.29% |
| snake_abs | -957 | -0.46% |
| snake_abs_conv | -958 | -0.46% |
| snake_abs_exit | -974 | -0.46% |
| snake_abs_exit_conv | -1,135 | -0.54% |
| random_hold | -1,342 | -0.64% |
| benchmark_smallcap | -1,424 | -0.71% |
| snake_anaconda | -1,464 | -0.72% |
| benchmark | -1,905 | -0.86% |
| snake_viper_tick | -2,662 | -1.29% |
| snake_viper_wild | -2,712 | -1.29% |
| gold | -3,913 | -2.17% |

Average per day so far: unified Rs +637, benchmark Rs +547, snake_abs_exit Rs +369, intramonth Rs +354, intraweek Rs +353, oracle Rs +334, snake_abs_exit_conv Rs +316, snake_viper_wild Rs +239, snake_abs_conv Rs +226, snake_abs Rs +224, random_hold Rs +197, snake_viper_tick Rs +127, snake_anaconda Rs +84, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -27, snake_nonews Rs -326, snake Rs -347, gold Rs -644

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.