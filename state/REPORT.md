# Paper trading report

Updated 2026-11-13 13:10 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,100 | +10.05% | 0 | - | 236 |
| benchmark | 219,316 | +9.66% | 0 | - | 237 |
| snake_abs_exit | 216,684 | +8.34% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,321 | +8.16% | 2 | 50% | 345 |
| intraweek | 215,574 | +7.79% | 30 | 53% | 3,302 |
| oracle | 212,828 | +6.41% | 0 | - | 233 |
| snake_abs | 212,154 | +6.08% | 1 | 100% | 255 |
| snake_abs_conv | 211,984 | +5.99% | 1 | 100% | 255 |
| intramonth | 210,609 | +5.30% | 0 | - | 235 |
| random_hold | 207,148 | +3.57% | 10 | 70% | 733 |
| snake_viper_wild | 205,530 | +2.77% | 14 | 50% | 2,496 |
| snake_anaconda | 204,315 | +2.16% | 3 | 33% | 374 |
| benchmark_smallcap | 202,690 | +1.34% | 0 | - | 237 |
| snake_viper_tick | 202,015 | +1.01% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,815 | -8.09% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,589 (-4.21%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +916 | +0.43% |
| snake_viper_wild | +237 | +0.12% |
| snake_viper_tick | +233 | +0.12% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -287 | -0.14% |
| benchmark_smallcap | -516 | -0.25% |
| unified | -597 | -0.27% |
| snake_abs_exit | -759 | -0.35% |
| random_hold | -906 | -0.44% |
| intramonth | -984 | -0.47% |
| benchmark | -1,232 | -0.56% |
| gold | -1,496 | -0.81% |
| snake_anaconda | -1,612 | -0.78% |
| snake_abs_exit_conv | -2,353 | -1.08% |
| snake_abs_conv | -3,551 | -1.65% |
| snake_abs | -3,557 | -1.65% |

Average per day so far: unified Rs +609, benchmark Rs +585, snake_abs_exit Rs +556, snake_abs_exit_conv Rs +544, intraweek Rs +472, snake_abs_conv Rs +399, snake_abs Rs +392, oracle Rs +389, intramonth Rs +321, snake_viper_wild Rs +221, random_hold Rs +217, snake_anaconda Rs +154, benchmark_smallcap Rs +93, snake_viper_tick Rs +92, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -490

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.