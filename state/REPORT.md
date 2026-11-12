# Paper trading report

Updated 2026-11-12 10:24 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,116 | +11.56% | 0 | - | 236 |
| benchmark | 220,938 | +10.47% | 0 | - | 237 |
| snake_abs_exit_conv | 219,727 | +9.86% | 2 | 50% | 345 |
| snake_abs_exit | 218,833 | +9.42% | 2 | 50% | 345 |
| snake_abs | 216,581 | +8.29% | 1 | 100% | 255 |
| snake_abs_conv | 216,419 | +8.21% | 1 | 100% | 255 |
| intraweek | 215,483 | +7.74% | 30 | 53% | 3,302 |
| oracle | 213,820 | +6.91% | 0 | - | 233 |
| intramonth | 213,252 | +6.63% | 0 | - | 235 |
| snake_viper_wild | 209,451 | +4.72% | 10 | 50% | 1,825 |
| random_hold | 208,185 | +4.09% | 10 | 70% | 733 |
| snake_anaconda | 207,452 | +3.73% | 3 | 33% | 374 |
| snake_viper_tick | 205,859 | +2.93% | 9 | 44% | 1,639 |
| benchmark_smallcap | 203,575 | +1.79% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 186,100 | -6.95% | 0 | - | 237 |

Combined allocator (virtual): Rs 193,080 (-3.46%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +3,329 | +1.63% |
| unified | +3,302 | +1.50% |
| snake_abs_conv | +2,961 | +1.39% |
| snake_abs | +2,956 | +1.38% |
| benchmark_smallcap | +2,769 | +1.38% |
| snake_viper_wild | +2,709 | +1.31% |
| snake_abs_exit | +2,671 | +1.24% |
| snake_viper_tick | +2,650 | +1.30% |
| snake_abs_exit_conv | +2,576 | +1.19% |
| intraweek | +2,350 | +1.10% |
| intramonth | +2,256 | +1.07% |
| oracle | +1,817 | +0.86% |
| benchmark | +1,675 | +0.76% |
| random_hold | +1,074 | +0.52% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,485 | -1.84% |

Average per day so far: unified Rs +722, snake_abs_exit_conv Rs +680, benchmark Rs +654, snake_abs_exit Rs +649, snake_abs_conv Rs +566, snake_abs Rs +553, intraweek Rs +484, oracle Rs +432, intramonth Rs +414, snake_viper_wild Rs +394, snake_viper_tick Rs +279, snake_anaconda Rs +276, random_hold Rs +256, benchmark_smallcap Rs +128, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.