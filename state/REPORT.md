# Paper trading report

Updated 2026-11-09 15:13 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,979 | +9.99% | 0 | - | 236 |
| benchmark | 218,153 | +9.08% | 0 | - | 237 |
| intraweek | 214,508 | +7.25% | 30 | 53% | 3,302 |
| snake_abs_exit | 212,325 | +6.16% | 2 | 50% | 308 |
| snake_abs_exit_conv | 212,211 | +6.11% | 2 | 50% | 330 |
| intramonth | 210,375 | +5.19% | 0 | - | 235 |
| snake_abs | 209,798 | +4.90% | 1 | 100% | 255 |
| oracle | 209,636 | +4.82% | 0 | - | 233 |
| snake_abs_conv | 209,636 | +4.82% | 1 | 100% | 255 |
| random_hold | 204,722 | +2.36% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,811 | -0.09% | 3 | 33% | 374 |
| benchmark_smallcap | 198,374 | -0.81% | 0 | - | 237 |
| snake_viper_wild | 197,179 | -1.41% | 7 | 57% | 1,332 |
| snake_viper_tick | 193,829 | -3.08% | 6 | 50% | 1,154 |
| gold | 192,199 | -3.90% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,341 (-4.83%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_conv | +4,409 | +2.15% |
| snake_abs | +4,379 | +2.13% |
| unified | +4,369 | +2.03% |
| intraweek | +4,146 | +1.97% |
| snake_abs_exit | +4,013 | +1.93% |
| snake_anaconda | +3,984 | +2.03% |
| oracle | +3,809 | +1.85% |
| snake_abs_exit_conv | +3,789 | +1.82% |
| intramonth | +2,772 | +1.33% |
| benchmark_smallcap | +1,581 | +0.80% |
| gold | +1,151 | +0.60% |
| snake_viper_wild | +1,142 | +0.58% |
| snake_viper_tick | +1,119 | +0.58% |
| random_hold | +815 | +0.40% |
| benchmark | +666 | +0.31% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +666, benchmark Rs +605, intraweek Rs +484, snake_abs_exit Rs +456, snake_abs_exit_conv Rs +452, snake_abs_conv Rs +357, snake_abs Rs +350, intramonth Rs +346, oracle Rs +321, random_hold Rs +157, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -8, benchmark_smallcap Rs -63, snake_viper_wild Rs -128, gold Rs -260, snake_viper_tick Rs -325, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.