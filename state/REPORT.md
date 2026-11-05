# Paper trading report

Updated 2026-11-05 14:43 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 216,107 | +8.05% | 0 | - | 236 |
| snake_abs_exit_conv | 214,917 | +7.46% | 1 | 100% | 255 |
| snake_abs_exit | 214,621 | +7.31% | 1 | 100% | 260 |
| benchmark | 213,992 | +7.00% | 0 | - | 237 |
| snake_abs | 211,800 | +5.90% | 1 | 100% | 255 |
| snake_abs_conv | 211,655 | +5.83% | 1 | 100% | 255 |
| intraweek | 209,999 | +5.00% | 25 | 48% | 2,757 |
| intramonth | 207,944 | +3.97% | 0 | - | 235 |
| snake_viper_wild | 205,429 | +2.71% | 3 | 33% | 702 |
| random_hold | 204,691 | +2.35% | 8 | 62% | 649 |
| oracle | 204,302 | +2.15% | 0 | - | 233 |
| snake_anaconda | 202,439 | +1.22% | 3 | 33% | 374 |
| snake_viper_tick | 201,899 | +0.95% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,103 | -0.45% | 0 | - | 237 |
| gold | 194,386 | -2.81% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,670 (-5.17%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,233 | +2.51% |
| gold | +2,992 | +1.56% |
| oracle | +2,510 | +1.24% |
| benchmark_smallcap | +2,433 | +1.24% |
| unified | +1,668 | +0.78% |
| random_hold | +1,382 | +0.68% |
| intramonth | +928 | +0.45% |
| intraweek | +301 | +0.14% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -98 | -0.05% |
| snake_abs_conv | -103 | -0.05% |
| snake_abs | -104 | -0.05% |
| snake_abs_exit | -279 | -0.13% |
| snake_anaconda | -1,382 | -0.68% |
| snake_viper_tick | -3,502 | -1.71% |
| snake_viper_wild | -3,601 | -1.72% |

Average per day so far: snake_abs_exit_conv Rs +597, snake_abs_exit Rs +585, unified Rs +575, benchmark Rs +500, snake_abs_conv Rs +466, snake_abs Rs +454, intraweek Rs +357, intramonth Rs +284, snake_viper_wild Rs +271, random_hold Rs +168, oracle Rs +154, snake_viper_tick Rs +112, snake_anaconda Rs +106, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -37, gold Rs -201, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.