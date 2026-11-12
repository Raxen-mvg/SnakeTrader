# Paper trading report

Updated 2026-11-12 12:42 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,366 | +10.68% | 0 | - | 236 |
| benchmark | 219,928 | +9.96% | 0 | - | 237 |
| snake_abs_exit_conv | 218,794 | +9.40% | 2 | 50% | 345 |
| snake_abs_exit | 217,792 | +8.90% | 2 | 50% | 345 |
| snake_abs | 215,891 | +7.95% | 1 | 100% | 255 |
| snake_abs_conv | 215,722 | +7.86% | 1 | 100% | 255 |
| intraweek | 214,794 | +7.40% | 30 | 53% | 3,302 |
| oracle | 213,349 | +6.67% | 0 | - | 233 |
| intramonth | 211,733 | +5.87% | 0 | - | 235 |
| random_hold | 208,060 | +4.03% | 10 | 70% | 733 |
| snake_viper_wild | 207,048 | +3.52% | 10 | 50% | 1,825 |
| snake_anaconda | 206,497 | +3.25% | 3 | 33% | 374 |
| snake_viper_tick | 203,507 | +1.75% | 9 | 44% | 1,639 |
| benchmark_smallcap | 203,071 | +1.54% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 186,018 | -6.99% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,221 (-3.89%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +2,374 | +1.16% |
| snake_abs | +2,266 | +1.06% |
| benchmark_smallcap | +2,264 | +1.13% |
| snake_abs_conv | +2,264 | +1.06% |
| intraweek | +1,661 | +0.78% |
| snake_abs_exit_conv | +1,643 | +0.76% |
| snake_abs_exit | +1,630 | +0.75% |
| unified | +1,553 | +0.71% |
| oracle | +1,346 | +0.64% |
| random_hold | +949 | +0.46% |
| intramonth | +737 | +0.35% |
| benchmark | +666 | +0.30% |
| snake_viper_wild | +306 | +0.15% |
| snake_viper_tick | +298 | +0.15% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,567 | -1.88% |

Average per day so far: unified Rs +668, snake_abs_exit_conv Rs +648, benchmark Rs +623, snake_abs_exit Rs +614, snake_abs_conv Rs +542, snake_abs Rs +530, intraweek Rs +462, oracle Rs +417, intramonth Rs +367, snake_viper_wild Rs +294, random_hold Rs +252, snake_anaconda Rs +241, snake_viper_tick Rs +167, benchmark_smallcap Rs +110, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -437

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.