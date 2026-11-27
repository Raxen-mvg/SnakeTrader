# Paper trading report

Updated 2026-11-27 12:46 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,350 | +12.18% | 0 | - | 237 |
| unified | 223,341 | +11.67% | 0 | - | 236 |
| oracle | 211,971 | +5.99% | 0 | - | 233 |
| intramonth | 210,868 | +5.43% | 0 | - | 235 |
| random_hold | 210,520 | +5.26% | 13 | 69% | 1,037 |
| intraweek | 208,316 | +4.16% | 40 | 55% | 4,400 |
| snake_abs_exit | 204,994 | +2.50% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,743 | +1.87% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,681 | +0.84% | 0 | - | 237 |
| snake_abs | 200,515 | +0.26% | 1 | 100% | 255 |
| snake_abs_conv | 200,337 | +0.17% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,933 | -3.03% | 3 | 33% | 374 |
| snake_viper_wild | 192,390 | -3.81% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,122 | -5.44% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,824 | -15.09% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,864 (-5.57%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +3,917 | +1.95% |
| gold | +3,831 | +2.31% |
| snake_abs_exit_conv | +3,346 | +1.67% |
| snake_abs_conv | +1,970 | +0.99% |
| snake_abs | +1,963 | +0.99% |
| random_hold | +1,926 | +0.92% |
| snake_anaconda | +1,637 | +0.85% |
| intraweek | +1,267 | +0.61% |
| benchmark_smallcap | +841 | +0.42% |
| intramonth | +335 | +0.16% |
| unified | +262 | +0.12% |
| snake_viper_wild | +184 | +0.10% |
| snake_viper_tick | +181 | +0.10% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -264 | -0.12% |
| benchmark | -1,637 | -0.72% |

Average per day so far: benchmark Rs +580, unified Rs +556, oracle Rs +285, intramonth Rs +259, random_hold Rs +250, intraweek Rs +198, snake_abs_exit Rs +128, snake_abs_exit_conv Rs +96, benchmark_smallcap Rs +44, nifty_calls Rs +44, snake_abs Rs +13, snake_abs_conv Rs +9, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -164, snake_viper_wild Rs -224, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -351, gold Rs -718

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.