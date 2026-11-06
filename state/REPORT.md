# Paper trading report

Updated 2026-11-06 10:31 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,193 | +7.60% | 0 | - | 237 |
| unified | 214,894 | +7.45% | 0 | - | 236 |
| intraweek | 210,856 | +5.43% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,719 | +4.86% | 1 | 100% | 255 |
| snake_abs_exit | 209,504 | +4.75% | 1 | 100% | 260 |
| intramonth | 206,827 | +3.41% | 0 | - | 235 |
| snake_abs | 206,668 | +3.33% | 1 | 100% | 255 |
| snake_abs_conv | 206,499 | +3.25% | 1 | 100% | 255 |
| oracle | 204,811 | +2.41% | 0 | - | 233 |
| random_hold | 203,425 | +1.71% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 197,898 | -1.05% | 3 | 33% | 702 |
| snake_anaconda | 196,809 | -1.59% | 3 | 33% | 374 |
| benchmark_smallcap | 195,202 | -2.40% | 0 | - | 237 |
| snake_viper_tick | 194,537 | -2.73% | 2 | 0% | 532 |
| gold | 189,898 | -5.05% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,518 (-6.24%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,437 | +0.69% |
| benchmark | +1,423 | +0.67% |
| oracle | +739 | +0.36% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -898 | -0.44% |
| unified | -1,089 | -0.50% |
| intramonth | -1,121 | -0.54% |
| benchmark_smallcap | -3,486 | -1.75% |
| gold | -4,324 | -2.23% |
| snake_abs | -5,020 | -2.37% |
| snake_abs_conv | -5,046 | -2.38% |
| snake_abs_exit_conv | -5,085 | -2.37% |
| snake_abs_exit | -5,154 | -2.40% |
| snake_anaconda | -5,670 | -2.80% |
| snake_viper_tick | -6,601 | -3.28% |
| snake_viper_wild | -6,758 | -3.30% |

Average per day so far: benchmark Rs +524, unified Rs +514, intraweek Rs +374, snake_abs_exit_conv Rs +374, snake_abs_exit Rs +366, snake_abs_conv Rs +250, snake_abs Rs +247, intramonth Rs +235, oracle Rs +166, random_hold Rs +118, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -100, snake_anaconda Rs -133, benchmark_smallcap Rs -192, snake_viper_tick Rs -304, gold Rs -348, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.