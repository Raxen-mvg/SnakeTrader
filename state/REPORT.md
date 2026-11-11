# Paper trading report

Updated 2026-11-11 10:10 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,884 | +10.44% | 0 | - | 237 |
| unified | 220,400 | +10.20% | 0 | - | 236 |
| snake_abs_exit_conv | 216,585 | +8.29% | 2 | 50% | 345 |
| intraweek | 215,126 | +7.56% | 30 | 53% | 3,302 |
| snake_abs_exit | 214,733 | +7.37% | 2 | 50% | 345 |
| snake_abs | 213,180 | +6.59% | 1 | 100% | 255 |
| snake_abs_conv | 213,021 | +6.51% | 1 | 100% | 255 |
| oracle | 211,344 | +5.67% | 0 | - | 233 |
| intramonth | 210,926 | +5.46% | 0 | - | 235 |
| random_hold | 206,346 | +3.17% | 9 | 67% | 709 |
| snake_anaconda | 202,782 | +1.39% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,502 | +0.75% | 0 | - | 237 |
| snake_viper_wild | 200,385 | +0.19% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 196,983 | -1.51% | 9 | 44% | 1,639 |
| gold | 189,141 | -5.43% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,290 (-4.36%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,676 | +2.21% |
| snake_abs_conv | +3,543 | +1.69% |
| snake_abs | +3,533 | +1.69% |
| benchmark_smallcap | +3,329 | +1.68% |
| snake_anaconda | +3,316 | +1.66% |
| snake_viper_wild | +2,955 | +1.50% |
| snake_viper_tick | +2,907 | +1.50% |
| benchmark | +2,792 | +1.28% |
| snake_abs_exit | +2,749 | +1.30% |
| oracle | +1,425 | +0.68% |
| random_hold | +1,386 | +0.68% |
| unified | +653 | +0.30% |
| intraweek | +584 | +0.27% |
| intramonth | +317 | +0.15% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -2,992 | -1.56% |

Average per day so far: benchmark Rs +674, unified Rs +658, snake_abs_exit_conv Rs +592, snake_abs_exit Rs +526, intraweek Rs +488, snake_abs_conv Rs +465, snake_abs Rs +454, oracle Rs +366, intramonth Rs +352, random_hold Rs +205, snake_anaconda Rs +107, nifty_calls Rs +59, benchmark_smallcap Rs +56, snake_viper_wild Rs +17, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -151, gold Rs -350, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.