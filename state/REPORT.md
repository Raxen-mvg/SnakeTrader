# Paper trading report

Updated 2026-11-12 15:01 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,627 | +10.31% | 0 | - | 236 |
| benchmark | 220,265 | +10.13% | 0 | - | 237 |
| snake_abs_exit_conv | 218,726 | +9.36% | 2 | 50% | 345 |
| snake_abs_exit | 217,535 | +8.77% | 2 | 50% | 345 |
| snake_abs | 215,747 | +7.87% | 1 | 100% | 255 |
| snake_abs_conv | 215,574 | +7.79% | 1 | 100% | 255 |
| intraweek | 214,366 | +7.18% | 30 | 53% | 3,302 |
| oracle | 212,875 | +6.44% | 0 | - | 233 |
| intramonth | 211,375 | +5.69% | 0 | - | 235 |
| random_hold | 207,944 | +3.97% | 10 | 70% | 733 |
| snake_anaconda | 205,616 | +2.81% | 3 | 33% | 374 |
| snake_viper_wild | 205,577 | +2.79% | 13 | 54% | 2,247 |
| benchmark_smallcap | 202,959 | +1.48% | 0 | - | 237 |
| snake_viper_tick | 202,062 | +1.03% | 12 | 50% | 2,054 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 185,212 | -7.39% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,853 (-4.07%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,152 | +1.07% |
| snake_abs | +2,123 | +0.99% |
| snake_abs_conv | +2,116 | +0.99% |
| snake_abs_exit_conv | +1,575 | +0.72% |
| snake_anaconda | +1,493 | +0.73% |
| snake_abs_exit | +1,372 | +0.64% |
| intraweek | +1,233 | +0.58% |
| benchmark | +1,002 | +0.46% |
| oracle | +872 | +0.41% |
| random_hold | +834 | +0.40% |
| unified | +813 | +0.37% |
| intramonth | +378 | +0.18% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -1,147 | -0.56% |
| snake_viper_wild | -1,165 | -0.56% |
| gold | -4,373 | -2.31% |

Average per day so far: snake_abs_exit_conv Rs +646, unified Rs +645, benchmark Rs +633, snake_abs_exit Rs +605, snake_abs_conv Rs +537, snake_abs Rs +525, intraweek Rs +449, oracle Rs +402, intramonth Rs +355, random_hold Rs +248, snake_viper_wild Rs +232, snake_anaconda Rs +208, benchmark_smallcap Rs +106, snake_viper_tick Rs +98, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -462

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.