# Paper trading report

Updated 2026-11-09 13:22 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,675 | +9.84% | 0 | - | 236 |
| benchmark | 217,013 | +8.51% | 0 | - | 237 |
| intraweek | 214,528 | +7.26% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,861 | +6.43% | 2 | 50% | 330 |
| snake_abs_exit | 212,466 | +6.23% | 2 | 50% | 308 |
| intramonth | 209,873 | +4.94% | 0 | - | 235 |
| snake_abs | 209,668 | +4.83% | 1 | 100% | 255 |
| snake_abs_conv | 209,503 | +4.75% | 1 | 100% | 255 |
| oracle | 209,424 | +4.71% | 0 | - | 233 |
| random_hold | 204,239 | +2.12% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,973 | -0.01% | 3 | 33% | 374 |
| snake_viper_wild | 199,638 | -0.18% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,374 | -0.81% | 0 | - | 237 |
| snake_viper_tick | 196,246 | -1.88% | 6 | 50% | 1,154 |
| gold | 192,035 | -3.98% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,178 (-4.91%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,439 | +2.13% |
| snake_abs_conv | +4,276 | +2.08% |
| snake_abs | +4,249 | +2.07% |
| intraweek | +4,165 | +1.98% |
| snake_abs_exit | +4,154 | +1.99% |
| snake_anaconda | +4,145 | +2.12% |
| unified | +4,066 | +1.89% |
| snake_viper_wild | +3,601 | +1.84% |
| oracle | +3,597 | +1.75% |
| snake_viper_tick | +3,537 | +1.83% |
| intramonth | +2,270 | +1.09% |
| benchmark_smallcap | +1,581 | +0.80% |
| gold | +986 | +0.52% |
| random_hold | +333 | +0.16% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -474 | -0.22% |

Average per day so far: unified Rs +656, benchmark Rs +567, intraweek Rs +484, snake_abs_exit_conv Rs +476, snake_abs_exit Rs +462, snake_abs_conv Rs +352, snake_abs Rs +345, intramonth Rs +329, oracle Rs +314, random_hold Rs +141, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -1, snake_viper_wild Rs -16, benchmark_smallcap Rs -63, snake_viper_tick Rs -198, gold Rs -266, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.