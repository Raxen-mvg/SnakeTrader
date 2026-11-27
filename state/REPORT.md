# Paper trading report

Updated 2026-11-27 09:56 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,436 | +12.72% | 0 | - | 237 |
| unified | 223,259 | +11.63% | 0 | - | 236 |
| oracle | 212,469 | +6.24% | 0 | - | 233 |
| intramonth | 210,981 | +5.49% | 0 | - | 235 |
| random_hold | 209,728 | +4.86% | 13 | 69% | 1,037 |
| intraweek | 207,889 | +3.94% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,207 | +2.60% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,101 | +2.05% | 2 | 50% | 345 |
| benchmark_smallcap | 201,939 | +0.97% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,178 | +0.59% | 1 | 100% | 255 |
| snake_abs_conv | 200,999 | +0.50% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,785 | -2.61% | 3 | 33% | 374 |
| snake_viper_wild | 192,950 | -3.52% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,670 | -5.17% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,476 | -15.76% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,804 (-5.60%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,130 | +2.05% |
| snake_abs_exit_conv | +3,704 | +1.85% |
| snake_abs_conv | +2,632 | +1.33% |
| snake_abs | +2,626 | +1.32% |
| snake_anaconda | +2,489 | +1.29% |
| gold | +2,482 | +1.50% |
| random_hold | +1,134 | +0.54% |
| benchmark_smallcap | +1,099 | +0.55% |
| intraweek | +840 | +0.41% |
| snake_viper_wild | +744 | +0.39% |
| snake_viper_tick | +729 | +0.39% |
| intramonth | +448 | +0.21% |
| oracle | +234 | +0.11% |
| unified | +180 | +0.08% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -551 | -0.24% |

Average per day so far: benchmark Rs +606, unified Rs +554, oracle Rs +297, intramonth Rs +261, random_hold Rs +232, intraweek Rs +188, snake_abs_exit Rs +134, snake_abs_exit_conv Rs +105, benchmark_smallcap Rs +51, nifty_calls Rs +44, snake_abs Rs +29, snake_abs_conv Rs +26, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -141, snake_viper_wild Rs -207, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -333, gold Rs -751

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.