# Paper trading report

Updated 2026-11-11 11:16 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,297 | +10.65% | 0 | - | 237 |
| unified | 220,428 | +10.21% | 0 | - | 236 |
| snake_abs_exit_conv | 216,196 | +8.10% | 2 | 50% | 345 |
| snake_abs_exit | 214,784 | +7.39% | 2 | 50% | 345 |
| intraweek | 214,017 | +7.01% | 30 | 53% | 3,302 |
| snake_abs | 213,042 | +6.52% | 1 | 100% | 255 |
| snake_abs_conv | 212,885 | +6.44% | 1 | 100% | 255 |
| oracle | 211,666 | +5.83% | 0 | - | 233 |
| intramonth | 211,245 | +5.62% | 0 | - | 235 |
| random_hold | 206,753 | +3.38% | 9 | 67% | 709 |
| snake_anaconda | 202,723 | +1.36% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,782 | +0.89% | 0 | - | 237 |
| snake_viper_wild | 200,880 | +0.44% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 197,469 | -1.27% | 9 | 44% | 1,639 |
| gold | 189,865 | -5.07% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,179 (-4.41%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,287 | +2.02% |
| benchmark_smallcap | +3,610 | +1.82% |
| snake_viper_wild | +3,450 | +1.75% |
| snake_abs_conv | +3,407 | +1.63% |
| snake_abs | +3,396 | +1.62% |
| snake_viper_tick | +3,392 | +1.75% |
| snake_anaconda | +3,256 | +1.63% |
| benchmark | +3,205 | +1.47% |
| snake_abs_exit | +2,800 | +1.32% |
| random_hold | +1,793 | +0.88% |
| oracle | +1,748 | +0.83% |
| unified | +681 | +0.31% |
| intramonth | +636 | +0.30% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -525 | -0.24% |
| gold | -2,269 | -1.18% |

Average per day so far: benchmark Rs +687, unified Rs +659, snake_abs_exit_conv Rs +578, snake_abs_exit Rs +528, snake_abs_conv Rs +460, intraweek Rs +452, snake_abs Rs +450, oracle Rs +376, intramonth Rs +363, random_hold Rs +218, snake_anaconda Rs +105, benchmark_smallcap Rs +66, nifty_calls Rs +59, snake_viper_wild Rs +38, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -127, gold Rs -327, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.