# Paper trading report

Updated 2026-11-12 12:59 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,519 | +10.76% | 0 | - | 236 |
| benchmark | 220,257 | +10.13% | 0 | - | 237 |
| snake_abs_exit_conv | 219,030 | +9.52% | 2 | 50% | 345 |
| snake_abs_exit | 217,929 | +8.96% | 2 | 50% | 345 |
| snake_abs | 215,918 | +7.96% | 1 | 100% | 255 |
| snake_abs_conv | 215,747 | +7.87% | 1 | 100% | 255 |
| intraweek | 214,705 | +7.35% | 30 | 53% | 3,302 |
| oracle | 213,380 | +6.69% | 0 | - | 233 |
| intramonth | 211,916 | +5.96% | 0 | - | 235 |
| random_hold | 208,209 | +4.10% | 10 | 70% | 733 |
| snake_viper_wild | 207,468 | +3.73% | 10 | 50% | 1,825 |
| snake_anaconda | 206,627 | +3.31% | 3 | 33% | 374 |
| snake_viper_tick | 203,918 | +1.96% | 9 | 44% | 1,639 |
| benchmark_smallcap | 203,194 | +1.60% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 186,084 | -6.96% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,295 (-3.85%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +2,504 | +1.23% |
| benchmark_smallcap | +2,388 | +1.19% |
| snake_abs | +2,293 | +1.07% |
| snake_abs_conv | +2,290 | +1.07% |
| snake_abs_exit_conv | +1,878 | +0.86% |
| snake_abs_exit | +1,767 | +0.82% |
| unified | +1,705 | +0.78% |
| intraweek | +1,571 | +0.74% |
| oracle | +1,377 | +0.65% |
| random_hold | +1,098 | +0.53% |
| benchmark | +994 | +0.45% |
| intramonth | +920 | +0.44% |
| snake_viper_wild | +726 | +0.35% |
| snake_viper_tick | +709 | +0.35% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,502 | -1.85% |

Average per day so far: unified Rs +672, snake_abs_exit_conv Rs +656, benchmark Rs +633, snake_abs_exit Rs +618, snake_abs_conv Rs +543, snake_abs Rs +531, intraweek Rs +460, oracle Rs +418, intramonth Rs +372, snake_viper_wild Rs +311, random_hold Rs +257, snake_anaconda Rs +245, snake_viper_tick Rs +187, benchmark_smallcap Rs +114, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -435

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.