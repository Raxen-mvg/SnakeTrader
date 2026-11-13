# Paper trading report

Updated 2026-11-13 13:58 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,033 | +10.02% | 0 | - | 236 |
| benchmark | 219,117 | +9.56% | 0 | - | 237 |
| snake_abs_exit | 216,436 | +8.22% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,093 | +8.05% | 2 | 50% | 345 |
| intraweek | 215,815 | +7.91% | 30 | 53% | 3,302 |
| oracle | 212,886 | +6.44% | 0 | - | 233 |
| snake_abs | 212,231 | +6.12% | 1 | 100% | 255 |
| snake_abs_conv | 212,065 | +6.03% | 1 | 100% | 255 |
| intramonth | 210,750 | +5.38% | 0 | - | 235 |
| random_hold | 207,045 | +3.52% | 10 | 70% | 733 |
| snake_viper_wild | 205,778 | +2.89% | 14 | 50% | 2,496 |
| snake_anaconda | 204,456 | +2.23% | 3 | 33% | 374 |
| benchmark_smallcap | 202,309 | +1.15% | 0 | - | 237 |
| snake_viper_tick | 202,259 | +1.13% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,766 | -8.12% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,650 (-4.18%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,157 | +0.54% |
| snake_viper_wild | +485 | +0.24% |
| snake_viper_tick | +477 | +0.24% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -230 | -0.11% |
| unified | -663 | -0.30% |
| intramonth | -843 | -0.40% |
| benchmark_smallcap | -897 | -0.44% |
| snake_abs_exit | -1,006 | -0.46% |
| random_hold | -1,009 | -0.48% |
| benchmark | -1,431 | -0.65% |
| snake_anaconda | -1,471 | -0.71% |
| gold | -1,545 | -0.83% |
| snake_abs_exit_conv | -2,581 | -1.18% |
| snake_abs_conv | -3,470 | -1.61% |
| snake_abs | -3,480 | -1.61% |

Average per day so far: unified Rs +607, benchmark Rs +579, snake_abs_exit Rs +548, snake_abs_exit_conv Rs +536, intraweek Rs +479, snake_abs_conv Rs +402, snake_abs Rs +395, oracle Rs +390, intramonth Rs +326, snake_viper_wild Rs +231, random_hold Rs +213, snake_anaconda Rs +159, snake_viper_tick Rs +103, benchmark_smallcap Rs +80, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -492

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.