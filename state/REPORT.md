# Paper trading report

Updated 2026-11-09 14:31 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,184 | +10.09% | 0 | - | 236 |
| benchmark | 217,817 | +8.91% | 0 | - | 237 |
| intraweek | 214,346 | +7.17% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,643 | +6.32% | 2 | 50% | 330 |
| snake_abs_exit | 212,623 | +6.31% | 2 | 50% | 308 |
| intramonth | 210,223 | +5.11% | 0 | - | 235 |
| snake_abs | 209,984 | +4.99% | 1 | 100% | 255 |
| snake_abs_conv | 209,817 | +4.91% | 1 | 100% | 255 |
| oracle | 209,402 | +4.70% | 0 | - | 233 |
| random_hold | 204,514 | +2.26% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,017 | +0.01% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 198,320 | -0.84% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,195 | -0.90% | 0 | - | 237 |
| snake_viper_tick | 194,954 | -2.52% | 6 | 50% | 1,154 |
| gold | 192,018 | -3.99% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,314 (-4.84%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_conv | +4,590 | +2.24% |
| unified | +4,574 | +2.12% |
| snake_abs | +4,565 | +2.22% |
| snake_abs_exit | +4,311 | +2.07% |
| snake_abs_exit_conv | +4,222 | +2.02% |
| snake_anaconda | +4,190 | +2.14% |
| intraweek | +3,983 | +1.89% |
| oracle | +3,576 | +1.74% |
| intramonth | +2,620 | +1.26% |
| snake_viper_wild | +2,283 | +1.17% |
| snake_viper_tick | +2,244 | +1.16% |
| benchmark_smallcap | +1,401 | +0.71% |
| gold | +970 | +0.51% |
| random_hold | +607 | +0.30% |
| benchmark | +329 | +0.15% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +673, benchmark Rs +594, intraweek Rs +478, snake_abs_exit_conv Rs +468, snake_abs_exit Rs +468, snake_abs_conv Rs +364, snake_abs Rs +357, intramonth Rs +341, oracle Rs +313, random_hold Rs +150, nifty_calls Rs +61, snake_anaconda Rs +1, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -69, snake_viper_wild Rs -76, snake_viper_tick Rs -266, gold Rs -266, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.