# Paper trading report

Updated 2026-11-26 12:04 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,040 | +13.02% | 0 | - | 237 |
| unified | 223,190 | +11.60% | 0 | - | 236 |
| oracle | 213,013 | +6.51% | 0 | - | 233 |
| intramonth | 210,338 | +5.17% | 0 | - | 235 |
| random_hold | 209,871 | +4.93% | 13 | 69% | 1,037 |
| intraweek | 208,456 | +4.23% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,773 | +0.39% | 0 | - | 237 |
| snake_abs_exit | 200,664 | +0.33% | 2 | 50% | 345 |
| snake_abs_exit_conv | 200,128 | +0.06% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 198,468 | -0.77% | 1 | 100% | 255 |
| snake_abs_conv | 198,271 | -0.86% | 1 | 100% | 255 |
| snake_anaconda | 192,263 | -3.87% | 3 | 33% | 374 |
| snake_viper_wild | 192,210 | -3.90% | 16 | 50% | 2,827 |
| snake_viper_tick | 188,946 | -5.53% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,010 | -17.00% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,762 (-5.62%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,962 | +0.99% |
| intraweek | +1,713 | +0.83% |
| gold | +1,414 | +0.86% |
| benchmark | +1,017 | +0.45% |
| random_hold | +378 | +0.18% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -782 | -0.37% |
| unified | -909 | -0.41% |
| intramonth | -1,356 | -0.64% |
| snake_abs_exit | -1,591 | -0.79% |
| snake_abs | -1,682 | -0.84% |
| snake_abs_conv | -1,701 | -0.85% |
| snake_abs_exit_conv | -1,848 | -0.92% |
| snake_anaconda | -2,290 | -1.18% |
| snake_viper_tick | -5,231 | -2.69% |
| snake_viper_wild | -5,333 | -2.70% |

Average per day so far: benchmark Rs +635, unified Rs +566, oracle Rs +317, intramonth Rs +252, random_hold Rs +241, intraweek Rs +206, nifty_calls Rs +45, benchmark_smallcap Rs +21, snake_abs_exit Rs +17, snake_abs_exit_conv Rs +3, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -39, snake_abs_conv Rs -46, snake_anaconda Rs -215, snake_viper_wild Rs -236, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -368, gold Rs -829

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.