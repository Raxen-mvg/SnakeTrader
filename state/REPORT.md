# Paper trading report

Updated 2026-11-12 14:19 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,029 | +10.52% | 0 | - | 236 |
| benchmark | 220,410 | +10.21% | 0 | - | 237 |
| snake_abs_exit_conv | 218,490 | +9.24% | 2 | 50% | 345 |
| snake_abs_exit | 217,375 | +8.69% | 2 | 50% | 345 |
| snake_abs | 215,589 | +7.79% | 1 | 100% | 255 |
| snake_abs_conv | 215,414 | +7.71% | 1 | 100% | 255 |
| intraweek | 214,489 | +7.25% | 30 | 53% | 3,302 |
| oracle | 212,931 | +6.47% | 0 | - | 233 |
| intramonth | 211,730 | +5.87% | 0 | - | 235 |
| random_hold | 207,958 | +3.98% | 10 | 70% | 733 |
| snake_viper_wild | 206,708 | +3.35% | 10 | 50% | 1,825 |
| snake_anaconda | 206,203 | +3.10% | 3 | 33% | 374 |
| snake_viper_tick | 203,173 | +1.59% | 9 | 44% | 1,639 |
| benchmark_smallcap | 202,914 | +1.46% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 185,212 | -7.39% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,981 (-4.01%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,107 | +1.05% |
| snake_anaconda | +2,080 | +1.02% |
| snake_abs | +1,964 | +0.92% |
| snake_abs_conv | +1,956 | +0.92% |
| intraweek | +1,356 | +0.64% |
| snake_abs_exit_conv | +1,338 | +0.62% |
| unified | +1,215 | +0.55% |
| snake_abs_exit | +1,212 | +0.56% |
| benchmark | +1,147 | +0.52% |
| oracle | +928 | +0.44% |
| random_hold | +847 | +0.41% |
| intramonth | +734 | +0.35% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_wild | -34 | -0.02% |
| snake_viper_tick | -36 | -0.02% |
| gold | -4,373 | -2.31% |

Average per day so far: unified Rs +657, benchmark Rs +638, snake_abs_exit_conv Rs +638, snake_abs_exit Rs +599, snake_abs_conv Rs +532, snake_abs Rs +520, intraweek Rs +453, oracle Rs +404, intramonth Rs +367, snake_viper_wild Rs +280, random_hold Rs +249, snake_anaconda Rs +230, snake_viper_tick Rs +151, benchmark_smallcap Rs +104, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -462

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.