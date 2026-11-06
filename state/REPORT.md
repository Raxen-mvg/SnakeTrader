# Paper trading report

Updated 2026-11-06 15:30 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 217,488 | +8.74% | 0 | - | 237 |
| unified | 215,609 | +7.80% | 0 | - | 236 |
| intraweek | 210,362 | +5.18% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,422 | +4.21% | 1 | 100% | 255 |
| snake_abs_exit | 208,312 | +4.16% | 1 | 100% | 260 |
| intramonth | 207,603 | +3.80% | 0 | - | 235 |
| oracle | 205,827 | +2.91% | 0 | - | 233 |
| snake_abs | 205,419 | +2.71% | 1 | 100% | 255 |
| snake_abs_conv | 205,227 | +2.61% | 1 | 100% | 255 |
| random_hold | 203,907 | +1.95% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,793 | -1.60% | 0 | - | 237 |
| snake_viper_wild | 196,037 | -1.98% | 4 | 25% | 842 |
| snake_anaconda | 195,827 | -2.09% | 3 | 33% | 374 |
| snake_viper_tick | 192,710 | -3.65% | 3 | 0% | 672 |
| gold | 191,048 | -4.48% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,386 (-6.31%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,718 | +1.74% |
| oracle | +1,755 | +0.86% |
| intraweek | +944 | +0.45% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intramonth | -346 | -0.17% |
| unified | -374 | -0.17% |
| random_hold | -417 | -0.20% |
| benchmark_smallcap | -1,894 | -0.95% |
| gold | -3,173 | -1.63% |
| snake_abs | -6,269 | -2.96% |
| snake_abs_conv | -6,318 | -2.99% |
| snake_abs_exit | -6,347 | -2.96% |
| snake_abs_exit_conv | -6,382 | -2.97% |
| snake_anaconda | -6,652 | -3.29% |
| snake_viper_tick | -8,428 | -4.19% |
| snake_viper_wild | -8,619 | -4.21% |

Average per day so far: benchmark Rs +603, unified Rs +538, intraweek Rs +357, snake_abs_exit_conv Rs +324, snake_abs_exit Rs +320, intramonth Rs +262, snake_abs_conv Rs +201, oracle Rs +201, snake_abs Rs +201, random_hold Rs +135, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -128, snake_anaconda Rs -174, snake_viper_wild Rs -189, gold Rs -309, snake_viper_tick Rs -405, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.