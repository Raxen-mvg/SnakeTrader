# Paper trading report

Updated 2026-11-16 12:39 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,732 | +10.37% | 0 | - | 236 |
| benchmark | 220,265 | +10.13% | 0 | - | 237 |
| snake_abs_exit | 213,466 | +6.73% | 2 | 50% | 345 |
| intraweek | 213,037 | +6.52% | 35 | 54% | 3,851 |
| oracle | 212,900 | +6.45% | 0 | - | 233 |
| snake_abs_exit_conv | 212,170 | +6.08% | 2 | 50% | 345 |
| intramonth | 211,639 | +5.82% | 0 | - | 235 |
| snake_abs | 209,283 | +4.64% | 1 | 100% | 255 |
| snake_abs_conv | 209,117 | +4.56% | 1 | 100% | 255 |
| random_hold | 207,986 | +3.99% | 10 | 70% | 733 |
| snake_viper_wild | 205,048 | +2.52% | 14 | 50% | 2,496 |
| snake_anaconda | 203,570 | +1.78% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,541 | +0.77% | 13 | 46% | 2,299 |
| benchmark_smallcap | 201,199 | +0.60% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,069 | -9.46% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,263 (-4.37%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,712 | +0.78% |
| intramonth | +1,582 | +0.75% |
| benchmark | +926 | +0.42% |
| random_hold | +760 | +0.37% |
| snake_viper_wild | +291 | +0.14% |
| snake_viper_tick | +286 | +0.14% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -197 | -0.09% |
| snake_anaconda | -1,322 | -0.65% |
| benchmark_smallcap | -1,670 | -0.82% |
| gold | -2,926 | -1.59% |
| intraweek | -3,108 | -1.44% |
| snake_abs_conv | -3,249 | -1.53% |
| snake_abs | -3,257 | -1.53% |
| snake_abs_exit | -3,519 | -1.62% |
| snake_abs_exit_conv | -4,211 | -1.95% |

Average per day so far: unified Rs +610, benchmark Rs +596, snake_abs_exit Rs +434, snake_abs_exit_conv Rs +393, intraweek Rs +383, oracle Rs +379, intramonth Rs +342, snake_abs_conv Rs +294, snake_abs Rs +290, random_hold Rs +235, snake_viper_wild Rs +194, snake_anaconda Rs +123, snake_viper_tick Rs +67, nifty_calls Rs +54, benchmark_smallcap Rs +40, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -347, snake Rs -368, gold Rs -557

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.