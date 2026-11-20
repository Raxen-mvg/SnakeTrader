# Paper trading report

Updated 2026-11-20 13:20 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,242 | +13.12% | 0 | - | 236 |
| benchmark | 224,342 | +12.17% | 0 | - | 237 |
| intramonth | 215,251 | +7.62% | 0 | - | 235 |
| intraweek | 215,116 | +7.56% | 35 | 54% | 3,851 |
| oracle | 212,501 | +6.25% | 0 | - | 233 |
| random_hold | 209,468 | +4.73% | 11 | 73% | 979 |
| snake_abs_exit | 209,063 | +4.53% | 2 | 50% | 345 |
| snake_abs_exit_conv | 207,112 | +3.56% | 2 | 50% | 345 |
| snake_abs | 206,230 | +3.12% | 1 | 100% | 255 |
| snake_abs_conv | 206,096 | +3.05% | 1 | 100% | 255 |
| snake_viper_wild | 203,781 | +1.89% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,997 | +0.50% | 0 | - | 237 |
| snake_anaconda | 200,362 | +0.18% | 3 | 33% | 374 |
| snake_viper_tick | 200,306 | +0.15% | 15 | 47% | 2,625 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,816 | -16.59% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,951 (-4.02%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,227 | +1.05% |
| benchmark | +1,966 | +0.88% |
| unified | +1,626 | +0.72% |
| intramonth | +1,243 | +0.58% |
| random_hold | +1,015 | +0.49% |
| oracle | +412 | +0.19% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -471 | -0.23% |
| snake_abs | -2,750 | -1.32% |
| snake_abs_conv | -2,764 | -1.32% |
| snake_anaconda | -3,101 | -1.52% |
| snake_viper_tick | -3,671 | -1.80% |
| snake_viper_wild | -3,742 | -1.80% |
| snake_abs_exit_conv | -3,953 | -1.87% |
| snake_abs_exit | -4,288 | -2.01% |
| gold | -7,957 | -4.55% |

Average per day so far: unified Rs +691, benchmark Rs +641, intramonth Rs +401, intraweek Rs +398, oracle Rs +329, snake_abs_exit Rs +259, random_hold Rs +249, snake_abs_exit_conv Rs +203, snake_abs_conv Rs +174, snake_abs Rs +173, snake_viper_wild Rs +126, nifty_calls Rs +48, benchmark_smallcap Rs +29, snake_viper_tick Rs +11, snake_anaconda Rs +11, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -873

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.