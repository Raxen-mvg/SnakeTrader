# Paper trading report

Updated 2026-11-11 12:40 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,620 | +10.31% | 0 | - | 236 |
| benchmark | 220,379 | +10.19% | 0 | - | 237 |
| snake_abs_exit_conv | 217,452 | +8.73% | 2 | 50% | 345 |
| snake_abs_exit | 216,379 | +8.19% | 2 | 50% | 345 |
| intraweek | 213,777 | +6.89% | 30 | 53% | 3,302 |
| snake_abs | 213,531 | +6.76% | 1 | 100% | 255 |
| snake_abs_conv | 213,381 | +6.69% | 1 | 100% | 255 |
| oracle | 211,982 | +5.99% | 0 | - | 233 |
| intramonth | 211,571 | +5.79% | 0 | - | 235 |
| random_hold | 206,922 | +3.46% | 9 | 67% | 709 |
| snake_viper_wild | 204,790 | +2.40% | 10 | 50% | 1,825 |
| snake_anaconda | 204,333 | +2.17% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,345 | +0.67% | 0 | - | 237 |
| snake_viper_tick | 201,298 | +0.65% | 9 | 44% | 1,639 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 190,046 | -4.98% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,364 (-4.32%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +7,360 | +3.73% |
| snake_viper_tick | +7,222 | +3.72% |
| snake_abs_exit_conv | +5,543 | +2.62% |
| snake_anaconda | +4,867 | +2.44% |
| snake_abs_exit | +4,395 | +2.07% |
| snake_abs_conv | +3,903 | +1.86% |
| snake_abs | +3,884 | +1.85% |
| benchmark_smallcap | +3,172 | +1.60% |
| benchmark | +2,287 | +1.05% |
| oracle | +2,064 | +0.98% |
| random_hold | +1,962 | +0.96% |
| intramonth | +962 | +0.46% |
| unified | +873 | +0.40% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -765 | -0.36% |
| gold | -2,088 | -1.09% |

Average per day so far: unified Rs +665, benchmark Rs +657, snake_abs_exit_conv Rs +623, snake_abs_exit Rs +585, snake_abs_conv Rs +478, snake_abs Rs +467, intraweek Rs +444, oracle Rs +387, intramonth Rs +373, random_hold Rs +223, snake_viper_wild Rs +208, snake_anaconda Rs +167, snake_viper_tick Rs +65, nifty_calls Rs +59, benchmark_smallcap Rs +50, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -321, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.