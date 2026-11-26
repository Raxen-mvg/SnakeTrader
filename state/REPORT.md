# Paper trading report

Updated 2026-11-26 09:52 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,199 | +12.60% | 0 | - | 237 |
| unified | 223,903 | +11.95% | 0 | - | 236 |
| oracle | 213,710 | +6.86% | 0 | - | 233 |
| intramonth | 211,480 | +5.74% | 0 | - | 235 |
| random_hold | 210,362 | +5.18% | 13 | 69% | 1,037 |
| intraweek | 208,121 | +4.06% | 40 | 55% | 4,400 |
| snake_abs_exit | 203,529 | +1.76% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,920 | +1.46% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,784 | +0.39% | 1 | 100% | 255 |
| benchmark_smallcap | 200,650 | +0.33% | 0 | - | 237 |
| snake_abs_conv | 200,612 | +0.31% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 195,988 | -2.01% | 16 | 50% | 2,827 |
| snake_anaconda | 195,075 | -2.46% | 3 | 33% | 374 |
| snake_viper_tick | 192,654 | -3.67% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,260 | -16.37% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,411 (-5.29%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,663 | +1.62% |
| benchmark_smallcap | +1,838 | +0.93% |
| intraweek | +1,378 | +0.67% |
| snake_abs_exit | +1,273 | +0.63% |
| snake_abs_exit_conv | +944 | +0.47% |
| random_hold | +869 | +0.41% |
| snake_abs_conv | +640 | +0.32% |
| snake_abs | +634 | +0.32% |
| snake_anaconda | +522 | +0.27% |
| benchmark | +176 | +0.08% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| oracle | -85 | -0.04% |
| unified | -196 | -0.09% |
| intramonth | -213 | -0.10% |
| snake_viper_tick | -1,523 | -0.78% |
| snake_viper_wild | -1,555 | -0.79% |

Average per day so far: benchmark Rs +615, unified Rs +583, oracle Rs +334, intramonth Rs +280, random_hold Rs +253, intraweek Rs +198, snake_abs_exit Rs +93, snake_abs_exit_conv Rs +77, nifty_calls Rs +45, snake_abs Rs +20, benchmark_smallcap Rs +18, snake_abs_conv Rs +16, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_viper_wild Rs -122, snake_anaconda Rs -137, snake_viper_tick Rs -245, snake_nonews Rs -284, snake Rs -304, gold Rs -799

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.