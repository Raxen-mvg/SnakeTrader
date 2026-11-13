# Paper trading report

Updated 2026-11-13 14:52 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,258 | +10.13% | 0 | - | 236 |
| benchmark | 219,285 | +9.64% | 0 | - | 237 |
| snake_abs_exit | 217,393 | +8.70% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,983 | +8.49% | 2 | 50% | 345 |
| intraweek | 216,143 | +8.07% | 30 | 53% | 3,302 |
| oracle | 213,332 | +6.67% | 0 | - | 233 |
| snake_abs | 213,150 | +6.58% | 1 | 100% | 255 |
| snake_abs_conv | 212,983 | +6.49% | 1 | 100% | 255 |
| intramonth | 210,824 | +5.41% | 0 | - | 235 |
| random_hold | 207,093 | +3.55% | 10 | 70% | 733 |
| snake_anaconda | 205,464 | +2.73% | 3 | 33% | 374 |
| snake_viper_wild | 205,306 | +2.65% | 14 | 50% | 2,496 |
| benchmark_smallcap | 202,970 | +1.49% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,794 | +0.90% | 13 | 46% | 2,299 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,029 | -7.99% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,942 (-4.03%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,485 | +0.69% |
| oracle | +217 | +0.10% |
| snake_viper_wild | +13 | +0.01% |
| snake_viper_tick | +13 | +0.01% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_abs_exit | -49 | -0.02% |
| benchmark_smallcap | -235 | -0.12% |
| unified | -439 | -0.20% |
| snake_anaconda | -463 | -0.23% |
| intramonth | -769 | -0.36% |
| random_hold | -961 | -0.46% |
| benchmark | -1,262 | -0.57% |
| gold | -1,282 | -0.69% |
| snake_abs_exit_conv | -1,691 | -0.77% |
| snake_abs_conv | -2,552 | -1.18% |
| snake_abs | -2,561 | -1.19% |

Average per day so far: unified Rs +614, benchmark Rs +584, snake_abs_exit Rs +580, snake_abs_exit_conv Rs +566, intraweek Rs +489, snake_abs_conv Rs +433, snake_abs Rs +424, oracle Rs +404, intramonth Rs +328, random_hold Rs +215, snake_viper_wild Rs +212, snake_anaconda Rs +195, benchmark_smallcap Rs +102, snake_viper_tick Rs +82, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -484

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.