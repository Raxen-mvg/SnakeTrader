# Paper trading report

Updated 2026-11-27 12:52 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,281 | +12.14% | 0 | - | 237 |
| unified | 223,373 | +11.69% | 0 | - | 236 |
| oracle | 211,908 | +5.95% | 0 | - | 233 |
| intramonth | 210,900 | +5.45% | 0 | - | 235 |
| random_hold | 210,465 | +5.23% | 13 | 69% | 1,037 |
| intraweek | 208,161 | +4.08% | 40 | 55% | 4,400 |
| snake_abs_exit | 204,958 | +2.48% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,860 | +1.93% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,681 | +0.84% | 0 | - | 237 |
| snake_abs | 200,568 | +0.28% | 1 | 100% | 255 |
| snake_abs_conv | 200,388 | +0.19% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,907 | -3.05% | 3 | 33% | 374 |
| snake_viper_wild | 192,390 | -3.81% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,122 | -5.44% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,660 | -15.17% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,837 (-5.58%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +3,881 | +1.93% |
| gold | +3,666 | +2.21% |
| snake_abs_exit_conv | +3,463 | +1.73% |
| snake_abs_conv | +2,021 | +1.02% |
| snake_abs | +2,016 | +1.01% |
| random_hold | +1,871 | +0.90% |
| snake_anaconda | +1,610 | +0.84% |
| intraweek | +1,113 | +0.54% |
| benchmark_smallcap | +841 | +0.42% |
| intramonth | +366 | +0.17% |
| unified | +294 | +0.13% |
| snake_viper_wild | +184 | +0.10% |
| snake_viper_tick | +181 | +0.10% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -328 | -0.15% |
| benchmark | -1,706 | -0.76% |

Average per day so far: benchmark Rs +578, unified Rs +556, oracle Rs +284, intramonth Rs +260, random_hold Rs +249, intraweek Rs +194, snake_abs_exit Rs +127, snake_abs_exit_conv Rs +99, benchmark_smallcap Rs +44, nifty_calls Rs +44, snake_abs Rs +14, snake_abs_conv Rs +10, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -165, snake_viper_wild Rs -224, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -351, gold Rs -722

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.