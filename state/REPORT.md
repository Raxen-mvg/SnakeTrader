# Paper trading report

Updated 2026-11-06 12:07 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,586 | +7.29% | 0 | - | 236 |
| benchmark | 214,481 | +7.24% | 0 | - | 237 |
| intraweek | 209,711 | +4.86% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,756 | +4.38% | 1 | 100% | 255 |
| snake_abs_exit | 208,567 | +4.28% | 1 | 100% | 260 |
| intramonth | 206,893 | +3.45% | 0 | - | 235 |
| snake_abs | 205,722 | +2.86% | 1 | 100% | 255 |
| snake_abs_conv | 205,549 | +2.77% | 1 | 100% | 255 |
| oracle | 204,601 | +2.30% | 0 | - | 233 |
| random_hold | 203,211 | +1.61% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 195,999 | -2.00% | 3 | 33% | 374 |
| snake_viper_wild | 195,522 | -2.24% | 3 | 33% | 702 |
| benchmark_smallcap | 194,451 | -2.77% | 0 | - | 237 |
| snake_viper_tick | 192,210 | -3.90% | 2 | 0% | 532 |
| gold | 190,210 | -4.89% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,953 (-6.52%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +711 | +0.33% |
| oracle | +529 | +0.26% |
| intraweek | +292 | +0.14% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intramonth | -1,056 | -0.51% |
| random_hold | -1,112 | -0.54% |
| unified | -1,398 | -0.65% |
| gold | -4,011 | -2.06% |
| benchmark_smallcap | -4,237 | -2.13% |
| snake_abs | -5,967 | -2.82% |
| snake_abs_conv | -5,996 | -2.83% |
| snake_abs_exit_conv | -6,048 | -2.81% |
| snake_abs_exit | -6,092 | -2.84% |
| snake_anaconda | -6,481 | -3.20% |
| snake_viper_tick | -8,928 | -4.44% |
| snake_viper_wild | -9,134 | -4.46% |

Average per day so far: unified Rs +503, benchmark Rs +499, snake_abs_exit_conv Rs +337, intraweek Rs +335, snake_abs_exit Rs +329, intramonth Rs +238, snake_abs_conv Rs +213, snake_abs Rs +212, oracle Rs +159, random_hold Rs +111, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -167, snake_viper_wild Rs -213, benchmark_smallcap Rs -222, gold Rs -338, snake_nonews Rs -411, snake_viper_tick Rs -433, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.