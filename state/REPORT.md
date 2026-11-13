# Paper trading report

Updated 2026-11-13 12:49 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,103 | +10.05% | 0 | - | 236 |
| benchmark | 219,194 | +9.60% | 0 | - | 237 |
| snake_abs_exit | 216,858 | +8.43% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,811 | +8.41% | 2 | 50% | 345 |
| intraweek | 215,562 | +7.78% | 30 | 53% | 3,302 |
| oracle | 212,972 | +6.49% | 0 | - | 233 |
| snake_abs | 212,727 | +6.36% | 1 | 100% | 255 |
| snake_abs_conv | 212,561 | +6.28% | 1 | 100% | 255 |
| intramonth | 210,676 | +5.34% | 0 | - | 235 |
| random_hold | 207,143 | +3.57% | 10 | 70% | 733 |
| snake_viper_wild | 205,581 | +2.79% | 14 | 50% | 2,496 |
| snake_anaconda | 205,073 | +2.54% | 3 | 33% | 374 |
| benchmark_smallcap | 202,544 | +1.27% | 0 | - | 237 |
| snake_viper_tick | 202,064 | +1.03% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,519 | -8.24% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,654 (-4.17%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +904 | +0.42% |
| snake_viper_wild | +288 | +0.14% |
| snake_viper_tick | +283 | +0.14% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -143 | -0.07% |
| snake_abs_exit | -584 | -0.27% |
| unified | -594 | -0.27% |
| benchmark_smallcap | -661 | -0.33% |
| snake_anaconda | -854 | -0.41% |
| random_hold | -911 | -0.44% |
| intramonth | -917 | -0.43% |
| benchmark | -1,354 | -0.61% |
| gold | -1,792 | -0.97% |
| snake_abs_exit_conv | -1,863 | -0.85% |
| snake_abs_conv | -2,974 | -1.38% |
| snake_abs | -2,984 | -1.38% |

Average per day so far: unified Rs +609, benchmark Rs +582, snake_abs_exit Rs +562, snake_abs_exit_conv Rs +560, intraweek Rs +472, snake_abs_conv Rs +419, snake_abs Rs +411, oracle Rs +393, intramonth Rs +324, snake_viper_wild Rs +223, random_hold Rs +216, snake_anaconda Rs +181, snake_viper_tick Rs +94, benchmark_smallcap Rs +88, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -499

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.