# Paper trading report

Updated 2026-11-11 12:34 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,571 | +10.29% | 0 | - | 237 |
| unified | 220,444 | +10.22% | 0 | - | 236 |
| snake_abs_exit_conv | 217,440 | +8.72% | 2 | 50% | 345 |
| snake_abs_exit | 216,359 | +8.18% | 2 | 50% | 345 |
| intraweek | 213,917 | +6.96% | 30 | 53% | 3,302 |
| snake_abs | 213,846 | +6.92% | 1 | 100% | 255 |
| snake_abs_conv | 213,689 | +6.84% | 1 | 100% | 255 |
| oracle | 211,891 | +5.95% | 0 | - | 233 |
| intramonth | 211,369 | +5.68% | 0 | - | 235 |
| random_hold | 206,933 | +3.47% | 9 | 67% | 709 |
| snake_viper_wild | 204,816 | +2.41% | 10 | 50% | 1,825 |
| snake_anaconda | 204,228 | +2.11% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,681 | +0.84% | 0 | - | 237 |
| snake_viper_tick | 201,323 | +0.66% | 9 | 44% | 1,639 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 190,062 | -4.97% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,336 (-4.33%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +7,386 | +3.74% |
| snake_viper_tick | +7,247 | +3.73% |
| snake_abs_exit_conv | +5,532 | +2.61% |
| snake_anaconda | +4,762 | +2.39% |
| snake_abs_exit | +4,376 | +2.06% |
| snake_abs_conv | +4,212 | +2.01% |
| snake_abs | +4,199 | +2.00% |
| benchmark_smallcap | +3,509 | +1.77% |
| benchmark | +2,479 | +1.14% |
| random_hold | +1,972 | +0.96% |
| oracle | +1,972 | +0.94% |
| intramonth | +760 | +0.36% |
| unified | +697 | +0.32% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -625 | -0.29% |
| gold | -2,071 | -1.08% |

Average per day so far: benchmark Rs +664, unified Rs +659, snake_abs_exit_conv Rs +623, snake_abs_exit Rs +584, snake_abs_conv Rs +489, snake_abs Rs +477, intraweek Rs +449, oracle Rs +384, intramonth Rs +367, random_hold Rs +224, snake_viper_wild Rs +209, snake_anaconda Rs +163, snake_viper_tick Rs +66, benchmark_smallcap Rs +62, nifty_calls Rs +59, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -321, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.