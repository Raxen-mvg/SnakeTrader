# Paper trading report

Updated 2026-11-09 14:55 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,905 | +9.95% | 0 | - | 236 |
| benchmark | 217,947 | +8.97% | 0 | - | 237 |
| intraweek | 214,480 | +7.24% | 30 | 53% | 3,302 |
| snake_abs_exit | 212,404 | +6.20% | 2 | 50% | 308 |
| snake_abs_exit_conv | 212,295 | +6.15% | 2 | 50% | 330 |
| intramonth | 210,205 | +5.10% | 0 | - | 235 |
| snake_abs | 209,767 | +4.88% | 1 | 100% | 255 |
| snake_abs_conv | 209,601 | +4.80% | 1 | 100% | 255 |
| oracle | 209,372 | +4.69% | 0 | - | 233 |
| random_hold | 204,500 | +2.25% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,820 | -0.09% | 3 | 33% | 374 |
| benchmark_smallcap | 198,127 | -0.94% | 0 | - | 237 |
| snake_viper_wild | 197,945 | -1.03% | 7 | 57% | 1,332 |
| snake_viper_tick | 194,585 | -2.71% | 6 | 50% | 1,154 |
| gold | 191,986 | -4.01% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,253 (-4.87%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_conv | +4,374 | +2.13% |
| snake_abs | +4,348 | +2.12% |
| unified | +4,295 | +1.99% |
| intraweek | +4,117 | +1.96% |
| snake_abs_exit | +4,092 | +1.96% |
| snake_anaconda | +3,993 | +2.04% |
| snake_abs_exit_conv | +3,873 | +1.86% |
| oracle | +3,545 | +1.72% |
| intramonth | +2,602 | +1.25% |
| snake_viper_wild | +1,908 | +0.97% |
| snake_viper_tick | +1,875 | +0.97% |
| benchmark_smallcap | +1,334 | +0.68% |
| gold | +937 | +0.49% |
| random_hold | +593 | +0.29% |
| benchmark | +459 | +0.21% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +663, benchmark Rs +598, intraweek Rs +483, snake_abs_exit Rs +459, snake_abs_exit_conv Rs +455, snake_abs_conv Rs +356, snake_abs Rs +349, intramonth Rs +340, oracle Rs +312, random_hold Rs +150, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -7, benchmark_smallcap Rs -72, snake_viper_wild Rs -93, gold Rs -267, snake_viper_tick Rs -285, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.