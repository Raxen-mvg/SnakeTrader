# Paper trading report

Updated 2026-11-06 10:38 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 214,948 | +7.47% | 0 | - | 237 |
| unified | 214,640 | +7.32% | 0 | - | 236 |
| intraweek | 210,423 | +5.21% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,533 | +4.77% | 1 | 100% | 255 |
| snake_abs_exit | 209,328 | +4.66% | 1 | 100% | 260 |
| intramonth | 206,607 | +3.30% | 0 | - | 235 |
| snake_abs | 206,485 | +3.24% | 1 | 100% | 255 |
| snake_abs_conv | 206,316 | +3.16% | 1 | 100% | 255 |
| oracle | 204,722 | +2.36% | 0 | - | 233 |
| random_hold | 203,228 | +1.61% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 197,719 | -1.14% | 3 | 33% | 702 |
| snake_anaconda | 196,685 | -1.66% | 3 | 33% | 374 |
| benchmark_smallcap | 194,989 | -2.51% | 0 | - | 237 |
| snake_viper_tick | 194,360 | -2.82% | 2 | 0% | 532 |
| gold | 190,210 | -4.89% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,324 (-6.34%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,178 | +0.55% |
| intraweek | +1,005 | +0.48% |
| oracle | +650 | +0.32% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -1,096 | -0.54% |
| intramonth | -1,342 | -0.65% |
| unified | -1,343 | -0.62% |
| benchmark_smallcap | -3,699 | -1.86% |
| gold | -4,011 | -2.06% |
| snake_abs | -5,203 | -2.46% |
| snake_abs_conv | -5,229 | -2.47% |
| snake_abs_exit_conv | -5,271 | -2.45% |
| snake_abs_exit | -5,331 | -2.48% |
| snake_anaconda | -5,794 | -2.86% |
| snake_viper_tick | -6,778 | -3.37% |
| snake_viper_wild | -6,937 | -3.39% |

Average per day so far: benchmark Rs +515, unified Rs +505, snake_abs_exit_conv Rs +367, intraweek Rs +359, snake_abs_exit Rs +359, snake_abs_conv Rs +243, snake_abs Rs +240, intramonth Rs +228, oracle Rs +163, random_hold Rs +111, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -109, snake_anaconda Rs -138, benchmark_smallcap Rs -200, snake_viper_tick Rs -313, gold Rs -338, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.