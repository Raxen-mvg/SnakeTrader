# Paper trading report

Updated 2026-11-11 15:24 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,753 | +9.88% | 0 | - | 236 |
| benchmark | 219,316 | +9.66% | 0 | - | 237 |
| snake_abs_exit_conv | 217,240 | +8.62% | 2 | 50% | 345 |
| snake_abs_exit | 216,124 | +8.06% | 2 | 50% | 345 |
| intraweek | 213,762 | +6.88% | 30 | 53% | 3,302 |
| snake_abs | 213,615 | +6.81% | 1 | 100% | 255 |
| snake_abs_conv | 213,448 | +6.72% | 1 | 100% | 255 |
| oracle | 212,635 | +6.32% | 0 | - | 233 |
| intramonth | 211,000 | +5.50% | 0 | - | 235 |
| random_hold | 207,275 | +3.64% | 9 | 67% | 709 |
| snake_viper_wild | 206,522 | +3.26% | 10 | 50% | 1,825 |
| snake_anaconda | 204,060 | +2.03% | 3 | 33% | 374 |
| snake_viper_tick | 202,994 | +1.50% | 9 | 44% | 1,639 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,773 | +0.39% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,569 | -5.22% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,229 (-4.39%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +9,092 | +4.61% |
| snake_viper_tick | +8,917 | +4.59% |
| snake_abs_exit_conv | +5,331 | +2.52% |
| snake_anaconda | +4,594 | +2.30% |
| snake_abs_exit | +4,141 | +1.95% |
| snake_abs_conv | +3,970 | +1.90% |
| snake_abs | +3,968 | +1.89% |
| oracle | +2,717 | +1.29% |
| benchmark_smallcap | +2,601 | +1.31% |
| random_hold | +2,314 | +1.13% |
| benchmark | +1,224 | +0.56% |
| intramonth | +391 | +0.18% |
| unified | +7 | +0.00% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -780 | -0.36% |
| gold | -2,565 | -1.33% |

Average per day so far: unified Rs +637, benchmark Rs +623, snake_abs_exit_conv Rs +616, snake_abs_exit Rs +576, snake_abs_conv Rs +480, snake_abs Rs +469, intraweek Rs +444, oracle Rs +408, intramonth Rs +355, snake_viper_wild Rs +284, random_hold Rs +235, snake_anaconda Rs +156, snake_viper_tick Rs +150, nifty_calls Rs +59, benchmark_smallcap Rs +29, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -336, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.