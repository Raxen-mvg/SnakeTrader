# Paper trading report

Updated 2026-11-16 09:49 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,754 | +10.38% | 0 | - | 237 |
| unified | 219,549 | +9.77% | 0 | - | 236 |
| snake_abs_exit | 214,370 | +7.18% | 2 | 50% | 345 |
| intraweek | 214,240 | +7.12% | 35 | 54% | 3,851 |
| oracle | 213,584 | +6.79% | 0 | - | 233 |
| snake_abs_exit_conv | 213,234 | +6.62% | 2 | 50% | 345 |
| snake_abs | 210,449 | +5.22% | 1 | 100% | 255 |
| intramonth | 210,281 | +5.14% | 0 | - | 235 |
| snake_abs_conv | 210,275 | +5.14% | 1 | 100% | 255 |
| random_hold | 207,613 | +3.81% | 10 | 70% | 733 |
| snake_anaconda | 204,496 | +2.25% | 3 | 33% | 374 |
| snake_viper_wild | 203,440 | +1.72% | 14 | 50% | 2,496 |
| benchmark_smallcap | 202,129 | +1.06% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 199,960 | -0.02% | 13 | 46% | 2,299 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 182,302 | -8.85% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,307 (-4.35%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,415 | +0.65% |
| unified | +528 | +0.24% |
| oracle | +486 | +0.23% |
| random_hold | +387 | +0.19% |
| intramonth | +224 | +0.11% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_anaconda | -396 | -0.19% |
| benchmark_smallcap | -740 | -0.36% |
| snake_viper_tick | -1,295 | -0.64% |
| snake_viper_wild | -1,317 | -0.64% |
| gold | -1,693 | -0.92% |
| intraweek | -1,905 | -0.88% |
| snake_abs | -2,091 | -0.98% |
| snake_abs_conv | -2,092 | -0.98% |
| snake_abs_exit | -2,615 | -1.21% |
| snake_abs_exit_conv | -3,147 | -1.45% |

Average per day so far: benchmark Rs +610, unified Rs +575, snake_abs_exit Rs +464, snake_abs_exit_conv Rs +427, intraweek Rs +419, oracle Rs +400, snake_abs_conv Rs +331, snake_abs Rs +327, intramonth Rs +302, random_hold Rs +224, snake_anaconda Rs +155, snake_viper_wild Rs +132, benchmark_smallcap Rs +71, nifty_calls Rs +54, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -2, snake_nonews Rs -347, snake Rs -368, gold Rs -521

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.