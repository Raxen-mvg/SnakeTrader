# Paper trading report

Updated 2026-11-12 13:20 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,427 | +10.71% | 0 | - | 236 |
| benchmark | 220,035 | +10.02% | 0 | - | 237 |
| snake_abs_exit_conv | 218,384 | +9.19% | 2 | 50% | 345 |
| snake_abs_exit | 217,383 | +8.69% | 2 | 50% | 345 |
| snake_abs | 215,393 | +7.70% | 1 | 100% | 255 |
| snake_abs_conv | 215,220 | +7.61% | 1 | 100% | 255 |
| intraweek | 214,461 | +7.23% | 30 | 53% | 3,302 |
| oracle | 213,302 | +6.65% | 0 | - | 233 |
| intramonth | 211,975 | +5.99% | 0 | - | 235 |
| random_hold | 208,044 | +4.02% | 10 | 70% | 733 |
| snake_viper_wild | 207,327 | +3.66% | 10 | 50% | 1,825 |
| snake_anaconda | 206,172 | +3.09% | 3 | 33% | 374 |
| snake_viper_tick | 203,780 | +1.89% | 9 | 44% | 1,639 |
| benchmark_smallcap | 203,093 | +1.55% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 186,051 | -6.97% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,122 (-3.94%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,287 | +1.14% |
| snake_anaconda | +2,049 | +1.00% |
| snake_abs | +1,769 | +0.83% |
| snake_abs_conv | +1,762 | +0.83% |
| unified | +1,613 | +0.73% |
| intraweek | +1,328 | +0.62% |
| oracle | +1,299 | +0.61% |
| snake_abs_exit_conv | +1,233 | +0.57% |
| snake_abs_exit | +1,220 | +0.56% |
| intramonth | +979 | +0.46% |
| random_hold | +933 | +0.45% |
| benchmark | +773 | +0.35% |
| snake_viper_wild | +586 | +0.28% |
| snake_viper_tick | +571 | +0.28% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,535 | -1.86% |

Average per day so far: unified Rs +670, snake_abs_exit_conv Rs +634, benchmark Rs +626, snake_abs_exit Rs +599, snake_abs_conv Rs +525, snake_abs Rs +513, intraweek Rs +452, oracle Rs +416, intramonth Rs +374, snake_viper_wild Rs +305, random_hold Rs +251, snake_anaconda Rs +229, snake_viper_tick Rs +180, benchmark_smallcap Rs +110, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -436

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.