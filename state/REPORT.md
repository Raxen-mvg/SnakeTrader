# Paper trading report

Updated 2026-11-12 14:46 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,843 | +10.42% | 0 | - | 236 |
| benchmark | 220,349 | +10.17% | 0 | - | 237 |
| snake_abs_exit_conv | 218,784 | +9.39% | 2 | 50% | 345 |
| snake_abs_exit | 217,738 | +8.87% | 2 | 50% | 345 |
| snake_abs | 215,728 | +7.86% | 1 | 100% | 255 |
| snake_abs_conv | 215,557 | +7.78% | 1 | 100% | 255 |
| intraweek | 214,314 | +7.16% | 30 | 53% | 3,302 |
| oracle | 212,771 | +6.39% | 0 | - | 233 |
| intramonth | 211,626 | +5.81% | 0 | - | 235 |
| random_hold | 207,958 | +3.98% | 10 | 70% | 733 |
| snake_anaconda | 206,458 | +3.23% | 3 | 33% | 374 |
| snake_viper_wild | 205,930 | +2.96% | 13 | 54% | 2,247 |
| benchmark_smallcap | 202,813 | +1.41% | 0 | - | 237 |
| snake_viper_tick | 202,409 | +1.21% | 12 | 50% | 2,054 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,785 | -7.61% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,909 (-4.05%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +2,335 | +1.14% |
| snake_abs | +2,103 | +0.98% |
| snake_abs_conv | +2,100 | +0.98% |
| benchmark_smallcap | +2,007 | +1.00% |
| snake_abs_exit_conv | +1,633 | +0.75% |
| snake_abs_exit | +1,576 | +0.73% |
| intraweek | +1,181 | +0.55% |
| benchmark | +1,086 | +0.49% |
| unified | +1,029 | +0.47% |
| random_hold | +848 | +0.41% |
| oracle | +768 | +0.36% |
| intramonth | +630 | +0.30% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -800 | -0.39% |
| snake_viper_wild | -812 | -0.39% |
| gold | -4,800 | -2.53% |

Average per day so far: unified Rs +651, snake_abs_exit_conv Rs +648, benchmark Rs +636, snake_abs_exit Rs +612, snake_abs_conv Rs +536, snake_abs Rs +524, intraweek Rs +447, oracle Rs +399, intramonth Rs +363, random_hold Rs +249, snake_viper_wild Rs +247, snake_anaconda Rs +239, snake_viper_tick Rs +115, benchmark_smallcap Rs +100, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -475

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.