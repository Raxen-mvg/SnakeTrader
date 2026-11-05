# Paper trading report

Updated 2026-11-05 13:16 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 217,688 | +8.84% | 0 | - | 236 |
| snake_abs_exit_conv | 214,201 | +7.10% | 1 | 100% | 255 |
| snake_abs_exit | 213,903 | +6.95% | 1 | 100% | 260 |
| benchmark | 213,295 | +6.65% | 0 | - | 237 |
| snake_abs | 211,084 | +5.54% | 1 | 100% | 255 |
| snake_abs_conv | 210,947 | +5.47% | 1 | 100% | 255 |
| intraweek | 210,764 | +5.38% | 25 | 48% | 2,757 |
| intramonth | 209,621 | +4.81% | 0 | - | 235 |
| snake_viper_wild | 206,719 | +3.36% | 3 | 33% | 702 |
| random_hold | 206,143 | +3.07% | 8 | 62% | 649 |
| oracle | 204,075 | +2.04% | 0 | - | 233 |
| snake_viper_tick | 203,170 | +1.58% | 2 | 0% | 532 |
| snake_anaconda | 202,368 | +1.18% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,991 | -0.51% | 0 | - | 237 |
| gold | 193,975 | -3.01% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,090 (-4.96%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,536 | +2.17% |
| unified | +3,249 | +1.51% |
| random_hold | +2,834 | +1.39% |
| intramonth | +2,605 | +1.26% |
| gold | +2,581 | +1.35% |
| benchmark_smallcap | +2,320 | +1.18% |
| oracle | +2,283 | +1.13% |
| intraweek | +1,066 | +0.51% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -811 | -0.38% |
| snake_abs_exit_conv | -814 | -0.38% |
| snake_abs | -819 | -0.39% |
| snake_abs_exit | -997 | -0.46% |
| snake_anaconda | -1,452 | -0.71% |
| snake_viper_tick | -2,230 | -1.09% |
| snake_viper_wild | -2,311 | -1.10% |

Average per day so far: unified Rs +632, snake_abs_exit_conv Rs +568, snake_abs_exit Rs +556, benchmark Rs +475, snake_abs_conv Rs +438, snake_abs Rs +426, intraweek Rs +384, intramonth Rs +344, snake_viper_wild Rs +336, random_hold Rs +219, snake_viper_tick Rs +186, oracle Rs +146, snake_anaconda Rs +103, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -42, gold Rs -215, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.