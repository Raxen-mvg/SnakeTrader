# Paper trading report

Updated 2026-11-13 11:28 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,444 | +10.22% | 0 | - | 236 |
| benchmark | 219,538 | +9.77% | 0 | - | 237 |
| snake_abs_exit_conv | 216,529 | +8.26% | 2 | 50% | 345 |
| snake_abs_exit | 216,467 | +8.23% | 2 | 50% | 345 |
| intraweek | 216,282 | +8.14% | 30 | 53% | 3,302 |
| oracle | 213,520 | +6.76% | 0 | - | 233 |
| snake_abs | 212,706 | +6.35% | 1 | 100% | 255 |
| snake_abs_conv | 212,538 | +6.27% | 1 | 100% | 255 |
| intramonth | 211,198 | +5.60% | 0 | - | 235 |
| random_hold | 207,257 | +3.63% | 10 | 70% | 733 |
| snake_viper_wild | 206,117 | +3.06% | 14 | 50% | 2,496 |
| snake_anaconda | 204,839 | +2.42% | 3 | 33% | 374 |
| benchmark_smallcap | 203,239 | +1.62% | 0 | - | 237 |
| snake_viper_tick | 202,591 | +1.30% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,897 | -8.05% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,079 (-3.96%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,624 | +0.76% |
| snake_viper_wild | +824 | +0.40% |
| snake_viper_tick | +810 | +0.40% |
| oracle | +405 | +0.19% |
| benchmark_smallcap | +34 | +0.02% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -253 | -0.11% |
| intramonth | -396 | -0.19% |
| random_hold | -797 | -0.38% |
| snake_abs_exit | -975 | -0.45% |
| benchmark | -1,010 | -0.46% |
| snake_anaconda | -1,088 | -0.53% |
| gold | -1,414 | -0.76% |
| snake_abs_exit_conv | -2,145 | -0.98% |
| snake_abs_conv | -2,997 | -1.39% |
| snake_abs | -3,005 | -1.39% |

Average per day so far: unified Rs +620, benchmark Rs +592, snake_abs_exit_conv Rs +551, snake_abs_exit Rs +549, intraweek Rs +493, snake_abs_conv Rs +418, snake_abs Rs +410, oracle Rs +410, intramonth Rs +339, snake_viper_wild Rs +245, random_hold Rs +220, snake_anaconda Rs +173, snake_viper_tick Rs +118, benchmark_smallcap Rs +112, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -488

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.