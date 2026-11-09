# Paper trading report

Updated 2026-11-09 12:50 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,941 | +9.97% | 0 | - | 236 |
| benchmark | 217,266 | +8.63% | 0 | - | 237 |
| intraweek | 214,961 | +7.48% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,229 | +6.12% | 2 | 50% | 330 |
| snake_abs_exit | 211,931 | +5.96% | 2 | 50% | 308 |
| intramonth | 210,071 | +5.04% | 0 | - | 235 |
| snake_abs | 209,632 | +4.82% | 1 | 100% | 255 |
| oracle | 209,560 | +4.78% | 0 | - | 233 |
| snake_abs_conv | 209,453 | +4.73% | 1 | 100% | 255 |
| random_hold | 204,442 | +2.22% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 199,414 | -0.29% | 7 | 57% | 1,332 |
| snake_anaconda | 199,377 | -0.31% | 3 | 33% | 374 |
| benchmark_smallcap | 198,542 | -0.73% | 0 | - | 237 |
| snake_viper_tick | 196,028 | -1.99% | 6 | 50% | 1,154 |
| gold | 192,413 | -3.79% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,326 (-4.84%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +4,599 | +2.19% |
| unified | +4,331 | +2.01% |
| snake_abs_conv | +4,226 | +2.06% |
| snake_abs | +4,213 | +2.05% |
| snake_abs_exit_conv | +3,808 | +1.83% |
| oracle | +3,733 | +1.81% |
| snake_abs_exit | +3,619 | +1.74% |
| snake_anaconda | +3,550 | +1.81% |
| snake_viper_wild | +3,376 | +1.72% |
| snake_viper_tick | +3,318 | +1.72% |
| intramonth | +2,468 | +1.19% |
| benchmark_smallcap | +1,749 | +0.89% |
| gold | +1,365 | +0.71% |
| random_hold | +536 | +0.26% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -222 | -0.10% |

Average per day so far: unified Rs +665, benchmark Rs +576, intraweek Rs +499, snake_abs_exit_conv Rs +453, snake_abs_exit Rs +442, snake_abs_conv Rs +350, snake_abs Rs +344, intramonth Rs +336, oracle Rs +319, random_hold Rs +148, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -25, snake_viper_wild Rs -27, benchmark_smallcap Rs -56, snake_viper_tick Rs -209, gold Rs -253, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.