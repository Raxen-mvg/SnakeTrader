# Paper trading report

Updated 2026-11-27 15:25 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 223,432 | +11.72% | 0 | - | 237 |
| unified | 223,061 | +11.53% | 0 | - | 236 |
| random_hold | 211,613 | +5.81% | 13 | 69% | 1,037 |
| oracle | 211,501 | +5.75% | 0 | - | 233 |
| intramonth | 210,914 | +5.46% | 0 | - | 235 |
| intraweek | 207,906 | +3.95% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 206,486 | +3.24% | 2 | 50% | 345 |
| snake_abs_exit | 204,275 | +2.14% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,569 | +0.78% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,716 | -0.14% | 1 | 100% | 255 |
| snake_abs_conv | 199,526 | -0.24% | 1 | 100% | 255 |
| snake_anaconda | 192,907 | -3.55% | 3 | 33% | 374 |
| snake_viper_wild | 192,620 | -3.69% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,347 | -5.33% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,761 | -14.62% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,865 (-5.57%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +6,089 | +3.04% |
| gold | +4,768 | +2.87% |
| snake_abs_exit | +3,197 | +1.59% |
| random_hold | +3,019 | +1.45% |
| snake_abs | +1,164 | +0.59% |
| snake_abs_conv | +1,159 | +0.58% |
| intraweek | +857 | +0.41% |
| benchmark_smallcap | +729 | +0.36% |
| snake_anaconda | +610 | +0.32% |
| snake_viper_wild | +414 | +0.22% |
| snake_viper_tick | +406 | +0.21% |
| intramonth | +381 | +0.18% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| unified | -18 | -0.01% |
| oracle | -734 | -0.35% |
| benchmark | -2,555 | -1.13% |

Average per day so far: benchmark Rs +558, unified Rs +549, random_hold Rs +277, oracle Rs +274, intramonth Rs +260, intraweek Rs +188, snake_abs_exit_conv Rs +166, snake_abs_exit Rs +110, nifty_calls Rs +44, benchmark_smallcap Rs +41, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -7, snake_abs_conv Rs -12, snake_anaconda Rs -192, snake_viper_wild Rs -217, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -344, gold Rs -696

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.