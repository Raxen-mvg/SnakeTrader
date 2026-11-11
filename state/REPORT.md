# Paper trading report

Updated 2026-11-11 11:28 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,244 | +10.62% | 0 | - | 237 |
| unified | 220,381 | +10.19% | 0 | - | 236 |
| snake_abs_exit_conv | 216,811 | +8.41% | 2 | 50% | 345 |
| snake_abs_exit | 215,407 | +7.70% | 2 | 50% | 345 |
| intraweek | 214,078 | +7.04% | 30 | 53% | 3,302 |
| snake_abs | 213,628 | +6.81% | 1 | 100% | 255 |
| snake_abs_conv | 213,470 | +6.74% | 1 | 100% | 255 |
| oracle | 211,922 | +5.96% | 0 | - | 233 |
| intramonth | 211,220 | +5.61% | 0 | - | 235 |
| random_hold | 206,836 | +3.42% | 9 | 67% | 709 |
| snake_anaconda | 203,428 | +1.71% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,801 | +0.90% | 10 | 50% | 1,825 |
| benchmark_smallcap | 201,771 | +0.89% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 198,370 | -0.81% | 9 | 44% | 1,639 |
| gold | 189,898 | -5.05% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,282 (-4.36%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,903 | +2.31% |
| snake_viper_wild | +4,371 | +2.21% |
| snake_viper_tick | +4,293 | +2.21% |
| snake_abs_conv | +3,993 | +1.91% |
| snake_abs | +3,981 | +1.90% |
| snake_anaconda | +3,961 | +1.99% |
| benchmark_smallcap | +3,598 | +1.82% |
| snake_abs_exit | +3,423 | +1.61% |
| benchmark | +3,152 | +1.45% |
| oracle | +2,003 | +0.95% |
| random_hold | +1,875 | +0.92% |
| unified | +634 | +0.29% |
| intramonth | +611 | +0.29% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -464 | -0.22% |
| gold | -2,236 | -1.16% |

Average per day so far: benchmark Rs +685, unified Rs +657, snake_abs_exit_conv Rs +600, snake_abs_exit Rs +550, snake_abs_conv Rs +481, snake_abs Rs +470, intraweek Rs +454, oracle Rs +385, intramonth Rs +362, random_hold Rs +221, snake_anaconda Rs +132, snake_viper_wild Rs +78, benchmark_smallcap Rs +66, nifty_calls Rs +59, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -81, gold Rs -326, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.