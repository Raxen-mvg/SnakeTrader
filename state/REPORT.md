# Paper trading report

Updated 2026-11-11 10:43 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,106 | +10.55% | 0 | - | 237 |
| unified | 220,728 | +10.36% | 0 | - | 236 |
| snake_abs_exit_conv | 215,907 | +7.95% | 2 | 50% | 345 |
| intraweek | 214,795 | +7.40% | 30 | 53% | 3,302 |
| snake_abs_exit | 214,527 | +7.26% | 2 | 50% | 345 |
| snake_abs | 212,778 | +6.39% | 1 | 100% | 255 |
| snake_abs_conv | 212,623 | +6.31% | 1 | 100% | 255 |
| oracle | 212,057 | +6.03% | 0 | - | 233 |
| intramonth | 211,509 | +5.75% | 0 | - | 235 |
| random_hold | 206,855 | +3.43% | 9 | 67% | 709 |
| snake_anaconda | 202,599 | +1.30% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,569 | +0.78% | 0 | - | 237 |
| snake_viper_wild | 200,659 | +0.33% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 197,251 | -1.38% | 9 | 44% | 1,639 |
| gold | 189,585 | -5.21% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,459 (-4.27%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +3,998 | +1.89% |
| benchmark_smallcap | +3,397 | +1.71% |
| snake_viper_wild | +3,229 | +1.64% |
| snake_viper_tick | +3,174 | +1.64% |
| snake_abs_conv | +3,146 | +1.50% |
| snake_anaconda | +3,132 | +1.57% |
| snake_abs | +3,131 | +1.49% |
| benchmark | +3,014 | +1.38% |
| snake_abs_exit | +2,543 | +1.20% |
| oracle | +2,139 | +1.02% |
| random_hold | +1,895 | +0.92% |
| unified | +981 | +0.45% |
| intramonth | +900 | +0.43% |
| intraweek | +253 | +0.12% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -2,548 | -1.33% |

Average per day so far: benchmark Rs +681, unified Rs +669, snake_abs_exit_conv Rs +568, snake_abs_exit Rs +519, intraweek Rs +477, snake_abs_conv Rs +451, snake_abs Rs +441, oracle Rs +389, intramonth Rs +371, random_hold Rs +221, snake_anaconda Rs +100, nifty_calls Rs +59, benchmark_smallcap Rs +58, snake_viper_wild Rs +29, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -137, gold Rs -336, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.