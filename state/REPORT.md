# Paper trading report

Updated 2026-11-11 12:49 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,517 | +10.26% | 0 | - | 237 |
| unified | 220,440 | +10.22% | 0 | - | 236 |
| snake_abs_exit_conv | 217,574 | +8.79% | 2 | 50% | 345 |
| snake_abs_exit | 216,511 | +8.26% | 2 | 50% | 345 |
| snake_abs | 213,851 | +6.93% | 1 | 100% | 255 |
| snake_abs_conv | 213,697 | +6.85% | 1 | 100% | 255 |
| intraweek | 213,527 | +6.76% | 30 | 53% | 3,302 |
| oracle | 211,849 | +5.92% | 0 | - | 233 |
| intramonth | 211,335 | +5.67% | 0 | - | 235 |
| random_hold | 206,815 | +3.41% | 9 | 67% | 709 |
| snake_viper_wild | 204,779 | +2.39% | 10 | 50% | 1,825 |
| snake_anaconda | 204,366 | +2.18% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,287 | +0.64% | 9 | 44% | 1,639 |
| benchmark_smallcap | 201,199 | +0.60% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 190,046 | -4.98% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,246 (-4.38%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +7,349 | +3.72% |
| snake_viper_tick | +7,211 | +3.71% |
| snake_abs_exit_conv | +5,665 | +2.67% |
| snake_anaconda | +4,899 | +2.46% |
| snake_abs_exit | +4,527 | +2.14% |
| snake_abs_conv | +4,219 | +2.01% |
| snake_abs | +4,205 | +2.01% |
| benchmark_smallcap | +3,027 | +1.53% |
| benchmark | +2,425 | +1.11% |
| oracle | +1,930 | +0.92% |
| random_hold | +1,855 | +0.91% |
| intramonth | +726 | +0.34% |
| unified | +693 | +0.32% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -1,014 | -0.47% |
| gold | -2,088 | -1.09% |

Average per day so far: benchmark Rs +662, unified Rs +659, snake_abs_exit_conv Rs +628, snake_abs_exit Rs +590, snake_abs_conv Rs +489, snake_abs Rs +478, intraweek Rs +436, oracle Rs +382, intramonth Rs +366, random_hold Rs +220, snake_viper_wild Rs +208, snake_anaconda Rs +168, snake_viper_tick Rs +64, nifty_calls Rs +59, benchmark_smallcap Rs +44, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -321, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.