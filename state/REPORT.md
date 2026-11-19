# Paper trading report

Updated 2026-11-19 11:32 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,646 | +11.82% | 0 | - | 236 |
| benchmark | 221,106 | +10.55% | 0 | - | 237 |
| snake_abs_exit | 213,542 | +6.77% | 2 | 50% | 345 |
| intramonth | 213,145 | +6.57% | 0 | - | 235 |
| intraweek | 211,829 | +5.91% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,580 | +5.79% | 2 | 50% | 345 |
| oracle | 211,096 | +5.55% | 0 | - | 233 |
| snake_abs | 209,104 | +4.55% | 1 | 100% | 255 |
| snake_abs_conv | 208,981 | +4.49% | 1 | 100% | 255 |
| random_hold | 207,659 | +3.83% | 10 | 70% | 733 |
| snake_viper_wild | 207,417 | +3.71% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,874 | +1.94% | 15 | 47% | 2,625 |
| snake_anaconda | 203,277 | +1.64% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,571 | +0.29% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,430 | -12.29% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,171 (-4.41%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,244 | +0.62% |
| unified | +1,034 | +0.47% |
| intramonth | +872 | +0.41% |
| benchmark | +811 | +0.37% |
| random_hold | +727 | +0.35% |
| snake_viper_wild | +378 | +0.18% |
| snake_viper_tick | +370 | +0.18% |
| oracle | +300 | +0.14% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -10 | -0.01% |
| snake_abs | -332 | -0.16% |
| snake_abs_conv | -343 | -0.16% |
| snake_abs_exit | -490 | -0.23% |
| snake_abs_exit_conv | -803 | -0.38% |
| snake_anaconda | -1,124 | -0.55% |
| gold | -1,891 | -1.07% |

Average per day so far: unified Rs +639, benchmark Rs +570, snake_abs_exit Rs +398, intramonth Rs +355, snake_abs_exit_conv Rs +341, intraweek Rs +320, oracle Rs +300, snake_abs_conv Rs +264, snake_abs Rs +260, snake_viper_wild Rs +256, random_hold Rs +207, snake_viper_tick Rs +149, snake_anaconda Rs +102, nifty_calls Rs +50, benchmark_smallcap Rs +17, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -664

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.