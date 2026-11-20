# Paper trading report

Updated 2026-11-20 14:02 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,386 | +13.19% | 0 | - | 236 |
| benchmark | 224,472 | +12.24% | 0 | - | 237 |
| intraweek | 215,833 | +7.92% | 35 | 54% | 3,851 |
| intramonth | 215,183 | +7.59% | 0 | - | 235 |
| oracle | 212,801 | +6.40% | 0 | - | 233 |
| random_hold | 210,102 | +5.05% | 11 | 73% | 979 |
| snake_abs_exit | 208,956 | +4.48% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,891 | +3.45% | 2 | 50% | 345 |
| snake_abs | 206,026 | +3.01% | 1 | 100% | 255 |
| snake_abs_conv | 205,895 | +2.95% | 1 | 100% | 255 |
| snake_viper_wild | 203,503 | +1.75% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,277 | +0.64% | 0 | - | 237 |
| snake_anaconda | 200,185 | +0.09% | 3 | 33% | 374 |
| snake_viper_tick | 200,033 | +0.02% | 15 | 47% | 2,625 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,263 | -15.87% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,116 (-3.94%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,944 | +1.38% |
| benchmark | +2,096 | +0.94% |
| unified | +1,771 | +0.79% |
| random_hold | +1,649 | +0.79% |
| intramonth | +1,175 | +0.55% |
| oracle | +712 | +0.34% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -191 | -0.10% |
| snake_abs | -2,954 | -1.41% |
| snake_abs_conv | -2,965 | -1.42% |
| snake_anaconda | -3,279 | -1.61% |
| snake_viper_tick | -3,944 | -1.93% |
| snake_viper_wild | -4,020 | -1.94% |
| snake_abs_exit_conv | -4,173 | -1.98% |
| snake_abs_exit | -4,395 | -2.06% |
| gold | -6,510 | -3.73% |

Average per day so far: unified Rs +694, benchmark Rs +644, intraweek Rs +417, intramonth Rs +400, oracle Rs +337, random_hold Rs +266, snake_abs_exit Rs +256, snake_abs_exit_conv Rs +197, snake_abs_conv Rs +168, snake_abs Rs +167, snake_viper_wild Rs +117, nifty_calls Rs +48, benchmark_smallcap Rs +38, snake_anaconda Rs +6, snake_viper_tick Rs +1, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -835

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.