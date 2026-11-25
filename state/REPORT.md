# Paper trading report

Updated 2026-11-25 11:55 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,079 | +13.04% | 0 | - | 237 |
| unified | 225,285 | +12.64% | 0 | - | 236 |
| intramonth | 212,988 | +6.49% | 0 | - | 235 |
| oracle | 212,498 | +6.25% | 0 | - | 233 |
| random_hold | 209,418 | +4.71% | 12 | 75% | 1,009 |
| intraweek | 207,497 | +3.75% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,661 | +1.33% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,068 | +1.03% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,441 | +0.72% | 1 | 100% | 255 |
| snake_abs_conv | 201,254 | +0.63% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,708 | -0.15% | 0 | - | 237 |
| snake_viper_wild | 196,929 | -1.54% | 16 | 50% | 2,827 |
| snake_anaconda | 194,183 | -2.91% | 3 | 33% | 374 |
| snake_viper_tick | 193,575 | -3.21% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,432 | -17.78% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,416 (-5.29%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,605 | +2.08% |
| unified | +1,000 | +0.45% |
| random_hold | +992 | +0.48% |
| benchmark_smallcap | +729 | +0.37% |
| intramonth | +237 | +0.11% |
| oracle | +156 | +0.07% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs | -4,020 | -1.96% |
| snake_abs_conv | -4,048 | -1.97% |
| snake_viper_tick | -4,117 | -2.08% |
| intraweek | -4,122 | -1.95% |
| snake_viper_wild | -4,195 | -2.09% |
| snake_anaconda | -4,520 | -2.27% |
| snake_abs_exit | -4,834 | -2.33% |
| snake_abs_exit_conv | -4,977 | -2.40% |
| gold | -4,998 | -2.95% |

Average per day so far: benchmark Rs +652, unified Rs +632, intramonth Rs +325, oracle Rs +312, random_hold Rs +235, intraweek Rs +187, snake_abs_exit Rs +72, snake_abs_exit_conv Rs +56, nifty_calls Rs +46, snake_abs Rs +38, snake_abs_conv Rs +34, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -8, snake_viper_wild Rs -96, snake_anaconda Rs -166, snake_viper_tick Rs -222, snake_nonews Rs -292, snake Rs -311, gold Rs -889

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.