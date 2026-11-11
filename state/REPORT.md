# Paper trading report

Updated 2026-11-11 09:31 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,838 | +10.42% | 0 | - | 237 |
| unified | 219,662 | +9.83% | 0 | - | 236 |
| snake_abs_exit_conv | 216,064 | +8.03% | 2 | 50% | 345 |
| snake_abs_exit | 214,844 | +7.42% | 2 | 50% | 345 |
| intraweek | 214,432 | +7.22% | 30 | 53% | 3,302 |
| snake_abs | 213,431 | +6.71% | 1 | 100% | 255 |
| snake_abs_conv | 213,268 | +6.63% | 1 | 100% | 255 |
| oracle | 211,204 | +5.60% | 0 | - | 233 |
| intramonth | 210,536 | +5.27% | 0 | - | 235 |
| random_hold | 205,814 | +2.91% | 9 | 67% | 709 |
| snake_anaconda | 203,014 | +1.51% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,919 | +0.46% | 0 | - | 237 |
| snake_viper_wild | 200,785 | +0.39% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 197,374 | -1.31% | 9 | 44% | 1,639 |
| gold | 189,437 | -5.28% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,914 (-4.54%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,155 | +1.96% |
| snake_abs_conv | +3,791 | +1.81% |
| snake_abs | +3,784 | +1.80% |
| snake_anaconda | +3,548 | +1.78% |
| snake_viper_wild | +3,355 | +1.70% |
| snake_viper_tick | +3,297 | +1.70% |
| snake_abs_exit | +2,860 | +1.35% |
| benchmark_smallcap | +2,746 | +1.39% |
| benchmark | +2,746 | +1.26% |
| oracle | +1,285 | +0.61% |
| random_hold | +853 | +0.42% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intramonth | -73 | -0.04% |
| unified | -85 | -0.04% |
| intraweek | -110 | -0.05% |
| gold | -2,696 | -1.40% |

Average per day so far: benchmark Rs +672, unified Rs +634, snake_abs_exit_conv Rs +574, snake_abs_exit Rs +530, snake_abs_conv Rs +474, intraweek Rs +466, snake_abs Rs +463, oracle Rs +361, intramonth Rs +340, random_hold Rs +188, snake_anaconda Rs +116, nifty_calls Rs +59, snake_viper_wild Rs +34, benchmark_smallcap Rs +34, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -131, gold Rs -341, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.