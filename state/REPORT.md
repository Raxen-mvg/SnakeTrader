# Paper trading report

Updated 2026-11-09 12:43 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,998 | +10.00% | 0 | - | 236 |
| benchmark | 217,143 | +8.57% | 0 | - | 237 |
| intraweek | 215,177 | +7.59% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,246 | +6.12% | 2 | 50% | 330 |
| snake_abs_exit | 211,962 | +5.98% | 2 | 50% | 308 |
| intramonth | 210,078 | +5.04% | 0 | - | 235 |
| snake_abs | 209,759 | +4.88% | 1 | 100% | 255 |
| oracle | 209,673 | +4.84% | 0 | - | 233 |
| snake_abs_conv | 209,580 | +4.79% | 1 | 100% | 255 |
| random_hold | 204,378 | +2.19% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,464 | -0.27% | 3 | 33% | 374 |
| snake_viper_wild | 199,414 | -0.29% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,643 | -0.68% | 0 | - | 237 |
| snake_viper_tick | 196,028 | -1.99% | 6 | 50% | 1,154 |
| gold | 192,347 | -3.83% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,399 (-4.80%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +4,814 | +2.29% |
| unified | +4,389 | +2.04% |
| snake_abs_conv | +4,353 | +2.12% |
| snake_abs | +4,339 | +2.11% |
| oracle | +3,846 | +1.87% |
| snake_abs_exit_conv | +3,824 | +1.83% |
| snake_abs_exit | +3,650 | +1.75% |
| snake_anaconda | +3,637 | +1.86% |
| snake_viper_wild | +3,377 | +1.72% |
| snake_viper_tick | +3,318 | +1.72% |
| intramonth | +2,475 | +1.19% |
| benchmark_smallcap | +1,850 | +0.94% |
| gold | +1,299 | +0.68% |
| random_hold | +472 | +0.23% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -344 | -0.16% |

Average per day so far: unified Rs +667, benchmark Rs +571, intraweek Rs +506, snake_abs_exit_conv Rs +454, snake_abs_exit Rs +443, snake_abs_conv Rs +355, snake_abs Rs +349, intramonth Rs +336, oracle Rs +322, random_hold Rs +146, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -21, snake_viper_wild Rs -27, benchmark_smallcap Rs -52, snake_viper_tick Rs -209, gold Rs -255, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.