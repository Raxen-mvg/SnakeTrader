# Paper trading report

Updated 2026-11-05 11:11 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,587 | +9.29% | 0 | - | 236 |
| snake_abs_exit_conv | 215,352 | +7.68% | 1 | 100% | 255 |
| snake_abs_exit | 215,061 | +7.53% | 1 | 100% | 260 |
| benchmark | 212,423 | +6.21% | 0 | - | 237 |
| snake_abs | 212,226 | +6.11% | 1 | 100% | 255 |
| snake_abs_conv | 212,092 | +6.05% | 1 | 100% | 255 |
| intraweek | 211,123 | +5.56% | 25 | 48% | 2,757 |
| intramonth | 210,431 | +5.22% | 0 | - | 235 |
| random_hold | 206,778 | +3.39% | 8 | 62% | 649 |
| snake_viper_wild | 206,750 | +3.38% | 3 | 33% | 702 |
| oracle | 204,334 | +2.17% | 0 | - | 233 |
| snake_anaconda | 203,480 | +1.74% | 3 | 33% | 374 |
| snake_viper_tick | 203,201 | +1.60% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,271 | -0.36% | 0 | - | 237 |
| gold | 193,975 | -3.01% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,669 (-4.67%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +4,148 | +1.93% |
| benchmark | +3,664 | +1.75% |
| random_hold | +3,469 | +1.71% |
| intramonth | +3,415 | +1.65% |
| benchmark_smallcap | +2,601 | +1.32% |
| gold | +2,581 | +1.35% |
| oracle | +2,542 | +1.26% |
| intraweek | +1,425 | +0.68% |
| snake_abs_exit_conv | +337 | +0.16% |
| snake_abs_conv | +334 | +0.16% |
| snake_abs | +323 | +0.15% |
| snake_abs_exit | +161 | +0.07% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_anaconda | -341 | -0.17% |
| snake_viper_tick | -2,200 | -1.07% |
| snake_viper_wild | -2,279 | -1.09% |

Average per day so far: unified Rs +664, snake_abs_exit_conv Rs +614, snake_abs_exit Rs +602, snake_abs_conv Rs +484, snake_abs Rs +470, benchmark Rs +444, intraweek Rs +397, intramonth Rs +373, snake_viper_wild Rs +338, random_hold Rs +242, snake_viper_tick Rs +188, oracle Rs +155, snake_anaconda Rs +151, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -30, gold Rs -215, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.