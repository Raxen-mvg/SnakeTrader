# Paper trading report

Updated 2026-11-17 09:52 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,175 | +11.59% | 0 | - | 236 |
| benchmark | 221,213 | +10.61% | 0 | - | 237 |
| snake_abs_exit | 215,000 | +7.50% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,568 | +6.78% | 2 | 50% | 345 |
| intramonth | 213,481 | +6.74% | 0 | - | 235 |
| oracle | 213,065 | +6.53% | 0 | - | 233 |
| intraweek | 212,657 | +6.33% | 35 | 54% | 3,851 |
| snake_abs | 210,156 | +5.08% | 1 | 100% | 255 |
| snake_abs_conv | 210,010 | +5.00% | 1 | 100% | 255 |
| random_hold | 208,108 | +4.05% | 10 | 70% | 733 |
| snake_viper_wild | 206,888 | +3.44% | 14 | 50% | 2,496 |
| snake_anaconda | 205,624 | +2.81% | 3 | 33% | 374 |
| snake_viper_tick | 203,351 | +1.68% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,174 | +1.09% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,135 | -9.43% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,961 (-4.02%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intramonth | +1,862 | +0.88% |
| unified | +1,737 | +0.78% |
| intraweek | +1,391 | +0.66% |
| benchmark_smallcap | +1,345 | +0.67% |
| benchmark | +1,132 | +0.51% |
| oracle | +1,042 | +0.49% |
| snake_viper_wild | +744 | +0.36% |
| snake_viper_tick | +731 | +0.36% |
| snake_abs_exit | +591 | +0.28% |
| snake_anaconda | +521 | +0.25% |
| snake_abs_exit_conv | +351 | +0.17% |
| random_hold | +315 | +0.15% |
| gold | +181 | +0.10% |
| snake_abs | +23 | +0.01% |
| snake_abs_conv | +20 | +0.01% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +662, benchmark Rs +606, snake_abs_exit Rs +469, snake_abs_exit_conv Rs +424, intramonth Rs +385, oracle Rs +373, intraweek Rs +362, snake_abs_conv Rs +313, snake_abs Rs +308, snake_viper_wild Rs +255, random_hold Rs +232, snake_anaconda Rs +187, snake_viper_tick Rs +140, benchmark_smallcap Rs +70, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -539

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.