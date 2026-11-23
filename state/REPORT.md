# Paper trading report

Updated 2026-11-23 10:49 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,589 | +12.29% | 0 | - | 236 |
| benchmark | 223,439 | +11.72% | 0 | - | 237 |
| intraweek | 212,684 | +6.34% | 40 | 55% | 4,400 |
| intramonth | 212,526 | +6.26% | 0 | - | 235 |
| oracle | 211,284 | +5.64% | 0 | - | 233 |
| random_hold | 209,883 | +4.94% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,737 | +3.37% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,699 | +2.85% | 2 | 50% | 345 |
| snake_abs | 204,182 | +2.09% | 1 | 100% | 255 |
| snake_abs_conv | 204,029 | +2.01% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,164 | +0.08% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,428 | -0.29% | 0 | - | 237 |
| snake_anaconda | 197,767 | -1.12% | 3 | 33% | 374 |
| snake_viper_tick | 196,753 | -1.62% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,545 | -15.23% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,342 (-4.83%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,496 | +0.89% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -876 | -0.42% |
| snake_abs_exit_conv | -917 | -0.44% |
| oracle | -1,194 | -0.56% |
| benchmark_smallcap | -1,480 | -0.74% |
| unified | -1,592 | -0.70% |
| benchmark | -1,698 | -0.75% |
| snake_abs | -1,738 | -0.84% |
| snake_abs_conv | -1,754 | -0.85% |
| snake_abs_exit | -1,825 | -0.88% |
| snake_anaconda | -2,138 | -1.07% |
| intramonth | -2,478 | -1.15% |
| snake_viper_tick | -2,619 | -1.31% |
| snake_viper_wild | -2,665 | -1.31% |
| intraweek | -3,028 | -1.40% |

Average per day so far: unified Rs +630, benchmark Rs +601, intraweek Rs +325, intramonth Rs +321, oracle Rs +289, random_hold Rs +253, snake_abs_exit Rs +187, snake_abs_exit_conv Rs +158, snake_abs Rs +113, snake_abs_conv Rs +112, nifty_calls Rs +47, snake_viper_wild Rs +5, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -16, snake_anaconda Rs -66, snake_viper_tick Rs -116, snake_nonews Rs -300, snake Rs -320, gold Rs -781

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.