# Paper trading report

Updated 2026-11-13 14:25 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,458 | +10.23% | 0 | - | 236 |
| benchmark | 219,018 | +9.51% | 0 | - | 237 |
| snake_abs_exit | 215,912 | +7.96% | 2 | 50% | 345 |
| intraweek | 215,825 | +7.91% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 215,797 | +7.90% | 2 | 50% | 345 |
| oracle | 212,964 | +6.48% | 0 | - | 233 |
| snake_abs | 212,075 | +6.04% | 1 | 100% | 255 |
| snake_abs_conv | 211,902 | +5.95% | 1 | 100% | 255 |
| intramonth | 210,940 | +5.47% | 0 | - | 235 |
| random_hold | 207,091 | +3.54% | 10 | 70% | 733 |
| snake_viper_wild | 205,157 | +2.58% | 14 | 50% | 2,496 |
| snake_anaconda | 204,157 | +2.08% | 3 | 33% | 374 |
| benchmark_smallcap | 202,241 | +1.12% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,648 | +0.82% | 13 | 46% | 2,299 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,963 | -8.02% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,743 (-4.13%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,167 | +0.54% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_viper_tick | -134 | -0.07% |
| snake_viper_wild | -136 | -0.07% |
| oracle | -151 | -0.07% |
| unified | -239 | -0.11% |
| intramonth | -654 | -0.31% |
| random_hold | -963 | -0.46% |
| benchmark_smallcap | -964 | -0.47% |
| gold | -1,348 | -0.73% |
| benchmark | -1,530 | -0.69% |
| snake_abs_exit | -1,531 | -0.70% |
| snake_anaconda | -1,770 | -0.86% |
| snake_abs_exit_conv | -2,877 | -1.32% |
| snake_abs_conv | -3,633 | -1.69% |
| snake_abs | -3,636 | -1.69% |

Average per day so far: unified Rs +620, benchmark Rs +576, snake_abs_exit Rs +530, snake_abs_exit_conv Rs +527, intraweek Rs +480, snake_abs_conv Rs +397, oracle Rs +393, snake_abs Rs +390, intramonth Rs +332, random_hold Rs +215, snake_viper_wild Rs +206, snake_anaconda Rs +148, benchmark_smallcap Rs +77, snake_viper_tick Rs +75, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -486

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.