# Paper trading report

Updated 2026-11-12 15:22 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,995 | +10.50% | 0 | - | 236 |
| benchmark | 220,724 | +10.36% | 0 | - | 237 |
| snake_abs_exit_conv | 219,143 | +9.57% | 2 | 50% | 345 |
| snake_abs_exit | 217,877 | +8.94% | 2 | 50% | 345 |
| snake_abs | 216,272 | +8.14% | 1 | 100% | 255 |
| snake_abs_conv | 216,093 | +8.05% | 1 | 100% | 255 |
| intraweek | 214,861 | +7.43% | 30 | 53% | 3,302 |
| oracle | 213,212 | +6.61% | 0 | - | 233 |
| intramonth | 211,787 | +5.89% | 0 | - | 235 |
| random_hold | 208,270 | +4.13% | 10 | 70% | 733 |
| snake_anaconda | 206,667 | +3.33% | 3 | 33% | 374 |
| snake_viper_wild | 205,336 | +2.67% | 13 | 54% | 2,247 |
| benchmark_smallcap | 203,475 | +1.74% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,824 | +0.91% | 12 | 50% | 2,054 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 185,442 | -7.28% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,207 (-3.90%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,668 | +1.33% |
| snake_abs | +2,648 | +1.24% |
| snake_abs_conv | +2,635 | +1.23% |
| snake_anaconda | +2,544 | +1.25% |
| snake_abs_exit_conv | +1,991 | +0.92% |
| intraweek | +1,728 | +0.81% |
| snake_abs_exit | +1,714 | +0.79% |
| benchmark | +1,461 | +0.67% |
| oracle | +1,209 | +0.57% |
| unified | +1,181 | +0.54% |
| random_hold | +1,160 | +0.56% |
| intramonth | +791 | +0.38% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -1,385 | -0.68% |
| snake_viper_wild | -1,406 | -0.68% |
| gold | -4,143 | -2.19% |

Average per day so far: snake_abs_exit_conv Rs +660, unified Rs +656, benchmark Rs +648, snake_abs_exit Rs +616, snake_abs_conv Rs +555, snake_abs Rs +542, intraweek Rs +464, oracle Rs +413, intramonth Rs +368, random_hold Rs +258, snake_anaconda Rs +247, snake_viper_wild Rs +222, benchmark_smallcap Rs +124, snake_viper_tick Rs +87, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -455

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.