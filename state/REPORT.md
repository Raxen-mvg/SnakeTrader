# Paper trading report

Updated 2026-11-23 13:37 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,767 | +11.88% | 0 | - | 236 |
| benchmark | 222,292 | +11.15% | 0 | - | 237 |
| intraweek | 212,054 | +6.03% | 40 | 55% | 4,400 |
| intramonth | 212,015 | +6.01% | 0 | - | 235 |
| oracle | 211,563 | +5.78% | 0 | - | 233 |
| random_hold | 208,818 | +4.41% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,608 | +3.30% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,255 | +2.63% | 2 | 50% | 345 |
| snake_abs | 204,149 | +2.08% | 1 | 100% | 255 |
| snake_abs_conv | 203,981 | +1.99% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,553 | +0.28% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,316 | -0.34% | 0 | - | 237 |
| snake_anaconda | 197,710 | -1.15% | 3 | 33% | 374 |
| snake_viper_tick | 197,133 | -1.43% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,348 | -15.33% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,942 (-5.03%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,299 | +0.77% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -916 | -0.43% |
| snake_abs_exit_conv | -1,362 | -0.66% |
| benchmark_smallcap | -1,592 | -0.79% |
| snake_abs | -1,770 | -0.86% |
| snake_abs_conv | -1,802 | -0.88% |
| random_hold | -1,941 | -0.92% |
| snake_abs_exit | -1,954 | -0.94% |
| snake_anaconda | -2,195 | -1.10% |
| snake_viper_tick | -2,238 | -1.12% |
| snake_viper_wild | -2,276 | -1.12% |
| unified | -2,415 | -1.07% |
| benchmark | -2,846 | -1.26% |
| intramonth | -2,989 | -1.39% |
| intraweek | -3,658 | -1.70% |

Average per day so far: unified Rs +609, benchmark Rs +572, intraweek Rs +309, intramonth Rs +308, oracle Rs +296, random_hold Rs +226, snake_abs_exit Rs +184, snake_abs_exit_conv Rs +146, snake_abs Rs +112, snake_abs_conv Rs +111, nifty_calls Rs +47, snake_viper_wild Rs +18, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -20, snake_anaconda Rs -67, snake_viper_tick Rs -102, snake_nonews Rs -300, snake Rs -320, gold Rs -786

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.