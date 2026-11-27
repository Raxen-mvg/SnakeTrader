# Paper trading report

Updated 2026-11-27 11:46 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,128 | +12.06% | 0 | - | 237 |
| unified | 222,100 | +11.05% | 0 | - | 236 |
| oracle | 211,672 | +5.84% | 0 | - | 233 |
| random_hold | 210,289 | +5.14% | 13 | 69% | 1,037 |
| intramonth | 210,266 | +5.13% | 0 | - | 235 |
| intraweek | 207,716 | +3.86% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,510 | +2.75% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,115 | +2.06% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,647 | +0.82% | 0 | - | 237 |
| snake_abs | 200,849 | +0.42% | 1 | 100% | 255 |
| snake_abs_conv | 200,674 | +0.34% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,265 | -2.87% | 3 | 33% | 374 |
| snake_viper_wild | 192,898 | -3.55% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,620 | -5.19% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,150 | -15.43% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,383 (-5.81%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,432 | +2.20% |
| snake_abs_exit_conv | +3,718 | +1.85% |
| gold | +3,156 | +1.90% |
| snake_abs_conv | +2,307 | +1.16% |
| snake_abs | +2,297 | +1.16% |
| snake_anaconda | +1,968 | +1.02% |
| random_hold | +1,695 | +0.81% |
| benchmark_smallcap | +807 | +0.40% |
| snake_viper_wild | +693 | +0.36% |
| snake_viper_tick | +679 | +0.36% |
| intraweek | +667 | +0.32% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intramonth | -268 | -0.13% |
| oracle | -563 | -0.27% |
| unified | -978 | -0.44% |
| benchmark | -1,859 | -0.82% |

Average per day so far: benchmark Rs +574, unified Rs +526, oracle Rs +278, random_hold Rs +245, intramonth Rs +244, intraweek Rs +184, snake_abs_exit Rs +141, snake_abs_exit_conv Rs +106, nifty_calls Rs +44, benchmark_smallcap Rs +43, snake_abs Rs +21, snake_abs_conv Rs +17, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -155, snake_viper_wild Rs -209, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -335, gold Rs -735

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.