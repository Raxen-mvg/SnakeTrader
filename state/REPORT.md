# Paper trading report

Updated 2026-11-13 13:16 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,865 | +9.93% | 0 | - | 236 |
| benchmark | 219,369 | +9.69% | 0 | - | 237 |
| snake_abs_exit | 216,659 | +8.33% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,296 | +8.15% | 2 | 50% | 345 |
| intraweek | 215,574 | +7.79% | 30 | 53% | 3,302 |
| oracle | 212,843 | +6.42% | 0 | - | 233 |
| snake_abs | 212,187 | +6.09% | 1 | 100% | 255 |
| snake_abs_conv | 212,017 | +6.01% | 1 | 100% | 255 |
| intramonth | 210,525 | +5.26% | 0 | - | 235 |
| random_hold | 207,061 | +3.53% | 10 | 70% | 733 |
| snake_viper_wild | 205,518 | +2.76% | 14 | 50% | 2,496 |
| snake_anaconda | 204,382 | +2.19% | 3 | 33% | 374 |
| benchmark_smallcap | 202,634 | +1.32% | 0 | - | 237 |
| snake_viper_tick | 202,003 | +1.00% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,848 | -8.08% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,538 (-4.23%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +916 | +0.43% |
| snake_viper_wild | +226 | +0.11% |
| snake_viper_tick | +221 | +0.11% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -272 | -0.13% |
| benchmark_smallcap | -572 | -0.28% |
| snake_abs_exit | -783 | -0.36% |
| unified | -832 | -0.38% |
| random_hold | -993 | -0.48% |
| intramonth | -1,068 | -0.51% |
| benchmark | -1,178 | -0.53% |
| gold | -1,463 | -0.79% |
| snake_anaconda | -1,545 | -0.75% |
| snake_abs_exit_conv | -2,378 | -1.09% |
| snake_abs_conv | -3,518 | -1.63% |
| snake_abs | -3,525 | -1.63% |

Average per day so far: unified Rs +602, benchmark Rs +587, snake_abs_exit Rs +555, snake_abs_exit_conv Rs +543, intraweek Rs +472, snake_abs_conv Rs +401, snake_abs Rs +393, oracle Rs +389, intramonth Rs +319, snake_viper_wild Rs +221, random_hold Rs +214, snake_anaconda Rs +156, snake_viper_tick Rs +91, benchmark_smallcap Rs +91, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -489

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.