# Paper trading report

Updated 2026-11-17 13:58 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,948 | +10.97% | 0 | - | 237 |
| unified | 221,515 | +10.76% | 0 | - | 236 |
| snake_abs_exit | 214,529 | +7.26% | 2 | 50% | 345 |
| intraweek | 213,134 | +6.57% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 212,992 | +6.50% | 2 | 50% | 345 |
| oracle | 212,307 | +6.15% | 0 | - | 233 |
| intramonth | 211,418 | +5.71% | 0 | - | 235 |
| snake_viper_wild | 209,989 | +4.99% | 14 | 50% | 2,496 |
| snake_abs | 209,844 | +4.92% | 1 | 100% | 255 |
| snake_abs_conv | 209,713 | +4.86% | 1 | 100% | 255 |
| random_hold | 207,484 | +3.74% | 10 | 70% | 733 |
| snake_viper_tick | 206,401 | +3.20% | 13 | 46% | 2,299 |
| snake_anaconda | 205,450 | +2.73% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,087 | +0.54% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,889 | -9.56% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,040 (-4.48%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,844 | +1.86% |
| snake_viper_tick | +3,781 | +1.87% |
| intraweek | +1,868 | +0.88% |
| benchmark | +1,867 | +0.85% |
| snake_anaconda | +347 | +0.17% |
| oracle | +284 | +0.13% |
| benchmark_smallcap | +258 | +0.13% |
| snake_abs_exit | +120 | +0.06% |
| unified | +78 | +0.04% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold | -66 | -0.04% |
| intramonth | -201 | -0.10% |
| snake_abs_exit_conv | -226 | -0.11% |
| snake_abs_conv | -276 | -0.13% |
| snake_abs | -289 | -0.14% |
| random_hold | -309 | -0.15% |

Average per day so far: benchmark Rs +627, unified Rs +615, snake_abs_exit Rs +454, snake_abs_exit_conv Rs +406, intraweek Rs +375, snake_viper_wild Rs +370, oracle Rs +352, intramonth Rs +326, snake_abs_conv Rs +304, snake_abs Rs +298, snake_viper_tick Rs +267, random_hold Rs +214, snake_anaconda Rs +182, nifty_calls Rs +52, benchmark_smallcap Rs +35, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -546

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.