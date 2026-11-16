# Paper trading report

Updated 2026-11-16 12:29 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,094 | +10.55% | 0 | - | 236 |
| benchmark | 220,234 | +10.12% | 0 | - | 237 |
| oracle | 213,452 | +6.73% | 0 | - | 233 |
| intraweek | 213,401 | +6.70% | 35 | 54% | 3,851 |
| snake_abs_exit | 213,306 | +6.65% | 2 | 50% | 345 |
| snake_abs_exit_conv | 211,923 | +5.96% | 2 | 50% | 345 |
| intramonth | 211,842 | +5.92% | 0 | - | 235 |
| snake_abs | 209,177 | +4.59% | 1 | 100% | 255 |
| snake_abs_conv | 209,014 | +4.51% | 1 | 100% | 255 |
| random_hold | 208,196 | +4.10% | 10 | 70% | 733 |
| snake_viper_wild | 205,493 | +2.75% | 14 | 50% | 2,496 |
| snake_anaconda | 203,460 | +1.73% | 3 | 33% | 374 |
| snake_viper_tick | 201,979 | +0.99% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,367 | +0.68% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,954 | -9.52% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,574 (-4.21%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +2,074 | +0.95% |
| intramonth | +1,785 | +0.85% |
| random_hold | +970 | +0.47% |
| benchmark | +895 | +0.41% |
| snake_viper_wild | +736 | +0.36% |
| snake_viper_tick | +724 | +0.36% |
| oracle | +354 | +0.17% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_anaconda | -1,432 | -0.70% |
| benchmark_smallcap | -1,502 | -0.74% |
| intraweek | -2,744 | -1.27% |
| gold | -3,041 | -1.65% |
| snake_abs_conv | -3,353 | -1.58% |
| snake_abs | -3,363 | -1.58% |
| snake_abs_exit | -3,679 | -1.70% |
| snake_abs_exit_conv | -4,459 | -2.06% |

Average per day so far: unified Rs +620, benchmark Rs +595, snake_abs_exit Rs +429, oracle Rs +396, intraweek Rs +394, snake_abs_exit_conv Rs +385, intramonth Rs +348, snake_abs_conv Rs +291, snake_abs Rs +287, random_hold Rs +241, snake_viper_wild Rs +211, snake_anaconda Rs +119, snake_viper_tick Rs +86, nifty_calls Rs +54, benchmark_smallcap Rs +46, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -347, snake Rs -368, gold Rs -560

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.