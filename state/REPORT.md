# Paper trading report

Updated 2026-11-17 14:50 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,772 | +10.89% | 0 | - | 237 |
| unified | 221,282 | +10.64% | 0 | - | 236 |
| intraweek | 213,854 | +6.93% | 35 | 54% | 3,851 |
| snake_abs_exit | 213,594 | +6.80% | 2 | 50% | 345 |
| oracle | 212,495 | +6.25% | 0 | - | 233 |
| snake_abs_exit_conv | 212,047 | +6.02% | 2 | 50% | 345 |
| intramonth | 211,180 | +5.59% | 0 | - | 235 |
| snake_viper_wild | 210,017 | +5.01% | 14 | 50% | 2,496 |
| snake_abs | 208,871 | +4.44% | 1 | 100% | 255 |
| snake_abs_conv | 208,739 | +4.37% | 1 | 100% | 255 |
| random_hold | 208,179 | +4.09% | 10 | 70% | 733 |
| snake_viper_tick | 206,429 | +3.21% | 13 | 46% | 2,299 |
| snake_anaconda | 204,423 | +2.21% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,087 | +0.54% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,543 | -9.73% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,140 (-4.43%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,872 | +1.88% |
| snake_viper_tick | +3,809 | +1.88% |
| intraweek | +2,588 | +1.23% |
| benchmark | +1,691 | +0.77% |
| oracle | +472 | +0.22% |
| random_hold | +386 | +0.19% |
| benchmark_smallcap | +258 | +0.13% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| unified | -156 | -0.07% |
| gold | -411 | -0.23% |
| intramonth | -439 | -0.21% |
| snake_anaconda | -680 | -0.33% |
| snake_abs_exit | -816 | -0.38% |
| snake_abs_exit_conv | -1,170 | -0.55% |
| snake_abs_conv | -1,251 | -0.60% |
| snake_abs | -1,262 | -0.60% |

Average per day so far: benchmark Rs +622, unified Rs +608, snake_abs_exit Rs +425, intraweek Rs +396, snake_abs_exit_conv Rs +376, snake_viper_wild Rs +371, oracle Rs +357, intramonth Rs +319, snake_abs_conv Rs +273, snake_abs Rs +269, snake_viper_tick Rs +268, random_hold Rs +234, snake_anaconda Rs +147, nifty_calls Rs +52, benchmark_smallcap Rs +35, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -556

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.