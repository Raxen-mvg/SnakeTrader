# Paper trading report

Updated 2026-11-04 11:08 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 212,585 | +6.29% | 0 | - | 236 |
| snake_abs_exit_conv | 208,300 | +4.15% | 1 | 100% | 255 |
| snake_abs_exit | 208,162 | +4.08% | 1 | 100% | 260 |
| benchmark | 207,374 | +3.69% | 0 | - | 237 |
| intraweek | 206,851 | +3.43% | 25 | 48% | 2,757 |
| snake_viper_wild | 206,813 | +3.41% | 3 | 33% | 702 |
| intramonth | 205,474 | +2.74% | 0 | - | 235 |
| snake_abs | 205,215 | +2.61% | 1 | 100% | 255 |
| snake_abs_conv | 205,061 | +2.53% | 1 | 100% | 255 |
| snake_viper_tick | 203,208 | +1.60% | 2 | 0% | 532 |
| random_hold | 202,099 | +1.05% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,470 | +0.23% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,179 | -1.41% | 3 | 33% | 361 |
| benchmark_smallcap | 194,495 | -2.75% | 0 | - | 237 |
| gold | 189,141 | -5.43% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 188,463 (-5.77%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,147 | +2.03% |
| snake_abs_exit_conv | +3,961 | +1.94% |
| snake_abs_conv | +3,920 | +1.95% |
| snake_abs | +3,906 | +1.94% |
| gold | +3,863 | +2.08% |
| snake_anaconda | +3,354 | +1.73% |
| intraweek | +1,766 | +0.86% |
| random_hold | +1,630 | +0.81% |
| benchmark_smallcap | +1,558 | +0.81% |
| intramonth | +1,503 | +0.74% |
| benchmark | +673 | +0.33% |
| unified | +584 | +0.28% |
| oracle | +480 | +0.24% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,958 | -1.91% |
| snake_viper_wild | -4,079 | -1.93% |

Average per day so far: unified Rs +466, snake_viper_wild Rs +359, snake_abs_exit_conv Rs +346, snake_abs_exit Rs +340, benchmark Rs +273, intraweek Rs +254, snake_abs_conv Rs +211, snake_abs Rs +209, intramonth Rs +203, snake_viper_tick Rs +201, random_hold Rs +78, nifty_calls Rs +68, oracle Rs +17, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -128, benchmark_smallcap Rs -239, gold Rs -402, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.