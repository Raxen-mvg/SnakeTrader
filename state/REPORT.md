# Paper trading report

Updated 2026-11-12 14:13 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,897 | +10.45% | 0 | - | 236 |
| benchmark | 220,387 | +10.19% | 0 | - | 237 |
| snake_abs_exit_conv | 218,372 | +9.19% | 2 | 50% | 345 |
| snake_abs_exit | 217,265 | +8.63% | 2 | 50% | 345 |
| snake_abs | 215,483 | +7.74% | 1 | 100% | 255 |
| snake_abs_conv | 215,304 | +7.65% | 1 | 100% | 255 |
| intraweek | 214,430 | +7.21% | 30 | 53% | 3,302 |
| oracle | 212,881 | +6.44% | 0 | - | 233 |
| intramonth | 211,485 | +5.74% | 0 | - | 235 |
| random_hold | 207,992 | +4.00% | 10 | 70% | 733 |
| snake_viper_wild | 206,632 | +3.32% | 10 | 50% | 1,825 |
| snake_anaconda | 206,097 | +3.05% | 3 | 33% | 374 |
| snake_viper_tick | 203,098 | +1.55% | 9 | 44% | 1,639 |
| benchmark_smallcap | 202,903 | +1.45% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 185,525 | -7.24% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,890 (-4.05%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,096 | +1.04% |
| snake_anaconda | +1,974 | +0.97% |
| snake_abs | +1,859 | +0.87% |
| snake_abs_conv | +1,847 | +0.86% |
| intraweek | +1,296 | +0.61% |
| snake_abs_exit_conv | +1,221 | +0.56% |
| benchmark | +1,125 | +0.51% |
| snake_abs_exit | +1,103 | +0.51% |
| unified | +1,083 | +0.49% |
| random_hold | +882 | +0.43% |
| oracle | +878 | +0.41% |
| intramonth | +489 | +0.23% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_wild | -110 | -0.05% |
| snake_viper_tick | -111 | -0.05% |
| gold | -4,061 | -2.14% |

Average per day so far: unified Rs +653, benchmark Rs +637, snake_abs_exit_conv Rs +634, snake_abs_exit Rs +595, snake_abs_conv Rs +528, snake_abs Rs +516, intraweek Rs +451, oracle Rs +403, intramonth Rs +359, snake_viper_wild Rs +276, random_hold Rs +250, snake_anaconda Rs +226, snake_viper_tick Rs +148, benchmark_smallcap Rs +104, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -452

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.