# Paper trading report

Updated 2026-11-17 14:08 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 222,055 | +11.03% | 0 | - | 237 |
| unified | 221,551 | +10.78% | 0 | - | 236 |
| snake_abs_exit | 213,685 | +6.84% | 2 | 50% | 345 |
| intraweek | 213,513 | +6.76% | 35 | 54% | 3,851 |
| oracle | 212,399 | +6.20% | 0 | - | 233 |
| snake_abs_exit_conv | 212,039 | +6.02% | 2 | 50% | 345 |
| intramonth | 211,426 | +5.71% | 0 | - | 235 |
| snake_viper_wild | 209,183 | +4.59% | 14 | 50% | 2,496 |
| snake_abs | 208,841 | +4.42% | 1 | 100% | 255 |
| snake_abs_conv | 208,700 | +4.35% | 1 | 100% | 255 |
| random_hold | 207,621 | +3.81% | 10 | 70% | 733 |
| snake_viper_tick | 205,608 | +2.80% | 13 | 46% | 2,299 |
| snake_anaconda | 204,399 | +2.20% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,210 | +0.60% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,872 | -9.56% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,130 (-4.43%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,039 | +1.47% |
| snake_viper_tick | +2,988 | +1.48% |
| intraweek | +2,247 | +1.06% |
| benchmark | +1,974 | +0.90% |
| benchmark_smallcap | +381 | +0.19% |
| oracle | +376 | +0.18% |
| unified | +114 | +0.05% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| gold | -82 | -0.04% |
| random_hold | -172 | -0.08% |
| intramonth | -193 | -0.09% |
| snake_anaconda | -703 | -0.34% |
| snake_abs_exit | -724 | -0.34% |
| snake_abs_exit_conv | -1,178 | -0.55% |
| snake_abs_conv | -1,290 | -0.61% |
| snake_abs | -1,293 | -0.61% |

Average per day so far: benchmark Rs +630, unified Rs +616, snake_abs_exit Rs +428, intraweek Rs +386, snake_abs_exit_conv Rs +376, oracle Rs +354, snake_viper_wild Rs +340, intramonth Rs +326, snake_abs_conv Rs +272, snake_abs Rs +268, snake_viper_tick Rs +234, random_hold Rs +218, snake_anaconda Rs +147, nifty_calls Rs +52, benchmark_smallcap Rs +39, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -547

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.