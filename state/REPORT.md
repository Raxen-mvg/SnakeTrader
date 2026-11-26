# Paper trading report

Updated 2026-11-26 13:31 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,359 | +12.68% | 0 | - | 237 |
| unified | 223,332 | +11.67% | 0 | - | 236 |
| oracle | 213,231 | +6.62% | 0 | - | 233 |
| intramonth | 210,520 | +5.26% | 0 | - | 235 |
| random_hold | 209,269 | +4.63% | 13 | 69% | 1,037 |
| intraweek | 207,794 | +3.90% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,448 | +0.22% | 0 | - | 237 |
| snake_abs_exit | 200,131 | +0.07% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit_conv | 199,549 | -0.23% | 2 | 50% | 345 |
| snake_abs | 197,883 | -1.06% | 1 | 100% | 255 |
| snake_abs_conv | 197,677 | -1.16% | 1 | 100% | 255 |
| snake_viper_wild | 192,220 | -3.89% | 16 | 50% | 2,827 |
| snake_anaconda | 191,634 | -4.18% | 3 | 33% | 374 |
| snake_viper_tick | 188,955 | -5.52% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,158 | -16.92% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,618 (-5.69%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,637 | +0.82% |
| gold | +1,562 | +0.95% |
| intraweek | +1,051 | +0.51% |
| benchmark | +337 | +0.15% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -224 | -0.11% |
| oracle | -564 | -0.26% |
| unified | -768 | -0.34% |
| intramonth | -1,173 | -0.55% |
| snake_abs_exit | -2,124 | -1.05% |
| snake_abs | -2,267 | -1.13% |
| snake_abs_conv | -2,295 | -1.15% |
| snake_abs_exit_conv | -2,427 | -1.20% |
| snake_anaconda | -2,919 | -1.50% |
| snake_viper_tick | -5,222 | -2.69% |
| snake_viper_wild | -5,323 | -2.69% |

Average per day so far: benchmark Rs +619, unified Rs +569, oracle Rs +323, intramonth Rs +257, random_hold Rs +226, intraweek Rs +190, nifty_calls Rs +45, benchmark_smallcap Rs +12, snake_abs_exit Rs +3, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_abs_exit_conv Rs -12, snake_abs Rs -54, snake_abs_conv Rs -61, snake_anaconda Rs -232, snake_viper_wild Rs -236, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -368, gold Rs -825

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.