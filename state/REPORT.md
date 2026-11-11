# Paper trading report

Updated 2026-11-11 10:01 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,221 | +10.61% | 0 | - | 237 |
| unified | 220,411 | +10.21% | 0 | - | 236 |
| snake_abs_exit_conv | 216,395 | +8.20% | 2 | 50% | 345 |
| intraweek | 215,247 | +7.62% | 30 | 53% | 3,302 |
| snake_abs_exit | 214,821 | +7.41% | 2 | 50% | 345 |
| snake_abs | 213,218 | +6.61% | 1 | 100% | 255 |
| snake_abs_conv | 213,057 | +6.53% | 1 | 100% | 255 |
| oracle | 211,459 | +5.73% | 0 | - | 233 |
| intramonth | 210,872 | +5.44% | 0 | - | 235 |
| random_hold | 206,224 | +3.11% | 9 | 67% | 709 |
| snake_anaconda | 202,886 | +1.44% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,535 | +0.77% | 0 | - | 237 |
| snake_viper_wild | 200,662 | +0.33% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 197,254 | -1.37% | 9 | 44% | 1,639 |
| gold | 189,306 | -5.35% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,314 (-4.34%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,487 | +2.12% |
| snake_abs_conv | +3,579 | +1.71% |
| snake_abs | +3,571 | +1.70% |
| snake_anaconda | +3,419 | +1.71% |
| benchmark_smallcap | +3,363 | +1.70% |
| snake_viper_wild | +3,232 | +1.64% |
| snake_viper_tick | +3,178 | +1.64% |
| benchmark | +3,129 | +1.44% |
| snake_abs_exit | +2,837 | +1.34% |
| oracle | +1,541 | +0.73% |
| random_hold | +1,263 | +0.62% |
| intraweek | +706 | +0.33% |
| unified | +664 | +0.30% |
| intramonth | +262 | +0.12% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -2,828 | -1.47% |

Average per day so far: benchmark Rs +685, unified Rs +658, snake_abs_exit_conv Rs +586, snake_abs_exit Rs +529, intraweek Rs +492, snake_abs_conv Rs +466, snake_abs Rs +456, oracle Rs +370, intramonth Rs +351, random_hold Rs +201, snake_anaconda Rs +111, nifty_calls Rs +59, benchmark_smallcap Rs +57, snake_viper_wild Rs +29, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -137, gold Rs -345, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.