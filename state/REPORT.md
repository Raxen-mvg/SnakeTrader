# Paper trading report

Updated 2026-11-27 13:49 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,082 | +12.04% | 0 | - | 237 |
| unified | 223,058 | +11.53% | 0 | - | 236 |
| oracle | 211,701 | +5.85% | 0 | - | 233 |
| random_hold | 210,822 | +5.41% | 13 | 69% | 1,037 |
| intramonth | 210,644 | +5.32% | 0 | - | 235 |
| intraweek | 208,263 | +4.13% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 205,318 | +2.66% | 2 | 50% | 345 |
| snake_abs_exit | 204,844 | +2.42% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,614 | +0.81% | 0 | - | 237 |
| snake_abs | 200,608 | +0.30% | 1 | 100% | 255 |
| snake_abs_conv | 200,427 | +0.21% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,917 | -3.04% | 3 | 33% | 374 |
| snake_viper_wild | 192,471 | -3.76% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,202 | -5.40% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,367 | -14.82% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,769 (-5.62%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,921 | +2.46% |
| gold | +4,373 | +2.63% |
| snake_abs_exit | +3,766 | +1.87% |
| random_hold | +2,228 | +1.07% |
| snake_abs_conv | +2,060 | +1.04% |
| snake_abs | +2,056 | +1.04% |
| snake_anaconda | +1,621 | +0.84% |
| intraweek | +1,214 | +0.59% |
| benchmark_smallcap | +773 | +0.39% |
| snake_viper_wild | +266 | +0.14% |
| snake_viper_tick | +261 | +0.14% |
| intramonth | +111 | +0.05% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| unified | -20 | -0.01% |
| oracle | -535 | -0.25% |
| benchmark | -1,905 | -0.84% |

Average per day so far: benchmark Rs +573, unified Rs +549, oracle Rs +279, random_hold Rs +258, intramonth Rs +253, intraweek Rs +197, snake_abs_exit_conv Rs +136, snake_abs_exit Rs +124, nifty_calls Rs +44, benchmark_smallcap Rs +42, snake_abs Rs +15, snake_abs_conv Rs +11, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -164, snake_viper_wild Rs -221, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -348, gold Rs -706

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.