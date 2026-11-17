# Paper trading report

Updated 2026-11-17 13:12 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,328 | +10.66% | 0 | - | 237 |
| unified | 221,207 | +10.60% | 0 | - | 236 |
| snake_abs_exit | 213,789 | +6.89% | 2 | 50% | 345 |
| intraweek | 213,396 | +6.70% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 212,134 | +6.07% | 2 | 50% | 345 |
| oracle | 211,787 | +5.89% | 0 | - | 233 |
| intramonth | 211,087 | +5.54% | 0 | - | 235 |
| snake_abs | 209,125 | +4.56% | 1 | 100% | 255 |
| snake_abs_conv | 208,983 | +4.49% | 1 | 100% | 255 |
| snake_viper_wild | 208,216 | +4.11% | 14 | 50% | 2,496 |
| random_hold | 207,270 | +3.63% | 10 | 70% | 733 |
| snake_viper_tick | 204,657 | +2.33% | 13 | 46% | 2,299 |
| snake_anaconda | 204,645 | +2.32% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,784 | +0.39% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,349 | -9.33% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,797 (-4.60%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,130 | +1.01% |
| snake_viper_wild | +2,072 | +1.00% |
| snake_viper_tick | +2,037 | +1.00% |
| benchmark | +1,247 | +0.57% |
| gold | +395 | +0.22% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| benchmark_smallcap | -45 | -0.02% |
| unified | -231 | -0.10% |
| oracle | -236 | -0.11% |
| snake_anaconda | -458 | -0.22% |
| random_hold | -523 | -0.25% |
| intramonth | -532 | -0.25% |
| snake_abs_exit | -621 | -0.29% |
| snake_abs_conv | -1,007 | -0.48% |
| snake_abs | -1,009 | -0.48% |
| snake_abs_exit_conv | -1,084 | -0.51% |

Average per day so far: benchmark Rs +609, unified Rs +606, snake_abs_exit Rs +431, intraweek Rs +383, snake_abs_exit_conv Rs +379, oracle Rs +337, intramonth Rs +317, snake_viper_wild Rs +304, snake_abs_conv Rs +281, snake_abs Rs +277, random_hold Rs +208, snake_viper_tick Rs +194, snake_anaconda Rs +155, nifty_calls Rs +52, benchmark_smallcap Rs +25, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -533

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.