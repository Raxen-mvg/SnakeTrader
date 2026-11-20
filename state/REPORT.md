# Paper trading report

Updated 2026-11-20 14:44 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,232 | +13.12% | 0 | - | 236 |
| benchmark | 224,709 | +12.36% | 0 | - | 237 |
| intraweek | 215,437 | +7.72% | 35 | 54% | 3,851 |
| intramonth | 215,099 | +7.55% | 0 | - | 235 |
| oracle | 212,694 | +6.35% | 0 | - | 233 |
| random_hold | 210,011 | +5.00% | 11 | 73% | 979 |
| snake_abs_exit | 208,763 | +4.38% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,889 | +3.44% | 2 | 50% | 345 |
| snake_abs | 206,016 | +3.01% | 1 | 100% | 255 |
| snake_abs_conv | 205,884 | +2.94% | 1 | 100% | 255 |
| snake_viper_wild | 203,265 | +1.63% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,042 | +0.52% | 0 | - | 237 |
| snake_anaconda | 200,086 | +0.04% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 199,800 | -0.10% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,227 | -16.39% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,982 (-4.01%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,548 | +1.20% |
| benchmark | +2,333 | +1.05% |
| unified | +1,617 | +0.72% |
| random_hold | +1,558 | +0.75% |
| intramonth | +1,091 | +0.51% |
| oracle | +606 | +0.29% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -426 | -0.21% |
| snake_abs | -2,964 | -1.42% |
| snake_abs_conv | -2,976 | -1.43% |
| snake_anaconda | -3,378 | -1.66% |
| snake_abs_exit_conv | -4,176 | -1.98% |
| snake_viper_tick | -4,177 | -2.05% |
| snake_viper_wild | -4,257 | -2.05% |
| snake_abs_exit | -4,588 | -2.15% |
| gold | -7,546 | -4.32% |

Average per day so far: unified Rs +690, benchmark Rs +650, intraweek Rs +406, intramonth Rs +397, oracle Rs +334, random_hold Rs +263, snake_abs_exit Rs +250, snake_abs_exit_conv Rs +197, snake_abs_conv Rs +168, snake_abs Rs +167, snake_viper_wild Rs +109, nifty_calls Rs +48, benchmark_smallcap Rs +31, snake_anaconda Rs +3, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -7, snake_nonews Rs -308, snake Rs -328, gold Rs -862

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.