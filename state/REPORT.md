# Paper trading report

Updated 2026-11-06 14:10 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 216,126 | +8.06% | 0 | - | 237 |
| unified | 215,149 | +7.58% | 0 | - | 236 |
| intraweek | 208,588 | +4.29% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,419 | +4.21% | 1 | 100% | 255 |
| snake_abs_exit | 208,316 | +4.16% | 1 | 100% | 260 |
| intramonth | 207,427 | +3.71% | 0 | - | 235 |
| oracle | 205,482 | +2.74% | 0 | - | 233 |
| snake_abs | 205,404 | +2.70% | 1 | 100% | 255 |
| snake_abs_conv | 205,220 | +2.61% | 1 | 100% | 255 |
| random_hold | 203,368 | +1.68% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,162 | -1.92% | 3 | 33% | 702 |
| snake_anaconda | 195,750 | -2.12% | 3 | 33% | 374 |
| benchmark_smallcap | 195,258 | -2.37% | 0 | - | 237 |
| snake_viper_tick | 192,836 | -3.58% | 2 | 0% | 532 |
| gold | 190,900 | -4.55% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,003 (-6.50%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,356 | +1.10% |
| oracle | +1,410 | +0.69% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -522 | -0.25% |
| intraweek | -831 | -0.40% |
| unified | -834 | -0.39% |
| random_hold | -956 | -0.47% |
| gold | -3,321 | -1.71% |
| benchmark_smallcap | -3,430 | -1.73% |
| snake_abs | -6,284 | -2.97% |
| snake_abs_conv | -6,325 | -2.99% |
| snake_abs_exit | -6,342 | -2.96% |
| snake_abs_exit_conv | -6,384 | -2.97% |
| snake_anaconda | -6,729 | -3.32% |
| snake_viper_tick | -8,302 | -4.13% |
| snake_viper_wild | -8,494 | -4.15% |

Average per day so far: benchmark Rs +556, unified Rs +522, snake_abs_exit_conv Rs +324, snake_abs_exit Rs +320, intraweek Rs +296, intramonth Rs +256, snake_abs_conv Rs +201, snake_abs Rs +200, oracle Rs +189, random_hold Rs +116, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -177, snake_viper_wild Rs -183, benchmark_smallcap Rs -190, gold Rs -314, snake_viper_tick Rs -398, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.