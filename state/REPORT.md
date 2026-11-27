# Paper trading report

Updated 2026-11-27 11:37 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,166 | +12.08% | 0 | - | 237 |
| unified | 222,205 | +11.10% | 0 | - | 236 |
| oracle | 211,915 | +5.96% | 0 | - | 233 |
| intramonth | 210,350 | +5.17% | 0 | - | 235 |
| random_hold | 210,282 | +5.14% | 13 | 69% | 1,037 |
| intraweek | 207,803 | +3.90% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,383 | +2.69% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,064 | +2.03% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,625 | +0.81% | 0 | - | 237 |
| snake_abs | 200,862 | +0.43% | 1 | 100% | 255 |
| snake_abs_conv | 200,686 | +0.34% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,377 | -2.81% | 3 | 33% | 374 |
| snake_viper_wild | 193,206 | -3.40% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,921 | -5.04% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,085 | -15.46% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,467 (-5.77%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,305 | +2.14% |
| snake_abs_exit_conv | +3,667 | +1.83% |
| gold | +3,091 | +1.86% |
| snake_abs_conv | +2,320 | +1.17% |
| snake_abs | +2,310 | +1.16% |
| snake_anaconda | +2,081 | +1.08% |
| random_hold | +1,687 | +0.81% |
| snake_viper_wild | +1,000 | +0.52% |
| snake_viper_tick | +980 | +0.52% |
| benchmark_smallcap | +785 | +0.39% |
| intraweek | +754 | +0.36% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intramonth | -183 | -0.09% |
| oracle | -321 | -0.15% |
| unified | -874 | -0.39% |
| benchmark | -1,821 | -0.81% |

Average per day so far: benchmark Rs +575, unified Rs +529, oracle Rs +284, intramonth Rs +246, random_hold Rs +245, intraweek Rs +186, snake_abs_exit Rs +138, snake_abs_exit_conv Rs +104, nifty_calls Rs +44, benchmark_smallcap Rs +43, snake_abs Rs +22, snake_abs_conv Rs +18, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -152, snake_viper_wild Rs -200, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -325, gold Rs -736

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.