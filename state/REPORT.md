# Paper trading report

Updated 2026-11-13 09:31 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,656 | +9.83% | 0 | - | 236 |
| benchmark | 219,324 | +9.66% | 0 | - | 237 |
| snake_abs_exit_conv | 217,280 | +8.64% | 2 | 50% | 345 |
| snake_abs_exit | 216,751 | +8.38% | 2 | 50% | 345 |
| intraweek | 215,450 | +7.72% | 30 | 53% | 3,302 |
| snake_abs | 214,504 | +7.25% | 1 | 100% | 255 |
| snake_abs_conv | 214,329 | +7.16% | 1 | 100% | 255 |
| oracle | 213,200 | +6.60% | 0 | - | 233 |
| intramonth | 210,979 | +5.49% | 0 | - | 235 |
| random_hold | 207,514 | +3.76% | 10 | 70% | 733 |
| snake_viper_wild | 205,744 | +2.87% | 13 | 54% | 2,328 |
| snake_anaconda | 204,135 | +2.07% | 3 | 33% | 374 |
| benchmark_smallcap | 202,724 | +1.36% | 0 | - | 237 |
| snake_viper_tick | 202,226 | +1.11% | 12 | 50% | 2,134 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,686 | -7.66% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,758 (-4.12%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +792 | +0.37% |
| snake_viper_wild | +451 | +0.22% |
| snake_viper_tick | +445 | +0.22% |
| oracle | +84 | +0.04% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| benchmark_smallcap | -482 | -0.24% |
| random_hold | -540 | -0.26% |
| intramonth | -615 | -0.29% |
| gold | -625 | -0.34% |
| snake_abs_exit | -692 | -0.32% |
| unified | -1,041 | -0.47% |
| snake_abs_conv | -1,206 | -0.56% |
| snake_abs | -1,208 | -0.56% |
| benchmark | -1,224 | -0.56% |
| snake_abs_exit_conv | -1,394 | -0.64% |
| snake_anaconda | -1,792 | -0.87% |

Average per day so far: unified Rs +596, benchmark Rs +586, snake_abs_exit_conv Rs +576, snake_abs_exit Rs +558, snake_abs_conv Rs +478, intraweek Rs +468, snake_abs Rs +468, oracle Rs +400, intramonth Rs +333, snake_viper_wild Rs +230, random_hold Rs +228, snake_anaconda Rs +148, snake_viper_tick Rs +101, benchmark_smallcap Rs +94, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -464

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.