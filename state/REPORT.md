# Paper trading report

Updated 2026-11-13 12:31 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,066 | +10.03% | 0 | - | 236 |
| benchmark | 219,224 | +9.61% | 0 | - | 237 |
| snake_abs_exit_conv | 216,650 | +8.32% | 2 | 50% | 345 |
| snake_abs_exit | 216,556 | +8.28% | 2 | 50% | 345 |
| intraweek | 216,117 | +8.06% | 30 | 53% | 3,302 |
| oracle | 213,232 | +6.62% | 0 | - | 233 |
| snake_abs | 212,870 | +6.43% | 1 | 100% | 255 |
| snake_abs_conv | 212,699 | +6.35% | 1 | 100% | 255 |
| intramonth | 210,600 | +5.30% | 0 | - | 235 |
| random_hold | 207,091 | +3.55% | 10 | 70% | 733 |
| snake_viper_wild | 205,543 | +2.77% | 14 | 50% | 2,496 |
| snake_anaconda | 205,086 | +2.54% | 3 | 33% | 374 |
| benchmark_smallcap | 202,611 | +1.31% | 0 | - | 237 |
| snake_viper_tick | 202,027 | +1.01% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,831 | -8.08% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,820 (-4.09%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,459 | +0.68% |
| snake_viper_wild | +250 | +0.12% |
| snake_viper_tick | +246 | +0.12% |
| oracle | +117 | +0.06% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| benchmark_smallcap | -594 | -0.29% |
| unified | -631 | -0.29% |
| snake_anaconda | -842 | -0.41% |
| snake_abs_exit | -886 | -0.41% |
| random_hold | -963 | -0.46% |
| intramonth | -993 | -0.47% |
| benchmark | -1,323 | -0.60% |
| gold | -1,480 | -0.80% |
| snake_abs_exit_conv | -2,024 | -0.93% |
| snake_abs_conv | -2,836 | -1.32% |
| snake_abs | -2,842 | -1.32% |

Average per day so far: unified Rs +608, benchmark Rs +583, snake_abs_exit_conv Rs +555, snake_abs_exit Rs +552, intraweek Rs +488, snake_abs_conv Rs +423, snake_abs Rs +415, oracle Rs +401, intramonth Rs +321, snake_viper_wild Rs +222, random_hold Rs +215, snake_anaconda Rs +182, snake_viper_tick Rs +92, benchmark_smallcap Rs +90, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -490

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.