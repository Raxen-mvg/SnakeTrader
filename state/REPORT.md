# Paper trading report

Updated 2026-11-11 10:31 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,068 | +10.53% | 0 | - | 237 |
| unified | 220,604 | +10.30% | 0 | - | 236 |
| snake_abs_exit_conv | 216,269 | +8.13% | 2 | 50% | 345 |
| snake_abs_exit | 214,750 | +7.38% | 2 | 50% | 345 |
| intraweek | 214,591 | +7.29% | 30 | 53% | 3,302 |
| snake_abs | 212,935 | +6.47% | 1 | 100% | 255 |
| snake_abs_conv | 212,782 | +6.39% | 1 | 100% | 255 |
| oracle | 211,623 | +5.81% | 0 | - | 233 |
| intramonth | 211,355 | +5.68% | 0 | - | 235 |
| random_hold | 206,259 | +3.13% | 9 | 67% | 709 |
| snake_anaconda | 202,736 | +1.37% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,569 | +0.78% | 0 | - | 237 |
| snake_viper_wild | 200,312 | +0.16% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 196,912 | -1.54% | 9 | 44% | 1,639 |
| gold | 189,421 | -5.29% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,296 (-4.35%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,360 | +2.06% |
| benchmark_smallcap | +3,397 | +1.71% |
| snake_abs_conv | +3,305 | +1.58% |
| snake_abs | +3,288 | +1.57% |
| snake_anaconda | +3,270 | +1.64% |
| benchmark | +2,976 | +1.36% |
| snake_viper_wild | +2,882 | +1.46% |
| snake_viper_tick | +2,835 | +1.46% |
| snake_abs_exit | +2,766 | +1.30% |
| oracle | +1,705 | +0.81% |
| random_hold | +1,299 | +0.63% |
| unified | +857 | +0.39% |
| intramonth | +746 | +0.35% |
| intraweek | +49 | +0.02% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -2,713 | -1.41% |

Average per day so far: benchmark Rs +680, unified Rs +665, snake_abs_exit_conv Rs +581, snake_abs_exit Rs +527, intraweek Rs +471, snake_abs_conv Rs +457, snake_abs Rs +446, oracle Rs +375, intramonth Rs +366, random_hold Rs +202, snake_anaconda Rs +105, nifty_calls Rs +59, benchmark_smallcap Rs +58, snake_viper_wild Rs +14, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -154, gold Rs -341, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.