# Paper trading report

Updated 2026-11-17 14:37 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,948 | +10.97% | 0 | - | 237 |
| unified | 221,498 | +10.75% | 0 | - | 236 |
| intraweek | 214,219 | +7.11% | 35 | 54% | 3,851 |
| snake_abs_exit | 213,445 | +6.72% | 2 | 50% | 345 |
| oracle | 212,319 | +6.16% | 0 | - | 233 |
| snake_abs_exit_conv | 211,846 | +5.92% | 2 | 50% | 345 |
| intramonth | 211,392 | +5.70% | 0 | - | 235 |
| snake_viper_wild | 209,451 | +4.72% | 14 | 50% | 2,496 |
| snake_abs | 208,649 | +4.33% | 1 | 100% | 255 |
| snake_abs_conv | 208,510 | +4.25% | 1 | 100% | 255 |
| random_hold | 207,802 | +3.90% | 10 | 70% | 733 |
| snake_viper_tick | 205,872 | +2.94% | 13 | 46% | 2,299 |
| snake_anaconda | 204,184 | +2.09% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,199 | +0.60% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,856 | -9.57% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,209 (-4.40%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,306 | +1.60% |
| snake_viper_tick | +3,252 | +1.60% |
| intraweek | +2,953 | +1.40% |
| benchmark | +1,867 | +0.85% |
| benchmark_smallcap | +370 | +0.18% |
| oracle | +296 | +0.14% |
| unified | +60 | +0.03% |
| random_hold | +9 | +0.00% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold | -99 | -0.06% |
| intramonth | -227 | -0.11% |
| snake_anaconda | -918 | -0.45% |
| snake_abs_exit | -964 | -0.45% |
| snake_abs_exit_conv | -1,372 | -0.64% |
| snake_abs_conv | -1,479 | -0.70% |
| snake_abs | -1,484 | -0.71% |

Average per day so far: benchmark Rs +627, unified Rs +614, snake_abs_exit Rs +420, intraweek Rs +406, snake_abs_exit_conv Rs +370, oracle Rs +352, snake_viper_wild Rs +350, intramonth Rs +325, snake_abs_conv Rs +266, snake_abs Rs +262, snake_viper_tick Rs +245, random_hold Rs +223, snake_anaconda Rs +139, nifty_calls Rs +52, benchmark_smallcap Rs +39, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -547

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.