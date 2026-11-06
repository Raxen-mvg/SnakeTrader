# Paper trading report

Updated 2026-11-06 14:01 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 216,332 | +8.17% | 0 | - | 237 |
| unified | 215,011 | +7.51% | 0 | - | 236 |
| snake_abs_exit_conv | 208,566 | +4.28% | 1 | 100% | 255 |
| snake_abs_exit | 208,473 | +4.24% | 1 | 100% | 260 |
| intraweek | 208,111 | +4.06% | 25 | 48% | 2,757 |
| intramonth | 207,333 | +3.67% | 0 | - | 235 |
| snake_abs | 205,554 | +2.78% | 1 | 100% | 255 |
| oracle | 205,476 | +2.74% | 0 | - | 233 |
| snake_abs_conv | 205,368 | +2.68% | 1 | 100% | 255 |
| random_hold | 203,531 | +1.76% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,228 | -1.89% | 3 | 33% | 702 |
| snake_anaconda | 195,917 | -2.04% | 3 | 33% | 374 |
| benchmark_smallcap | 195,403 | -2.30% | 0 | - | 237 |
| snake_viper_tick | 192,901 | -3.55% | 2 | 0% | 532 |
| gold | 190,720 | -4.64% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,970 (-6.51%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,563 | +1.20% |
| oracle | +1,404 | +0.69% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -616 | -0.30% |
| random_hold | -792 | -0.39% |
| unified | -972 | -0.45% |
| intraweek | -1,307 | -0.62% |
| benchmark_smallcap | -3,285 | -1.65% |
| gold | -3,502 | -1.80% |
| snake_abs | -6,135 | -2.90% |
| snake_abs_conv | -6,177 | -2.92% |
| snake_abs_exit | -6,186 | -2.88% |
| snake_abs_exit_conv | -6,238 | -2.90% |
| snake_anaconda | -6,562 | -3.24% |
| snake_viper_tick | -8,237 | -4.09% |
| snake_viper_wild | -8,428 | -4.12% |

Average per day so far: benchmark Rs +563, unified Rs +518, snake_abs_exit_conv Rs +329, snake_abs_exit Rs +326, intraweek Rs +280, intramonth Rs +253, snake_abs_conv Rs +206, snake_abs Rs +206, oracle Rs +189, random_hold Rs +122, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -170, snake_viper_wild Rs -180, benchmark_smallcap Rs -184, gold Rs -320, snake_viper_tick Rs -394, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.