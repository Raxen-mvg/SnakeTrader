# Paper trading report

Updated 2026-11-23 15:01 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,892 | +11.95% | 0 | - | 236 |
| benchmark | 221,573 | +10.79% | 0 | - | 237 |
| oracle | 211,956 | +5.98% | 0 | - | 233 |
| intramonth | 211,680 | +5.84% | 0 | - | 235 |
| intraweek | 211,639 | +5.82% | 40 | 55% | 4,400 |
| random_hold | 208,664 | +4.33% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,233 | +3.62% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,602 | +3.30% | 2 | 50% | 345 |
| snake_abs | 205,387 | +2.69% | 1 | 100% | 255 |
| snake_abs_conv | 205,209 | +2.60% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,532 | +0.77% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,786 | -0.11% | 0 | - | 237 |
| snake_anaconda | 198,364 | -0.82% | 3 | 33% | 374 |
| snake_viper_tick | 198,092 | -0.95% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,528 | -15.24% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,078 (-4.96%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,480 | +0.88% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -15 | -0.01% |
| oracle | -523 | -0.25% |
| snake_abs | -533 | -0.26% |
| snake_abs_conv | -574 | -0.28% |
| benchmark_smallcap | -1,121 | -0.56% |
| snake_viper_tick | -1,280 | -0.64% |
| snake_viper_wild | -1,297 | -0.64% |
| snake_abs_exit | -1,329 | -0.64% |
| snake_anaconda | -1,541 | -0.77% |
| random_hold | -2,096 | -0.99% |
| unified | -2,290 | -1.01% |
| intramonth | -3,324 | -1.55% |
| benchmark | -3,565 | -1.58% |
| intraweek | -4,073 | -1.89% |

Average per day so far: unified Rs +613, benchmark Rs +553, oracle Rs +307, intramonth Rs +299, intraweek Rs +298, random_hold Rs +222, snake_abs_exit Rs +201, snake_abs_exit_conv Rs +183, snake_abs Rs +146, snake_abs_conv Rs +145, snake_viper_wild Rs +49, nifty_calls Rs +47, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -6, snake_anaconda Rs -48, snake_viper_tick Rs -68, snake_nonews Rs -300, snake Rs -320, gold Rs -781

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.