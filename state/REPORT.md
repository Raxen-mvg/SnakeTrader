# Paper trading report

Updated 2026-11-26 13:00 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,048 | +13.02% | 0 | - | 237 |
| unified | 223,453 | +11.73% | 0 | - | 236 |
| oracle | 213,259 | +6.63% | 0 | - | 233 |
| intramonth | 210,567 | +5.28% | 0 | - | 235 |
| random_hold | 209,963 | +4.98% | 13 | 69% | 1,037 |
| intraweek | 208,282 | +4.14% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,672 | +0.34% | 0 | - | 237 |
| snake_abs_exit | 200,396 | +0.20% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit_conv | 199,892 | -0.05% | 2 | 50% | 345 |
| snake_abs | 198,236 | -0.88% | 1 | 100% | 255 |
| snake_abs_conv | 198,036 | -0.98% | 1 | 100% | 255 |
| snake_anaconda | 191,986 | -4.01% | 3 | 33% | 374 |
| snake_viper_wild | 191,841 | -4.08% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,584 | -5.71% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,323 | -16.84% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,850 (-5.57%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,861 | +0.94% |
| gold | +1,726 | +1.05% |
| intraweek | +1,539 | +0.74% |
| benchmark | +1,025 | +0.46% |
| random_hold | +470 | +0.23% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -536 | -0.25% |
| unified | -647 | -0.29% |
| intramonth | -1,127 | -0.53% |
| snake_abs_exit | -1,859 | -0.92% |
| snake_abs | -1,914 | -0.96% |
| snake_abs_conv | -1,936 | -0.97% |
| snake_abs_exit_conv | -2,084 | -1.03% |
| snake_anaconda | -2,567 | -1.32% |
| snake_viper_tick | -5,593 | -2.88% |
| snake_viper_wild | -5,703 | -2.89% |

Average per day so far: benchmark Rs +635, unified Rs +572, oracle Rs +323, intramonth Rs +258, random_hold Rs +243, intraweek Rs +202, nifty_calls Rs +45, benchmark_smallcap Rs +18, snake_abs_exit Rs +10, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_abs_exit_conv Rs -3, snake_abs Rs -45, snake_abs_conv Rs -52, snake_anaconda Rs -223, snake_viper_wild Rs -247, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -381, gold Rs -821

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.