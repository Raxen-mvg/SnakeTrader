# Paper trading report

Updated 2026-11-05 10:07 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,670 | +9.34% | 0 | - | 236 |
| snake_abs_exit_conv | 215,848 | +7.92% | 1 | 100% | 255 |
| snake_abs_exit | 215,596 | +7.80% | 1 | 100% | 260 |
| snake_abs | 212,730 | +6.37% | 1 | 100% | 255 |
| snake_abs_conv | 212,575 | +6.29% | 1 | 100% | 255 |
| benchmark | 212,454 | +6.23% | 0 | - | 237 |
| intraweek | 210,587 | +5.29% | 25 | 48% | 2,757 |
| intramonth | 210,488 | +5.24% | 0 | - | 235 |
| random_hold | 206,402 | +3.20% | 8 | 62% | 649 |
| snake_viper_wild | 206,050 | +3.02% | 3 | 33% | 702 |
| oracle | 204,464 | +2.23% | 0 | - | 233 |
| snake_anaconda | 202,907 | +1.45% | 3 | 33% | 374 |
| snake_viper_tick | 202,522 | +1.26% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,338 | -0.33% | 0 | - | 237 |
| gold | 195,060 | -2.47% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,633 (-4.68%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +4,231 | +1.97% |
| benchmark | +3,695 | +1.77% |
| gold | +3,666 | +1.92% |
| intramonth | +3,472 | +1.68% |
| random_hold | +3,093 | +1.52% |
| oracle | +2,672 | +1.32% |
| benchmark_smallcap | +2,668 | +1.36% |
| intraweek | +889 | +0.42% |
| snake_abs_exit_conv | +833 | +0.39% |
| snake_abs | +827 | +0.39% |
| snake_abs_conv | +817 | +0.39% |
| snake_abs_exit | +696 | +0.32% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_anaconda | -913 | -0.45% |
| snake_viper_tick | -2,878 | -1.40% |
| snake_viper_wild | -2,980 | -1.43% |

Average per day so far: unified Rs +667, snake_abs_exit_conv Rs +634, snake_abs_exit Rs +624, snake_abs_conv Rs +503, snake_abs Rs +490, benchmark Rs +445, intraweek Rs +378, intramonth Rs +375, snake_viper_wild Rs +302, random_hold Rs +229, oracle Rs +159, snake_viper_tick Rs +148, snake_anaconda Rs +126, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -28, gold Rs -176, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.