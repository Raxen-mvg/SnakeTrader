# Paper trading report

Updated 2026-11-12 12:21 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,673 | +10.84% | 0 | - | 236 |
| benchmark | 220,035 | +10.02% | 0 | - | 237 |
| snake_abs_exit_conv | 219,632 | +9.82% | 2 | 50% | 345 |
| snake_abs_exit | 218,698 | +9.35% | 2 | 50% | 345 |
| snake_abs | 216,552 | +8.28% | 1 | 100% | 255 |
| snake_abs_conv | 216,390 | +8.20% | 1 | 100% | 255 |
| intraweek | 214,870 | +7.43% | 30 | 53% | 3,302 |
| oracle | 213,442 | +6.72% | 0 | - | 233 |
| intramonth | 211,850 | +5.92% | 0 | - | 235 |
| random_hold | 208,021 | +4.01% | 10 | 70% | 733 |
| snake_viper_wild | 207,599 | +3.80% | 10 | 50% | 1,825 |
| snake_anaconda | 207,284 | +3.64% | 3 | 33% | 374 |
| snake_viper_tick | 204,047 | +2.02% | 9 | 44% | 1,639 |
| benchmark_smallcap | 203,138 | +1.57% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 186,067 | -6.97% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,447 (-3.78%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +3,161 | +1.55% |
| snake_abs_conv | +2,933 | +1.37% |
| snake_abs | +2,928 | +1.37% |
| snake_abs_exit | +2,536 | +1.17% |
| snake_abs_exit_conv | +2,481 | +1.14% |
| benchmark_smallcap | +2,332 | +1.16% |
| unified | +1,859 | +0.85% |
| intraweek | +1,737 | +0.81% |
| oracle | +1,439 | +0.68% |
| random_hold | +910 | +0.44% |
| snake_viper_wild | +857 | +0.41% |
| intramonth | +854 | +0.41% |
| snake_viper_tick | +838 | +0.41% |
| benchmark | +773 | +0.35% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,518 | -1.86% |

Average per day so far: unified Rs +677, snake_abs_exit_conv Rs +677, snake_abs_exit Rs +645, benchmark Rs +626, snake_abs_conv Rs +565, snake_abs Rs +552, intraweek Rs +465, oracle Rs +420, intramonth Rs +370, snake_viper_wild Rs +317, snake_anaconda Rs +270, random_hold Rs +251, snake_viper_tick Rs +193, benchmark_smallcap Rs +112, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -435

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.