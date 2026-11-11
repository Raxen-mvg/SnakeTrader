# Paper trading report

Updated 2026-11-11 09:55 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,221 | +10.61% | 0 | - | 237 |
| unified | 220,599 | +10.30% | 0 | - | 236 |
| snake_abs_exit_conv | 216,421 | +8.21% | 2 | 50% | 345 |
| intraweek | 215,430 | +7.71% | 30 | 53% | 3,302 |
| snake_abs_exit | 214,724 | +7.36% | 2 | 50% | 345 |
| snake_abs | 213,270 | +6.63% | 1 | 100% | 255 |
| snake_abs_conv | 213,111 | +6.55% | 1 | 100% | 255 |
| oracle | 211,232 | +5.62% | 0 | - | 233 |
| intramonth | 211,095 | +5.55% | 0 | - | 235 |
| random_hold | 206,302 | +3.15% | 9 | 67% | 709 |
| snake_anaconda | 202,635 | +1.32% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,434 | +0.72% | 0 | - | 237 |
| snake_viper_wild | 200,124 | +0.06% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 196,728 | -1.64% | 9 | 44% | 1,639 |
| gold | 189,174 | -5.41% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,394 (-4.30%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,512 | +2.13% |
| snake_abs_conv | +3,633 | +1.74% |
| snake_abs | +3,624 | +1.73% |
| benchmark_smallcap | +3,262 | +1.65% |
| snake_anaconda | +3,169 | +1.59% |
| benchmark | +3,129 | +1.44% |
| snake_abs_exit | +2,740 | +1.29% |
| snake_viper_wild | +2,694 | +1.36% |
| snake_viper_tick | +2,651 | +1.37% |
| random_hold | +1,342 | +0.66% |
| oracle | +1,313 | +0.63% |
| intraweek | +888 | +0.41% |
| unified | +852 | +0.39% |
| intramonth | +486 | +0.23% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -2,959 | -1.54% |

Average per day so far: benchmark Rs +685, unified Rs +664, snake_abs_exit_conv Rs +586, snake_abs_exit Rs +526, intraweek Rs +498, snake_abs_conv Rs +468, snake_abs Rs +458, oracle Rs +362, intramonth Rs +358, random_hold Rs +203, snake_anaconda Rs +101, nifty_calls Rs +59, benchmark_smallcap Rs +53, snake_viper_wild Rs +5, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -164, gold Rs -349, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.