# Paper trading report

Updated 2026-11-12 15:25 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,825 | +10.41% | 0 | - | 236 |
| benchmark | 220,762 | +10.38% | 0 | - | 237 |
| snake_abs_exit_conv | 219,054 | +9.53% | 2 | 50% | 345 |
| snake_abs_exit | 217,810 | +8.90% | 2 | 50% | 345 |
| snake_abs | 216,120 | +8.06% | 1 | 100% | 255 |
| snake_abs_conv | 215,939 | +7.97% | 1 | 100% | 255 |
| intraweek | 214,714 | +7.36% | 30 | 53% | 3,302 |
| oracle | 213,213 | +6.61% | 0 | - | 233 |
| intramonth | 211,721 | +5.86% | 0 | - | 235 |
| random_hold | 208,155 | +4.08% | 10 | 70% | 733 |
| snake_anaconda | 206,674 | +3.34% | 3 | 33% | 374 |
| snake_viper_wild | 205,343 | +2.67% | 13 | 54% | 2,247 |
| benchmark_smallcap | 203,452 | +1.73% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,831 | +0.92% | 12 | 50% | 2,054 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 185,393 | -7.30% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,118 (-3.94%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,646 | +1.32% |
| snake_anaconda | +2,551 | +1.25% |
| snake_abs | +2,495 | +1.17% |
| snake_abs_conv | +2,481 | +1.16% |
| snake_abs_exit_conv | +1,903 | +0.88% |
| snake_abs_exit | +1,648 | +0.76% |
| intraweek | +1,580 | +0.74% |
| benchmark | +1,499 | +0.68% |
| oracle | +1,210 | +0.57% |
| random_hold | +1,044 | +0.50% |
| unified | +1,011 | +0.46% |
| intramonth | +724 | +0.34% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -1,378 | -0.68% |
| snake_viper_wild | -1,399 | -0.68% |
| gold | -4,192 | -2.21% |

Average per day so far: snake_abs_exit_conv Rs +657, unified Rs +651, benchmark Rs +649, snake_abs_exit Rs +614, snake_abs_conv Rs +550, snake_abs Rs +537, intraweek Rs +460, oracle Rs +413, intramonth Rs +366, random_hold Rs +255, snake_anaconda Rs +247, snake_viper_wild Rs +223, benchmark_smallcap Rs +123, snake_viper_tick Rs +87, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -456

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.