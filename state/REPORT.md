# Paper trading report

Updated 2026-11-04 13:22 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,223 | +7.11% | 0 | - | 236 |
| snake_abs_exit_conv | 212,907 | +6.45% | 1 | 100% | 255 |
| snake_abs_exit | 212,771 | +6.39% | 1 | 100% | 260 |
| snake_abs | 209,803 | +4.90% | 1 | 100% | 255 |
| snake_abs_conv | 209,649 | +4.82% | 1 | 100% | 255 |
| intraweek | 209,560 | +4.78% | 25 | 48% | 2,757 |
| benchmark | 208,132 | +4.07% | 0 | - | 237 |
| snake_viper_wild | 206,786 | +3.39% | 3 | 33% | 702 |
| intramonth | 206,466 | +3.23% | 0 | - | 235 |
| snake_viper_tick | 203,181 | +1.59% | 2 | 0% | 532 |
| random_hold | 202,621 | +1.31% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,281 | +0.64% | 0 | - | 233 |
| snake_anaconda | 201,275 | +0.64% | 3 | 33% | 361 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 195,560 | -2.22% | 0 | - | 237 |
| gold | 190,983 | -4.51% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,322 (-5.34%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +8,757 | +4.29% |
| snake_abs_exit_conv | +8,569 | +4.19% |
| snake_abs_conv | +8,508 | +4.23% |
| snake_abs | +8,494 | +4.22% |
| snake_anaconda | +7,451 | +3.84% |
| gold | +5,705 | +3.08% |
| intraweek | +4,474 | +2.18% |
| benchmark_smallcap | +2,623 | +1.36% |
| intramonth | +2,495 | +1.22% |
| unified | +2,222 | +1.05% |
| random_hold | +2,153 | +1.07% |
| benchmark | +1,431 | +0.69% |
| oracle | +1,292 | +0.65% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,986 | -1.92% |
| snake_viper_wild | -4,107 | -1.95% |

Average per day so far: snake_abs_exit_conv Rs +538, snake_abs_exit Rs +532, unified Rs +527, snake_abs_conv Rs +402, snake_abs Rs +392, snake_viper_wild Rs +357, intraweek Rs +354, benchmark Rs +301, intramonth Rs +239, snake_viper_tick Rs +199, random_hold Rs +97, nifty_calls Rs +68, snake_anaconda Rs +58, oracle Rs +47, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -193, gold Rs -334, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.