# Paper trading report

Updated 2026-11-26 10:13 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,306 | +12.65% | 0 | - | 237 |
| unified | 223,944 | +11.97% | 0 | - | 236 |
| oracle | 213,435 | +6.72% | 0 | - | 233 |
| intramonth | 211,424 | +5.71% | 0 | - | 235 |
| random_hold | 210,205 | +5.10% | 13 | 69% | 1,037 |
| intraweek | 208,449 | +4.22% | 40 | 55% | 4,400 |
| snake_abs_exit | 203,344 | +1.67% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,693 | +1.35% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,694 | +0.35% | 0 | - | 237 |
| snake_abs | 200,584 | +0.29% | 1 | 100% | 255 |
| snake_abs_conv | 200,411 | +0.21% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,233 | -1.88% | 16 | 50% | 2,827 |
| snake_anaconda | 194,916 | -2.54% | 3 | 33% | 374 |
| snake_viper_tick | 192,894 | -3.55% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,032 | -15.98% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,354 (-5.32%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +3,436 | +2.09% |
| benchmark_smallcap | +1,883 | +0.95% |
| intraweek | +1,706 | +0.82% |
| snake_abs_exit | +1,089 | +0.54% |
| snake_abs_exit_conv | +717 | +0.35% |
| random_hold | +712 | +0.34% |
| snake_abs_conv | +439 | +0.22% |
| snake_abs | +435 | +0.22% |
| snake_anaconda | +363 | +0.19% |
| benchmark | +283 | +0.13% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| unified | -155 | -0.07% |
| intramonth | -269 | -0.13% |
| oracle | -360 | -0.17% |
| snake_viper_tick | -1,283 | -0.66% |
| snake_viper_wild | -1,310 | -0.66% |

Average per day so far: benchmark Rs +617, unified Rs +584, oracle Rs +328, intramonth Rs +279, random_hold Rs +249, intraweek Rs +206, snake_abs_exit Rs +88, snake_abs_exit_conv Rs +71, nifty_calls Rs +45, benchmark_smallcap Rs +19, snake_abs Rs +15, snake_abs_conv Rs +11, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_viper_wild Rs -114, snake_anaconda Rs -141, snake_viper_tick Rs -237, snake_nonews Rs -284, snake Rs -304, gold Rs -780

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.