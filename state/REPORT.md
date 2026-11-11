# Paper trading report

Updated 2026-11-11 14:35 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,453 | +10.23% | 0 | - | 236 |
| benchmark | 220,073 | +10.04% | 0 | - | 237 |
| snake_abs_exit_conv | 217,601 | +8.80% | 2 | 50% | 345 |
| snake_abs_exit | 216,841 | +8.42% | 2 | 50% | 345 |
| snake_abs | 214,384 | +7.19% | 1 | 100% | 255 |
| snake_abs_conv | 214,224 | +7.11% | 1 | 100% | 255 |
| intraweek | 213,574 | +6.79% | 30 | 53% | 3,302 |
| oracle | 211,798 | +5.90% | 0 | - | 233 |
| intramonth | 211,437 | +5.72% | 0 | - | 235 |
| random_hold | 207,146 | +3.57% | 9 | 67% | 709 |
| snake_viper_wild | 206,620 | +3.31% | 10 | 50% | 1,825 |
| snake_anaconda | 204,608 | +2.30% | 3 | 33% | 374 |
| snake_viper_tick | 203,089 | +1.54% | 9 | 44% | 1,639 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,345 | +0.67% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,404 | -5.30% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,328 (-4.34%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +9,190 | +4.66% |
| snake_viper_tick | +9,013 | +4.64% |
| snake_abs_exit_conv | +5,692 | +2.69% |
| snake_anaconda | +5,141 | +2.58% |
| snake_abs_exit | +4,857 | +2.29% |
| snake_abs_conv | +4,746 | +2.27% |
| snake_abs | +4,737 | +2.26% |
| benchmark_smallcap | +3,172 | +1.60% |
| random_hold | +2,185 | +1.07% |
| benchmark | +1,981 | +0.91% |
| oracle | +1,879 | +0.90% |
| intramonth | +828 | +0.39% |
| unified | +706 | +0.32% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -967 | -0.45% |
| gold | -2,729 | -1.42% |

Average per day so far: unified Rs +660, benchmark Rs +648, snake_abs_exit_conv Rs +629, snake_abs_exit Rs +601, snake_abs_conv Rs +508, snake_abs Rs +496, intraweek Rs +438, oracle Rs +381, intramonth Rs +369, snake_viper_wild Rs +288, random_hold Rs +231, snake_anaconda Rs +177, snake_viper_tick Rs +154, nifty_calls Rs +59, benchmark_smallcap Rs +50, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -342, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.