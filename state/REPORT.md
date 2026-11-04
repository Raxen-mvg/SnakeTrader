# Paper trading report

Updated 2026-11-04 13:28 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,254 | +7.13% | 0 | - | 236 |
| snake_abs_exit_conv | 212,397 | +6.20% | 1 | 100% | 255 |
| snake_abs_exit | 212,262 | +6.13% | 1 | 100% | 260 |
| snake_abs | 209,296 | +4.65% | 1 | 100% | 255 |
| snake_abs_conv | 209,144 | +4.57% | 1 | 100% | 255 |
| intraweek | 209,142 | +4.57% | 25 | 48% | 2,757 |
| benchmark | 208,254 | +4.13% | 0 | - | 237 |
| snake_viper_wild | 207,043 | +3.52% | 3 | 33% | 702 |
| intramonth | 206,454 | +3.23% | 0 | - | 235 |
| snake_viper_tick | 203,435 | +1.72% | 2 | 0% | 532 |
| random_hold | 202,781 | +1.39% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,299 | +0.65% | 0 | - | 233 |
| snake_anaconda | 200,934 | +0.47% | 3 | 33% | 361 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 195,740 | -2.13% | 0 | - | 237 |
| gold | 190,687 | -4.66% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,349 (-5.33%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +8,247 | +4.04% |
| snake_abs_exit_conv | +8,059 | +3.94% |
| snake_abs_conv | +8,003 | +3.98% |
| snake_abs | +7,987 | +3.97% |
| snake_anaconda | +7,110 | +3.67% |
| gold | +5,409 | +2.92% |
| intraweek | +4,056 | +1.98% |
| benchmark_smallcap | +2,802 | +1.45% |
| intramonth | +2,483 | +1.22% |
| random_hold | +2,312 | +1.15% |
| unified | +2,253 | +1.06% |
| benchmark | +1,553 | +0.75% |
| oracle | +1,310 | +0.66% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,731 | -1.80% |
| snake_viper_wild | -3,850 | -1.82% |

Average per day so far: unified Rs +528, snake_abs_exit_conv Rs +517, snake_abs_exit Rs +511, snake_abs_conv Rs +381, snake_abs Rs +372, snake_viper_wild Rs +371, intraweek Rs +339, benchmark Rs +306, intramonth Rs +239, snake_viper_tick Rs +215, random_hold Rs +103, nifty_calls Rs +68, oracle Rs +48, snake_anaconda Rs +42, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -185, gold Rs -345, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.