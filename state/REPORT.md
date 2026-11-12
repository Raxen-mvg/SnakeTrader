# Paper trading report

Updated 2026-11-12 13:55 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,947 | +10.47% | 0 | - | 236 |
| benchmark | 220,440 | +10.22% | 0 | - | 237 |
| snake_abs_exit_conv | 218,276 | +9.14% | 2 | 50% | 345 |
| snake_abs_exit | 217,122 | +8.56% | 2 | 50% | 345 |
| snake_abs | 215,256 | +7.63% | 1 | 100% | 255 |
| snake_abs_conv | 215,083 | +7.54% | 1 | 100% | 255 |
| intraweek | 214,592 | +7.30% | 30 | 53% | 3,302 |
| oracle | 212,878 | +6.44% | 0 | - | 233 |
| intramonth | 211,509 | +5.75% | 0 | - | 235 |
| random_hold | 207,999 | +4.00% | 10 | 70% | 733 |
| snake_viper_wild | 206,642 | +3.32% | 10 | 50% | 1,825 |
| snake_anaconda | 205,996 | +3.00% | 3 | 33% | 374 |
| snake_viper_tick | 203,108 | +1.55% | 9 | 44% | 1,639 |
| benchmark_smallcap | 202,791 | +1.40% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 185,705 | -7.15% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,901 (-4.05%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,984 | +0.99% |
| snake_anaconda | +1,873 | +0.92% |
| snake_abs | +1,631 | +0.76% |
| snake_abs_conv | +1,625 | +0.76% |
| intraweek | +1,459 | +0.68% |
| benchmark | +1,178 | +0.54% |
| unified | +1,133 | +0.52% |
| snake_abs_exit_conv | +1,124 | +0.52% |
| snake_abs_exit | +960 | +0.44% |
| random_hold | +889 | +0.43% |
| oracle | +875 | +0.41% |
| intramonth | +513 | +0.24% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_wild | -100 | -0.05% |
| snake_viper_tick | -101 | -0.05% |
| gold | -3,880 | -2.05% |

Average per day so far: unified Rs +655, benchmark Rs +639, snake_abs_exit_conv Rs +630, snake_abs_exit Rs +590, snake_abs_conv Rs +520, snake_abs Rs +509, intraweek Rs +456, oracle Rs +402, intramonth Rs +360, snake_viper_wild Rs +277, random_hold Rs +250, snake_anaconda Rs +222, snake_viper_tick Rs +148, benchmark_smallcap Rs +100, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -447

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.