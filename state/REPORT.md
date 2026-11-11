# Paper trading report

Updated 2026-11-11 11:13 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,313 | +10.66% | 0 | - | 237 |
| unified | 220,442 | +10.22% | 0 | - | 236 |
| snake_abs_exit_conv | 216,390 | +8.20% | 2 | 50% | 345 |
| snake_abs_exit | 214,948 | +7.47% | 2 | 50% | 345 |
| intraweek | 214,113 | +7.06% | 30 | 53% | 3,302 |
| snake_abs | 213,146 | +6.57% | 1 | 100% | 255 |
| snake_abs_conv | 212,987 | +6.49% | 1 | 100% | 255 |
| oracle | 211,707 | +5.85% | 0 | - | 233 |
| intramonth | 211,269 | +5.63% | 0 | - | 235 |
| random_hold | 206,705 | +3.35% | 9 | 67% | 709 |
| snake_anaconda | 202,834 | +1.42% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,804 | +0.90% | 0 | - | 237 |
| snake_viper_wild | 201,510 | +0.76% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 198,085 | -0.96% | 9 | 44% | 1,639 |
| gold | 189,931 | -5.04% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,221 (-4.39%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,482 | +2.12% |
| snake_viper_wild | +4,080 | +2.07% |
| snake_viper_tick | +4,009 | +2.07% |
| benchmark_smallcap | +3,632 | +1.83% |
| snake_abs_conv | +3,510 | +1.68% |
| snake_abs | +3,499 | +1.67% |
| snake_anaconda | +3,368 | +1.69% |
| benchmark | +3,221 | +1.48% |
| snake_abs_exit | +2,964 | +1.40% |
| oracle | +1,789 | +0.85% |
| random_hold | +1,744 | +0.85% |
| unified | +696 | +0.32% |
| intramonth | +660 | +0.31% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -429 | -0.20% |
| gold | -2,203 | -1.15% |

Average per day so far: benchmark Rs +688, unified Rs +659, snake_abs_exit_conv Rs +585, snake_abs_exit Rs +534, snake_abs_conv Rs +464, intraweek Rs +455, snake_abs Rs +453, oracle Rs +378, intramonth Rs +364, random_hold Rs +216, snake_anaconda Rs +109, benchmark_smallcap Rs +67, snake_viper_wild Rs +66, nifty_calls Rs +59, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -96, gold Rs -325, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.