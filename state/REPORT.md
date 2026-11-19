# Paper trading report

Updated 2026-11-19 10:32 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,853 | +11.93% | 0 | - | 236 |
| benchmark | 220,418 | +10.21% | 0 | - | 237 |
| snake_abs_exit | 213,548 | +6.77% | 2 | 50% | 345 |
| intramonth | 213,334 | +6.67% | 0 | - | 235 |
| intraweek | 211,839 | +5.92% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,780 | +5.89% | 2 | 50% | 345 |
| oracle | 210,809 | +5.40% | 0 | - | 233 |
| snake_abs | 209,313 | +4.66% | 1 | 100% | 255 |
| snake_abs_conv | 209,190 | +4.59% | 1 | 100% | 255 |
| snake_viper_wild | 207,878 | +3.94% | 16 | 50% | 2,827 |
| random_hold | 207,801 | +3.90% | 10 | 70% | 733 |
| snake_viper_tick | 204,325 | +2.16% | 15 | 47% | 2,625 |
| snake_anaconda | 203,509 | +1.75% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,078 | +0.04% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,559 | -12.72% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,198 (-4.40%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,241 | +0.56% |
| intramonth | +1,061 | +0.50% |
| random_hold | +868 | +0.42% |
| snake_viper_wild | +839 | +0.41% |
| snake_viper_tick | +822 | +0.40% |
| benchmark_smallcap | +751 | +0.38% |
| benchmark | +122 | +0.06% |
| oracle | +13 | +0.01% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -0 | -0.00% |
| snake_abs | -124 | -0.06% |
| snake_abs_conv | -134 | -0.06% |
| snake_abs_exit | -484 | -0.23% |
| snake_abs_exit_conv | -604 | -0.28% |
| snake_anaconda | -892 | -0.44% |
| gold | -2,762 | -1.56% |

Average per day so far: unified Rs +645, benchmark Rs +552, snake_abs_exit Rs +398, intramonth Rs +360, snake_abs_exit_conv Rs +346, intraweek Rs +320, oracle Rs +292, snake_viper_wild Rs +272, snake_abs_conv Rs +270, snake_abs Rs +266, random_hold Rs +211, snake_viper_tick Rs +166, snake_anaconda Rs +110, nifty_calls Rs +50, benchmark_smallcap Rs +2, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -688

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.