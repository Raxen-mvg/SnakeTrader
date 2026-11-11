# Paper trading report

Updated 2026-11-11 11:01 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,290 | +10.64% | 0 | - | 237 |
| unified | 220,727 | +10.36% | 0 | - | 236 |
| snake_abs_exit_conv | 216,173 | +8.09% | 2 | 50% | 345 |
| snake_abs_exit | 214,780 | +7.39% | 2 | 50% | 345 |
| intraweek | 214,388 | +7.19% | 30 | 53% | 3,302 |
| snake_abs | 212,541 | +6.27% | 1 | 100% | 255 |
| snake_abs_conv | 212,390 | +6.20% | 1 | 100% | 255 |
| oracle | 212,001 | +6.00% | 0 | - | 233 |
| intramonth | 211,559 | +5.78% | 0 | - | 235 |
| random_hold | 206,889 | +3.44% | 9 | 67% | 709 |
| snake_anaconda | 202,535 | +1.27% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,715 | +0.86% | 0 | - | 237 |
| snake_viper_wild | 201,332 | +0.67% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 197,911 | -1.04% | 9 | 44% | 1,639 |
| gold | 189,931 | -5.04% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,378 (-4.31%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,264 | +2.01% |
| snake_viper_wild | +3,901 | +1.98% |
| snake_viper_tick | +3,834 | +1.98% |
| benchmark_smallcap | +3,542 | +1.79% |
| benchmark | +3,198 | +1.47% |
| snake_anaconda | +3,068 | +1.54% |
| snake_abs_conv | +2,912 | +1.39% |
| snake_abs | +2,894 | +1.38% |
| snake_abs_exit | +2,796 | +1.32% |
| oracle | +2,082 | +0.99% |
| random_hold | +1,928 | +0.94% |
| unified | +980 | +0.45% |
| intramonth | +950 | +0.45% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -154 | -0.07% |
| gold | -2,203 | -1.15% |

Average per day so far: benchmark Rs +687, unified Rs +669, snake_abs_exit_conv Rs +578, snake_abs_exit Rs +528, intraweek Rs +464, snake_abs_conv Rs +442, snake_abs Rs +432, oracle Rs +387, intramonth Rs +373, random_hold Rs +222, snake_anaconda Rs +97, benchmark_smallcap Rs +64, nifty_calls Rs +59, snake_viper_wild Rs +58, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -104, gold Rs -325, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.