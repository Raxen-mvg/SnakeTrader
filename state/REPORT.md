# Paper trading report

Updated 2026-11-19 14:19 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,494 | +11.75% | 0 | - | 236 |
| benchmark | 222,276 | +11.14% | 0 | - | 237 |
| snake_abs_exit | 213,171 | +6.59% | 2 | 50% | 345 |
| intramonth | 213,116 | +6.56% | 0 | - | 235 |
| intraweek | 211,879 | +5.94% | 35 | 54% | 3,851 |
| oracle | 211,279 | +5.64% | 0 | - | 233 |
| snake_abs_exit_conv | 210,905 | +5.45% | 2 | 50% | 345 |
| snake_abs | 208,799 | +4.40% | 1 | 100% | 255 |
| snake_abs_conv | 208,674 | +4.34% | 1 | 100% | 255 |
| random_hold | 207,931 | +3.96% | 10 | 70% | 733 |
| snake_viper_wild | 207,576 | +3.79% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,029 | +2.01% | 15 | 47% | 2,625 |
| snake_anaconda | 203,298 | +1.65% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,672 | +0.34% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,822 | -12.59% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,198 (-4.40%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,981 | +0.90% |
| benchmark_smallcap | +1,345 | +0.68% |
| random_hold | +998 | +0.48% |
| unified | +882 | +0.40% |
| intramonth | +842 | +0.40% |
| snake_viper_wild | +536 | +0.26% |
| snake_viper_tick | +525 | +0.26% |
| oracle | +483 | +0.23% |
| intraweek | +39 | +0.02% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -637 | -0.30% |
| snake_abs_conv | -651 | -0.31% |
| snake_abs_exit | -861 | -0.40% |
| snake_anaconda | -1,103 | -0.54% |
| snake_abs_exit_conv | -1,478 | -0.70% |
| gold | -2,499 | -1.41% |

Average per day so far: unified Rs +635, benchmark Rs +602, snake_abs_exit Rs +387, intramonth Rs +354, intraweek Rs +321, snake_abs_exit_conv Rs +321, oracle Rs +305, snake_viper_wild Rs +261, snake_abs_conv Rs +255, snake_abs Rs +251, random_hold Rs +214, snake_viper_tick Rs +155, snake_anaconda Rs +103, nifty_calls Rs +50, benchmark_smallcap Rs +20, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -680

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.