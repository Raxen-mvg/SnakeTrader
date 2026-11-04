# Paper trading report

Updated 2026-11-04 11:05 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 212,727 | +6.36% | 0 | - | 236 |
| snake_abs_exit_conv | 208,552 | +4.28% | 1 | 100% | 255 |
| snake_abs_exit | 208,413 | +4.21% | 1 | 100% | 260 |
| intraweek | 207,645 | +3.82% | 25 | 48% | 2,757 |
| benchmark | 207,374 | +3.69% | 0 | - | 237 |
| snake_viper_wild | 206,714 | +3.36% | 3 | 33% | 702 |
| intramonth | 205,575 | +2.79% | 0 | - | 235 |
| snake_abs | 205,459 | +2.73% | 1 | 100% | 255 |
| snake_abs_conv | 205,310 | +2.65% | 1 | 100% | 255 |
| snake_viper_tick | 203,111 | +1.56% | 2 | 0% | 532 |
| random_hold | 202,088 | +1.04% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,526 | +0.26% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,425 | -1.29% | 3 | 33% | 361 |
| benchmark_smallcap | 194,394 | -2.80% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| gold | 188,714 | -5.64% | 0 | - | 237 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 188,588 (-5.71%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,399 | +2.16% |
| snake_abs_exit_conv | +4,213 | +2.06% |
| snake_abs_conv | +4,169 | +2.07% |
| snake_abs | +4,149 | +2.06% |
| snake_anaconda | +3,601 | +1.86% |
| gold | +3,436 | +1.85% |
| intraweek | +2,560 | +1.25% |
| random_hold | +1,620 | +0.81% |
| intramonth | +1,604 | +0.79% |
| benchmark_smallcap | +1,457 | +0.76% |
| unified | +726 | +0.34% |
| benchmark | +673 | +0.33% |
| oracle | +537 | +0.27% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -4,055 | -1.96% |
| snake_viper_wild | -4,178 | -1.98% |

Average per day so far: unified Rs +471, snake_abs_exit_conv Rs +356, snake_viper_wild Rs +353, snake_abs_exit Rs +351, intraweek Rs +283, benchmark Rs +273, snake_abs_conv Rs +221, snake_abs Rs +218, intramonth Rs +206, snake_viper_tick Rs +194, random_hold Rs +77, nifty_calls Rs +68, oracle Rs +19, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -117, benchmark_smallcap Rs -244, gold Rs -418, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.