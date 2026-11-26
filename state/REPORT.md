# Paper trading report

Updated 2026-11-26 12:42 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,101 | +13.05% | 0 | - | 237 |
| unified | 223,409 | +11.71% | 0 | - | 236 |
| oracle | 213,253 | +6.63% | 0 | - | 233 |
| intramonth | 210,493 | +5.25% | 0 | - | 235 |
| random_hold | 209,850 | +4.92% | 13 | 69% | 1,037 |
| intraweek | 208,264 | +4.13% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,571 | +0.29% | 0 | - | 237 |
| snake_abs_exit | 200,223 | +0.11% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit_conv | 199,783 | -0.11% | 2 | 50% | 345 |
| snake_abs | 198,184 | -0.91% | 1 | 100% | 255 |
| snake_abs_conv | 197,984 | -1.01% | 1 | 100% | 255 |
| snake_anaconda | 191,937 | -4.03% | 3 | 33% | 374 |
| snake_viper_wild | 191,846 | -4.08% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,589 | -5.71% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,306 | -16.85% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,798 (-5.60%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,760 | +0.89% |
| gold | +1,710 | +1.04% |
| intraweek | +1,521 | +0.73% |
| benchmark | +1,079 | +0.48% |
| random_hold | +357 | +0.17% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -542 | -0.25% |
| unified | -691 | -0.31% |
| intramonth | -1,201 | -0.57% |
| snake_abs | -1,966 | -0.98% |
| snake_abs_conv | -1,988 | -0.99% |
| snake_abs_exit | -2,032 | -1.00% |
| snake_abs_exit_conv | -2,193 | -1.09% |
| snake_anaconda | -2,616 | -1.34% |
| snake_viper_tick | -5,588 | -2.88% |
| snake_viper_wild | -5,698 | -2.88% |

Average per day so far: benchmark Rs +637, unified Rs +571, oracle Rs +323, intramonth Rs +256, random_hold Rs +240, intraweek Rs +202, nifty_calls Rs +45, benchmark_smallcap Rs +15, snake_abs_exit Rs +6, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_abs_exit_conv Rs -6, snake_abs Rs -47, snake_abs_conv Rs -53, snake_anaconda Rs -224, snake_viper_wild Rs -247, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -380, gold Rs -822

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.