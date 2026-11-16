# Paper trading report

Updated 2026-11-16 09:32 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,372 | +10.19% | 0 | - | 237 |
| unified | 219,595 | +9.80% | 0 | - | 236 |
| snake_abs_exit | 215,182 | +7.59% | 2 | 50% | 345 |
| intraweek | 214,771 | +7.38% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 213,779 | +6.89% | 2 | 50% | 345 |
| oracle | 213,560 | +6.78% | 0 | - | 233 |
| snake_abs | 210,862 | +5.43% | 1 | 100% | 255 |
| snake_abs_conv | 210,698 | +5.35% | 1 | 100% | 255 |
| intramonth | 210,485 | +5.24% | 0 | - | 235 |
| random_hold | 207,458 | +3.73% | 10 | 70% | 733 |
| snake_anaconda | 205,092 | +2.55% | 3 | 33% | 374 |
| snake_viper_wild | 204,046 | +2.02% | 14 | 50% | 2,496 |
| benchmark_smallcap | 201,849 | +0.93% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 200,557 | +0.28% | 13 | 46% | 2,299 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 182,467 | -8.77% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,429 (-4.29%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,033 | +0.47% |
| unified | +575 | +0.26% |
| oracle | +462 | +0.22% |
| intramonth | +428 | +0.20% |
| random_hold | +232 | +0.11% |
| snake_anaconda | +200 | +0.10% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_viper_tick | -698 | -0.35% |
| snake_viper_wild | -711 | -0.35% |
| benchmark_smallcap | -1,020 | -0.50% |
| intraweek | -1,374 | -0.64% |
| gold | -1,529 | -0.83% |
| snake_abs_conv | -1,669 | -0.79% |
| snake_abs | -1,678 | -0.79% |
| snake_abs_exit | -1,803 | -0.83% |
| snake_abs_exit_conv | -2,602 | -1.20% |

Average per day so far: benchmark Rs +599, unified Rs +576, snake_abs_exit Rs +490, snake_abs_exit_conv Rs +444, intraweek Rs +434, oracle Rs +399, snake_abs_conv Rs +345, snake_abs Rs +339, intramonth Rs +308, random_hold Rs +219, snake_anaconda Rs +176, snake_viper_wild Rs +156, benchmark_smallcap Rs +62, nifty_calls Rs +54, snake_viper_tick Rs +24, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -347, snake Rs -368, gold Rs -516

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.