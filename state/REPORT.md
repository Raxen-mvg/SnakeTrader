# Paper trading report

Updated 2026-11-06 11:04 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,946 | +7.47% | 0 | - | 236 |
| benchmark | 214,642 | +7.32% | 0 | - | 237 |
| intraweek | 210,723 | +5.36% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,784 | +4.89% | 1 | 100% | 255 |
| snake_abs_exit | 209,571 | +4.79% | 1 | 100% | 260 |
| intramonth | 207,047 | +3.52% | 0 | - | 235 |
| snake_abs | 206,739 | +3.37% | 1 | 100% | 255 |
| snake_abs_conv | 206,569 | +3.28% | 1 | 100% | 255 |
| oracle | 205,018 | +2.51% | 0 | - | 233 |
| random_hold | 203,473 | +1.74% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 197,127 | -1.44% | 3 | 33% | 702 |
| snake_anaconda | 196,982 | -1.51% | 3 | 33% | 374 |
| benchmark_smallcap | 194,708 | -2.65% | 0 | - | 237 |
| snake_viper_tick | 193,789 | -3.11% | 2 | 0% | 532 |
| gold | 189,865 | -5.07% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,542 (-6.23%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,305 | +0.62% |
| oracle | +947 | +0.46% |
| benchmark | +872 | +0.41% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -850 | -0.42% |
| intramonth | -902 | -0.43% |
| unified | -1,037 | -0.48% |
| benchmark_smallcap | -3,980 | -2.00% |
| gold | -4,357 | -2.24% |
| snake_abs | -4,950 | -2.34% |
| snake_abs_conv | -4,976 | -2.35% |
| snake_abs_exit_conv | -5,019 | -2.34% |
| snake_abs_exit | -5,088 | -2.37% |
| snake_anaconda | -5,498 | -2.71% |
| snake_viper_tick | -7,349 | -3.65% |
| snake_viper_wild | -7,529 | -3.68% |

Average per day so far: unified Rs +515, benchmark Rs +505, snake_abs_exit_conv Rs +376, intraweek Rs +370, snake_abs_exit Rs +368, snake_abs_conv Rs +253, snake_abs Rs +250, intramonth Rs +243, oracle Rs +173, random_hold Rs +120, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -126, snake_viper_wild Rs -137, benchmark_smallcap Rs -212, snake_viper_tick Rs -345, gold Rs -349, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.