# Paper trading report

Updated 2026-11-19 09:53 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,356 | +12.18% | 0 | - | 236 |
| benchmark | 220,310 | +10.15% | 0 | - | 237 |
| snake_abs_exit | 214,366 | +7.18% | 2 | 50% | 345 |
| intramonth | 214,141 | +7.07% | 0 | - | 235 |
| snake_abs_exit_conv | 212,400 | +6.20% | 2 | 50% | 345 |
| intraweek | 211,879 | +5.94% | 35 | 54% | 3,851 |
| oracle | 211,608 | +5.80% | 0 | - | 233 |
| snake_abs | 209,662 | +4.83% | 1 | 100% | 255 |
| snake_abs_conv | 209,544 | +4.77% | 1 | 100% | 255 |
| random_hold | 207,981 | +3.99% | 10 | 70% | 733 |
| snake_viper_wild | 207,731 | +3.87% | 16 | 50% | 2,827 |
| snake_anaconda | 204,363 | +2.18% | 3 | 33% | 374 |
| snake_viper_tick | 204,180 | +2.09% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,482 | +0.24% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,921 | -12.54% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,684 (-4.16%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| intramonth | +1,867 | +0.88% |
| unified | +1,745 | +0.78% |
| benchmark_smallcap | +1,155 | +0.58% |
| random_hold | +1,048 | +0.51% |
| oracle | +812 | +0.39% |
| snake_viper_wild | +691 | +0.33% |
| snake_viper_tick | +677 | +0.33% |
| snake_abs_exit | +335 | +0.16% |
| snake_abs | +226 | +0.11% |
| snake_abs_conv | +219 | +0.10% |
| intraweek | +40 | +0.02% |
| snake_abs_exit_conv | +16 | +0.01% |
| benchmark | +15 | +0.01% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_anaconda | -38 | -0.02% |
| gold | -2,400 | -1.35% |

Average per day so far: unified Rs +658, benchmark Rs +549, snake_abs_exit Rs +423, intramonth Rs +382, snake_abs_exit_conv Rs +365, intraweek Rs +321, oracle Rs +314, snake_abs_conv Rs +281, snake_abs Rs +276, snake_viper_wild Rs +267, random_hold Rs +216, snake_viper_tick Rs +161, snake_anaconda Rs +136, nifty_calls Rs +50, benchmark_smallcap Rs +15, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -678

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.