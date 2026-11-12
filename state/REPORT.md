# Paper trading report

Updated 2026-11-12 12:24 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,683 | +10.84% | 0 | - | 236 |
| benchmark | 220,112 | +10.06% | 0 | - | 237 |
| snake_abs_exit_conv | 219,519 | +9.76% | 2 | 50% | 345 |
| snake_abs_exit | 218,622 | +9.31% | 2 | 50% | 345 |
| snake_abs | 216,621 | +8.31% | 1 | 100% | 255 |
| snake_abs_conv | 216,456 | +8.23% | 1 | 100% | 255 |
| intraweek | 214,827 | +7.41% | 30 | 53% | 3,302 |
| oracle | 213,507 | +6.75% | 0 | - | 233 |
| intramonth | 211,934 | +5.97% | 0 | - | 235 |
| random_hold | 208,008 | +4.00% | 10 | 70% | 733 |
| snake_viper_wild | 207,690 | +3.85% | 10 | 50% | 1,825 |
| snake_anaconda | 207,220 | +3.61% | 3 | 33% | 374 |
| snake_viper_tick | 204,136 | +2.07% | 9 | 44% | 1,639 |
| benchmark_smallcap | 203,239 | +1.62% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 185,985 | -7.01% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,462 (-3.77%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +3,097 | +1.52% |
| snake_abs_conv | +2,998 | +1.41% |
| snake_abs | +2,997 | +1.40% |
| snake_abs_exit | +2,460 | +1.14% |
| benchmark_smallcap | +2,433 | +1.21% |
| snake_abs_exit_conv | +2,368 | +1.09% |
| unified | +1,869 | +0.85% |
| intraweek | +1,694 | +0.80% |
| oracle | +1,504 | +0.71% |
| snake_viper_wild | +948 | +0.46% |
| intramonth | +938 | +0.45% |
| snake_viper_tick | +927 | +0.46% |
| random_hold | +897 | +0.43% |
| benchmark | +849 | +0.39% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,600 | -1.90% |

Average per day so far: unified Rs +678, snake_abs_exit_conv Rs +673, snake_abs_exit Rs +642, benchmark Rs +628, snake_abs_conv Rs +567, snake_abs Rs +554, intraweek Rs +463, oracle Rs +422, intramonth Rs +373, snake_viper_wild Rs +320, snake_anaconda Rs +267, random_hold Rs +250, snake_viper_tick Rs +197, benchmark_smallcap Rs +116, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -438

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.