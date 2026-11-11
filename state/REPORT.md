# Paper trading report

Updated 2026-11-11 14:49 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,276 | +10.14% | 0 | - | 236 |
| benchmark | 219,691 | +9.85% | 0 | - | 237 |
| snake_abs_exit_conv | 217,057 | +8.53% | 2 | 50% | 345 |
| snake_abs_exit | 216,220 | +8.11% | 2 | 50% | 345 |
| snake_abs | 214,007 | +7.00% | 1 | 100% | 255 |
| snake_abs_conv | 213,839 | +6.92% | 1 | 100% | 255 |
| intraweek | 213,192 | +6.60% | 30 | 53% | 3,302 |
| oracle | 211,633 | +5.82% | 0 | - | 233 |
| intramonth | 211,201 | +5.60% | 0 | - | 235 |
| random_hold | 207,139 | +3.57% | 9 | 67% | 709 |
| snake_viper_wild | 206,314 | +3.16% | 10 | 50% | 1,825 |
| snake_anaconda | 203,948 | +1.97% | 3 | 33% | 374 |
| snake_viper_tick | 202,789 | +1.39% | 9 | 44% | 1,639 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,390 | +0.69% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,322 | -5.34% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,113 (-4.44%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +8,884 | +4.50% |
| snake_viper_tick | +8,712 | +4.49% |
| snake_abs_exit_conv | +5,148 | +2.43% |
| snake_anaconda | +4,481 | +2.25% |
| snake_abs_conv | +4,361 | +2.08% |
| snake_abs | +4,361 | +2.08% |
| snake_abs_exit | +4,237 | +2.00% |
| benchmark_smallcap | +3,217 | +1.62% |
| random_hold | +2,179 | +1.06% |
| oracle | +1,714 | +0.82% |
| benchmark | +1,599 | +0.73% |
| intramonth | +592 | +0.28% |
| unified | +529 | +0.24% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -1,350 | -0.63% |
| gold | -2,811 | -1.46% |

Average per day so far: unified Rs +654, benchmark Rs +635, snake_abs_exit_conv Rs +609, snake_abs_exit Rs +579, snake_abs_conv Rs +494, snake_abs Rs +483, intraweek Rs +426, oracle Rs +375, intramonth Rs +361, snake_viper_wild Rs +275, random_hold Rs +230, snake_anaconda Rs +152, snake_viper_tick Rs +139, nifty_calls Rs +59, benchmark_smallcap Rs +51, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -344, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.