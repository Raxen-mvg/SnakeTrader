# Paper trading report

Updated 2026-11-19 10:42 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,882 | +11.94% | 0 | - | 236 |
| benchmark | 220,655 | +10.33% | 0 | - | 237 |
| intramonth | 213,415 | +6.71% | 0 | - | 235 |
| snake_abs_exit | 213,329 | +6.67% | 2 | 50% | 345 |
| intraweek | 212,107 | +6.05% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,506 | +5.75% | 2 | 50% | 345 |
| oracle | 211,093 | +5.55% | 0 | - | 233 |
| snake_abs | 209,196 | +4.60% | 1 | 100% | 255 |
| snake_abs_conv | 209,065 | +4.53% | 1 | 100% | 255 |
| random_hold | 207,745 | +3.87% | 10 | 70% | 733 |
| snake_viper_wild | 207,720 | +3.86% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,170 | +2.08% | 15 | 47% | 2,625 |
| snake_anaconda | 203,325 | +1.66% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,302 | +0.15% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,724 | -12.64% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,308 (-4.35%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,271 | +0.57% |
| intramonth | +1,142 | +0.54% |
| benchmark_smallcap | +975 | +0.49% |
| random_hold | +813 | +0.39% |
| snake_viper_wild | +680 | +0.33% |
| snake_viper_tick | +666 | +0.33% |
| benchmark | +360 | +0.16% |
| oracle | +297 | +0.14% |
| intraweek | +268 | +0.13% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -241 | -0.12% |
| snake_abs_conv | -259 | -0.12% |
| snake_abs_exit | -702 | -0.33% |
| snake_abs_exit_conv | -878 | -0.41% |
| snake_anaconda | -1,076 | -0.53% |
| gold | -2,598 | -1.47% |

Average per day so far: unified Rs +645, benchmark Rs +558, snake_abs_exit Rs +392, intramonth Rs +363, snake_abs_exit_conv Rs +338, intraweek Rs +327, oracle Rs +300, snake_abs_conv Rs +267, snake_viper_wild Rs +266, snake_abs Rs +263, random_hold Rs +209, snake_viper_tick Rs +160, snake_anaconda Rs +104, nifty_calls Rs +50, benchmark_smallcap Rs +9, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -683

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.