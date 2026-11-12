# Paper trading report

Updated 2026-11-12 13:31 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,284 | +10.64% | 0 | - | 236 |
| benchmark | 220,265 | +10.13% | 0 | - | 237 |
| snake_abs_exit_conv | 218,694 | +9.35% | 2 | 50% | 345 |
| snake_abs_exit | 217,632 | +8.82% | 2 | 50% | 345 |
| snake_abs | 215,720 | +7.86% | 1 | 100% | 255 |
| snake_abs_conv | 215,553 | +7.78% | 1 | 100% | 255 |
| intraweek | 214,545 | +7.27% | 30 | 53% | 3,302 |
| oracle | 213,232 | +6.62% | 0 | - | 233 |
| intramonth | 211,818 | +5.91% | 0 | - | 235 |
| random_hold | 208,091 | +4.04% | 10 | 70% | 733 |
| snake_viper_wild | 207,175 | +3.59% | 10 | 50% | 1,825 |
| snake_anaconda | 206,510 | +3.25% | 3 | 33% | 374 |
| snake_viper_tick | 203,631 | +1.81% | 9 | 44% | 1,639 |
| benchmark_smallcap | 203,127 | +1.56% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 186,248 | -6.88% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,137 (-3.93%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +2,388 | +1.17% |
| benchmark_smallcap | +2,320 | +1.16% |
| snake_abs_conv | +2,096 | +0.98% |
| snake_abs | +2,095 | +0.98% |
| snake_abs_exit_conv | +1,543 | +0.71% |
| unified | +1,471 | +0.67% |
| snake_abs_exit | +1,470 | +0.68% |
| intraweek | +1,411 | +0.66% |
| oracle | +1,229 | +0.58% |
| benchmark | +1,002 | +0.46% |
| random_hold | +980 | +0.47% |
| intramonth | +822 | +0.39% |
| snake_viper_wild | +434 | +0.21% |
| snake_viper_tick | +422 | +0.21% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,337 | -1.76% |

Average per day so far: unified Rs +665, snake_abs_exit_conv Rs +645, benchmark Rs +633, snake_abs_exit Rs +608, snake_abs_conv Rs +536, snake_abs Rs +524, intraweek Rs +455, oracle Rs +413, intramonth Rs +369, snake_viper_wild Rs +299, random_hold Rs +253, snake_anaconda Rs +241, snake_viper_tick Rs +173, benchmark_smallcap Rs +112, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -430

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.