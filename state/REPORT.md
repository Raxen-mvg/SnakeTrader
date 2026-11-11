# Paper trading report

Updated 2026-11-11 13:55 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,261 | +10.13% | 0 | - | 236 |
| benchmark | 219,530 | +9.77% | 0 | - | 237 |
| snake_abs_exit_conv | 217,107 | +8.55% | 2 | 50% | 345 |
| snake_abs_exit | 216,149 | +8.07% | 2 | 50% | 345 |
| snake_abs | 213,342 | +6.67% | 1 | 100% | 255 |
| snake_abs_conv | 213,189 | +6.59% | 1 | 100% | 255 |
| intraweek | 213,020 | +6.51% | 30 | 53% | 3,302 |
| oracle | 211,601 | +5.80% | 0 | - | 233 |
| intramonth | 211,172 | +5.59% | 0 | - | 235 |
| random_hold | 206,897 | +3.45% | 9 | 67% | 709 |
| snake_viper_wild | 205,432 | +2.72% | 10 | 50% | 1,825 |
| snake_anaconda | 203,914 | +1.96% | 3 | 33% | 374 |
| snake_viper_tick | 201,926 | +0.96% | 9 | 44% | 1,639 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,627 | +0.31% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,799 | -5.10% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,012 (-4.49%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +8,002 | +4.05% |
| snake_viper_tick | +7,850 | +4.04% |
| snake_abs_exit_conv | +5,198 | +2.45% |
| snake_anaconda | +4,447 | +2.23% |
| snake_abs_exit | +4,166 | +1.97% |
| snake_abs_conv | +3,711 | +1.77% |
| snake_abs | +3,695 | +1.76% |
| benchmark_smallcap | +2,455 | +1.24% |
| random_hold | +1,936 | +0.94% |
| oracle | +1,682 | +0.80% |
| benchmark | +1,438 | +0.66% |
| intramonth | +562 | +0.27% |
| unified | +514 | +0.23% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -1,522 | -0.71% |
| gold | -2,334 | -1.22% |

Average per day so far: unified Rs +654, benchmark Rs +630, snake_abs_exit_conv Rs +611, snake_abs_exit Rs +577, snake_abs_conv Rs +471, snake_abs Rs +460, intraweek Rs +420, oracle Rs +374, intramonth Rs +360, snake_viper_wild Rs +236, random_hold Rs +222, snake_anaconda Rs +151, snake_viper_tick Rs +96, nifty_calls Rs +59, benchmark_smallcap Rs +23, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -329, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.