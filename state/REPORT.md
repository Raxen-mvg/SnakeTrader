# Paper trading report

Updated 2026-11-13 13:55 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,188 | +10.09% | 0 | - | 236 |
| benchmark | 219,125 | +9.56% | 0 | - | 237 |
| snake_abs_exit | 216,327 | +8.16% | 2 | 50% | 345 |
| snake_abs_exit_conv | 215,950 | +7.97% | 2 | 50% | 345 |
| intraweek | 215,770 | +7.88% | 30 | 53% | 3,302 |
| oracle | 212,852 | +6.43% | 0 | - | 233 |
| snake_abs | 212,061 | +6.03% | 1 | 100% | 255 |
| snake_abs_conv | 211,892 | +5.95% | 1 | 100% | 255 |
| intramonth | 210,908 | +5.45% | 0 | - | 235 |
| random_hold | 207,154 | +3.58% | 10 | 70% | 733 |
| snake_viper_wild | 205,464 | +2.73% | 14 | 50% | 2,496 |
| snake_anaconda | 204,207 | +2.10% | 3 | 33% | 374 |
| benchmark_smallcap | 202,331 | +1.17% | 0 | - | 237 |
| snake_viper_tick | 201,950 | +0.97% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,700 | -8.15% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,676 (-4.16%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,112 | +0.52% |
| snake_viper_wild | +171 | +0.08% |
| snake_viper_tick | +169 | +0.08% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -263 | -0.12% |
| unified | -509 | -0.23% |
| intramonth | -685 | -0.32% |
| benchmark_smallcap | -874 | -0.43% |
| random_hold | -899 | -0.43% |
| snake_abs_exit | -1,115 | -0.51% |
| benchmark | -1,423 | -0.65% |
| gold | -1,611 | -0.87% |
| snake_anaconda | -1,720 | -0.83% |
| snake_abs_exit_conv | -2,724 | -1.25% |
| snake_abs_conv | -3,643 | -1.69% |
| snake_abs | -3,650 | -1.69% |

Average per day so far: unified Rs +612, benchmark Rs +580, snake_abs_exit Rs +544, snake_abs_exit_conv Rs +532, intraweek Rs +478, snake_abs_conv Rs +396, oracle Rs +389, snake_abs Rs +389, intramonth Rs +331, snake_viper_wild Rs +219, random_hold Rs +217, snake_anaconda Rs +150, snake_viper_tick Rs +89, benchmark_smallcap Rs +80, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -494

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.