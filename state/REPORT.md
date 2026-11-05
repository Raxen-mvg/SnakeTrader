# Paper trading report

Updated 2026-11-05 15:30 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 215,983 | +7.99% | 0 | - | 236 |
| snake_abs_exit_conv | 214,803 | +7.40% | 1 | 100% | 255 |
| snake_abs_exit | 214,659 | +7.33% | 1 | 100% | 260 |
| benchmark | 213,770 | +6.88% | 0 | - | 237 |
| snake_abs | 211,688 | +5.84% | 1 | 100% | 255 |
| snake_abs_conv | 211,545 | +5.77% | 1 | 100% | 255 |
| intraweek | 209,418 | +4.71% | 25 | 48% | 2,757 |
| intramonth | 207,949 | +3.97% | 0 | - | 235 |
| snake_viper_wild | 204,656 | +2.33% | 3 | 33% | 702 |
| random_hold | 204,323 | +2.16% | 8 | 62% | 649 |
| oracle | 204,072 | +2.04% | 0 | - | 233 |
| snake_anaconda | 202,479 | +1.24% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,138 | +0.57% | 2 | 0% | 532 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,688 | -0.66% | 0 | - | 237 |
| gold | 194,221 | -2.89% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,409 (-5.30%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,011 | +2.40% |
| gold | +2,828 | +1.48% |
| oracle | +2,280 | +1.13% |
| benchmark_smallcap | +2,018 | +1.03% |
| unified | +1,544 | +0.72% |
| random_hold | +1,014 | +0.50% |
| intramonth | +933 | +0.45% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs_exit_conv | -212 | -0.10% |
| snake_abs_conv | -213 | -0.10% |
| snake_abs | -215 | -0.10% |
| snake_abs_exit | -241 | -0.11% |
| intraweek | -279 | -0.13% |
| snake_anaconda | -1,341 | -0.66% |
| snake_viper_tick | -4,262 | -2.08% |
| snake_viper_wild | -4,374 | -2.09% |

Average per day so far: snake_abs_exit_conv Rs +592, snake_abs_exit Rs +586, unified Rs +571, benchmark Rs +492, snake_abs_conv Rs +462, snake_abs Rs +450, intraweek Rs +336, intramonth Rs +284, snake_viper_wild Rs +233, random_hold Rs +154, oracle Rs +145, snake_anaconda Rs +108, snake_viper_tick Rs +67, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -55, gold Rs -206, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.