# Paper trading report

Updated 2026-11-11 15:28 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,837 | +9.92% | 0 | - | 236 |
| benchmark | 219,461 | +9.73% | 0 | - | 237 |
| snake_abs_exit_conv | 217,539 | +8.77% | 2 | 50% | 345 |
| snake_abs_exit | 216,492 | +8.25% | 2 | 50% | 345 |
| intraweek | 213,962 | +6.98% | 30 | 53% | 3,302 |
| snake_abs | 213,875 | +6.94% | 1 | 100% | 255 |
| snake_abs_conv | 213,708 | +6.85% | 1 | 100% | 255 |
| oracle | 212,381 | +6.19% | 0 | - | 233 |
| intramonth | 211,017 | +5.51% | 0 | - | 235 |
| random_hold | 207,293 | +3.65% | 9 | 67% | 709 |
| snake_viper_wild | 207,087 | +3.54% | 10 | 50% | 1,825 |
| snake_anaconda | 204,398 | +2.20% | 3 | 33% | 374 |
| snake_viper_tick | 203,548 | +1.77% | 9 | 44% | 1,639 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,694 | +0.35% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,520 | -5.24% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,284 (-4.36%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +9,657 | +4.89% |
| snake_viper_tick | +9,471 | +4.88% |
| snake_abs_exit_conv | +5,631 | +2.66% |
| snake_anaconda | +4,931 | +2.47% |
| snake_abs_exit | +4,508 | +2.13% |
| snake_abs_conv | +4,230 | +2.02% |
| snake_abs | +4,228 | +2.02% |
| benchmark_smallcap | +2,522 | +1.27% |
| oracle | +2,463 | +1.17% |
| random_hold | +2,332 | +1.14% |
| benchmark | +1,369 | +0.63% |
| intramonth | +408 | +0.19% |
| unified | +90 | +0.04% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -580 | -0.27% |
| gold | -2,614 | -1.36% |

Average per day so far: unified Rs +640, benchmark Rs +628, snake_abs_exit_conv Rs +626, snake_abs_exit Rs +589, snake_abs_conv Rs +490, snake_abs Rs +478, intraweek Rs +450, oracle Rs +399, intramonth Rs +355, snake_viper_wild Rs +308, random_hold Rs +235, snake_viper_tick Rs +177, snake_anaconda Rs +169, nifty_calls Rs +59, benchmark_smallcap Rs +26, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -338, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.