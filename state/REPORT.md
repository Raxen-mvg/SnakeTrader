# Paper trading report

Updated 2026-11-18 13:10 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,871 | +11.44% | 0 | - | 236 |
| benchmark | 219,660 | +9.83% | 0 | - | 237 |
| intramonth | 212,729 | +6.36% | 0 | - | 235 |
| intraweek | 212,695 | +6.35% | 35 | 54% | 3,851 |
| snake_abs_exit | 212,124 | +6.06% | 2 | 50% | 345 |
| oracle | 211,878 | +5.94% | 0 | - | 233 |
| snake_abs_exit_conv | 210,407 | +5.20% | 2 | 50% | 345 |
| snake_abs | 207,576 | +3.79% | 1 | 100% | 255 |
| snake_abs_conv | 207,436 | +3.72% | 1 | 100% | 255 |
| random_hold | 207,030 | +3.52% | 10 | 70% | 733 |
| snake_viper_wild | 206,627 | +3.31% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,099 | +1.55% | 15 | 47% | 2,625 |
| snake_anaconda | 202,564 | +1.28% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,181 | -0.41% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 176,762 | -11.62% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,108 (-4.45%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,433 | +0.65% |
| intramonth | +1,186 | +0.56% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| oracle | -608 | -0.29% |
| intraweek | -627 | -0.29% |
| snake_abs | -982 | -0.47% |
| snake_abs_conv | -983 | -0.47% |
| snake_abs_exit | -1,018 | -0.48% |
| snake_abs_exit_conv | -1,167 | -0.55% |
| benchmark_smallcap | -1,390 | -0.69% |
| random_hold | -1,403 | -0.67% |
| snake_anaconda | -1,491 | -0.73% |
| benchmark | -1,943 | -0.88% |
| snake_viper_tick | -2,738 | -1.33% |
| snake_viper_wild | -2,788 | -1.33% |
| gold | -3,962 | -2.19% |

Average per day so far: unified Rs +635, benchmark Rs +546, snake_abs_exit Rs +367, intramonth Rs +354, intraweek Rs +353, oracle Rs +330, snake_abs_exit_conv Rs +315, snake_viper_wild Rs +237, snake_abs_conv Rs +225, snake_abs Rs +223, random_hold Rs +195, snake_viper_tick Rs +124, snake_anaconda Rs +83, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -26, snake_nonews Rs -326, snake Rs -347, gold Rs -645

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.