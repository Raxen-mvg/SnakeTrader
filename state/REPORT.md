# Paper trading report

Updated 2026-11-06 13:34 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,774 | +7.89% | 0 | - | 237 |
| unified | 214,660 | +7.33% | 0 | - | 236 |
| snake_abs_exit_conv | 208,617 | +4.31% | 1 | 100% | 255 |
| snake_abs_exit | 208,516 | +4.26% | 1 | 100% | 260 |
| intraweek | 208,226 | +4.11% | 25 | 48% | 2,757 |
| intramonth | 206,973 | +3.49% | 0 | - | 235 |
| snake_abs | 205,600 | +2.80% | 1 | 100% | 255 |
| snake_abs_conv | 205,418 | +2.71% | 1 | 100% | 255 |
| oracle | 205,210 | +2.60% | 0 | - | 233 |
| random_hold | 203,235 | +1.62% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,069 | -1.97% | 3 | 33% | 702 |
| snake_anaconda | 196,028 | -1.99% | 3 | 33% | 374 |
| benchmark_smallcap | 195,000 | -2.50% | 0 | - | 237 |
| snake_viper_tick | 192,748 | -3.63% | 2 | 0% | 532 |
| gold | 190,259 | -4.87% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,851 (-6.57%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,004 | +0.94% |
| oracle | +1,138 | +0.56% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -975 | -0.47% |
| random_hold | -1,088 | -0.53% |
| intraweek | -1,192 | -0.57% |
| unified | -1,324 | -0.61% |
| benchmark_smallcap | -3,688 | -1.86% |
| gold | -3,962 | -2.04% |
| snake_abs | -6,088 | -2.88% |
| snake_abs_conv | -6,126 | -2.90% |
| snake_abs_exit | -6,143 | -2.86% |
| snake_abs_exit_conv | -6,186 | -2.88% |
| snake_anaconda | -6,451 | -3.19% |
| snake_viper_tick | -8,390 | -4.17% |
| snake_viper_wild | -8,587 | -4.20% |

Average per day so far: benchmark Rs +544, unified Rs +506, snake_abs_exit_conv Rs +331, snake_abs_exit Rs +328, intraweek Rs +284, intramonth Rs +240, snake_abs_conv Rs +208, snake_abs Rs +207, oracle Rs +180, random_hold Rs +112, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -165, snake_viper_wild Rs -187, benchmark_smallcap Rs -200, gold Rs -336, snake_viper_tick Rs -403, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.