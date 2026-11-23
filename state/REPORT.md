# Paper trading report

Updated 2026-11-23 12:23 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,200 | +12.10% | 0 | - | 236 |
| benchmark | 222,866 | +11.43% | 0 | - | 237 |
| intraweek | 212,397 | +6.20% | 40 | 55% | 4,400 |
| intramonth | 212,056 | +6.03% | 0 | - | 235 |
| oracle | 211,820 | +5.91% | 0 | - | 233 |
| random_hold | 208,850 | +4.42% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,310 | +3.65% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,028 | +3.01% | 2 | 50% | 345 |
| snake_abs | 205,035 | +2.52% | 1 | 100% | 255 |
| snake_abs_conv | 204,874 | +2.44% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,340 | +0.67% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,663 | -0.17% | 0 | - | 237 |
| snake_anaconda | 198,417 | -0.79% | 3 | 33% | 374 |
| snake_viper_tick | 197,904 | -1.05% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,137 | -14.93% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,240 (-4.88%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,088 | +1.24% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -589 | -0.28% |
| oracle | -659 | -0.31% |
| snake_abs | -885 | -0.43% |
| snake_abs_conv | -909 | -0.44% |
| benchmark_smallcap | -1,244 | -0.62% |
| snake_abs_exit | -1,252 | -0.60% |
| snake_viper_tick | -1,468 | -0.74% |
| snake_anaconda | -1,488 | -0.74% |
| snake_viper_wild | -1,489 | -0.73% |
| random_hold | -1,909 | -0.91% |
| unified | -1,982 | -0.88% |
| benchmark | -2,272 | -1.01% |
| intramonth | -2,948 | -1.37% |
| intraweek | -3,315 | -1.54% |

Average per day so far: unified Rs +621, benchmark Rs +586, intraweek Rs +318, intramonth Rs +309, oracle Rs +303, random_hold Rs +227, snake_abs_exit Rs +203, snake_abs_exit_conv Rs +167, snake_abs Rs +136, snake_abs_conv Rs +135, nifty_calls Rs +47, snake_viper_wild Rs +43, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -10, snake_anaconda Rs -47, snake_viper_tick Rs -75, snake_nonews Rs -300, snake Rs -320, gold Rs -766

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.