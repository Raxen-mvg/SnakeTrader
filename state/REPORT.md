# Paper trading report

Updated 2026-11-25 11:06 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,926 | +12.96% | 0 | - | 237 |
| unified | 224,924 | +12.46% | 0 | - | 236 |
| intramonth | 212,742 | +6.37% | 0 | - | 235 |
| oracle | 212,019 | +6.01% | 0 | - | 233 |
| random_hold | 210,044 | +5.02% | 12 | 75% | 1,009 |
| intraweek | 208,580 | +4.29% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,624 | +0.81% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,129 | +0.56% | 2 | 50% | 345 |
| snake_abs | 201,123 | +0.56% | 1 | 100% | 255 |
| snake_abs_conv | 200,929 | +0.46% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,473 | -0.26% | 0 | - | 237 |
| snake_viper_wild | 195,364 | -2.32% | 16 | 50% | 2,827 |
| snake_anaconda | 193,239 | -3.38% | 3 | 33% | 374 |
| snake_viper_tick | 192,043 | -3.98% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,909 | -17.55% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,312 (-5.34%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,452 | +2.01% |
| random_hold | +1,618 | +0.78% |
| unified | +639 | +0.28% |
| benchmark_smallcap | +493 | +0.25% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -10 | -0.01% |
| oracle | -323 | -0.15% |
| intraweek | -3,039 | -1.44% |
| snake_abs | -4,338 | -2.11% |
| snake_abs_conv | -4,374 | -2.13% |
| gold | -4,521 | -2.67% |
| snake_anaconda | -5,464 | -2.75% |
| snake_viper_tick | -5,650 | -2.86% |
| snake_viper_wild | -5,760 | -2.86% |
| snake_abs_exit | -5,871 | -2.83% |
| snake_abs_exit_conv | -5,917 | -2.86% |

Average per day so far: benchmark Rs +648, unified Rs +623, intramonth Rs +319, oracle Rs +300, random_hold Rs +251, intraweek Rs +215, nifty_calls Rs +46, snake_abs_exit Rs +44, snake_abs_exit_conv Rs +31, snake_abs Rs +30, snake_abs_conv Rs +25, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -15, snake_viper_wild Rs -145, snake_anaconda Rs -193, snake_viper_tick Rs -274, snake_nonews Rs -292, snake Rs -311, gold Rs -877

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.