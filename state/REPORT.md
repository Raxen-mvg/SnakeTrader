# Paper trading report

Updated 2026-11-11 13:19 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,666 | +10.33% | 0 | - | 236 |
| benchmark | 220,609 | +10.30% | 0 | - | 237 |
| snake_abs_exit_conv | 218,332 | +9.17% | 2 | 50% | 345 |
| snake_abs_exit | 217,264 | +8.63% | 2 | 50% | 345 |
| snake_abs | 214,846 | +7.42% | 1 | 100% | 255 |
| snake_abs_conv | 214,693 | +7.35% | 1 | 100% | 255 |
| intraweek | 213,523 | +6.76% | 30 | 53% | 3,302 |
| oracle | 212,030 | +6.01% | 0 | - | 233 |
| intramonth | 211,708 | +5.85% | 0 | - | 235 |
| random_hold | 207,146 | +3.57% | 9 | 67% | 709 |
| snake_viper_wild | 205,683 | +2.84% | 10 | 50% | 1,825 |
| snake_anaconda | 205,134 | +2.57% | 3 | 33% | 374 |
| snake_viper_tick | 202,171 | +1.09% | 9 | 44% | 1,639 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,345 | +0.67% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,980 | -5.01% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,482 (-4.26%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +8,253 | +4.18% |
| snake_viper_tick | +8,095 | +4.17% |
| snake_abs_exit_conv | +6,423 | +3.03% |
| snake_anaconda | +5,668 | +2.84% |
| snake_abs_exit | +5,280 | +2.49% |
| snake_abs_conv | +5,216 | +2.49% |
| snake_abs | +5,199 | +2.48% |
| benchmark_smallcap | +3,172 | +1.60% |
| benchmark | +2,517 | +1.15% |
| random_hold | +2,185 | +1.07% |
| oracle | +2,111 | +1.01% |
| intramonth | +1,099 | +0.52% |
| unified | +919 | +0.42% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -1,019 | -0.47% |
| gold | -2,154 | -1.12% |

Average per day so far: unified Rs +667, benchmark Rs +665, snake_abs_exit_conv Rs +655, snake_abs_exit Rs +617, snake_abs_conv Rs +525, snake_abs Rs +512, intraweek Rs +436, oracle Rs +388, intramonth Rs +378, snake_viper_wild Rs +247, random_hold Rs +231, snake_anaconda Rs +197, snake_viper_tick Rs +109, nifty_calls Rs +59, benchmark_smallcap Rs +50, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -323, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.