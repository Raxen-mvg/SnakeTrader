# Paper trading report

Updated 2026-11-11 09:44 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,596 | +10.80% | 0 | - | 237 |
| unified | 220,345 | +10.17% | 0 | - | 236 |
| snake_abs_exit_conv | 216,367 | +8.18% | 2 | 50% | 345 |
| intraweek | 215,021 | +7.51% | 30 | 53% | 3,302 |
| snake_abs_exit | 214,788 | +7.39% | 2 | 50% | 345 |
| snake_abs | 213,350 | +6.67% | 1 | 100% | 255 |
| snake_abs_conv | 213,190 | +6.59% | 1 | 100% | 255 |
| oracle | 211,343 | +5.67% | 0 | - | 233 |
| intramonth | 210,932 | +5.47% | 0 | - | 235 |
| random_hold | 206,082 | +3.04% | 9 | 67% | 709 |
| snake_anaconda | 202,916 | +1.46% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,289 | +0.64% | 0 | - | 237 |
| snake_viper_wild | 200,171 | +0.09% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 196,773 | -1.61% | 9 | 44% | 1,639 |
| gold | 189,240 | -5.38% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,248 (-4.38%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,458 | +2.10% |
| snake_abs_conv | +3,713 | +1.77% |
| snake_abs | +3,704 | +1.77% |
| benchmark | +3,504 | +1.61% |
| snake_anaconda | +3,450 | +1.73% |
| benchmark_smallcap | +3,116 | +1.57% |
| snake_abs_exit | +2,804 | +1.32% |
| snake_viper_wild | +2,741 | +1.39% |
| snake_viper_tick | +2,697 | +1.39% |
| oracle | +1,424 | +0.68% |
| random_hold | +1,122 | +0.55% |
| unified | +598 | +0.27% |
| intraweek | +479 | +0.22% |
| intramonth | +323 | +0.15% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -2,893 | -1.51% |

Average per day so far: benchmark Rs +697, unified Rs +656, snake_abs_exit_conv Rs +585, snake_abs_exit Rs +528, intraweek Rs +485, snake_abs_conv Rs +471, snake_abs Rs +460, oracle Rs +366, intramonth Rs +353, random_hold Rs +196, snake_anaconda Rs +112, nifty_calls Rs +59, benchmark_smallcap Rs +48, snake_viper_wild Rs +7, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -161, gold Rs -347, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.