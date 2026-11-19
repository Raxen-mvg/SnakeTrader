# Paper trading report

Updated 2026-11-19 10:21 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,704 | +11.85% | 0 | - | 236 |
| benchmark | 220,479 | +10.24% | 0 | - | 237 |
| snake_abs_exit | 213,862 | +6.93% | 2 | 50% | 345 |
| intramonth | 213,183 | +6.59% | 0 | - | 235 |
| intraweek | 212,490 | +6.25% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 212,101 | +6.05% | 2 | 50% | 345 |
| oracle | 210,995 | +5.50% | 0 | - | 233 |
| snake_abs | 209,553 | +4.78% | 1 | 100% | 255 |
| snake_abs_conv | 209,436 | +4.72% | 1 | 100% | 255 |
| random_hold | 207,921 | +3.96% | 10 | 70% | 733 |
| snake_viper_wild | 207,734 | +3.87% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,184 | +2.09% | 15 | 47% | 2,625 |
| snake_anaconda | 203,735 | +1.87% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,358 | +0.18% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,592 | -12.70% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,297 (-4.35%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,093 | +0.49% |
| benchmark_smallcap | +1,031 | +0.52% |
| random_hold | +989 | +0.48% |
| intramonth | +909 | +0.43% |
| snake_viper_wild | +695 | +0.34% |
| snake_viper_tick | +681 | +0.33% |
| intraweek | +650 | +0.31% |
| oracle | +199 | +0.09% |
| benchmark | +184 | +0.08% |
| snake_abs | +117 | +0.06% |
| snake_abs_conv | +111 | +0.05% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_abs_exit | -170 | -0.08% |
| snake_abs_exit_conv | -283 | -0.13% |
| snake_anaconda | -666 | -0.33% |
| gold | -2,729 | -1.54% |

Average per day so far: unified Rs +641, benchmark Rs +553, snake_abs_exit Rs +408, intramonth Rs +356, snake_abs_exit_conv Rs +356, intraweek Rs +338, oracle Rs +297, snake_abs_conv Rs +278, snake_abs Rs +273, snake_viper_wild Rs +267, random_hold Rs +214, snake_viper_tick Rs +161, snake_anaconda Rs +117, nifty_calls Rs +50, benchmark_smallcap Rs +11, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -687

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.