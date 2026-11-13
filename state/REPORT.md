# Paper trading report

Updated 2026-11-13 13:19 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,070 | +10.04% | 0 | - | 236 |
| benchmark | 219,385 | +9.69% | 0 | - | 237 |
| snake_abs_exit | 216,687 | +8.34% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,331 | +8.16% | 2 | 50% | 345 |
| intraweek | 215,552 | +7.78% | 30 | 53% | 3,302 |
| oracle | 212,967 | +6.48% | 0 | - | 233 |
| snake_abs | 212,226 | +6.11% | 1 | 100% | 255 |
| snake_abs_conv | 212,056 | +6.03% | 1 | 100% | 255 |
| intramonth | 210,754 | +5.38% | 0 | - | 235 |
| random_hold | 207,126 | +3.56% | 10 | 70% | 733 |
| snake_viper_wild | 205,518 | +2.76% | 14 | 50% | 2,496 |
| snake_anaconda | 204,421 | +2.21% | 3 | 33% | 374 |
| benchmark_smallcap | 202,623 | +1.31% | 0 | - | 237 |
| snake_viper_tick | 202,003 | +1.00% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,831 | -8.08% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,628 (-4.19%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +894 | +0.42% |
| snake_viper_wild | +226 | +0.11% |
| snake_viper_tick | +221 | +0.11% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -149 | -0.07% |
| benchmark_smallcap | -583 | -0.29% |
| unified | -627 | -0.28% |
| snake_abs_exit | -756 | -0.35% |
| intramonth | -839 | -0.40% |
| random_hold | -928 | -0.45% |
| benchmark | -1,163 | -0.53% |
| gold | -1,480 | -0.80% |
| snake_anaconda | -1,506 | -0.73% |
| snake_abs_exit_conv | -2,343 | -1.07% |
| snake_abs_conv | -3,479 | -1.61% |
| snake_abs | -3,486 | -1.62% |

Average per day so far: unified Rs +608, benchmark Rs +587, snake_abs_exit Rs +556, snake_abs_exit_conv Rs +544, intraweek Rs +471, snake_abs_conv Rs +402, snake_abs Rs +394, oracle Rs +393, intramonth Rs +326, snake_viper_wild Rs +221, random_hold Rs +216, snake_anaconda Rs +158, snake_viper_tick Rs +91, benchmark_smallcap Rs +90, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -490

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.