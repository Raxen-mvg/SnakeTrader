# Paper trading report

Updated 2026-11-12 15:04 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,629 | +10.31% | 0 | - | 236 |
| benchmark | 220,349 | +10.17% | 0 | - | 237 |
| snake_abs_exit_conv | 218,776 | +9.39% | 2 | 50% | 345 |
| snake_abs_exit | 217,531 | +8.77% | 2 | 50% | 345 |
| snake_abs | 215,854 | +7.93% | 1 | 100% | 255 |
| snake_abs_conv | 215,682 | +7.84% | 1 | 100% | 255 |
| intraweek | 214,412 | +7.21% | 30 | 53% | 3,302 |
| oracle | 212,966 | +6.48% | 0 | - | 233 |
| intramonth | 211,510 | +5.75% | 0 | - | 235 |
| random_hold | 207,842 | +3.92% | 10 | 70% | 733 |
| snake_anaconda | 205,663 | +2.83% | 3 | 33% | 374 |
| snake_viper_wild | 205,502 | +2.75% | 13 | 54% | 2,247 |
| benchmark_smallcap | 203,026 | +1.51% | 0 | - | 237 |
| snake_viper_tick | 201,988 | +0.99% | 12 | 50% | 2,054 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 185,311 | -7.34% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,898 (-4.05%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs | +2,230 | +1.04% |
| snake_abs_conv | +2,224 | +1.04% |
| benchmark_smallcap | +2,220 | +1.10% |
| snake_abs_exit_conv | +1,624 | +0.75% |
| snake_anaconda | +1,540 | +0.75% |
| snake_abs_exit | +1,369 | +0.63% |
| intraweek | +1,278 | +0.60% |
| benchmark | +1,086 | +0.49% |
| oracle | +963 | +0.45% |
| unified | +815 | +0.37% |
| random_hold | +731 | +0.35% |
| intramonth | +514 | +0.24% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -1,221 | -0.60% |
| snake_viper_wild | -1,240 | -0.60% |
| gold | -4,274 | -2.25% |

Average per day so far: snake_abs_exit_conv Rs +647, unified Rs +645, benchmark Rs +636, snake_abs_exit Rs +605, snake_abs_conv Rs +541, snake_abs Rs +528, intraweek Rs +450, oracle Rs +405, intramonth Rs +360, random_hold Rs +245, snake_viper_wild Rs +229, snake_anaconda Rs +210, benchmark_smallcap Rs +108, snake_viper_tick Rs +95, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -459

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.