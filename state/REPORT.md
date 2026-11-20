# Paper trading report

Updated 2026-11-20 10:06 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,984 | +12.49% | 0 | - | 236 |
| benchmark | 222,437 | +11.22% | 0 | - | 237 |
| intramonth | 214,148 | +7.07% | 0 | - | 235 |
| intraweek | 213,607 | +6.80% | 35 | 54% | 3,851 |
| oracle | 212,629 | +6.32% | 0 | - | 233 |
| snake_abs_exit | 210,299 | +5.15% | 2 | 50% | 345 |
| random_hold | 208,736 | +4.37% | 11 | 73% | 979 |
| snake_abs_exit_conv | 208,063 | +4.03% | 2 | 50% | 345 |
| snake_abs | 206,754 | +3.38% | 1 | 100% | 255 |
| snake_abs_conv | 206,617 | +3.31% | 1 | 100% | 255 |
| snake_viper_wild | 205,377 | +2.69% | 16 | 50% | 2,827 |
| snake_viper_tick | 201,876 | +0.94% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,128 | +0.56% | 3 | 33% | 374 |
| benchmark_smallcap | 200,482 | +0.24% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,073 | -17.46% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,560 (-4.22%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +718 | +0.34% |
| oracle | +540 | +0.26% |
| unified | +368 | +0.16% |
| random_hold | +283 | +0.14% |
| intramonth | +140 | +0.07% |
| benchmark | +61 | +0.03% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -986 | -0.49% |
| snake_viper_tick | -2,101 | -1.03% |
| snake_viper_wild | -2,146 | -1.03% |
| snake_abs | -2,225 | -1.06% |
| snake_abs_conv | -2,244 | -1.07% |
| snake_anaconda | -2,335 | -1.15% |
| snake_abs_exit_conv | -3,001 | -1.42% |
| snake_abs_exit | -3,052 | -1.43% |
| gold | -9,700 | -5.55% |

Average per day so far: unified Rs +657, benchmark Rs +590, intramonth Rs +372, intraweek Rs +358, oracle Rs +332, snake_abs_exit Rs +294, snake_abs_exit_conv Rs +230, random_hold Rs +230, snake_abs_conv Rs +189, snake_abs Rs +188, snake_viper_wild Rs +179, snake_viper_tick Rs +69, nifty_calls Rs +48, snake_anaconda Rs +34, benchmark_smallcap Rs +14, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -919

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.