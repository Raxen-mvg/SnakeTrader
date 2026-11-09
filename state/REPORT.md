# Paper trading report

Updated 2026-11-09 14:16 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,087 | +10.04% | 0 | - | 236 |
| benchmark | 217,878 | +8.94% | 0 | - | 237 |
| intraweek | 214,528 | +7.26% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 213,252 | +6.63% | 2 | 50% | 330 |
| snake_abs_exit | 212,635 | +6.32% | 2 | 50% | 308 |
| intramonth | 210,079 | +5.04% | 0 | - | 235 |
| snake_abs | 209,892 | +4.95% | 1 | 100% | 255 |
| snake_abs_conv | 209,726 | +4.86% | 1 | 100% | 255 |
| oracle | 209,430 | +4.71% | 0 | - | 233 |
| random_hold | 204,356 | +2.18% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,039 | +0.02% | 3 | 33% | 374 |
| snake_viper_wild | 200,006 | +0.00% | 7 | 57% | 1,332 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,240 | -0.88% | 0 | - | 237 |
| snake_viper_tick | 196,608 | -1.70% | 6 | 50% | 1,154 |
| gold | 192,133 | -3.93% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,320 (-4.84%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,830 | +2.32% |
| snake_abs_conv | +4,499 | +2.19% |
| unified | +4,477 | +2.08% |
| snake_abs | +4,473 | +2.18% |
| snake_abs_exit | +4,323 | +2.08% |
| snake_anaconda | +4,211 | +2.15% |
| intraweek | +4,166 | +1.98% |
| snake_viper_wild | +3,968 | +2.02% |
| snake_viper_tick | +3,898 | +2.02% |
| oracle | +3,603 | +1.75% |
| intramonth | +2,476 | +1.19% |
| benchmark_smallcap | +1,446 | +0.73% |
| gold | +1,085 | +0.57% |
| random_hold | +449 | +0.22% |
| benchmark | +390 | +0.18% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +670, benchmark Rs +596, snake_abs_exit_conv Rs +491, intraweek Rs +484, snake_abs_exit Rs +468, snake_abs_conv Rs +360, snake_abs Rs +353, intramonth Rs +336, oracle Rs +314, random_hold Rs +145, nifty_calls Rs +61, snake_anaconda Rs +2, snake_viper_wild Rs +0, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, benchmark_smallcap Rs -68, snake_viper_tick Rs -179, gold Rs -262, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.