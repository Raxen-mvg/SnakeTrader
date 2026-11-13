# Paper trading report

Updated 2026-11-13 11:31 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,577 | +10.29% | 0 | - | 236 |
| benchmark | 219,607 | +9.80% | 0 | - | 237 |
| snake_abs_exit_conv | 216,513 | +8.26% | 2 | 50% | 345 |
| snake_abs_exit | 216,420 | +8.21% | 2 | 50% | 345 |
| intraweek | 216,245 | +8.12% | 30 | 53% | 3,302 |
| oracle | 213,537 | +6.77% | 0 | - | 233 |
| snake_abs | 212,778 | +6.39% | 1 | 100% | 255 |
| snake_abs_conv | 212,607 | +6.30% | 1 | 100% | 255 |
| intramonth | 211,277 | +5.64% | 0 | - | 235 |
| random_hold | 207,305 | +3.65% | 10 | 70% | 733 |
| snake_viper_wild | 206,005 | +3.00% | 14 | 50% | 2,496 |
| snake_anaconda | 204,839 | +2.42% | 3 | 33% | 374 |
| benchmark_smallcap | 203,250 | +1.62% | 0 | - | 237 |
| snake_viper_tick | 202,481 | +1.24% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,798 | -8.10% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,111 (-3.94%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,587 | +0.74% |
| snake_viper_wild | +712 | +0.35% |
| snake_viper_tick | +700 | +0.35% |
| oracle | +422 | +0.20% |
| benchmark_smallcap | +45 | +0.02% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -120 | -0.05% |
| intramonth | -316 | -0.15% |
| random_hold | -748 | -0.36% |
| benchmark | -941 | -0.43% |
| snake_abs_exit | -1,023 | -0.47% |
| snake_anaconda | -1,088 | -0.53% |
| gold | -1,512 | -0.82% |
| snake_abs_exit_conv | -2,161 | -0.99% |
| snake_abs_conv | -2,928 | -1.36% |
| snake_abs | -2,934 | -1.36% |

Average per day so far: unified Rs +624, benchmark Rs +594, snake_abs_exit_conv Rs +550, snake_abs_exit Rs +547, intraweek Rs +492, snake_abs_conv Rs +420, snake_abs Rs +412, oracle Rs +410, intramonth Rs +342, snake_viper_wild Rs +240, random_hold Rs +221, snake_anaconda Rs +173, snake_viper_tick Rs +113, benchmark_smallcap Rs +112, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -491

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.