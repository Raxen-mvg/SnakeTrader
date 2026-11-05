# Paper trading report

Updated 2026-11-05 14:40 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 216,135 | +8.07% | 0 | - | 236 |
| snake_abs_exit_conv | 214,715 | +7.36% | 1 | 100% | 255 |
| snake_abs_exit | 214,419 | +7.21% | 1 | 100% | 260 |
| benchmark | 213,961 | +6.98% | 0 | - | 237 |
| snake_abs | 211,597 | +5.80% | 1 | 100% | 255 |
| snake_abs_conv | 211,456 | +5.73% | 1 | 100% | 255 |
| intraweek | 209,894 | +4.95% | 25 | 48% | 2,757 |
| intramonth | 208,044 | +4.02% | 0 | - | 235 |
| snake_viper_wild | 205,356 | +2.68% | 3 | 33% | 702 |
| random_hold | 204,656 | +2.33% | 8 | 62% | 649 |
| oracle | 204,126 | +2.06% | 0 | - | 233 |
| snake_anaconda | 202,444 | +1.22% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,827 | +0.91% | 2 | 0% | 532 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,991 | -0.51% | 0 | - | 237 |
| gold | 194,435 | -2.78% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,589 (-5.21%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,202 | +2.49% |
| gold | +3,041 | +1.59% |
| oracle | +2,334 | +1.16% |
| benchmark_smallcap | +2,320 | +1.18% |
| unified | +1,696 | +0.79% |
| random_hold | +1,347 | +0.66% |
| intramonth | +1,029 | +0.50% |
| intraweek | +197 | +0.09% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -300 | -0.14% |
| snake_abs_conv | -302 | -0.14% |
| snake_abs | -306 | -0.14% |
| snake_abs_exit | -481 | -0.22% |
| snake_anaconda | -1,377 | -0.68% |
| snake_viper_tick | -3,573 | -1.74% |
| snake_viper_wild | -3,674 | -1.76% |

Average per day so far: snake_abs_exit_conv Rs +589, snake_abs_exit Rs +577, unified Rs +576, benchmark Rs +499, snake_abs_conv Rs +458, snake_abs Rs +446, intraweek Rs +353, intramonth Rs +287, snake_viper_wild Rs +268, random_hold Rs +166, oracle Rs +147, snake_viper_tick Rs +107, snake_anaconda Rs +106, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -42, gold Rs -199, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.