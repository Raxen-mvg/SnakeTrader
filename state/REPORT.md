# Paper trading report

Updated 2026-11-19 13:04 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,817 | +11.91% | 0 | - | 236 |
| benchmark | 221,649 | +10.82% | 0 | - | 237 |
| intramonth | 213,479 | +6.74% | 0 | - | 235 |
| snake_abs_exit | 212,544 | +6.27% | 2 | 50% | 345 |
| intraweek | 211,736 | +5.87% | 35 | 54% | 3,851 |
| oracle | 211,135 | +5.57% | 0 | - | 233 |
| snake_abs_exit_conv | 210,711 | +5.36% | 2 | 50% | 345 |
| snake_abs | 208,155 | +4.08% | 1 | 100% | 255 |
| snake_abs_conv | 208,019 | +4.01% | 1 | 100% | 255 |
| random_hold | 207,723 | +3.86% | 10 | 70% | 733 |
| snake_viper_wild | 207,633 | +3.82% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,085 | +2.04% | 15 | 47% | 2,625 |
| snake_anaconda | 202,728 | +1.36% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,706 | +0.35% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,200 | -12.40% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,249 (-4.38%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,379 | +0.69% |
| benchmark | +1,354 | +0.61% |
| intramonth | +1,205 | +0.57% |
| unified | +1,205 | +0.54% |
| random_hold | +791 | +0.38% |
| snake_viper_wild | +594 | +0.29% |
| snake_viper_tick | +582 | +0.29% |
| oracle | +339 | +0.16% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -103 | -0.05% |
| snake_abs | -1,281 | -0.61% |
| snake_abs_conv | -1,306 | -0.62% |
| snake_abs_exit | -1,488 | -0.69% |
| snake_abs_exit_conv | -1,672 | -0.79% |
| snake_anaconda | -1,673 | -0.82% |
| gold | -2,121 | -1.20% |

Average per day so far: unified Rs +644, benchmark Rs +585, snake_abs_exit Rs +369, intramonth Rs +364, intraweek Rs +317, snake_abs_exit_conv Rs +315, oracle Rs +301, snake_viper_wild Rs +263, snake_abs_conv Rs +236, snake_abs Rs +233, random_hold Rs +209, snake_viper_tick Rs +157, snake_anaconda Rs +85, nifty_calls Rs +50, benchmark_smallcap Rs +21, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -670

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.