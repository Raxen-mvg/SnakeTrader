# Paper trading report

Updated 2026-11-17 13:22 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,535 | +10.77% | 0 | - | 236 |
| benchmark | 221,450 | +10.72% | 0 | - | 237 |
| snake_abs_exit | 214,163 | +7.08% | 2 | 50% | 345 |
| intraweek | 214,095 | +7.05% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 212,561 | +6.28% | 2 | 50% | 345 |
| oracle | 212,131 | +6.07% | 0 | - | 233 |
| intramonth | 211,362 | +5.68% | 0 | - | 235 |
| snake_abs | 209,391 | +4.70% | 1 | 100% | 255 |
| snake_abs_conv | 209,250 | +4.62% | 1 | 100% | 255 |
| snake_viper_wild | 208,887 | +4.44% | 14 | 50% | 2,496 |
| random_hold | 207,445 | +3.72% | 10 | 70% | 733 |
| snake_viper_tick | 205,317 | +2.66% | 13 | 46% | 2,299 |
| snake_anaconda | 204,977 | +2.49% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,076 | +0.54% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,300 | -9.35% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,127 (-4.44%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,829 | +1.34% |
| snake_viper_wild | +2,743 | +1.33% |
| snake_viper_tick | +2,697 | +1.33% |
| benchmark | +1,369 | +0.62% |
| gold | +345 | +0.19% |
| benchmark_smallcap | +247 | +0.12% |
| oracle | +108 | +0.05% |
| unified | +97 | +0.04% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_anaconda | -125 | -0.06% |
| snake_abs_exit | -247 | -0.12% |
| intramonth | -257 | -0.12% |
| random_hold | -349 | -0.17% |
| snake_abs_exit_conv | -657 | -0.31% |
| snake_abs_conv | -739 | -0.35% |
| snake_abs | -743 | -0.35% |

Average per day so far: unified Rs +615, benchmark Rs +613, snake_abs_exit Rs +443, intraweek Rs +403, snake_abs_exit_conv Rs +393, oracle Rs +347, snake_viper_wild Rs +329, intramonth Rs +325, snake_abs_conv Rs +289, snake_abs Rs +285, snake_viper_tick Rs +222, random_hold Rs +213, snake_anaconda Rs +166, nifty_calls Rs +52, benchmark_smallcap Rs +35, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -534

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.