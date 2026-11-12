# Paper trading report

Updated 2026-11-12 15:13 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,582 | +10.29% | 0 | - | 236 |
| benchmark | 220,517 | +10.26% | 0 | - | 237 |
| snake_abs_exit_conv | 219,124 | +9.56% | 2 | 50% | 345 |
| snake_abs_exit | 217,895 | +8.95% | 2 | 50% | 345 |
| snake_abs | 216,105 | +8.05% | 1 | 100% | 255 |
| snake_abs_conv | 215,931 | +7.97% | 1 | 100% | 255 |
| intraweek | 214,632 | +7.32% | 30 | 53% | 3,302 |
| oracle | 212,916 | +6.46% | 0 | - | 233 |
| intramonth | 211,581 | +5.79% | 0 | - | 235 |
| random_hold | 207,886 | +3.94% | 10 | 70% | 733 |
| snake_anaconda | 206,574 | +3.29% | 3 | 33% | 374 |
| snake_viper_wild | 205,542 | +2.77% | 13 | 54% | 2,247 |
| benchmark_smallcap | 203,105 | +1.55% | 0 | - | 237 |
| snake_viper_tick | 202,028 | +1.01% | 12 | 50% | 2,054 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 185,344 | -7.33% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,990 (-4.01%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs | +2,480 | +1.16% |
| snake_abs_conv | +2,474 | +1.16% |
| snake_anaconda | +2,451 | +1.20% |
| benchmark_smallcap | +2,298 | +1.14% |
| snake_abs_exit_conv | +1,973 | +0.91% |
| snake_abs_exit | +1,733 | +0.80% |
| intraweek | +1,499 | +0.70% |
| benchmark | +1,255 | +0.57% |
| oracle | +913 | +0.43% |
| random_hold | +776 | +0.37% |
| unified | +768 | +0.35% |
| intramonth | +585 | +0.28% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -1,181 | -0.58% |
| snake_viper_wild | -1,200 | -0.58% |
| gold | -4,242 | -2.24% |

Average per day so far: snake_abs_exit_conv Rs +659, unified Rs +643, benchmark Rs +641, snake_abs_exit Rs +617, snake_abs_conv Rs +549, snake_abs Rs +537, intraweek Rs +457, oracle Rs +404, intramonth Rs +362, random_hold Rs +246, snake_anaconda Rs +243, snake_viper_wild Rs +231, benchmark_smallcap Rs +111, snake_viper_tick Rs +97, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -458

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.