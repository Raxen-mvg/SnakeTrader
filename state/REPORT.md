# Paper trading report

Updated 2026-11-06 09:28 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,043 | +7.02% | 0 | - | 236 |
| benchmark | 213,762 | +6.88% | 0 | - | 237 |
| snake_abs_exit_conv | 210,517 | +5.26% | 1 | 100% | 255 |
| snake_abs_exit | 210,275 | +5.14% | 1 | 100% | 260 |
| intraweek | 208,813 | +4.41% | 25 | 48% | 2,757 |
| snake_abs | 207,433 | +3.72% | 1 | 100% | 255 |
| snake_abs_conv | 207,285 | +3.64% | 1 | 100% | 255 |
| intramonth | 206,139 | +3.07% | 0 | - | 235 |
| oracle | 203,561 | +1.78% | 0 | - | 233 |
| random_hold | 202,851 | +1.43% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,763 | -1.12% | 3 | 33% | 374 |
| snake_viper_wild | 197,231 | -1.38% | 3 | 33% | 702 |
| benchmark_smallcap | 194,731 | -2.63% | 0 | - | 237 |
| snake_viper_tick | 193,890 | -3.06% | 2 | 0% | 532 |
| gold | 190,424 | -4.79% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,095 (-6.45%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -8 | -0.00% |
| oracle | -511 | -0.25% |
| intraweek | -605 | -0.29% |
| random_hold | -1,472 | -0.72% |
| intramonth | -1,810 | -0.87% |
| unified | -1,941 | -0.90% |
| gold | -3,798 | -1.96% |
| benchmark_smallcap | -3,957 | -1.99% |
| snake_abs | -4,256 | -2.01% |
| snake_abs_conv | -4,260 | -2.01% |
| snake_abs_exit_conv | -4,287 | -2.00% |
| snake_abs_exit | -4,383 | -2.04% |
| snake_anaconda | -4,716 | -2.33% |
| snake_viper_tick | -7,248 | -3.60% |
| snake_viper_wild | -7,425 | -3.63% |

Average per day so far: unified Rs +484, benchmark Rs +475, snake_abs_exit_conv Rs +404, snake_abs_exit Rs +395, intraweek Rs +304, snake_abs_conv Rs +280, snake_abs Rs +275, intramonth Rs +212, oracle Rs +123, random_hold Rs +98, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -93, snake_viper_wild Rs -132, benchmark_smallcap Rs -211, gold Rs -330, snake_viper_tick Rs -339, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.