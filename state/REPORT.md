# Paper trading report

Updated 2026-11-13 12:34 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,102 | +10.05% | 0 | - | 236 |
| benchmark | 219,232 | +9.62% | 0 | - | 237 |
| snake_abs_exit_conv | 216,619 | +8.31% | 2 | 50% | 345 |
| snake_abs_exit | 216,563 | +8.28% | 2 | 50% | 345 |
| intraweek | 216,133 | +8.07% | 30 | 53% | 3,302 |
| oracle | 213,233 | +6.62% | 0 | - | 233 |
| snake_abs | 212,840 | +6.42% | 1 | 100% | 255 |
| snake_abs_conv | 212,669 | +6.33% | 1 | 100% | 255 |
| intramonth | 210,676 | +5.34% | 0 | - | 235 |
| random_hold | 207,110 | +3.56% | 10 | 70% | 733 |
| snake_viper_wild | 205,572 | +2.79% | 14 | 50% | 2,496 |
| snake_anaconda | 205,026 | +2.51% | 3 | 33% | 374 |
| benchmark_smallcap | 202,578 | +1.29% | 0 | - | 237 |
| snake_viper_tick | 202,056 | +1.03% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,831 | -8.08% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,839 (-4.08%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,475 | +0.69% |
| snake_viper_wild | +279 | +0.14% |
| snake_viper_tick | +274 | +0.14% |
| oracle | +118 | +0.06% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -595 | -0.27% |
| benchmark_smallcap | -628 | -0.31% |
| snake_abs_exit | -879 | -0.40% |
| snake_anaconda | -902 | -0.44% |
| intramonth | -918 | -0.43% |
| random_hold | -943 | -0.45% |
| benchmark | -1,316 | -0.60% |
| gold | -1,480 | -0.80% |
| snake_abs_exit_conv | -2,055 | -0.94% |
| snake_abs_conv | -2,866 | -1.33% |
| snake_abs | -2,871 | -1.33% |

Average per day so far: unified Rs +609, benchmark Rs +583, snake_abs_exit_conv Rs +554, snake_abs_exit Rs +552, intraweek Rs +489, snake_abs_conv Rs +422, snake_abs Rs +414, oracle Rs +401, intramonth Rs +324, snake_viper_wild Rs +223, random_hold Rs +215, snake_anaconda Rs +179, snake_viper_tick Rs +93, benchmark_smallcap Rs +89, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -490

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.