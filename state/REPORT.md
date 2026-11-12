# Paper trading report

Updated 2026-11-12 14:58 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,655 | +10.33% | 0 | - | 236 |
| benchmark | 220,303 | +10.15% | 0 | - | 237 |
| snake_abs_exit_conv | 218,935 | +9.47% | 2 | 50% | 345 |
| snake_abs_exit | 217,793 | +8.90% | 2 | 50% | 345 |
| snake_abs | 215,947 | +7.97% | 1 | 100% | 255 |
| snake_abs_conv | 215,776 | +7.89% | 1 | 100% | 255 |
| intraweek | 214,541 | +7.27% | 30 | 53% | 3,302 |
| oracle | 212,830 | +6.42% | 0 | - | 233 |
| intramonth | 211,474 | +5.74% | 0 | - | 235 |
| random_hold | 207,938 | +3.97% | 10 | 70% | 733 |
| snake_anaconda | 206,314 | +3.16% | 3 | 33% | 374 |
| snake_viper_wild | 205,508 | +2.75% | 13 | 54% | 2,247 |
| benchmark_smallcap | 203,004 | +1.50% | 0 | - | 237 |
| snake_viper_tick | 201,994 | +1.00% | 12 | 50% | 2,054 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 185,146 | -7.43% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,931 (-4.03%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs | +2,323 | +1.09% |
| snake_abs_conv | +2,318 | +1.09% |
| benchmark_smallcap | +2,197 | +1.09% |
| snake_anaconda | +2,191 | +1.07% |
| snake_abs_exit_conv | +1,783 | +0.82% |
| snake_abs_exit | +1,631 | +0.76% |
| intraweek | +1,408 | +0.66% |
| benchmark | +1,040 | +0.47% |
| unified | +841 | +0.38% |
| oracle | +828 | +0.39% |
| random_hold | +827 | +0.40% |
| intramonth | +478 | +0.23% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -1,215 | -0.60% |
| snake_viper_wild | -1,234 | -0.60% |
| gold | -4,439 | -2.34% |

Average per day so far: snake_abs_exit_conv Rs +653, unified Rs +645, benchmark Rs +634, snake_abs_exit Rs +614, snake_abs_conv Rs +544, snake_abs Rs +532, intraweek Rs +454, oracle Rs +401, intramonth Rs +359, random_hold Rs +248, snake_anaconda Rs +234, snake_viper_wild Rs +230, benchmark_smallcap Rs +107, snake_viper_tick Rs +95, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -464

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.