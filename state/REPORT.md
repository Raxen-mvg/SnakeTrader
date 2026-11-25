# Paper trading report

Updated 2026-11-25 14:58 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,740 | +12.37% | 0 | - | 237 |
| unified | 224,490 | +12.24% | 0 | - | 236 |
| oracle | 213,346 | +6.67% | 0 | - | 233 |
| intramonth | 211,946 | +5.97% | 0 | - | 235 |
| random_hold | 209,652 | +4.83% | 12 | 75% | 1,009 |
| intraweek | 206,958 | +3.48% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,295 | +1.15% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,017 | +1.01% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,337 | +0.17% | 1 | 100% | 255 |
| snake_abs_conv | 200,157 | +0.08% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,991 | -0.51% | 0 | - | 237 |
| snake_viper_wild | 197,649 | -1.18% | 16 | 50% | 2,827 |
| snake_anaconda | 194,356 | -2.82% | 3 | 33% | 374 |
| snake_viper_tick | 194,280 | -2.86% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,007 | -17.50% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,143 (-5.43%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,267 | +1.48% |
| random_hold | +1,226 | +0.59% |
| oracle | +1,004 | +0.47% |
| unified | +205 | +0.09% |
| benchmark_smallcap | +11 | +0.01% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -805 | -0.38% |
| snake_viper_tick | -3,412 | -1.73% |
| snake_viper_wild | -3,475 | -1.73% |
| snake_anaconda | -4,348 | -2.19% |
| gold | -4,422 | -2.61% |
| intraweek | -4,661 | -2.20% |
| snake_abs_exit_conv | -5,029 | -2.43% |
| snake_abs | -5,124 | -2.49% |
| snake_abs_conv | -5,145 | -2.51% |
| snake_abs_exit | -5,200 | -2.51% |

Average per day so far: benchmark Rs +618, unified Rs +612, oracle Rs +334, intramonth Rs +299, random_hold Rs +241, intraweek Rs +174, snake_abs_exit Rs +62, snake_abs_exit_conv Rs +55, nifty_calls Rs +46, snake_abs Rs +9, snake_abs_conv Rs +4, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -28, snake_viper_wild Rs -73, snake_anaconda Rs -161, snake_viper_tick Rs -197, snake_nonews Rs -292, snake Rs -311, gold Rs -875

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.