# Paper trading report

Updated 2026-11-09 14:22 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,279 | +10.14% | 0 | - | 236 |
| benchmark | 218,023 | +9.01% | 0 | - | 237 |
| intraweek | 214,355 | +7.18% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,996 | +6.50% | 2 | 50% | 330 |
| snake_abs_exit | 212,766 | +6.38% | 2 | 50% | 308 |
| intramonth | 210,269 | +5.13% | 0 | - | 235 |
| snake_abs | 210,002 | +5.00% | 1 | 100% | 255 |
| snake_abs_conv | 209,837 | +4.92% | 1 | 100% | 255 |
| oracle | 209,514 | +4.76% | 0 | - | 233 |
| random_hold | 204,512 | +2.26% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,166 | +0.08% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 198,872 | -0.56% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,262 | -0.87% | 0 | - | 237 |
| snake_viper_tick | 195,495 | -2.25% | 6 | 50% | 1,154 |
| gold | 191,903 | -4.05% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,370 (-4.81%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +4,670 | +2.17% |
| snake_abs_conv | +4,610 | +2.25% |
| snake_abs | +4,583 | +2.23% |
| snake_abs_exit_conv | +4,575 | +2.19% |
| snake_abs_exit | +4,454 | +2.14% |
| snake_anaconda | +4,339 | +2.22% |
| intraweek | +3,992 | +1.90% |
| oracle | +3,687 | +1.79% |
| snake_viper_wild | +2,835 | +1.45% |
| snake_viper_tick | +2,785 | +1.45% |
| intramonth | +2,666 | +1.28% |
| benchmark_smallcap | +1,469 | +0.75% |
| gold | +855 | +0.45% |
| random_hold | +606 | +0.30% |
| benchmark | +536 | +0.25% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +676, benchmark Rs +601, snake_abs_exit_conv Rs +481, intraweek Rs +478, snake_abs_exit Rs +473, snake_abs_conv Rs +364, snake_abs Rs +357, intramonth Rs +342, oracle Rs +317, random_hold Rs +150, nifty_calls Rs +61, snake_anaconda Rs +7, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, snake_viper_wild Rs -51, benchmark_smallcap Rs -67, snake_viper_tick Rs -237, gold Rs -270, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.