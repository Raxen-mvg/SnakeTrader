# Paper trading report

Updated 2026-11-13 11:19 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,459 | +10.23% | 0 | - | 236 |
| benchmark | 219,614 | +9.81% | 0 | - | 237 |
| snake_abs_exit | 216,529 | +8.27% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,525 | +8.26% | 2 | 50% | 345 |
| intraweek | 216,162 | +8.08% | 30 | 53% | 3,302 |
| oracle | 213,533 | +6.77% | 0 | - | 233 |
| snake_abs | 212,754 | +6.38% | 1 | 100% | 255 |
| snake_abs_conv | 212,586 | +6.29% | 1 | 100% | 255 |
| intramonth | 211,317 | +5.66% | 0 | - | 235 |
| random_hold | 207,096 | +3.55% | 10 | 70% | 733 |
| snake_viper_wild | 206,128 | +3.06% | 14 | 50% | 2,496 |
| snake_anaconda | 204,866 | +2.43% | 3 | 33% | 374 |
| benchmark_smallcap | 203,116 | +1.56% | 0 | - | 237 |
| snake_viper_tick | 202,603 | +1.30% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,667 | -8.17% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,061 (-3.97%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,504 | +0.70% |
| snake_viper_wild | +836 | +0.41% |
| snake_viper_tick | +821 | +0.41% |
| oracle | +418 | +0.20% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| benchmark_smallcap | -90 | -0.04% |
| unified | -238 | -0.11% |
| intramonth | -276 | -0.13% |
| snake_abs_exit | -913 | -0.42% |
| benchmark | -933 | -0.42% |
| random_hold | -958 | -0.46% |
| snake_anaconda | -1,061 | -0.52% |
| gold | -1,644 | -0.89% |
| snake_abs_exit_conv | -2,149 | -0.98% |
| snake_abs_conv | -2,949 | -1.37% |
| snake_abs | -2,957 | -1.37% |

Average per day so far: unified Rs +620, benchmark Rs +594, snake_abs_exit Rs +551, snake_abs_exit_conv Rs +551, intraweek Rs +490, snake_abs_conv Rs +420, snake_abs Rs +411, oracle Rs +410, intramonth Rs +343, snake_viper_wild Rs +245, random_hold Rs +215, snake_anaconda Rs +174, snake_viper_tick Rs +118, benchmark_smallcap Rs +107, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -495

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.