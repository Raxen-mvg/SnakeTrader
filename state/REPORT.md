# Paper trading report

Updated 2026-11-13 13:28 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,249 | +10.12% | 0 | - | 236 |
| benchmark | 219,461 | +9.73% | 0 | - | 237 |
| snake_abs_exit | 216,406 | +8.20% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,166 | +8.08% | 2 | 50% | 345 |
| intraweek | 215,819 | +7.91% | 30 | 53% | 3,302 |
| oracle | 212,977 | +6.49% | 0 | - | 233 |
| snake_abs | 212,016 | +6.01% | 1 | 100% | 255 |
| snake_abs_conv | 211,847 | +5.92% | 1 | 100% | 255 |
| intramonth | 210,911 | +5.46% | 0 | - | 235 |
| random_hold | 207,169 | +3.58% | 10 | 70% | 733 |
| snake_viper_wild | 205,533 | +2.77% | 14 | 50% | 2,496 |
| snake_anaconda | 204,282 | +2.14% | 3 | 33% | 374 |
| benchmark_smallcap | 202,746 | +1.37% | 0 | - | 237 |
| snake_viper_tick | 202,018 | +1.01% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,913 | -8.04% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,736 (-4.13%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,161 | +0.54% |
| snake_viper_wild | +240 | +0.12% |
| snake_viper_tick | +236 | +0.12% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -138 | -0.07% |
| unified | -447 | -0.20% |
| benchmark_smallcap | -460 | -0.23% |
| intramonth | -682 | -0.32% |
| random_hold | -885 | -0.42% |
| snake_abs_exit | -1,036 | -0.48% |
| benchmark | -1,086 | -0.49% |
| gold | -1,397 | -0.75% |
| snake_anaconda | -1,646 | -0.80% |
| snake_abs_exit_conv | -2,508 | -1.15% |
| snake_abs_conv | -3,688 | -1.71% |
| snake_abs | -3,695 | -1.71% |

Average per day so far: unified Rs +614, benchmark Rs +590, snake_abs_exit Rs +547, snake_abs_exit_conv Rs +539, intraweek Rs +479, snake_abs_conv Rs +395, oracle Rs +393, snake_abs Rs +388, intramonth Rs +331, snake_viper_wild Rs +221, random_hold Rs +217, snake_anaconda Rs +153, benchmark_smallcap Rs +95, snake_viper_tick Rs +92, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -487

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.