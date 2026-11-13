# Paper trading report

Updated 2026-11-13 11:10 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,432 | +10.22% | 0 | - | 236 |
| benchmark | 219,767 | +9.88% | 0 | - | 237 |
| snake_abs_exit_conv | 216,869 | +8.43% | 2 | 50% | 345 |
| snake_abs_exit | 216,628 | +8.31% | 2 | 50% | 345 |
| intraweek | 216,044 | +8.02% | 30 | 53% | 3,302 |
| oracle | 213,485 | +6.74% | 0 | - | 233 |
| snake_abs | 212,802 | +6.40% | 1 | 100% | 255 |
| snake_abs_conv | 212,638 | +6.32% | 1 | 100% | 255 |
| intramonth | 211,214 | +5.61% | 0 | - | 235 |
| random_hold | 207,066 | +3.53% | 10 | 70% | 733 |
| snake_viper_wild | 206,509 | +3.25% | 14 | 50% | 2,496 |
| snake_anaconda | 205,005 | +2.50% | 3 | 33% | 374 |
| benchmark_smallcap | 203,374 | +1.69% | 0 | - | 237 |
| snake_viper_tick | 202,977 | +1.49% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,390 | -7.80% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,017 (-3.99%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,386 | +0.65% |
| snake_viper_wild | +1,216 | +0.59% |
| snake_viper_tick | +1,195 | +0.59% |
| oracle | +370 | +0.17% |
| benchmark_smallcap | +168 | +0.08% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -264 | -0.12% |
| intramonth | -379 | -0.18% |
| benchmark | -780 | -0.35% |
| snake_abs_exit | -814 | -0.37% |
| gold | -921 | -0.50% |
| snake_anaconda | -922 | -0.45% |
| random_hold | -988 | -0.47% |
| snake_abs_exit_conv | -1,805 | -0.83% |
| snake_abs_conv | -2,897 | -1.34% |
| snake_abs | -2,909 | -1.35% |

Average per day so far: unified Rs +619, benchmark Rs +599, snake_abs_exit_conv Rs +562, snake_abs_exit Rs +554, intraweek Rs +486, snake_abs_conv Rs +421, snake_abs Rs +413, oracle Rs +409, intramonth Rs +340, snake_viper_wild Rs +260, random_hold Rs +214, snake_anaconda Rs +179, snake_viper_tick Rs +135, benchmark_smallcap Rs +116, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -473

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.