# Paper trading report

Updated 2026-11-19 14:52 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,108 | +12.05% | 0 | - | 236 |
| benchmark | 222,223 | +11.11% | 0 | - | 237 |
| snake_abs_exit | 213,777 | +6.89% | 2 | 50% | 345 |
| intramonth | 213,656 | +6.83% | 0 | - | 235 |
| oracle | 211,663 | +5.83% | 0 | - | 233 |
| intraweek | 211,442 | +5.72% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,435 | +5.72% | 2 | 50% | 345 |
| snake_abs | 209,209 | +4.60% | 1 | 100% | 255 |
| snake_abs_conv | 209,091 | +4.55% | 1 | 100% | 255 |
| random_hold | 208,146 | +4.07% | 10 | 70% | 733 |
| snake_viper_wild | 207,691 | +3.85% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,141 | +2.07% | 15 | 47% | 2,625 |
| snake_anaconda | 203,735 | +1.87% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,177 | +0.59% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,839 | -12.58% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,497 (-4.25%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,928 | +0.88% |
| benchmark_smallcap | +1,850 | +0.93% |
| unified | +1,496 | +0.67% |
| intramonth | +1,382 | +0.65% |
| random_hold | +1,214 | +0.59% |
| oracle | +867 | +0.41% |
| snake_viper_wild | +651 | +0.32% |
| snake_viper_tick | +638 | +0.31% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -228 | -0.11% |
| snake_abs_conv | -233 | -0.11% |
| snake_abs_exit | -254 | -0.12% |
| intraweek | -398 | -0.19% |
| snake_anaconda | -666 | -0.33% |
| snake_abs_exit_conv | -948 | -0.45% |
| gold | -2,482 | -1.40% |

Average per day so far: unified Rs +652, benchmark Rs +601, snake_abs_exit Rs +405, intramonth Rs +369, snake_abs_exit_conv Rs +336, oracle Rs +315, intraweek Rs +309, snake_abs_conv Rs +267, snake_viper_wild Rs +265, snake_abs Rs +263, random_hold Rs +220, snake_viper_tick Rs +159, snake_anaconda Rs +117, nifty_calls Rs +50, benchmark_smallcap Rs +36, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -680

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.