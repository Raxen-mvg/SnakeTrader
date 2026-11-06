# Paper trading report

Updated 2026-11-06 13:13 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,514 | +7.76% | 0 | - | 237 |
| unified | 214,749 | +7.38% | 0 | - | 236 |
| intraweek | 208,549 | +4.27% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,446 | +4.22% | 1 | 100% | 255 |
| snake_abs_exit | 208,345 | +4.17% | 1 | 100% | 260 |
| intramonth | 207,146 | +3.57% | 0 | - | 235 |
| snake_abs | 205,436 | +2.72% | 1 | 100% | 255 |
| oracle | 205,309 | +2.65% | 0 | - | 233 |
| snake_abs_conv | 205,251 | +2.62% | 1 | 100% | 255 |
| random_hold | 203,407 | +1.70% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,992 | -1.50% | 3 | 33% | 702 |
| snake_anaconda | 195,884 | -2.06% | 3 | 33% | 374 |
| benchmark_smallcap | 194,989 | -2.51% | 0 | - | 237 |
| snake_viper_tick | 193,655 | -3.17% | 2 | 0% | 532 |
| gold | 190,078 | -4.96% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,935 (-6.53%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,744 | +0.82% |
| oracle | +1,237 | +0.61% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -802 | -0.39% |
| intraweek | -870 | -0.41% |
| random_hold | -916 | -0.45% |
| unified | -1,234 | -0.57% |
| benchmark_smallcap | -3,699 | -1.86% |
| gold | -4,143 | -2.13% |
| snake_abs | -6,252 | -2.95% |
| snake_abs_conv | -6,294 | -2.98% |
| snake_abs_exit | -6,314 | -2.94% |
| snake_abs_exit_conv | -6,357 | -2.96% |
| snake_anaconda | -6,595 | -3.26% |
| snake_viper_tick | -7,483 | -3.72% |
| snake_viper_wild | -7,664 | -3.75% |

Average per day so far: benchmark Rs +535, unified Rs +509, snake_abs_exit_conv Rs +325, snake_abs_exit Rs +321, intraweek Rs +295, intramonth Rs +246, snake_abs_conv Rs +202, snake_abs Rs +201, oracle Rs +183, random_hold Rs +117, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -143, snake_anaconda Rs -171, benchmark_smallcap Rs -200, gold Rs -342, snake_viper_tick Rs -352, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.