# Paper trading report

Updated 2026-11-23 14:46 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,191 | +12.10% | 0 | - | 236 |
| benchmark | 222,055 | +11.03% | 0 | - | 237 |
| oracle | 212,302 | +6.15% | 0 | - | 233 |
| intraweek | 212,138 | +6.07% | 40 | 55% | 4,400 |
| intramonth | 212,063 | +6.03% | 0 | - | 235 |
| random_hold | 208,865 | +4.43% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,184 | +3.59% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,559 | +3.28% | 2 | 50% | 345 |
| snake_abs | 205,224 | +2.61% | 1 | 100% | 255 |
| snake_abs_conv | 205,045 | +2.52% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,383 | +0.69% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,955 | -0.02% | 0 | - | 237 |
| snake_anaconda | 198,268 | -0.87% | 3 | 33% | 374 |
| snake_viper_tick | 197,946 | -1.03% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,874 | -15.06% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,303 (-4.85%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,825 | +1.09% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -57 | -0.03% |
| oracle | -177 | -0.08% |
| snake_abs | -696 | -0.34% |
| snake_abs_conv | -738 | -0.36% |
| benchmark_smallcap | -953 | -0.47% |
| snake_abs_exit | -1,378 | -0.66% |
| snake_viper_tick | -1,425 | -0.71% |
| snake_viper_wild | -1,446 | -0.71% |
| snake_anaconda | -1,638 | -0.82% |
| random_hold | -1,894 | -0.90% |
| unified | -1,991 | -0.88% |
| intramonth | -2,942 | -1.37% |
| benchmark | -3,083 | -1.37% |
| intraweek | -3,574 | -1.66% |

Average per day so far: unified Rs +620, benchmark Rs +566, oracle Rs +315, intraweek Rs +311, intramonth Rs +309, random_hold Rs +227, snake_abs_exit Rs +200, snake_abs_exit_conv Rs +182, snake_abs Rs +141, snake_abs_conv Rs +140, nifty_calls Rs +47, snake_viper_wild Rs +45, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -1, snake_anaconda Rs -51, snake_viper_tick Rs -73, snake_nonews Rs -300, snake Rs -320, gold Rs -772

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.