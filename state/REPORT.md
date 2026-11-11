# Paper trading report

Updated 2026-11-11 10:22 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,984 | +10.49% | 0 | - | 237 |
| unified | 220,234 | +10.12% | 0 | - | 236 |
| snake_abs_exit_conv | 216,297 | +8.15% | 2 | 50% | 345 |
| snake_abs_exit | 214,739 | +7.37% | 2 | 50% | 345 |
| intraweek | 214,536 | +7.27% | 30 | 53% | 3,302 |
| snake_abs | 212,913 | +6.46% | 1 | 100% | 255 |
| snake_abs_conv | 212,761 | +6.38% | 1 | 100% | 255 |
| oracle | 211,386 | +5.69% | 0 | - | 233 |
| intramonth | 210,816 | +5.41% | 0 | - | 235 |
| random_hold | 206,306 | +3.15% | 9 | 67% | 709 |
| snake_anaconda | 202,732 | +1.37% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,546 | +0.77% | 0 | - | 237 |
| snake_viper_wild | 200,123 | +0.06% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 196,726 | -1.64% | 9 | 44% | 1,639 |
| gold | 189,487 | -5.26% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,108 (-4.45%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,388 | +2.07% |
| benchmark_smallcap | +3,374 | +1.70% |
| snake_abs_conv | +3,283 | +1.57% |
| snake_abs | +3,266 | +1.56% |
| snake_anaconda | +3,266 | +1.64% |
| benchmark | +2,892 | +1.33% |
| snake_abs_exit | +2,756 | +1.30% |
| snake_viper_wild | +2,693 | +1.36% |
| snake_viper_tick | +2,650 | +1.36% |
| oracle | +1,467 | +0.70% |
| random_hold | +1,345 | +0.66% |
| unified | +487 | +0.22% |
| intramonth | +207 | +0.10% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -6 | -0.00% |
| gold | -2,647 | -1.38% |

Average per day so far: benchmark Rs +677, unified Rs +653, snake_abs_exit_conv Rs +582, snake_abs_exit Rs +526, intraweek Rs +469, snake_abs_conv Rs +456, snake_abs Rs +445, oracle Rs +367, intramonth Rs +349, random_hold Rs +203, snake_anaconda Rs +105, nifty_calls Rs +59, benchmark_smallcap Rs +57, snake_viper_wild Rs +5, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -164, gold Rs -339, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.