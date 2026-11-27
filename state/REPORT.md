# Paper trading report

Updated 2026-11-27 15:13 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 223,370 | +11.69% | 0 | - | 237 |
| unified | 222,889 | +11.45% | 0 | - | 236 |
| oracle | 211,628 | +5.81% | 0 | - | 233 |
| random_hold | 211,291 | +5.64% | 13 | 69% | 1,037 |
| intramonth | 210,705 | +5.35% | 0 | - | 235 |
| intraweek | 207,869 | +3.93% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 206,378 | +3.19% | 2 | 50% | 345 |
| snake_abs_exit | 204,104 | +2.05% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,546 | +0.77% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,455 | -0.27% | 1 | 100% | 255 |
| snake_abs_conv | 199,267 | -0.37% | 1 | 100% | 255 |
| snake_anaconda | 193,005 | -3.50% | 3 | 33% | 374 |
| snake_viper_wild | 192,567 | -3.72% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,296 | -5.35% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,778 | -14.61% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,766 (-5.62%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +5,981 | +2.98% |
| gold | +4,784 | +2.88% |
| snake_abs_exit | +3,026 | +1.50% |
| random_hold | +2,697 | +1.29% |
| snake_abs | +903 | +0.46% |
| snake_abs_conv | +900 | +0.45% |
| intraweek | +820 | +0.40% |
| snake_anaconda | +709 | +0.37% |
| benchmark_smallcap | +706 | +0.35% |
| snake_viper_wild | +362 | +0.19% |
| snake_viper_tick | +355 | +0.19% |
| intramonth | +171 | +0.08% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| unified | -189 | -0.09% |
| oracle | -608 | -0.29% |
| benchmark | -2,616 | -1.16% |

Average per day so far: benchmark Rs +556, unified Rs +545, oracle Rs +277, random_hold Rs +269, intramonth Rs +255, intraweek Rs +187, snake_abs_exit_conv Rs +164, snake_abs_exit Rs +105, nifty_calls Rs +44, benchmark_smallcap Rs +41, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -14, snake_abs_conv Rs -19, snake_anaconda Rs -189, snake_viper_wild Rs -219, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -345, gold Rs -696

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.