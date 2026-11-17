# Paper trading report

Updated 2026-11-17 14:41 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,948 | +10.97% | 0 | - | 237 |
| unified | 221,392 | +10.70% | 0 | - | 236 |
| intraweek | 214,063 | +7.03% | 35 | 54% | 3,851 |
| snake_abs_exit | 213,255 | +6.63% | 2 | 50% | 345 |
| oracle | 212,123 | +6.06% | 0 | - | 233 |
| snake_abs_exit_conv | 211,718 | +5.86% | 2 | 50% | 345 |
| intramonth | 211,315 | +5.66% | 0 | - | 235 |
| snake_viper_wild | 209,433 | +4.72% | 14 | 50% | 2,496 |
| snake_abs | 208,557 | +4.28% | 1 | 100% | 255 |
| snake_abs_conv | 208,417 | +4.21% | 1 | 100% | 255 |
| random_hold | 207,769 | +3.88% | 10 | 70% | 733 |
| snake_viper_tick | 205,854 | +2.93% | 13 | 46% | 2,299 |
| snake_anaconda | 203,954 | +1.98% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,177 | +0.59% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,757 | -9.62% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,098 (-4.45%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,289 | +1.60% |
| snake_viper_tick | +3,234 | +1.60% |
| intraweek | +2,797 | +1.32% |
| benchmark | +1,867 | +0.85% |
| benchmark_smallcap | +348 | +0.17% |
| oracle | +100 | +0.05% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -25 | -0.01% |
| unified | -45 | -0.02% |
| gold | -197 | -0.11% |
| intramonth | -304 | -0.14% |
| snake_anaconda | -1,149 | -0.56% |
| snake_abs_exit | -1,154 | -0.54% |
| snake_abs_exit_conv | -1,499 | -0.70% |
| snake_abs_conv | -1,573 | -0.75% |
| snake_abs | -1,577 | -0.75% |

Average per day so far: benchmark Rs +627, unified Rs +611, snake_abs_exit Rs +414, intraweek Rs +402, snake_abs_exit_conv Rs +366, snake_viper_wild Rs +349, oracle Rs +346, intramonth Rs +323, snake_abs_conv Rs +263, snake_abs Rs +259, snake_viper_tick Rs +244, random_hold Rs +222, snake_anaconda Rs +132, nifty_calls Rs +52, benchmark_smallcap Rs +38, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -550

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.