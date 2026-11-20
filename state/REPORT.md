# Paper trading report

Updated 2026-11-20 11:23 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,821 | +12.91% | 0 | - | 236 |
| benchmark | 222,942 | +11.47% | 0 | - | 237 |
| intramonth | 214,791 | +7.40% | 0 | - | 235 |
| intraweek | 214,366 | +7.18% | 35 | 54% | 3,851 |
| oracle | 212,782 | +6.39% | 0 | - | 233 |
| snake_abs_exit | 210,421 | +5.21% | 2 | 50% | 345 |
| random_hold | 209,159 | +4.58% | 11 | 73% | 979 |
| snake_abs_exit_conv | 208,054 | +4.03% | 2 | 50% | 345 |
| snake_abs | 207,232 | +3.62% | 1 | 100% | 255 |
| snake_abs_conv | 207,094 | +3.55% | 1 | 100% | 255 |
| snake_viper_wild | 205,810 | +2.90% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,298 | +1.15% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,131 | +0.56% | 3 | 33% | 374 |
| benchmark_smallcap | 200,414 | +0.21% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,240 | -16.88% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,972 (-4.01%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,477 | +0.69% |
| unified | +1,206 | +0.54% |
| intramonth | +783 | +0.37% |
| random_hold | +706 | +0.34% |
| oracle | +694 | +0.33% |
| benchmark | +566 | +0.26% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -1,054 | -0.52% |
| snake_viper_tick | -1,679 | -0.82% |
| snake_viper_wild | -1,713 | -0.82% |
| snake_abs | -1,747 | -0.84% |
| snake_abs_conv | -1,766 | -0.85% |
| snake_anaconda | -2,333 | -1.15% |
| snake_abs_exit | -2,931 | -1.37% |
| snake_abs_exit_conv | -3,010 | -1.43% |
| gold | -8,532 | -4.88% |

Average per day so far: unified Rs +680, benchmark Rs +604, intramonth Rs +389, intraweek Rs +378, oracle Rs +336, snake_abs_exit Rs +298, random_hold Rs +241, snake_abs_exit_conv Rs +230, snake_abs_conv Rs +203, snake_abs Rs +201, snake_viper_wild Rs +194, snake_viper_tick Rs +85, nifty_calls Rs +48, snake_anaconda Rs +34, benchmark_smallcap Rs +12, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -888

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.