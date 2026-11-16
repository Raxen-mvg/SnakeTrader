# Paper trading report

Updated 2026-11-16 14:08 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,520 | +10.26% | 0 | - | 236 |
| benchmark | 219,630 | +9.81% | 0 | - | 237 |
| snake_abs_exit | 213,287 | +6.64% | 2 | 50% | 345 |
| snake_abs_exit_conv | 212,111 | +6.05% | 2 | 50% | 345 |
| oracle | 211,251 | +5.62% | 0 | - | 233 |
| intramonth | 211,195 | +5.60% | 0 | - | 235 |
| intraweek | 211,051 | +5.53% | 35 | 54% | 3,851 |
| snake_abs | 209,442 | +4.72% | 1 | 100% | 255 |
| snake_abs_conv | 209,281 | +4.64% | 1 | 100% | 255 |
| random_hold | 207,695 | +3.85% | 10 | 70% | 733 |
| snake_viper_wild | 205,417 | +2.71% | 14 | 50% | 2,496 |
| snake_anaconda | 203,800 | +1.90% | 3 | 33% | 374 |
| snake_viper_tick | 201,904 | +0.95% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,291 | +0.14% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,184 | -9.41% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,306 (-4.85%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,500 | +0.69% |
| intramonth | +1,138 | +0.54% |
| snake_viper_wild | +660 | +0.32% |
| snake_viper_tick | +649 | +0.32% |
| random_hold | +469 | +0.23% |
| benchmark | +291 | +0.13% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_anaconda | -1,092 | -0.53% |
| oracle | -1,847 | -0.87% |
| benchmark_smallcap | -2,578 | -1.27% |
| gold | -2,811 | -1.53% |
| snake_abs_conv | -3,086 | -1.45% |
| snake_abs | -3,098 | -1.46% |
| snake_abs_exit | -3,698 | -1.70% |
| snake_abs_exit_conv | -4,270 | -1.97% |
| intraweek | -5,094 | -2.36% |

Average per day so far: unified Rs +604, benchmark Rs +577, snake_abs_exit Rs +429, snake_abs_exit_conv Rs +391, oracle Rs +331, intramonth Rs +329, intraweek Rs +325, snake_abs_conv Rs +299, snake_abs Rs +295, random_hold Rs +226, snake_viper_wild Rs +208, snake_anaconda Rs +131, snake_viper_tick Rs +83, nifty_calls Rs +54, benchmark_smallcap Rs +10, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -347, snake Rs -368, gold Rs -553

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.