# Paper trading report

Updated 2026-11-16 09:39 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,517 | +10.26% | 0 | - | 237 |
| unified | 219,141 | +9.57% | 0 | - | 236 |
| snake_abs_exit | 215,109 | +7.55% | 2 | 50% | 345 |
| intraweek | 215,072 | +7.54% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 213,890 | +6.95% | 2 | 50% | 345 |
| oracle | 213,329 | +6.66% | 0 | - | 233 |
| snake_abs | 210,852 | +5.43% | 1 | 100% | 255 |
| snake_abs_conv | 210,685 | +5.34% | 1 | 100% | 255 |
| intramonth | 210,219 | +5.11% | 0 | - | 235 |
| random_hold | 207,993 | +4.00% | 10 | 70% | 733 |
| snake_anaconda | 204,948 | +2.47% | 3 | 33% | 374 |
| snake_viper_wild | 203,920 | +1.96% | 14 | 50% | 2,496 |
| benchmark_smallcap | 201,961 | +0.98% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 200,432 | +0.22% | 13 | 46% | 2,299 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 182,319 | -8.84% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,385 (-4.31%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,178 | +0.54% |
| random_hold | +767 | +0.37% |
| oracle | +231 | +0.11% |
| intramonth | +162 | +0.08% |
| unified | +121 | +0.06% |
| snake_anaconda | +56 | +0.03% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_viper_tick | -823 | -0.41% |
| snake_viper_wild | -837 | -0.41% |
| benchmark_smallcap | -908 | -0.45% |
| intraweek | -1,073 | -0.50% |
| gold | -1,677 | -0.91% |
| snake_abs_conv | -1,681 | -0.79% |
| snake_abs | -1,689 | -0.79% |
| snake_abs_exit | -1,876 | -0.86% |
| snake_abs_exit_conv | -2,491 | -1.15% |

Average per day so far: benchmark Rs +603, unified Rs +563, snake_abs_exit Rs +487, snake_abs_exit_conv Rs +448, intraweek Rs +443, oracle Rs +392, snake_abs_conv Rs +345, snake_abs Rs +339, intramonth Rs +301, random_hold Rs +235, snake_anaconda Rs +171, snake_viper_wild Rs +151, benchmark_smallcap Rs +65, nifty_calls Rs +54, snake_viper_tick Rs +19, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -347, snake Rs -368, gold Rs -520

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.