# Paper trading report

Updated 2026-11-12 13:59 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,838 | +10.42% | 0 | - | 236 |
| benchmark | 220,211 | +10.11% | 0 | - | 237 |
| snake_abs_exit_conv | 218,668 | +9.33% | 2 | 50% | 345 |
| snake_abs_exit | 217,537 | +8.77% | 2 | 50% | 345 |
| snake_abs | 215,766 | +7.88% | 1 | 100% | 255 |
| snake_abs_conv | 215,593 | +7.80% | 1 | 100% | 255 |
| intraweek | 214,389 | +7.19% | 30 | 53% | 3,302 |
| oracle | 212,793 | +6.40% | 0 | - | 233 |
| intramonth | 211,430 | +5.71% | 0 | - | 235 |
| random_hold | 207,954 | +3.98% | 10 | 70% | 733 |
| snake_viper_wild | 207,013 | +3.51% | 10 | 50% | 1,825 |
| snake_anaconda | 206,382 | +3.19% | 3 | 33% | 374 |
| snake_viper_tick | 203,472 | +1.74% | 9 | 44% | 1,639 |
| benchmark_smallcap | 202,791 | +1.40% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 185,541 | -7.23% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,905 (-4.05%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +2,259 | +1.11% |
| snake_abs | +2,141 | +1.00% |
| snake_abs_conv | +2,135 | +1.00% |
| benchmark_smallcap | +1,984 | +0.99% |
| snake_abs_exit_conv | +1,517 | +0.70% |
| snake_abs_exit | +1,374 | +0.64% |
| intraweek | +1,255 | +0.59% |
| unified | +1,024 | +0.47% |
| benchmark | +949 | +0.43% |
| random_hold | +844 | +0.41% |
| oracle | +791 | +0.37% |
| intramonth | +434 | +0.21% |
| snake_viper_wild | +272 | +0.13% |
| snake_viper_tick | +263 | +0.13% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -4,044 | -2.13% |

Average per day so far: unified Rs +651, snake_abs_exit_conv Rs +644, benchmark Rs +632, snake_abs_exit Rs +605, snake_abs_conv Rs +538, snake_abs Rs +526, intraweek Rs +450, oracle Rs +400, intramonth Rs +357, snake_viper_wild Rs +292, random_hold Rs +249, snake_anaconda Rs +236, snake_viper_tick Rs +165, benchmark_smallcap Rs +100, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -452

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.