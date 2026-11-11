# Paper trading report

Updated 2026-11-11 11:07 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,358 | +10.68% | 0 | - | 237 |
| unified | 220,815 | +10.41% | 0 | - | 236 |
| snake_abs_exit_conv | 215,984 | +7.99% | 2 | 50% | 345 |
| intraweek | 214,624 | +7.31% | 30 | 53% | 3,302 |
| snake_abs_exit | 214,580 | +7.29% | 2 | 50% | 345 |
| snake_abs | 212,334 | +6.17% | 1 | 100% | 255 |
| snake_abs_conv | 212,183 | +6.09% | 1 | 100% | 255 |
| oracle | 211,978 | +5.99% | 0 | - | 233 |
| intramonth | 211,617 | +5.81% | 0 | - | 235 |
| random_hold | 206,851 | +3.43% | 9 | 67% | 709 |
| snake_anaconda | 202,351 | +1.18% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,804 | +0.90% | 0 | - | 237 |
| snake_viper_wild | 200,735 | +0.37% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 197,326 | -1.34% | 9 | 44% | 1,639 |
| gold | 189,898 | -5.05% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,423 (-4.29%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,075 | +1.92% |
| benchmark_smallcap | +3,632 | +1.83% |
| snake_viper_wild | +3,305 | +1.67% |
| benchmark | +3,267 | +1.50% |
| snake_viper_tick | +3,249 | +1.67% |
| snake_anaconda | +2,884 | +1.45% |
| snake_abs_conv | +2,705 | +1.29% |
| snake_abs | +2,687 | +1.28% |
| snake_abs_exit | +2,596 | +1.23% |
| oracle | +2,060 | +0.98% |
| random_hold | +1,891 | +0.92% |
| unified | +1,068 | +0.49% |
| intramonth | +1,008 | +0.48% |
| intraweek | +82 | +0.04% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -2,236 | -1.16% |

Average per day so far: benchmark Rs +689, unified Rs +671, snake_abs_exit_conv Rs +571, snake_abs_exit Rs +521, intraweek Rs +472, snake_abs_conv Rs +435, snake_abs Rs +425, oracle Rs +386, intramonth Rs +375, random_hold Rs +221, snake_anaconda Rs +90, benchmark_smallcap Rs +67, nifty_calls Rs +59, snake_viper_wild Rs +32, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -134, gold Rs -326, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.