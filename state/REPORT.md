# Paper trading report

Updated 2026-11-23 12:16 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,310 | +12.15% | 0 | - | 236 |
| benchmark | 222,927 | +11.46% | 0 | - | 237 |
| intraweek | 212,587 | +6.29% | 40 | 55% | 4,400 |
| intramonth | 212,177 | +6.09% | 0 | - | 235 |
| oracle | 211,727 | +5.86% | 0 | - | 233 |
| random_hold | 209,043 | +4.52% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,068 | +3.53% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,676 | +2.84% | 2 | 50% | 345 |
| snake_abs | 204,764 | +2.38% | 1 | 100% | 255 |
| snake_abs_conv | 204,592 | +2.30% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,249 | +0.62% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,697 | -0.15% | 0 | - | 237 |
| snake_anaconda | 198,040 | -0.98% | 3 | 33% | 374 |
| snake_viper_tick | 197,815 | -1.09% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,235 | -14.88% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,267 (-4.87%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,187 | +1.30% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -751 | -0.35% |
| snake_abs_exit_conv | -940 | -0.46% |
| snake_abs | -1,156 | -0.56% |
| snake_abs_conv | -1,191 | -0.58% |
| benchmark_smallcap | -1,211 | -0.60% |
| snake_abs_exit | -1,494 | -0.72% |
| snake_viper_tick | -1,557 | -0.78% |
| snake_viper_wild | -1,580 | -0.78% |
| random_hold | -1,716 | -0.81% |
| snake_anaconda | -1,865 | -0.93% |
| unified | -1,872 | -0.83% |
| benchmark | -2,211 | -0.98% |
| intramonth | -2,827 | -1.31% |
| intraweek | -3,126 | -1.45% |

Average per day so far: unified Rs +623, benchmark Rs +588, intraweek Rs +323, intramonth Rs +312, oracle Rs +301, random_hold Rs +232, snake_abs_exit Rs +196, snake_abs_exit_conv Rs +158, snake_abs Rs +129, snake_abs_conv Rs +128, nifty_calls Rs +47, snake_viper_wild Rs +40, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -9, snake_anaconda Rs -58, snake_viper_tick Rs -78, snake_nonews Rs -300, snake Rs -320, gold Rs -763

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.