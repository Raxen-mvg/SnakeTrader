# Paper trading report

Updated 2026-11-17 11:04 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,264 | +11.13% | 0 | - | 236 |
| benchmark | 221,649 | +10.82% | 0 | - | 237 |
| snake_abs_exit | 216,069 | +8.04% | 2 | 50% | 345 |
| snake_abs_exit_conv | 214,113 | +7.06% | 2 | 50% | 345 |
| intraweek | 214,112 | +7.06% | 35 | 54% | 3,851 |
| oracle | 212,977 | +6.49% | 0 | - | 233 |
| intramonth | 212,390 | +6.20% | 0 | - | 235 |
| snake_abs | 210,623 | +5.31% | 1 | 100% | 255 |
| snake_abs_conv | 210,475 | +5.24% | 1 | 100% | 255 |
| random_hold | 208,378 | +4.19% | 10 | 70% | 733 |
| snake_viper_wild | 207,407 | +3.70% | 14 | 50% | 2,496 |
| snake_anaconda | 206,085 | +3.04% | 3 | 33% | 374 |
| snake_viper_tick | 203,861 | +1.93% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,387 | +1.19% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,793 | -9.10% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,792 (-4.10%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,846 | +1.35% |
| snake_abs_exit | +1,660 | +0.77% |
| benchmark | +1,568 | +0.71% |
| benchmark_smallcap | +1,558 | +0.78% |
| snake_viper_wild | +1,263 | +0.61% |
| snake_viper_tick | +1,241 | +0.61% |
| snake_anaconda | +982 | +0.48% |
| oracle | +954 | +0.45% |
| snake_abs_exit_conv | +896 | +0.42% |
| gold | +838 | +0.46% |
| unified | +826 | +0.37% |
| intramonth | +771 | +0.36% |
| random_hold | +585 | +0.28% |
| snake_abs | +489 | +0.23% |
| snake_abs_conv | +485 | +0.23% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +636, benchmark Rs +619, snake_abs_exit Rs +502, snake_abs_exit_conv Rs +441, intraweek Rs +403, oracle Rs +371, intramonth Rs +354, snake_abs_conv Rs +327, snake_abs Rs +322, snake_viper_wild Rs +274, random_hold Rs +239, snake_anaconda Rs +203, snake_viper_tick Rs +161, benchmark_smallcap Rs +77, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -520

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.