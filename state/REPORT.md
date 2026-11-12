# Paper trading report

Updated 2026-11-12 13:41 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,118 | +10.56% | 0 | - | 236 |
| benchmark | 220,433 | +10.22% | 0 | - | 237 |
| snake_abs_exit_conv | 218,390 | +9.20% | 2 | 50% | 345 |
| snake_abs_exit | 217,250 | +8.62% | 2 | 50% | 345 |
| snake_abs | 215,425 | +7.71% | 1 | 100% | 255 |
| snake_abs_conv | 215,250 | +7.62% | 1 | 100% | 255 |
| intraweek | 214,528 | +7.26% | 30 | 53% | 3,302 |
| oracle | 213,126 | +6.56% | 0 | - | 233 |
| intramonth | 211,696 | +5.85% | 0 | - | 235 |
| random_hold | 207,955 | +3.98% | 10 | 70% | 733 |
| snake_viper_wild | 207,262 | +3.63% | 10 | 50% | 1,825 |
| snake_anaconda | 206,207 | +3.10% | 3 | 33% | 374 |
| snake_viper_tick | 203,715 | +1.86% | 9 | 44% | 1,639 |
| benchmark_smallcap | 202,802 | +1.40% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 186,051 | -6.97% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,012 (-3.99%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +2,084 | +1.02% |
| benchmark_smallcap | +1,995 | +0.99% |
| snake_abs | +1,801 | +0.84% |
| snake_abs_conv | +1,792 | +0.84% |
| intraweek | +1,395 | +0.66% |
| unified | +1,304 | +0.59% |
| snake_abs_exit_conv | +1,239 | +0.57% |
| benchmark | +1,170 | +0.53% |
| oracle | +1,123 | +0.53% |
| snake_abs_exit | +1,088 | +0.50% |
| random_hold | +845 | +0.41% |
| intramonth | +700 | +0.33% |
| snake_viper_wild | +520 | +0.25% |
| snake_viper_tick | +506 | +0.25% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,535 | -1.86% |

Average per day so far: unified Rs +660, benchmark Rs +639, snake_abs_exit_conv Rs +634, snake_abs_exit Rs +595, snake_abs_conv Rs +526, snake_abs Rs +514, intraweek Rs +454, oracle Rs +410, intramonth Rs +366, snake_viper_wild Rs +303, random_hold Rs +249, snake_anaconda Rs +230, snake_viper_tick Rs +177, benchmark_smallcap Rs +100, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -436

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.