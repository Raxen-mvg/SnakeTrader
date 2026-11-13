# Paper trading report

Updated 2026-11-13 12:46 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,879 | +9.94% | 0 | - | 236 |
| benchmark | 219,201 | +9.60% | 0 | - | 237 |
| snake_abs_exit_conv | 216,547 | +8.27% | 2 | 50% | 345 |
| snake_abs_exit | 216,472 | +8.24% | 2 | 50% | 345 |
| intraweek | 215,715 | +7.86% | 30 | 53% | 3,302 |
| oracle | 212,917 | +6.46% | 0 | - | 233 |
| snake_abs | 212,684 | +6.34% | 1 | 100% | 255 |
| snake_abs_conv | 212,515 | +6.26% | 1 | 100% | 255 |
| intramonth | 210,468 | +5.23% | 0 | - | 235 |
| random_hold | 207,119 | +3.56% | 10 | 70% | 733 |
| snake_viper_wild | 205,639 | +2.82% | 14 | 50% | 2,496 |
| snake_anaconda | 204,854 | +2.43% | 3 | 33% | 374 |
| benchmark_smallcap | 202,589 | +1.29% | 0 | - | 237 |
| snake_viper_tick | 202,121 | +1.06% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,568 | -8.22% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,605 (-4.20%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,057 | +0.49% |
| snake_viper_wild | +346 | +0.17% |
| snake_viper_tick | +340 | +0.17% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -198 | -0.09% |
| benchmark_smallcap | -617 | -0.30% |
| unified | -817 | -0.37% |
| random_hold | -935 | -0.45% |
| snake_abs_exit | -970 | -0.45% |
| snake_anaconda | -1,074 | -0.52% |
| intramonth | -1,126 | -0.53% |
| benchmark | -1,346 | -0.61% |
| gold | -1,743 | -0.94% |
| snake_abs_exit_conv | -2,127 | -0.97% |
| snake_abs_conv | -3,020 | -1.40% |
| snake_abs | -3,027 | -1.40% |

Average per day so far: unified Rs +602, benchmark Rs +582, snake_abs_exit_conv Rs +552, snake_abs_exit Rs +549, intraweek Rs +476, snake_abs_conv Rs +417, snake_abs Rs +409, oracle Rs +391, intramonth Rs +317, snake_viper_wild Rs +226, random_hold Rs +216, snake_anaconda Rs +173, snake_viper_tick Rs +96, benchmark_smallcap Rs +89, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -498

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.