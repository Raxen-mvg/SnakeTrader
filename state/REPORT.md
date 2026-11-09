# Paper trading report

Updated 2026-11-09 13:31 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,519 | +9.76% | 0 | - | 236 |
| benchmark | 216,983 | +8.49% | 0 | - | 237 |
| intraweek | 214,740 | +7.37% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,917 | +6.46% | 2 | 50% | 330 |
| snake_abs_exit | 212,559 | +6.28% | 2 | 50% | 308 |
| snake_abs | 209,766 | +4.88% | 1 | 100% | 255 |
| intramonth | 209,684 | +4.84% | 0 | - | 235 |
| snake_abs_conv | 209,601 | +4.80% | 1 | 100% | 255 |
| oracle | 209,340 | +4.67% | 0 | - | 233 |
| random_hold | 204,257 | +2.13% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,067 | +0.03% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 199,425 | -0.29% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,318 | -0.84% | 0 | - | 237 |
| snake_viper_tick | 196,037 | -1.98% | 6 | 50% | 1,154 |
| gold | 192,133 | -3.93% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,169 (-4.92%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,495 | +2.16% |
| intraweek | +4,378 | +2.08% |
| snake_abs_conv | +4,374 | +2.13% |
| snake_abs | +4,346 | +2.12% |
| snake_abs_exit | +4,247 | +2.04% |
| snake_anaconda | +4,240 | +2.17% |
| unified | +3,910 | +1.81% |
| oracle | +3,513 | +1.71% |
| snake_viper_wild | +3,388 | +1.73% |
| snake_viper_tick | +3,328 | +1.73% |
| intramonth | +2,081 | +1.00% |
| benchmark_smallcap | +1,525 | +0.78% |
| gold | +1,085 | +0.57% |
| random_hold | +351 | +0.17% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -505 | -0.23% |

Average per day so far: unified Rs +651, benchmark Rs +566, intraweek Rs +491, snake_abs_exit_conv Rs +478, snake_abs_exit Rs +465, snake_abs_conv Rs +356, snake_abs Rs +349, intramonth Rs +323, oracle Rs +311, random_hold Rs +142, nifty_calls Rs +61, snake_anaconda Rs +3, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, snake_viper_wild Rs -26, benchmark_smallcap Rs -65, snake_viper_tick Rs -209, gold Rs -262, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.