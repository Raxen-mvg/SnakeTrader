# Paper trading report

Updated 2026-11-11 10:16 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,022 | +10.51% | 0 | - | 237 |
| unified | 220,337 | +10.17% | 0 | - | 236 |
| snake_abs_exit_conv | 216,261 | +8.13% | 2 | 50% | 345 |
| snake_abs_exit | 214,898 | +7.45% | 2 | 50% | 345 |
| intraweek | 214,137 | +7.07% | 30 | 53% | 3,302 |
| snake_abs | 213,105 | +6.55% | 1 | 100% | 255 |
| snake_abs_conv | 212,950 | +6.47% | 1 | 100% | 255 |
| oracle | 210,939 | +5.47% | 0 | - | 233 |
| intramonth | 210,883 | +5.44% | 0 | - | 235 |
| random_hold | 206,280 | +3.14% | 9 | 67% | 709 |
| snake_anaconda | 202,767 | +1.38% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,311 | +0.66% | 0 | - | 237 |
| snake_viper_wild | 200,314 | +0.16% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 196,914 | -1.54% | 9 | 44% | 1,639 |
| gold | 189,240 | -5.38% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,008 (-4.50%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,352 | +2.05% |
| snake_abs_conv | +3,473 | +1.66% |
| snake_abs | +3,459 | +1.65% |
| snake_anaconda | +3,301 | +1.66% |
| benchmark_smallcap | +3,139 | +1.58% |
| benchmark | +2,930 | +1.34% |
| snake_abs_exit | +2,914 | +1.38% |
| snake_viper_wild | +2,884 | +1.46% |
| snake_viper_tick | +2,837 | +1.46% |
| random_hold | +1,320 | +0.64% |
| oracle | +1,020 | +0.49% |
| unified | +590 | +0.27% |
| intramonth | +274 | +0.13% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -405 | -0.19% |
| gold | -2,893 | -1.51% |

Average per day so far: benchmark Rs +678, unified Rs +656, snake_abs_exit_conv Rs +581, snake_abs_exit Rs +532, snake_abs_conv Rs +463, intraweek Rs +456, snake_abs Rs +452, oracle Rs +353, intramonth Rs +351, random_hold Rs +203, snake_anaconda Rs +106, nifty_calls Rs +59, benchmark_smallcap Rs +49, snake_viper_wild Rs +14, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -154, gold Rs -347, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.