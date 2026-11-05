# Paper trading report

Updated 2026-11-05 09:42 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,298 | +9.15% | 0 | - | 236 |
| snake_abs_exit_conv | 216,475 | +8.24% | 1 | 100% | 255 |
| snake_abs_exit | 216,181 | +8.09% | 1 | 100% | 260 |
| snake_abs | 213,339 | +6.67% | 1 | 100% | 255 |
| snake_abs_conv | 213,190 | +6.59% | 1 | 100% | 255 |
| benchmark | 212,492 | +6.25% | 0 | - | 237 |
| intraweek | 211,126 | +5.56% | 25 | 48% | 2,757 |
| intramonth | 210,152 | +5.08% | 0 | - | 235 |
| snake_viper_wild | 206,630 | +3.31% | 3 | 33% | 702 |
| random_hold | 205,724 | +2.86% | 8 | 62% | 649 |
| oracle | 204,312 | +2.16% | 0 | - | 233 |
| snake_anaconda | 203,456 | +1.73% | 3 | 33% | 374 |
| snake_viper_tick | 203,098 | +1.55% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,327 | -0.34% | 0 | - | 237 |
| gold | 195,274 | -2.36% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,936 (-4.53%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +3,880 | +2.03% |
| unified | +3,859 | +1.80% |
| benchmark | +3,733 | +1.79% |
| intramonth | +3,136 | +1.51% |
| benchmark_smallcap | +2,657 | +1.35% |
| oracle | +2,519 | +1.25% |
| random_hold | +2,415 | +1.19% |
| snake_abs_exit_conv | +1,461 | +0.68% |
| snake_abs | +1,436 | +0.68% |
| snake_abs_conv | +1,432 | +0.68% |
| intraweek | +1,429 | +0.68% |
| snake_abs_exit | +1,280 | +0.60% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_anaconda | -364 | -0.18% |
| snake_viper_tick | -2,302 | -1.12% |
| snake_viper_wild | -2,400 | -1.15% |

Average per day so far: snake_abs_exit_conv Rs +659, unified Rs +654, snake_abs_exit Rs +647, snake_abs_conv Rs +528, snake_abs Rs +513, benchmark Rs +446, intraweek Rs +397, intramonth Rs +363, snake_viper_wild Rs +332, random_hold Rs +204, snake_viper_tick Rs +182, oracle Rs +154, snake_anaconda Rs +150, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -28, gold Rs -169, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.