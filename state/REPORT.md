# Paper trading report

Updated 2026-11-17 13:06 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,649 | +10.82% | 0 | - | 237 |
| unified | 221,561 | +10.78% | 0 | - | 236 |
| snake_abs_exit | 214,240 | +7.12% | 2 | 50% | 345 |
| intraweek | 213,755 | +6.88% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 212,641 | +6.32% | 2 | 50% | 345 |
| oracle | 211,952 | +5.98% | 0 | - | 233 |
| intramonth | 211,438 | +5.72% | 0 | - | 235 |
| snake_abs | 209,545 | +4.77% | 1 | 100% | 255 |
| snake_abs_conv | 209,406 | +4.70% | 1 | 100% | 255 |
| snake_viper_wild | 208,329 | +4.17% | 14 | 50% | 2,496 |
| random_hold | 207,447 | +3.72% | 10 | 70% | 733 |
| snake_anaconda | 205,060 | +2.53% | 3 | 33% | 374 |
| snake_viper_tick | 204,769 | +2.38% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,177 | +0.59% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,415 | -9.29% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,057 (-4.47%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,489 | +1.18% |
| snake_viper_wild | +2,185 | +1.06% |
| snake_viper_tick | +2,149 | +1.06% |
| benchmark | +1,568 | +0.71% |
| gold | +460 | +0.25% |
| benchmark_smallcap | +348 | +0.17% |
| unified | +123 | +0.06% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_anaconda | -43 | -0.02% |
| oracle | -71 | -0.03% |
| snake_abs_exit | -170 | -0.08% |
| intramonth | -180 | -0.09% |
| random_hold | -346 | -0.17% |
| snake_abs_exit_conv | -576 | -0.27% |
| snake_abs_conv | -583 | -0.28% |
| snake_abs | -589 | -0.28% |

Average per day so far: benchmark Rs +619, unified Rs +616, snake_abs_exit Rs +445, snake_abs_exit_conv Rs +395, intraweek Rs +393, oracle Rs +341, intramonth Rs +327, snake_viper_wild Rs +308, snake_abs_conv Rs +294, snake_abs Rs +289, random_hold Rs +213, snake_viper_tick Rs +199, snake_anaconda Rs +169, nifty_calls Rs +52, benchmark_smallcap Rs +38, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -531

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.