# Paper trading report

Updated 2026-11-27 12:55 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,128 | +12.06% | 0 | - | 237 |
| unified | 223,413 | +11.71% | 0 | - | 236 |
| oracle | 211,815 | +5.91% | 0 | - | 233 |
| intramonth | 210,911 | +5.46% | 0 | - | 235 |
| random_hold | 210,642 | +5.32% | 13 | 69% | 1,037 |
| intraweek | 208,363 | +4.18% | 40 | 55% | 4,400 |
| snake_abs_exit | 204,827 | +2.41% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,070 | +2.04% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,513 | +0.76% | 0 | - | 237 |
| snake_abs | 200,586 | +0.29% | 1 | 100% | 255 |
| snake_abs_conv | 200,404 | +0.20% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,821 | -3.09% | 3 | 33% | 374 |
| snake_viper_wild | 192,380 | -3.81% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,112 | -5.44% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,726 | -15.14% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,863 (-5.57%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +3,750 | +1.86% |
| gold | +3,732 | +2.25% |
| snake_abs_exit_conv | +3,673 | +1.83% |
| random_hold | +2,048 | +0.98% |
| snake_abs_conv | +2,037 | +1.03% |
| snake_abs | +2,034 | +1.02% |
| snake_anaconda | +1,524 | +0.79% |
| intraweek | +1,314 | +0.64% |
| benchmark_smallcap | +673 | +0.34% |
| intramonth | +378 | +0.18% |
| unified | +334 | +0.15% |
| snake_viper_wild | +174 | +0.09% |
| snake_viper_tick | +171 | +0.09% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -421 | -0.20% |
| benchmark | -1,859 | -0.82% |

Average per day so far: benchmark Rs +574, unified Rs +557, oracle Rs +281, intramonth Rs +260, random_hold Rs +253, intraweek Rs +199, snake_abs_exit Rs +124, snake_abs_exit_conv Rs +104, nifty_calls Rs +44, benchmark_smallcap Rs +40, snake_abs Rs +15, snake_abs_conv Rs +10, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -167, snake_viper_wild Rs -224, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -351, gold Rs -721

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.