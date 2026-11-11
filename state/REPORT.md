# Paper trading report

Updated 2026-11-11 10:40 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,144 | +10.57% | 0 | - | 237 |
| unified | 220,925 | +10.46% | 0 | - | 236 |
| snake_abs_exit_conv | 215,914 | +7.96% | 2 | 50% | 345 |
| snake_abs_exit | 214,357 | +7.18% | 2 | 50% | 345 |
| intraweek | 214,337 | +7.17% | 30 | 53% | 3,302 |
| snake_abs | 212,778 | +6.39% | 1 | 100% | 255 |
| snake_abs_conv | 212,621 | +6.31% | 1 | 100% | 255 |
| oracle | 211,897 | +5.95% | 0 | - | 233 |
| intramonth | 211,660 | +5.83% | 0 | - | 235 |
| random_hold | 206,828 | +3.41% | 9 | 67% | 709 |
| snake_anaconda | 202,475 | +1.24% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,625 | +0.81% | 0 | - | 237 |
| snake_viper_wild | 200,327 | +0.16% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 196,926 | -1.54% | 9 | 44% | 1,639 |
| gold | 189,569 | -5.22% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,398 (-4.30%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,005 | +1.89% |
| benchmark_smallcap | +3,453 | +1.74% |
| snake_abs_conv | +3,144 | +1.50% |
| snake_abs | +3,132 | +1.49% |
| benchmark | +3,052 | +1.40% |
| snake_anaconda | +3,008 | +1.51% |
| snake_viper_wild | +2,897 | +1.47% |
| snake_viper_tick | +2,849 | +1.47% |
| snake_abs_exit | +2,373 | +1.12% |
| oracle | +1,978 | +0.94% |
| random_hold | +1,868 | +0.91% |
| unified | +1,178 | +0.54% |
| intramonth | +1,051 | +0.50% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -205 | -0.10% |
| gold | -2,565 | -1.33% |

Average per day so far: benchmark Rs +682, unified Rs +675, snake_abs_exit_conv Rs +568, snake_abs_exit Rs +513, intraweek Rs +462, snake_abs_conv Rs +451, snake_abs Rs +441, oracle Rs +384, intramonth Rs +376, random_hold Rs +220, snake_anaconda Rs +95, benchmark_smallcap Rs +60, nifty_calls Rs +59, snake_viper_wild Rs +14, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -154, gold Rs -336, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.