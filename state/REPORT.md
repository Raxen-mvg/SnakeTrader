# Paper trading report

Updated 2026-11-13 13:37 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,453 | +10.23% | 0 | - | 236 |
| benchmark | 219,408 | +9.70% | 0 | - | 237 |
| snake_abs_exit | 216,892 | +8.45% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,553 | +8.28% | 2 | 50% | 345 |
| intraweek | 216,016 | +8.01% | 30 | 53% | 3,302 |
| oracle | 213,168 | +6.58% | 0 | - | 233 |
| snake_abs | 212,518 | +6.26% | 1 | 100% | 255 |
| snake_abs_conv | 212,352 | +6.18% | 1 | 100% | 255 |
| intramonth | 211,088 | +5.54% | 0 | - | 235 |
| random_hold | 207,340 | +3.67% | 10 | 70% | 733 |
| snake_viper_wild | 205,789 | +2.90% | 14 | 50% | 2,496 |
| snake_anaconda | 204,781 | +2.39% | 3 | 33% | 374 |
| benchmark_smallcap | 202,768 | +1.38% | 0 | - | 237 |
| snake_viper_tick | 202,269 | +1.14% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,946 | -8.03% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,922 (-4.04%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,358 | +0.63% |
| snake_viper_wild | +496 | +0.24% |
| snake_viper_tick | +488 | +0.24% |
| oracle | +53 | +0.03% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -244 | -0.11% |
| benchmark_smallcap | -437 | -0.21% |
| intramonth | -506 | -0.24% |
| snake_abs_exit | -551 | -0.25% |
| random_hold | -713 | -0.34% |
| benchmark | -1,140 | -0.52% |
| snake_anaconda | -1,146 | -0.56% |
| gold | -1,365 | -0.74% |
| snake_abs_exit_conv | -2,121 | -0.97% |
| snake_abs_conv | -3,183 | -1.48% |
| snake_abs | -3,193 | -1.48% |

Average per day so far: unified Rs +620, benchmark Rs +588, snake_abs_exit Rs +563, snake_abs_exit_conv Rs +552, intraweek Rs +485, snake_abs_conv Rs +412, snake_abs Rs +404, oracle Rs +399, intramonth Rs +336, snake_viper_wild Rs +232, random_hold Rs +222, snake_anaconda Rs +171, snake_viper_tick Rs +103, benchmark_smallcap Rs +95, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -486

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.