# Paper trading report

Updated 2026-11-11 12:04 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,389 | +10.70% | 0 | - | 237 |
| unified | 220,455 | +10.23% | 0 | - | 236 |
| snake_abs_exit_conv | 216,588 | +8.29% | 2 | 50% | 345 |
| snake_abs_exit | 215,222 | +7.61% | 2 | 50% | 345 |
| intraweek | 214,229 | +7.11% | 30 | 53% | 3,302 |
| snake_abs | 213,041 | +6.52% | 1 | 100% | 255 |
| snake_abs_conv | 212,887 | +6.44% | 1 | 100% | 255 |
| oracle | 211,909 | +5.96% | 0 | - | 233 |
| intramonth | 211,427 | +5.71% | 0 | - | 235 |
| random_hold | 206,823 | +3.41% | 9 | 67% | 709 |
| snake_anaconda | 203,229 | +1.61% | 3 | 33% | 374 |
| benchmark_smallcap | 201,883 | +0.94% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,652 | +0.83% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 198,224 | -0.89% | 9 | 44% | 1,639 |
| gold | 189,815 | -5.09% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,311 (-4.34%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,679 | +2.21% |
| snake_viper_wild | +4,221 | +2.14% |
| snake_viper_tick | +4,147 | +2.14% |
| snake_anaconda | +3,762 | +1.89% |
| benchmark_smallcap | +3,711 | +1.87% |
| snake_abs_conv | +3,410 | +1.63% |
| snake_abs | +3,394 | +1.62% |
| benchmark | +3,297 | +1.51% |
| snake_abs_exit | +3,239 | +1.53% |
| oracle | +1,991 | +0.95% |
| random_hold | +1,863 | +0.91% |
| intramonth | +818 | +0.39% |
| unified | +709 | +0.32% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -313 | -0.15% |
| gold | -2,318 | -1.21% |

Average per day so far: benchmark Rs +690, unified Rs +660, snake_abs_exit_conv Rs +592, snake_abs_exit Rs +544, snake_abs_conv Rs +460, intraweek Rs +459, snake_abs Rs +450, oracle Rs +384, intramonth Rs +369, random_hold Rs +220, snake_anaconda Rs +124, snake_viper_wild Rs +72, benchmark_smallcap Rs +70, nifty_calls Rs +59, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -89, gold Rs -329, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.