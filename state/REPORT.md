# Paper trading report

Updated 2026-11-06 13:40 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,782 | +7.89% | 0 | - | 237 |
| unified | 214,741 | +7.37% | 0 | - | 236 |
| snake_abs_exit_conv | 208,690 | +4.34% | 1 | 100% | 255 |
| snake_abs_exit | 208,593 | +4.30% | 1 | 100% | 260 |
| intraweek | 208,233 | +4.12% | 25 | 48% | 2,757 |
| intramonth | 207,041 | +3.52% | 0 | - | 235 |
| snake_abs | 205,673 | +2.84% | 1 | 100% | 255 |
| snake_abs_conv | 205,489 | +2.75% | 1 | 100% | 255 |
| oracle | 205,312 | +2.66% | 0 | - | 233 |
| random_hold | 203,300 | +1.65% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,286 | -1.86% | 3 | 33% | 702 |
| snake_anaconda | 195,982 | -2.01% | 3 | 33% | 374 |
| benchmark_smallcap | 195,134 | -2.43% | 0 | - | 237 |
| snake_viper_tick | 192,962 | -3.52% | 2 | 0% | 532 |
| gold | 190,391 | -4.80% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,913 (-6.54%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,012 | +0.94% |
| oracle | +1,240 | +0.61% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -908 | -0.44% |
| random_hold | -1,023 | -0.50% |
| intraweek | -1,186 | -0.57% |
| unified | -1,243 | -0.57% |
| benchmark_smallcap | -3,554 | -1.79% |
| gold | -3,831 | -1.97% |
| snake_abs | -6,016 | -2.84% |
| snake_abs_conv | -6,056 | -2.86% |
| snake_abs_exit | -6,066 | -2.83% |
| snake_abs_exit_conv | -6,113 | -2.85% |
| snake_anaconda | -6,497 | -3.21% |
| snake_viper_tick | -8,176 | -4.07% |
| snake_viper_wild | -8,370 | -4.09% |

Average per day so far: benchmark Rs +544, unified Rs +508, snake_abs_exit_conv Rs +334, snake_abs_exit Rs +331, intraweek Rs +284, intramonth Rs +243, snake_abs_conv Rs +211, snake_abs Rs +210, oracle Rs +183, random_hold Rs +114, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -167, snake_viper_wild Rs -177, benchmark_smallcap Rs -195, gold Rs -331, snake_viper_tick Rs -391, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.