# Paper trading report

Updated 2026-11-25 15:16 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,985 | +12.49% | 0 | - | 237 |
| unified | 223,949 | +11.97% | 0 | - | 236 |
| oracle | 213,137 | +6.57% | 0 | - | 233 |
| intramonth | 211,389 | +5.70% | 0 | - | 235 |
| random_hold | 210,000 | +5.00% | 12 | 75% | 1,009 |
| intraweek | 206,908 | +3.45% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,375 | +1.19% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,084 | +1.04% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,353 | +0.18% | 1 | 100% | 255 |
| snake_abs_conv | 200,176 | +0.09% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,957 | -0.52% | 0 | - | 237 |
| snake_viper_wild | 197,462 | -1.27% | 16 | 50% | 2,827 |
| snake_anaconda | 194,454 | -2.77% | 3 | 33% | 374 |
| snake_viper_tick | 194,097 | -2.95% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,909 | -17.55% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,012 (-5.49%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,511 | +1.58% |
| random_hold | +1,573 | +0.76% |
| oracle | +795 | +0.37% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| benchmark_smallcap | -22 | -0.01% |
| unified | -336 | -0.15% |
| intramonth | -1,362 | -0.64% |
| snake_viper_tick | -3,596 | -1.82% |
| snake_viper_wild | -3,663 | -1.82% |
| snake_anaconda | -4,250 | -2.14% |
| gold | -4,521 | -2.67% |
| intraweek | -4,711 | -2.23% |
| snake_abs_exit_conv | -4,962 | -2.40% |
| snake_abs | -5,108 | -2.49% |
| snake_abs_exit | -5,120 | -2.47% |
| snake_abs_conv | -5,126 | -2.50% |

Average per day so far: benchmark Rs +625, unified Rs +599, oracle Rs +328, intramonth Rs +285, random_hold Rs +250, intraweek Rs +173, snake_abs_exit Rs +64, snake_abs_exit_conv Rs +56, nifty_calls Rs +46, snake_abs Rs +9, snake_abs_conv Rs +5, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -29, snake_viper_wild Rs -79, snake_anaconda Rs -158, snake_viper_tick Rs -204, snake_nonews Rs -292, snake Rs -311, gold Rs -877

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.