# Paper trading report

Updated 2026-11-13 15:13 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 219,385 | +9.69% | 0 | - | 237 |
| unified | 219,316 | +9.66% | 0 | - | 236 |
| snake_abs_exit | 216,969 | +8.48% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,470 | +8.23% | 2 | 50% | 345 |
| intraweek | 216,224 | +8.11% | 30 | 53% | 3,302 |
| oracle | 212,970 | +6.49% | 0 | - | 233 |
| snake_abs | 212,549 | +6.28% | 1 | 100% | 255 |
| snake_abs_conv | 212,376 | +6.19% | 1 | 100% | 255 |
| intramonth | 210,198 | +5.10% | 0 | - | 235 |
| random_hold | 207,161 | +3.58% | 10 | 70% | 733 |
| snake_viper_wild | 204,878 | +2.44% | 14 | 50% | 2,496 |
| snake_anaconda | 204,853 | +2.43% | 3 | 33% | 374 |
| benchmark_smallcap | 202,914 | +1.46% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,373 | +0.69% | 13 | 46% | 2,299 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,078 | -7.96% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,624 (-4.19%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,566 | +0.73% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -145 | -0.07% |
| benchmark_smallcap | -291 | -0.14% |
| snake_viper_tick | -408 | -0.20% |
| snake_viper_wild | -415 | -0.20% |
| snake_abs_exit | -473 | -0.22% |
| random_hold | -892 | -0.43% |
| snake_anaconda | -1,074 | -0.52% |
| benchmark | -1,163 | -0.53% |
| gold | -1,233 | -0.67% |
| unified | -1,381 | -0.63% |
| intramonth | -1,395 | -0.66% |
| snake_abs_exit_conv | -2,204 | -1.01% |
| snake_abs_conv | -3,159 | -1.47% |
| snake_abs | -3,162 | -1.47% |

Average per day so far: benchmark Rs +587, unified Rs +585, snake_abs_exit Rs +566, snake_abs_exit_conv Rs +549, intraweek Rs +492, snake_abs_conv Rs +413, snake_abs Rs +405, oracle Rs +393, intramonth Rs +309, random_hold Rs +217, snake_viper_wild Rs +195, snake_anaconda Rs +173, benchmark_smallcap Rs +100, snake_viper_tick Rs +62, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -482

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.