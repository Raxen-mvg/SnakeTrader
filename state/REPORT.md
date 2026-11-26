# Paper trading report

Updated 2026-11-26 11:23 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,010 | +13.01% | 0 | - | 237 |
| unified | 223,356 | +11.68% | 0 | - | 236 |
| oracle | 213,053 | +6.53% | 0 | - | 233 |
| intramonth | 210,608 | +5.30% | 0 | - | 235 |
| random_hold | 209,787 | +4.89% | 13 | 69% | 1,037 |
| intraweek | 208,342 | +4.17% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,729 | +0.86% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,154 | +0.58% | 2 | 50% | 345 |
| benchmark_smallcap | 200,493 | +0.25% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,385 | -0.31% | 1 | 100% | 255 |
| snake_abs_conv | 199,197 | -0.40% | 1 | 100% | 255 |
| snake_viper_wild | 193,310 | -3.35% | 16 | 50% | 2,827 |
| snake_anaconda | 193,268 | -3.37% | 3 | 33% | 374 |
| snake_viper_tick | 190,022 | -4.99% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,227 | -16.39% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,868 (-5.57%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,630 | +1.60% |
| benchmark_smallcap | +1,681 | +0.85% |
| intraweek | +1,599 | +0.77% |
| benchmark | +987 | +0.44% |
| random_hold | +294 | +0.14% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -527 | -0.26% |
| oracle | -742 | -0.35% |
| unified | -744 | -0.33% |
| snake_abs | -765 | -0.38% |
| snake_abs_conv | -775 | -0.39% |
| snake_abs_exit_conv | -822 | -0.41% |
| intramonth | -1,085 | -0.51% |
| snake_anaconda | -1,285 | -0.66% |
| snake_viper_tick | -4,155 | -2.14% |
| snake_viper_wild | -4,234 | -2.14% |

Average per day so far: benchmark Rs +634, unified Rs +570, oracle Rs +318, intramonth Rs +259, random_hold Rs +239, intraweek Rs +203, snake_abs_exit Rs +45, nifty_calls Rs +45, snake_abs_exit_conv Rs +30, benchmark_smallcap Rs +13, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -16, snake_abs_conv Rs -21, snake_anaconda Rs -187, snake_viper_wild Rs -203, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -333, gold Rs -799

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.