# Paper trading report

Updated 2026-11-13 15:30 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 219,339 | +9.67% | 0 | - | 237 |
| unified | 219,020 | +9.51% | 0 | - | 236 |
| snake_abs_exit | 216,985 | +8.49% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,381 | +8.19% | 2 | 50% | 345 |
| intraweek | 216,145 | +8.07% | 30 | 53% | 3,302 |
| oracle | 213,098 | +6.55% | 0 | - | 233 |
| snake_abs | 212,540 | +6.27% | 1 | 100% | 255 |
| snake_abs_conv | 212,367 | +6.18% | 1 | 100% | 255 |
| intramonth | 210,057 | +5.03% | 0 | - | 235 |
| random_hold | 207,226 | +3.61% | 10 | 70% | 733 |
| snake_anaconda | 204,892 | +2.45% | 3 | 33% | 374 |
| snake_viper_wild | 204,757 | +2.38% | 14 | 50% | 2,496 |
| benchmark_smallcap | 202,869 | +1.44% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,255 | +0.63% | 13 | 46% | 2,299 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,996 | -8.00% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,567 (-4.22%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,487 | +0.69% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -18 | -0.01% |
| benchmark_smallcap | -336 | -0.17% |
| snake_abs_exit | -458 | -0.21% |
| snake_viper_tick | -527 | -0.26% |
| snake_viper_wild | -536 | -0.26% |
| random_hold | -828 | -0.40% |
| snake_anaconda | -1,035 | -0.50% |
| benchmark | -1,209 | -0.55% |
| gold | -1,315 | -0.71% |
| intramonth | -1,536 | -0.73% |
| unified | -1,676 | -0.76% |
| snake_abs_exit_conv | -2,293 | -1.05% |
| snake_abs_conv | -3,168 | -1.47% |
| snake_abs | -3,171 | -1.47% |

Average per day so far: benchmark Rs +586, unified Rs +576, snake_abs_exit Rs +566, snake_abs_exit_conv Rs +546, intraweek Rs +489, snake_abs_conv Rs +412, snake_abs Rs +405, oracle Rs +397, intramonth Rs +305, random_hold Rs +219, snake_viper_wild Rs +190, snake_anaconda Rs +175, benchmark_smallcap Rs +99, snake_viper_tick Rs +57, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -485

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.