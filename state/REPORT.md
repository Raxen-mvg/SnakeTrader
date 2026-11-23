# Paper trading report

Updated 2026-11-23 14:37 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,100 | +12.05% | 0 | - | 236 |
| benchmark | 222,162 | +11.08% | 0 | - | 237 |
| intramonth | 212,159 | +6.08% | 0 | - | 235 |
| oracle | 212,125 | +6.06% | 0 | - | 233 |
| intraweek | 212,121 | +6.06% | 40 | 55% | 4,400 |
| random_hold | 208,630 | +4.32% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,204 | +3.60% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,496 | +3.25% | 2 | 50% | 345 |
| snake_abs | 205,141 | +2.57% | 1 | 100% | 255 |
| snake_abs_conv | 204,963 | +2.48% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,124 | +0.56% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,753 | -0.12% | 0 | - | 237 |
| snake_anaconda | 198,250 | -0.88% | 3 | 33% | 374 |
| snake_viper_tick | 197,693 | -1.15% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,512 | -15.24% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,225 (-4.89%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,463 | +0.87% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -120 | -0.06% |
| oracle | -353 | -0.17% |
| snake_abs | -779 | -0.38% |
| snake_abs_conv | -820 | -0.40% |
| benchmark_smallcap | -1,155 | -0.57% |
| snake_abs_exit | -1,358 | -0.65% |
| snake_anaconda | -1,655 | -0.83% |
| snake_viper_tick | -1,679 | -0.84% |
| snake_viper_wild | -1,705 | -0.84% |
| unified | -2,082 | -0.92% |
| random_hold | -2,129 | -1.01% |
| intramonth | -2,845 | -1.32% |
| benchmark | -2,976 | -1.32% |
| intraweek | -3,591 | -1.67% |

Average per day so far: unified Rs +618, benchmark Rs +568, intramonth Rs +312, oracle Rs +311, intraweek Rs +311, random_hold Rs +221, snake_abs_exit Rs +200, snake_abs_exit_conv Rs +180, snake_abs Rs +139, snake_abs_conv Rs +138, nifty_calls Rs +47, snake_viper_wild Rs +36, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -7, snake_anaconda Rs -51, snake_viper_tick Rs -82, snake_nonews Rs -300, snake Rs -320, gold Rs -782

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.