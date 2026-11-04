# Paper trading report

Updated 2026-11-04 10:18 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 212,562 | +6.28% | 0 | - | 236 |
| snake_abs_exit_conv | 209,076 | +4.54% | 1 | 100% | 255 |
| snake_abs_exit | 208,925 | +4.46% | 1 | 100% | 260 |
| intraweek | 208,880 | +4.44% | 25 | 48% | 2,757 |
| benchmark | 208,323 | +4.16% | 0 | - | 237 |
| snake_viper_wild | 206,751 | +3.38% | 3 | 33% | 702 |
| snake_abs | 205,977 | +2.99% | 1 | 100% | 255 |
| snake_abs_conv | 205,827 | +2.91% | 1 | 100% | 255 |
| intramonth | 205,151 | +2.58% | 0 | - | 235 |
| snake_viper_tick | 203,148 | +1.57% | 2 | 0% | 532 |
| random_hold | 202,474 | +1.24% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,351 | +0.18% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,806 | -1.10% | 3 | 33% | 361 |
| benchmark_smallcap | 194,596 | -2.70% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 187,465 | -6.27% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,689 (-5.66%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,911 | +2.41% |
| snake_abs_exit_conv | +4,737 | +2.32% |
| snake_abs_conv | +4,686 | +2.33% |
| snake_abs | +4,667 | +2.32% |
| snake_anaconda | +3,981 | +2.05% |
| intraweek | +3,794 | +1.85% |
| gold | +2,187 | +1.18% |
| random_hold | +2,006 | +1.00% |
| benchmark_smallcap | +1,659 | +0.86% |
| benchmark | +1,622 | +0.79% |
| intramonth | +1,180 | +0.58% |
| unified | +561 | +0.27% |
| oracle | +362 | +0.18% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -4,019 | -1.94% |
| snake_viper_wild | -4,142 | -1.96% |

Average per day so far: unified Rs +465, snake_abs_exit_conv Rs +378, snake_abs_exit Rs +372, snake_viper_wild Rs +355, intraweek Rs +329, benchmark Rs +308, snake_abs_conv Rs +243, snake_abs Rs +239, snake_viper_tick Rs +197, intramonth Rs +191, random_hold Rs +92, nifty_calls Rs +68, oracle Rs +13, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -100, benchmark_smallcap Rs -235, snake_nonews Rs -444, gold Rs -464, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.