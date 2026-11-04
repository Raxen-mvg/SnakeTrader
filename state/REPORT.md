# Paper trading report

Updated 2026-11-04 12:46 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,878 | +6.94% | 0 | - | 236 |
| snake_abs_exit_conv | 212,529 | +6.26% | 1 | 100% | 255 |
| snake_abs_exit | 212,383 | +6.19% | 1 | 100% | 260 |
| snake_abs | 209,426 | +4.71% | 1 | 100% | 255 |
| snake_abs_conv | 209,273 | +4.64% | 1 | 100% | 255 |
| intraweek | 209,109 | +4.55% | 25 | 48% | 2,757 |
| benchmark | 207,948 | +3.97% | 0 | - | 237 |
| snake_viper_wild | 206,985 | +3.49% | 3 | 33% | 702 |
| intramonth | 206,270 | +3.13% | 0 | - | 235 |
| snake_viper_tick | 203,378 | +1.69% | 2 | 0% | 532 |
| random_hold | 202,941 | +1.47% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,191 | +0.59% | 0 | - | 233 |
| snake_anaconda | 200,934 | +0.47% | 3 | 33% | 361 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 195,112 | -2.44% | 0 | - | 237 |
| gold | 190,654 | -4.67% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,223 (-5.39%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +8,369 | +4.10% |
| snake_abs_exit_conv | +8,191 | +4.01% |
| snake_abs_conv | +8,132 | +4.04% |
| snake_abs | +8,117 | +4.03% |
| snake_anaconda | +7,110 | +3.67% |
| gold | +5,376 | +2.90% |
| intraweek | +4,024 | +1.96% |
| random_hold | +2,473 | +1.23% |
| intramonth | +2,299 | +1.13% |
| benchmark_smallcap | +2,175 | +1.13% |
| unified | +1,877 | +0.89% |
| benchmark | +1,247 | +0.60% |
| oracle | +1,201 | +0.60% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,789 | -1.83% |
| snake_viper_wild | -3,908 | -1.85% |

Average per day so far: snake_abs_exit_conv Rs +522, snake_abs_exit Rs +516, unified Rs +514, snake_abs_conv Rs +386, snake_abs Rs +377, snake_viper_wild Rs +368, intraweek Rs +337, benchmark Rs +294, intramonth Rs +232, snake_viper_tick Rs +211, random_hold Rs +109, nifty_calls Rs +68, oracle Rs +44, snake_anaconda Rs +42, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -213, gold Rs -346, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.