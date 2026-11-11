# Paper trading report

Updated 2026-11-11 10:34 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,114 | +10.56% | 0 | - | 237 |
| unified | 220,653 | +10.33% | 0 | - | 236 |
| snake_abs_exit_conv | 215,873 | +7.94% | 2 | 50% | 345 |
| snake_abs_exit | 214,524 | +7.26% | 2 | 50% | 345 |
| intraweek | 214,123 | +7.06% | 30 | 53% | 3,302 |
| snake_abs | 212,743 | +6.37% | 1 | 100% | 255 |
| snake_abs_conv | 212,589 | +6.29% | 1 | 100% | 255 |
| oracle | 211,649 | +5.83% | 0 | - | 233 |
| intramonth | 211,300 | +5.65% | 0 | - | 235 |
| random_hold | 206,394 | +3.20% | 9 | 67% | 709 |
| snake_anaconda | 202,550 | +1.27% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,625 | +0.81% | 0 | - | 237 |
| snake_viper_wild | 200,340 | +0.17% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 196,939 | -1.53% | 9 | 44% | 1,639 |
| gold | 189,454 | -5.27% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,190 (-4.41%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +3,964 | +1.87% |
| benchmark_smallcap | +3,453 | +1.74% |
| snake_abs_conv | +3,111 | +1.49% |
| snake_abs | +3,096 | +1.48% |
| snake_anaconda | +3,084 | +1.55% |
| benchmark | +3,022 | +1.39% |
| snake_viper_wild | +2,910 | +1.47% |
| snake_viper_tick | +2,862 | +1.48% |
| snake_abs_exit | +2,540 | +1.20% |
| oracle | +1,731 | +0.82% |
| random_hold | +1,433 | +0.70% |
| unified | +906 | +0.41% |
| intramonth | +691 | +0.33% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -419 | -0.20% |
| gold | -2,680 | -1.40% |

Average per day so far: benchmark Rs +681, unified Rs +666, snake_abs_exit_conv Rs +567, snake_abs_exit Rs +519, intraweek Rs +456, snake_abs_conv Rs +450, snake_abs Rs +439, oracle Rs +376, intramonth Rs +365, random_hold Rs +206, snake_anaconda Rs +98, benchmark_smallcap Rs +60, nifty_calls Rs +59, snake_viper_wild Rs +15, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -153, gold Rs -340, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.