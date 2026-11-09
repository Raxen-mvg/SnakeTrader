# Paper trading report

Updated 2026-11-09 13:28 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,656 | +9.83% | 0 | - | 236 |
| benchmark | 217,013 | +8.51% | 0 | - | 237 |
| intraweek | 214,714 | +7.36% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,920 | +6.46% | 2 | 50% | 330 |
| snake_abs_exit | 212,561 | +6.28% | 2 | 50% | 308 |
| intramonth | 209,851 | +4.92% | 0 | - | 235 |
| snake_abs | 209,768 | +4.88% | 1 | 100% | 255 |
| snake_abs_conv | 209,604 | +4.80% | 1 | 100% | 255 |
| oracle | 209,433 | +4.72% | 0 | - | 233 |
| random_hold | 204,298 | +2.15% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,070 | +0.04% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 199,425 | -0.29% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,352 | -0.82% | 0 | - | 237 |
| snake_viper_tick | 196,037 | -1.98% | 6 | 50% | 1,154 |
| gold | 191,986 | -4.01% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,226 (-4.89%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,498 | +2.16% |
| snake_abs_conv | +4,377 | +2.13% |
| intraweek | +4,352 | +2.07% |
| snake_abs | +4,349 | +2.12% |
| snake_abs_exit | +4,249 | +2.04% |
| snake_anaconda | +4,243 | +2.17% |
| unified | +4,047 | +1.88% |
| oracle | +3,606 | +1.75% |
| snake_viper_wild | +3,388 | +1.73% |
| snake_viper_tick | +3,328 | +1.73% |
| intramonth | +2,248 | +1.08% |
| benchmark_smallcap | +1,558 | +0.79% |
| gold | +937 | +0.49% |
| random_hold | +392 | +0.19% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -474 | -0.22% |

Average per day so far: unified Rs +655, benchmark Rs +567, intraweek Rs +490, snake_abs_exit_conv Rs +479, snake_abs_exit Rs +465, snake_abs_conv Rs +356, snake_abs Rs +349, intramonth Rs +328, oracle Rs +314, random_hold Rs +143, nifty_calls Rs +61, snake_anaconda Rs +3, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, snake_viper_wild Rs -26, benchmark_smallcap Rs -63, snake_viper_tick Rs -209, gold Rs -267, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.