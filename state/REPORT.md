# Paper trading report

Updated 2026-11-09 14:37 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,912 | +9.96% | 0 | - | 236 |
| benchmark | 217,977 | +8.99% | 0 | - | 237 |
| intraweek | 214,457 | +7.23% | 30 | 53% | 3,302 |
| snake_abs_exit | 212,703 | +6.35% | 2 | 50% | 308 |
| snake_abs_exit_conv | 212,662 | +6.33% | 2 | 50% | 330 |
| snake_abs | 210,064 | +5.03% | 1 | 100% | 255 |
| snake_abs_conv | 209,896 | +4.95% | 1 | 100% | 255 |
| intramonth | 209,783 | +4.89% | 0 | - | 235 |
| oracle | 209,113 | +4.56% | 0 | - | 233 |
| random_hold | 204,399 | +2.20% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,111 | +0.06% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 198,217 | -0.89% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,094 | -0.95% | 0 | - | 237 |
| snake_viper_tick | 194,853 | -2.57% | 6 | 50% | 1,154 |
| gold | 192,035 | -3.98% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,192 (-4.90%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_conv | +4,669 | +2.27% |
| snake_abs | +4,645 | +2.26% |
| snake_abs_exit | +4,391 | +2.11% |
| unified | +4,302 | +2.00% |
| snake_anaconda | +4,284 | +2.19% |
| snake_abs_exit_conv | +4,241 | +2.04% |
| intraweek | +4,094 | +1.95% |
| oracle | +3,286 | +1.60% |
| intramonth | +2,180 | +1.05% |
| snake_viper_wild | +2,180 | +1.11% |
| snake_viper_tick | +2,143 | +1.11% |
| benchmark_smallcap | +1,300 | +0.66% |
| gold | +986 | +0.52% |
| random_hold | +493 | +0.24% |
| benchmark | +490 | +0.23% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +664, benchmark Rs +599, intraweek Rs +482, snake_abs_exit Rs +470, snake_abs_exit_conv Rs +469, snake_abs_conv Rs +367, snake_abs Rs +359, intramonth Rs +326, oracle Rs +304, random_hold Rs +147, nifty_calls Rs +61, snake_anaconda Rs +4, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -73, snake_viper_wild Rs -81, gold Rs -266, snake_viper_tick Rs -271, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.