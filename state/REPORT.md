# Paper trading report

Updated 2026-11-17 11:50 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,306 | +11.15% | 0 | - | 236 |
| benchmark | 222,085 | +11.04% | 0 | - | 237 |
| snake_abs_exit | 215,014 | +7.51% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,151 | +6.58% | 2 | 50% | 345 |
| intraweek | 212,863 | +6.43% | 35 | 54% | 3,851 |
| oracle | 212,495 | +6.25% | 0 | - | 233 |
| intramonth | 212,234 | +6.12% | 0 | - | 235 |
| snake_abs | 209,817 | +4.91% | 1 | 100% | 255 |
| snake_abs_conv | 209,667 | +4.83% | 1 | 100% | 255 |
| random_hold | 208,012 | +4.01% | 10 | 70% | 733 |
| snake_viper_wild | 207,262 | +3.63% | 14 | 50% | 2,496 |
| snake_anaconda | 205,426 | +2.71% | 3 | 33% | 374 |
| snake_viper_tick | 203,718 | +1.86% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,230 | +1.11% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,300 | -9.35% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,434 (-4.28%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,004 | +0.91% |
| intraweek | +1,597 | +0.76% |
| benchmark_smallcap | +1,401 | +0.70% |
| snake_viper_wild | +1,118 | +0.54% |
| snake_viper_tick | +1,099 | +0.54% |
| unified | +869 | +0.39% |
| intramonth | +615 | +0.29% |
| snake_abs_exit | +605 | +0.28% |
| oracle | +472 | +0.22% |
| gold | +345 | +0.19% |
| snake_anaconda | +323 | +0.16% |
| random_hold | +219 | +0.10% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -67 | -0.03% |
| snake_abs | -317 | -0.15% |
| snake_abs_conv | -323 | -0.15% |

Average per day so far: unified Rs +637, benchmark Rs +631, snake_abs_exit Rs +469, snake_abs_exit_conv Rs +411, intraweek Rs +368, oracle Rs +357, intramonth Rs +350, snake_abs_conv Rs +302, snake_abs Rs +297, snake_viper_wild Rs +269, random_hold Rs +229, snake_anaconda Rs +181, snake_viper_tick Rs +155, benchmark_smallcap Rs +72, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -534

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.