# Paper trading report

Updated 2026-11-16 09:24 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,219 | +10.11% | 0 | - | 237 |
| unified | 220,061 | +10.03% | 0 | - | 236 |
| intraweek | 216,677 | +8.34% | 30 | 53% | 3,302 |
| snake_abs_exit | 215,785 | +7.89% | 2 | 50% | 345 |
| snake_abs_exit_conv | 214,239 | +7.12% | 2 | 50% | 345 |
| oracle | 213,329 | +6.66% | 0 | - | 233 |
| snake_abs | 211,303 | +5.65% | 1 | 100% | 255 |
| snake_abs_conv | 211,142 | +5.57% | 1 | 100% | 255 |
| intramonth | 210,983 | +5.49% | 0 | - | 235 |
| random_hold | 207,101 | +3.55% | 10 | 70% | 733 |
| snake_anaconda | 205,144 | +2.57% | 3 | 33% | 374 |
| snake_viper_wild | 204,782 | +2.39% | 14 | 50% | 2,496 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,782 | +0.89% | 0 | - | 237 |
| snake_viper_tick | 201,280 | +0.64% | 13 | 46% | 2,299 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 182,385 | -8.81% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,902 (-4.05%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,041 | +0.47% |
| intramonth | +926 | +0.44% |
| benchmark | +880 | +0.40% |
| intraweek | +532 | +0.25% |
| snake_anaconda | +252 | +0.12% |
| oracle | +231 | +0.11% |
| snake_viper_tick | +25 | +0.01% |
| snake_viper_wild | +25 | +0.01% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -125 | -0.06% |
| benchmark_smallcap | -1,087 | -0.54% |
| snake_abs_exit | -1,200 | -0.55% |
| snake_abs_conv | -1,225 | -0.58% |
| snake_abs | -1,237 | -0.58% |
| gold | -1,611 | -0.88% |
| snake_abs_exit_conv | -2,142 | -0.99% |

Average per day so far: benchmark Rs +595, unified Rs +590, snake_abs_exit Rs +509, intraweek Rs +491, snake_abs_exit_conv Rs +459, oracle Rs +392, snake_abs_conv Rs +359, snake_abs Rs +353, intramonth Rs +323, random_hold Rs +209, snake_viper_wild Rs +184, snake_anaconda Rs +177, benchmark_smallcap Rs +59, snake_viper_tick Rs +56, nifty_calls Rs +54, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -347, snake Rs -368, gold Rs -518

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.