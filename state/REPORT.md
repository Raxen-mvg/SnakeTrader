# Paper trading report

Updated 2026-11-23 15:08 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,173 | +12.09% | 0 | - | 236 |
| benchmark | 221,489 | +10.74% | 0 | - | 237 |
| oracle | 212,347 | +6.17% | 0 | - | 233 |
| intramonth | 211,929 | +5.96% | 0 | - | 235 |
| intraweek | 211,580 | +5.79% | 40 | 55% | 4,400 |
| random_hold | 208,511 | +4.26% | 12 | 75% | 1,009 |
| snake_abs_exit | 208,100 | +4.05% | 2 | 50% | 345 |
| snake_abs_exit_conv | 207,600 | +3.80% | 2 | 50% | 345 |
| snake_abs | 205,968 | +2.98% | 1 | 100% | 255 |
| snake_abs_conv | 205,816 | +2.91% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,532 | +0.77% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,394 | -0.30% | 0 | - | 237 |
| snake_anaconda | 199,298 | -0.35% | 3 | 33% | 374 |
| snake_viper_tick | 198,092 | -0.95% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,397 | -15.30% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,273 (-4.86%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,348 | +0.80% |
| snake_abs_exit_conv | +983 | +0.48% |
| snake_abs | +49 | +0.02% |
| snake_abs_conv | +33 | +0.02% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| oracle | -131 | -0.06% |
| snake_abs_exit | -463 | -0.22% |
| snake_anaconda | -608 | -0.30% |
| snake_viper_tick | -1,280 | -0.64% |
| snake_viper_wild | -1,297 | -0.64% |
| benchmark_smallcap | -1,513 | -0.75% |
| unified | -2,008 | -0.89% |
| random_hold | -2,248 | -1.07% |
| intramonth | -3,075 | -1.43% |
| benchmark | -3,649 | -1.62% |
| intraweek | -4,132 | -1.92% |

Average per day so far: unified Rs +620, benchmark Rs +551, oracle Rs +317, intramonth Rs +306, intraweek Rs +297, snake_abs_exit Rs +225, random_hold Rs +218, snake_abs_exit_conv Rs +211, snake_abs_conv Rs +162, snake_abs Rs +161, snake_viper_wild Rs +49, nifty_calls Rs +47, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -17, snake_anaconda Rs -21, snake_viper_tick Rs -68, snake_nonews Rs -300, snake Rs -320, gold Rs -785

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.