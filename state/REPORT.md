# Paper trading report

Updated 2026-11-06 13:04 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,131 | +7.57% | 0 | - | 237 |
| unified | 214,520 | +7.26% | 0 | - | 236 |
| snake_abs_exit_conv | 208,451 | +4.22% | 1 | 100% | 255 |
| intraweek | 208,307 | +4.15% | 25 | 48% | 2,757 |
| snake_abs_exit | 208,300 | +4.15% | 1 | 100% | 260 |
| intramonth | 206,783 | +3.39% | 0 | - | 235 |
| snake_abs | 205,445 | +2.72% | 1 | 100% | 255 |
| snake_abs_conv | 205,257 | +2.63% | 1 | 100% | 255 |
| oracle | 204,979 | +2.49% | 0 | - | 233 |
| random_hold | 203,206 | +1.60% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,336 | -1.83% | 3 | 33% | 702 |
| snake_anaconda | 195,901 | -2.05% | 3 | 33% | 374 |
| benchmark_smallcap | 194,641 | -2.68% | 0 | - | 237 |
| snake_viper_tick | 193,012 | -3.49% | 2 | 0% | 532 |
| gold | 189,931 | -5.04% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,755 (-6.62%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,362 | +0.64% |
| oracle | +907 | +0.44% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -1,112 | -0.53% |
| random_hold | -1,117 | -0.55% |
| intramonth | -1,166 | -0.56% |
| unified | -1,464 | -0.68% |
| benchmark_smallcap | -4,047 | -2.04% |
| gold | -4,291 | -2.21% |
| snake_abs | -6,243 | -2.95% |
| snake_abs_conv | -6,287 | -2.97% |
| snake_abs_exit_conv | -6,352 | -2.96% |
| snake_abs_exit | -6,359 | -2.96% |
| snake_anaconda | -6,579 | -3.25% |
| snake_viper_tick | -8,126 | -4.04% |
| snake_viper_wild | -8,320 | -4.07% |

Average per day so far: benchmark Rs +522, unified Rs +501, snake_abs_exit_conv Rs +325, snake_abs_exit Rs +319, intraweek Rs +286, intramonth Rs +234, snake_abs_conv Rs +202, snake_abs Rs +202, oracle Rs +172, random_hold Rs +111, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -171, snake_viper_wild Rs -174, benchmark_smallcap Rs -214, gold Rs -347, snake_viper_tick Rs -388, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.