# Paper trading report

Updated 2026-11-11 13:52 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,208 | +10.10% | 0 | - | 236 |
| benchmark | 219,568 | +9.78% | 0 | - | 237 |
| snake_abs_exit_conv | 217,339 | +8.67% | 2 | 50% | 345 |
| snake_abs_exit | 216,290 | +8.14% | 2 | 50% | 345 |
| snake_abs | 213,515 | +6.76% | 1 | 100% | 255 |
| snake_abs_conv | 213,363 | +6.68% | 1 | 100% | 255 |
| intraweek | 213,131 | +6.57% | 30 | 53% | 3,302 |
| oracle | 211,654 | +5.83% | 0 | - | 233 |
| intramonth | 211,135 | +5.57% | 0 | - | 235 |
| random_hold | 206,810 | +3.40% | 9 | 67% | 709 |
| snake_viper_wild | 204,994 | +2.50% | 10 | 50% | 1,825 |
| snake_anaconda | 204,126 | +2.06% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,497 | +0.75% | 9 | 44% | 1,639 |
| benchmark_smallcap | 200,616 | +0.31% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,815 | -5.09% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,039 (-4.48%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +7,564 | +3.83% |
| snake_viper_tick | +7,421 | +3.82% |
| snake_abs_exit_conv | +5,430 | +2.56% |
| snake_anaconda | +4,659 | +2.34% |
| snake_abs_exit | +4,306 | +2.03% |
| snake_abs_conv | +3,885 | +1.85% |
| snake_abs | +3,868 | +1.84% |
| benchmark_smallcap | +2,444 | +1.23% |
| random_hold | +1,850 | +0.90% |
| oracle | +1,735 | +0.83% |
| benchmark | +1,476 | +0.68% |
| intramonth | +526 | +0.25% |
| unified | +461 | +0.21% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -1,411 | -0.66% |
| gold | -2,318 | -1.21% |

Average per day so far: unified Rs +652, benchmark Rs +631, snake_abs_exit_conv Rs +619, snake_abs_exit Rs +582, snake_abs_conv Rs +477, snake_abs Rs +466, intraweek Rs +424, oracle Rs +376, intramonth Rs +359, random_hold Rs +220, snake_viper_wild Rs +217, snake_anaconda Rs +159, snake_viper_tick Rs +75, nifty_calls Rs +59, benchmark_smallcap Rs +23, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -329, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.