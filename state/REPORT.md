# Paper trading report

Updated 2026-11-23 10:45 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,435 | +12.22% | 0 | - | 236 |
| benchmark | 223,363 | +11.68% | 0 | - | 237 |
| intraweek | 212,620 | +6.31% | 40 | 55% | 4,400 |
| intramonth | 212,320 | +6.16% | 0 | - | 235 |
| oracle | 211,119 | +5.56% | 0 | - | 233 |
| random_hold | 209,810 | +4.91% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,880 | +3.44% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,831 | +2.92% | 2 | 50% | 345 |
| snake_abs | 204,310 | +2.15% | 1 | 100% | 255 |
| snake_abs_conv | 204,158 | +2.08% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,087 | +0.04% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,327 | -0.34% | 0 | - | 237 |
| snake_anaconda | 197,891 | -1.05% | 3 | 33% | 374 |
| snake_viper_tick | 196,677 | -1.66% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,381 | -15.31% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,262 (-4.87%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,332 | +0.79% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -785 | -0.38% |
| random_hold | -950 | -0.45% |
| oracle | -1,360 | -0.64% |
| benchmark_smallcap | -1,581 | -0.79% |
| snake_abs | -1,610 | -0.78% |
| snake_abs_conv | -1,625 | -0.79% |
| snake_abs_exit | -1,683 | -0.81% |
| unified | -1,747 | -0.77% |
| benchmark | -1,775 | -0.79% |
| snake_anaconda | -2,015 | -1.01% |
| intramonth | -2,685 | -1.25% |
| snake_viper_tick | -2,694 | -1.35% |
| snake_viper_wild | -2,742 | -1.35% |
| intraweek | -3,092 | -1.43% |

Average per day so far: unified Rs +627, benchmark Rs +599, intraweek Rs +324, intramonth Rs +316, oracle Rs +285, random_hold Rs +252, snake_abs_exit Rs +191, snake_abs_exit_conv Rs +162, snake_abs Rs +116, snake_abs_conv Rs +116, nifty_calls Rs +47, snake_viper_wild Rs +3, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -19, snake_anaconda Rs -62, snake_viper_tick Rs -119, snake_nonews Rs -300, snake Rs -320, gold Rs -785

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.