# Paper trading report

Updated 2026-11-16 15:25 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,870 | +10.94% | 0 | - | 236 |
| benchmark | 220,265 | +10.13% | 0 | - | 237 |
| snake_abs_exit | 215,231 | +7.62% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,909 | +6.95% | 2 | 50% | 345 |
| oracle | 212,198 | +6.10% | 0 | - | 233 |
| intramonth | 211,887 | +5.94% | 0 | - | 235 |
| intraweek | 211,881 | +5.94% | 35 | 54% | 3,851 |
| snake_abs | 211,024 | +5.51% | 1 | 100% | 255 |
| snake_abs_conv | 210,879 | +5.44% | 1 | 100% | 255 |
| random_hold | 207,850 | +3.92% | 10 | 70% | 733 |
| snake_viper_wild | 206,473 | +3.24% | 14 | 50% | 2,496 |
| snake_anaconda | 205,726 | +2.86% | 3 | 33% | 374 |
| snake_viper_tick | 202,944 | +1.47% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,672 | +0.34% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,757 | -9.62% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,065 (-4.47%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +2,849 | +1.30% |
| intramonth | +1,830 | +0.87% |
| snake_viper_wild | +1,716 | +0.84% |
| snake_viper_tick | +1,689 | +0.84% |
| benchmark | +926 | +0.42% |
| snake_anaconda | +834 | +0.41% |
| random_hold | +624 | +0.30% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -900 | -0.42% |
| snake_abs_conv | -1,488 | -0.70% |
| snake_abs | -1,516 | -0.71% |
| snake_abs_exit | -1,754 | -0.81% |
| benchmark_smallcap | -2,197 | -1.08% |
| snake_abs_exit_conv | -2,473 | -1.14% |
| gold | -3,239 | -1.76% |
| intraweek | -4,264 | -1.97% |

Average per day so far: unified Rs +643, benchmark Rs +596, snake_abs_exit Rs +491, snake_abs_exit_conv Rs +449, oracle Rs +359, snake_abs_conv Rs +351, intramonth Rs +350, intraweek Rs +349, snake_abs Rs +345, snake_viper_wild Rs +249, random_hold Rs +231, snake_anaconda Rs +197, snake_viper_tick Rs +128, nifty_calls Rs +54, benchmark_smallcap Rs +22, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -347, snake Rs -368, gold Rs -566

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.