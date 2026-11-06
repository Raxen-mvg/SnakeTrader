# Paper trading report

Updated 2026-11-06 12:46 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,284 | +7.64% | 0 | - | 237 |
| unified | 214,383 | +7.19% | 0 | - | 236 |
| intraweek | 209,309 | +4.66% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,798 | +4.40% | 1 | 100% | 255 |
| snake_abs_exit | 208,621 | +4.31% | 1 | 100% | 260 |
| intramonth | 206,565 | +3.28% | 0 | - | 235 |
| snake_abs | 205,767 | +2.88% | 1 | 100% | 255 |
| snake_abs_conv | 205,592 | +2.80% | 1 | 100% | 255 |
| oracle | 204,811 | +2.40% | 0 | - | 233 |
| random_hold | 203,108 | +1.55% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,054 | -1.97% | 3 | 33% | 374 |
| snake_viper_wild | 195,695 | -2.15% | 3 | 33% | 702 |
| benchmark_smallcap | 194,809 | -2.60% | 0 | - | 237 |
| snake_viper_tick | 192,381 | -3.81% | 2 | 0% | 532 |
| gold | 189,947 | -5.03% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,873 (-6.56%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,515 | +0.71% |
| oracle | +739 | +0.36% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -109 | -0.05% |
| random_hold | -1,215 | -0.59% |
| intramonth | -1,383 | -0.67% |
| unified | -1,601 | -0.74% |
| benchmark_smallcap | -3,879 | -1.95% |
| gold | -4,274 | -2.20% |
| snake_abs | -5,921 | -2.80% |
| snake_abs_conv | -5,953 | -2.81% |
| snake_abs_exit_conv | -6,005 | -2.80% |
| snake_abs_exit | -6,038 | -2.81% |
| snake_anaconda | -6,425 | -3.17% |
| snake_viper_tick | -8,757 | -4.35% |
| snake_viper_wild | -8,961 | -4.38% |

Average per day so far: benchmark Rs +527, unified Rs +496, snake_abs_exit_conv Rs +338, snake_abs_exit Rs +332, intraweek Rs +321, intramonth Rs +226, snake_abs_conv Rs +215, snake_abs Rs +214, oracle Rs +166, random_hold Rs +107, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -164, snake_viper_wild Rs -205, benchmark_smallcap Rs -208, gold Rs -347, snake_nonews Rs -411, snake_viper_tick Rs -423, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.