# Paper trading report

Updated 2026-11-13 12:37 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,097 | +10.05% | 0 | - | 236 |
| benchmark | 219,331 | +9.67% | 0 | - | 237 |
| snake_abs_exit_conv | 216,631 | +8.32% | 2 | 50% | 345 |
| snake_abs_exit | 216,542 | +8.27% | 2 | 50% | 345 |
| intraweek | 216,268 | +8.13% | 30 | 53% | 3,302 |
| oracle | 213,257 | +6.63% | 0 | - | 233 |
| snake_abs | 212,806 | +6.40% | 1 | 100% | 255 |
| snake_abs_conv | 212,637 | +6.32% | 1 | 100% | 255 |
| intramonth | 210,607 | +5.30% | 0 | - | 235 |
| random_hold | 207,150 | +3.58% | 10 | 70% | 733 |
| snake_viper_wild | 205,813 | +2.91% | 14 | 50% | 2,496 |
| snake_anaconda | 204,994 | +2.50% | 3 | 33% | 374 |
| benchmark_smallcap | 202,679 | +1.34% | 0 | - | 237 |
| snake_viper_tick | 202,292 | +1.15% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,618 | -8.19% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,870 (-4.07%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,610 | +0.75% |
| snake_viper_wild | +520 | +0.25% |
| snake_viper_tick | +511 | +0.25% |
| oracle | +142 | +0.07% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| benchmark_smallcap | -527 | -0.26% |
| unified | -600 | -0.27% |
| snake_abs_exit | -900 | -0.41% |
| random_hold | -904 | -0.43% |
| snake_anaconda | -933 | -0.45% |
| intramonth | -986 | -0.47% |
| benchmark | -1,216 | -0.55% |
| gold | -1,693 | -0.91% |
| snake_abs_exit_conv | -2,043 | -0.93% |
| snake_abs_conv | -2,898 | -1.34% |
| snake_abs | -2,906 | -1.35% |

Average per day so far: unified Rs +609, benchmark Rs +586, snake_abs_exit_conv Rs +554, snake_abs_exit Rs +551, intraweek Rs +493, snake_abs_conv Rs +421, snake_abs Rs +413, oracle Rs +402, intramonth Rs +321, snake_viper_wild Rs +233, random_hold Rs +217, snake_anaconda Rs +178, snake_viper_tick Rs +104, benchmark_smallcap Rs +92, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -496

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.