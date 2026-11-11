# Paper trading report

Updated 2026-11-11 13:48 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,477 | +10.24% | 0 | - | 236 |
| benchmark | 219,783 | +9.89% | 0 | - | 237 |
| snake_abs_exit_conv | 217,465 | +8.73% | 2 | 50% | 345 |
| snake_abs_exit | 216,528 | +8.26% | 2 | 50% | 345 |
| snake_abs | 213,867 | +6.93% | 1 | 100% | 255 |
| snake_abs_conv | 213,714 | +6.86% | 1 | 100% | 255 |
| intraweek | 213,356 | +6.68% | 30 | 53% | 3,302 |
| oracle | 211,690 | +5.84% | 0 | - | 233 |
| intramonth | 211,351 | +5.67% | 0 | - | 235 |
| random_hold | 206,899 | +3.45% | 9 | 67% | 709 |
| snake_viper_wild | 205,141 | +2.57% | 10 | 50% | 1,825 |
| snake_anaconda | 204,267 | +2.13% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,641 | +0.82% | 9 | 44% | 1,639 |
| benchmark_smallcap | 200,840 | +0.42% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,815 | -5.09% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,204 (-4.40%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +7,711 | +3.90% |
| snake_viper_tick | +7,565 | +3.90% |
| snake_abs_exit_conv | +5,556 | +2.62% |
| snake_anaconda | +4,800 | +2.41% |
| snake_abs_exit | +4,544 | +2.14% |
| snake_abs_conv | +4,236 | +2.02% |
| snake_abs | +4,220 | +2.01% |
| benchmark_smallcap | +2,668 | +1.35% |
| random_hold | +1,939 | +0.95% |
| oracle | +1,772 | +0.84% |
| benchmark | +1,691 | +0.78% |
| intramonth | +742 | +0.35% |
| unified | +730 | +0.33% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -1,186 | -0.55% |
| gold | -2,318 | -1.21% |

Average per day so far: unified Rs +661, benchmark Rs +638, snake_abs_exit_conv Rs +624, snake_abs_exit Rs +590, snake_abs_conv Rs +490, snake_abs Rs +478, intraweek Rs +431, oracle Rs +377, intramonth Rs +366, snake_viper_wild Rs +224, random_hold Rs +223, snake_anaconda Rs +164, snake_viper_tick Rs +82, nifty_calls Rs +59, benchmark_smallcap Rs +31, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -329, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.