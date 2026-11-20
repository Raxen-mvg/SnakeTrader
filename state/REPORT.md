# Paper trading report

Updated 2026-11-20 12:52 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,110 | +13.05% | 0 | - | 236 |
| benchmark | 224,441 | +12.22% | 0 | - | 237 |
| intramonth | 215,137 | +7.57% | 0 | - | 235 |
| intraweek | 214,495 | +7.25% | 35 | 54% | 3,851 |
| oracle | 212,687 | +6.34% | 0 | - | 233 |
| snake_abs_exit | 209,129 | +4.56% | 2 | 50% | 345 |
| random_hold | 208,984 | +4.49% | 11 | 73% | 979 |
| snake_abs_exit_conv | 207,140 | +3.57% | 2 | 50% | 345 |
| snake_abs | 206,261 | +3.13% | 1 | 100% | 255 |
| snake_abs_conv | 206,126 | +3.06% | 1 | 100% | 255 |
| snake_viper_wild | 205,142 | +2.57% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,644 | +0.82% | 15 | 47% | 2,625 |
| benchmark_smallcap | 201,098 | +0.55% | 0 | - | 237 |
| snake_anaconda | 200,265 | +0.13% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,487 | -16.76% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,882 (-4.06%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,066 | +0.93% |
| intraweek | +1,605 | +0.75% |
| unified | +1,495 | +0.67% |
| intramonth | +1,129 | +0.53% |
| oracle | +598 | +0.28% |
| random_hold | +531 | +0.26% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -370 | -0.18% |
| snake_viper_tick | -2,333 | -1.14% |
| snake_viper_wild | -2,381 | -1.15% |
| snake_abs | -2,719 | -1.30% |
| snake_abs_conv | -2,734 | -1.31% |
| snake_anaconda | -3,198 | -1.57% |
| snake_abs_exit_conv | -3,925 | -1.86% |
| snake_abs_exit | -4,222 | -1.98% |
| gold | -8,286 | -4.74% |

Average per day so far: unified Rs +687, benchmark Rs +643, intramonth Rs +398, intraweek Rs +381, oracle Rs +334, snake_abs_exit Rs +261, random_hold Rs +236, snake_abs_exit_conv Rs +204, snake_abs_conv Rs +175, snake_abs Rs +174, snake_viper_wild Rs +171, snake_viper_tick Rs +61, nifty_calls Rs +48, benchmark_smallcap Rs +32, snake_anaconda Rs +8, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -882

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.