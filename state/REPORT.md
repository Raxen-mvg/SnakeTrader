# Paper trading report

Updated 2026-11-09 13:13 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,810 | +9.90% | 0 | - | 236 |
| benchmark | 217,250 | +8.62% | 0 | - | 237 |
| intraweek | 215,045 | +7.52% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 213,198 | +6.60% | 2 | 50% | 330 |
| snake_abs_exit | 212,718 | +6.36% | 2 | 50% | 308 |
| snake_abs | 210,185 | +5.09% | 1 | 100% | 255 |
| snake_abs_conv | 210,017 | +5.01% | 1 | 100% | 255 |
| intramonth | 209,919 | +4.96% | 0 | - | 235 |
| oracle | 209,631 | +4.82% | 0 | - | 233 |
| random_hold | 204,441 | +2.22% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,207 | +0.10% | 3 | 33% | 374 |
| snake_viper_wild | 200,085 | +0.04% | 7 | 57% | 1,332 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,654 | -0.67% | 0 | - | 237 |
| snake_viper_tick | 196,686 | -1.66% | 6 | 50% | 1,154 |
| gold | 192,249 | -3.88% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,404 (-4.80%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_conv | +4,790 | +2.33% |
| snake_abs_exit_conv | +4,776 | +2.29% |
| snake_abs | +4,766 | +2.32% |
| intraweek | +4,683 | +2.23% |
| snake_abs_exit | +4,406 | +2.12% |
| snake_anaconda | +4,380 | +2.24% |
| unified | +4,201 | +1.95% |
| snake_viper_wild | +4,048 | +2.06% |
| snake_viper_tick | +3,977 | +2.06% |
| oracle | +3,804 | +1.85% |
| intramonth | +2,316 | +1.12% |
| benchmark_smallcap | +1,861 | +0.95% |
| gold | +1,200 | +0.63% |
| random_hold | +534 | +0.26% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -237 | -0.11% |

Average per day so far: unified Rs +660, benchmark Rs +575, intraweek Rs +502, snake_abs_exit_conv Rs +489, snake_abs_exit Rs +471, snake_abs_conv Rs +371, snake_abs Rs +364, intramonth Rs +331, oracle Rs +321, random_hold Rs +148, nifty_calls Rs +61, snake_anaconda Rs +8, snake_viper_wild Rs +4, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, benchmark_smallcap Rs -52, snake_viper_tick Rs -174, gold Rs -258, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.