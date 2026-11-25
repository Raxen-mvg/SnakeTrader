# Paper trading report

Updated 2026-11-25 09:35 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,854 | +12.93% | 0 | - | 236 |
| benchmark | 224,870 | +12.44% | 0 | - | 237 |
| intramonth | 213,446 | +6.72% | 0 | - | 235 |
| oracle | 213,156 | +6.58% | 0 | - | 233 |
| intraweek | 211,657 | +5.83% | 40 | 55% | 4,400 |
| random_hold | 209,492 | +4.75% | 12 | 75% | 1,009 |
| snake_abs_exit | 203,227 | +1.61% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,696 | +1.35% | 2 | 50% | 345 |
| snake_abs | 201,895 | +0.95% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_conv | 201,713 | +0.86% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,943 | -0.03% | 0 | - | 237 |
| snake_viper_wild | 199,209 | -0.40% | 16 | 50% | 2,827 |
| snake_viper_tick | 195,817 | -2.09% | 15 | 47% | 2,625 |
| snake_anaconda | 195,105 | -2.45% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,566 | -17.22% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,251 (-4.87%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,397 | +1.53% |
| unified | +1,569 | +0.70% |
| random_hold | +1,066 | +0.51% |
| benchmark_smallcap | +964 | +0.48% |
| oracle | +814 | +0.38% |
| intramonth | +695 | +0.33% |
| intraweek | +38 | +0.02% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -1,875 | -0.95% |
| snake_viper_wild | -1,915 | -0.95% |
| snake_abs | -3,566 | -1.74% |
| snake_abs_conv | -3,589 | -1.75% |
| snake_anaconda | -3,599 | -1.81% |
| gold | -3,863 | -2.28% |
| snake_abs_exit | -4,268 | -2.06% |
| snake_abs_exit_conv | -4,350 | -2.10% |

Average per day so far: unified Rs +646, benchmark Rs +622, intramonth Rs +336, oracle Rs +329, intraweek Rs +291, random_hold Rs +237, snake_abs_exit Rs +87, snake_abs_exit_conv Rs +73, snake_abs Rs +50, snake_abs_conv Rs +46, nifty_calls Rs +46, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -2, snake_viper_wild Rs -25, snake_anaconda Rs -140, snake_viper_tick Rs -144, snake_nonews Rs -292, snake Rs -311, gold Rs -861

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.