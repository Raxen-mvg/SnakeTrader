# Paper trading report

Updated 2026-11-12 13:27 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,440 | +10.72% | 0 | - | 236 |
| benchmark | 220,142 | +10.07% | 0 | - | 237 |
| snake_abs_exit_conv | 218,740 | +9.37% | 2 | 50% | 345 |
| snake_abs_exit | 217,662 | +8.83% | 2 | 50% | 345 |
| snake_abs | 215,963 | +7.98% | 1 | 100% | 255 |
| snake_abs_conv | 215,794 | +7.90% | 1 | 100% | 255 |
| intraweek | 214,478 | +7.24% | 30 | 53% | 3,302 |
| oracle | 213,263 | +6.63% | 0 | - | 233 |
| intramonth | 212,101 | +6.05% | 0 | - | 235 |
| random_hold | 208,048 | +4.02% | 10 | 70% | 733 |
| snake_viper_wild | 207,040 | +3.52% | 10 | 50% | 1,825 |
| snake_anaconda | 206,597 | +3.30% | 3 | 33% | 374 |
| snake_viper_tick | 203,498 | +1.75% | 9 | 44% | 1,639 |
| benchmark_smallcap | 203,071 | +1.54% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 186,297 | -6.85% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,211 (-3.89%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +2,474 | +1.21% |
| snake_abs | +2,338 | +1.09% |
| snake_abs_conv | +2,336 | +1.09% |
| benchmark_smallcap | +2,264 | +1.13% |
| unified | +1,626 | +0.74% |
| snake_abs_exit_conv | +1,589 | +0.73% |
| snake_abs_exit | +1,500 | +0.69% |
| intraweek | +1,345 | +0.63% |
| oracle | +1,260 | +0.59% |
| intramonth | +1,104 | +0.52% |
| random_hold | +937 | +0.45% |
| benchmark | +880 | +0.40% |
| snake_viper_wild | +298 | +0.14% |
| snake_viper_tick | +289 | +0.14% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,288 | -1.73% |

Average per day so far: unified Rs +670, snake_abs_exit_conv Rs +646, benchmark Rs +629, snake_abs_exit Rs +609, snake_abs_conv Rs +545, snake_abs Rs +532, intraweek Rs +452, oracle Rs +414, intramonth Rs +378, snake_viper_wild Rs +293, random_hold Rs +251, snake_anaconda Rs +244, snake_viper_tick Rs +167, benchmark_smallcap Rs +110, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -428

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.