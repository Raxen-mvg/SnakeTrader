# Paper trading report

Updated 2026-11-11 09:51 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,481 | +10.74% | 0 | - | 237 |
| unified | 220,469 | +10.23% | 0 | - | 236 |
| snake_abs_exit_conv | 216,274 | +8.14% | 2 | 50% | 345 |
| intraweek | 215,344 | +7.67% | 30 | 53% | 3,302 |
| snake_abs_exit | 214,759 | +7.38% | 2 | 50% | 345 |
| snake_abs | 213,271 | +6.64% | 1 | 100% | 255 |
| snake_abs_conv | 213,114 | +6.56% | 1 | 100% | 255 |
| oracle | 211,390 | +5.70% | 0 | - | 233 |
| intramonth | 210,969 | +5.48% | 0 | - | 235 |
| random_hold | 206,141 | +3.07% | 9 | 67% | 709 |
| snake_anaconda | 202,838 | +1.42% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,356 | +0.68% | 0 | - | 237 |
| snake_viper_wild | 200,594 | +0.30% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 197,188 | -1.41% | 9 | 44% | 1,639 |
| gold | 189,125 | -5.44% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,342 (-4.33%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,365 | +2.06% |
| snake_abs_conv | +3,636 | +1.74% |
| snake_abs | +3,624 | +1.73% |
| benchmark | +3,389 | +1.55% |
| snake_anaconda | +3,371 | +1.69% |
| benchmark_smallcap | +3,184 | +1.61% |
| snake_viper_wild | +3,164 | +1.60% |
| snake_viper_tick | +3,111 | +1.60% |
| snake_abs_exit | +2,775 | +1.31% |
| oracle | +1,472 | +0.70% |
| random_hold | +1,181 | +0.58% |
| intraweek | +802 | +0.37% |
| unified | +722 | +0.33% |
| intramonth | +360 | +0.17% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,009 | -1.57% |

Average per day so far: benchmark Rs +693, unified Rs +660, snake_abs_exit_conv Rs +581, snake_abs_exit Rs +527, intraweek Rs +495, snake_abs_conv Rs +468, snake_abs Rs +458, oracle Rs +367, intramonth Rs +354, random_hold Rs +198, snake_anaconda Rs +109, nifty_calls Rs +59, benchmark_smallcap Rs +50, snake_viper_wild Rs +26, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -141, gold Rs -351, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.