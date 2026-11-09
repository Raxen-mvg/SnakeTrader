# Paper trading report

Updated 2026-11-09 13:55 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,120 | +10.06% | 0 | - | 236 |
| benchmark | 217,518 | +8.76% | 0 | - | 237 |
| intraweek | 214,649 | +7.33% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 213,352 | +6.68% | 2 | 50% | 330 |
| snake_abs_exit | 212,914 | +6.46% | 2 | 50% | 308 |
| snake_abs | 210,257 | +5.13% | 1 | 100% | 255 |
| intramonth | 210,157 | +5.08% | 0 | - | 235 |
| snake_abs_conv | 210,091 | +5.04% | 1 | 100% | 255 |
| oracle | 209,407 | +4.70% | 0 | - | 233 |
| random_hold | 204,391 | +2.19% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,329 | +0.16% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 199,495 | -0.25% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,116 | -0.94% | 0 | - | 237 |
| snake_viper_tick | 196,107 | -1.95% | 6 | 50% | 1,154 |
| gold | 192,216 | -3.89% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,397 (-4.80%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,930 | +2.37% |
| snake_abs_conv | +4,864 | +2.37% |
| snake_abs | +4,837 | +2.35% |
| snake_abs_exit | +4,602 | +2.21% |
| unified | +4,511 | +2.09% |
| snake_anaconda | +4,502 | +2.30% |
| intraweek | +4,287 | +2.04% |
| oracle | +3,580 | +1.74% |
| snake_viper_wild | +3,458 | +1.76% |
| snake_viper_tick | +3,397 | +1.76% |
| intramonth | +2,554 | +1.23% |
| benchmark_smallcap | +1,323 | +0.67% |
| gold | +1,167 | +0.61% |
| random_hold | +484 | +0.24% |
| benchmark | +31 | +0.01% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +671, benchmark Rs +584, snake_abs_exit_conv Rs +495, intraweek Rs +488, snake_abs_exit Rs +478, snake_abs_conv Rs +374, snake_abs Rs +366, intramonth Rs +339, oracle Rs +314, random_hold Rs +146, nifty_calls Rs +61, snake_anaconda Rs +13, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, snake_viper_wild Rs -23, benchmark_smallcap Rs -72, snake_viper_tick Rs -205, gold Rs -259, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.