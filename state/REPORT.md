# Paper trading report

Updated 2026-11-17 13:42 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,700 | +10.85% | 0 | - | 236 |
| benchmark | 221,664 | +10.83% | 0 | - | 237 |
| snake_abs_exit | 214,751 | +7.38% | 2 | 50% | 345 |
| intraweek | 213,398 | +6.70% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 213,078 | +6.54% | 2 | 50% | 345 |
| oracle | 212,308 | +6.15% | 0 | - | 233 |
| intramonth | 211,624 | +5.81% | 0 | - | 235 |
| snake_abs | 209,961 | +4.98% | 1 | 100% | 255 |
| snake_abs_conv | 209,824 | +4.91% | 1 | 100% | 255 |
| snake_viper_wild | 209,264 | +4.63% | 14 | 50% | 2,496 |
| random_hold | 207,510 | +3.75% | 10 | 70% | 733 |
| snake_viper_tick | 205,687 | +2.84% | 13 | 46% | 2,299 |
| snake_anaconda | 205,568 | +2.78% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,076 | +0.54% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,872 | -9.56% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,160 (-4.42%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,120 | +1.51% |
| snake_viper_tick | +3,068 | +1.51% |
| intraweek | +2,132 | +1.01% |
| benchmark | +1,584 | +0.72% |
| snake_anaconda | +465 | +0.23% |
| snake_abs_exit | +342 | +0.16% |
| oracle | +285 | +0.14% |
| unified | +262 | +0.12% |
| benchmark_smallcap | +247 | +0.12% |
| intramonth | +5 | +0.00% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold | -82 | -0.04% |
| snake_abs_exit_conv | -139 | -0.07% |
| snake_abs_conv | -166 | -0.08% |
| snake_abs | -172 | -0.08% |
| random_hold | -283 | -0.14% |

Average per day so far: unified Rs +620, benchmark Rs +619, snake_abs_exit Rs +461, snake_abs_exit_conv Rs +409, intraweek Rs +383, oracle Rs +352, snake_viper_wild Rs +343, intramonth Rs +332, snake_abs_conv Rs +307, snake_abs Rs +302, snake_viper_tick Rs +237, random_hold Rs +215, snake_anaconda Rs +186, nifty_calls Rs +52, benchmark_smallcap Rs +35, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -547

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.