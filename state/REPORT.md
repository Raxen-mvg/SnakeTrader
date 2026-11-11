# Paper trading report

Updated 2026-11-11 15:30 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,814 | +9.91% | 0 | - | 236 |
| benchmark | 219,262 | +9.63% | 0 | - | 237 |
| snake_abs_exit_conv | 217,151 | +8.58% | 2 | 50% | 345 |
| snake_abs_exit | 216,162 | +8.08% | 2 | 50% | 345 |
| snake_abs | 213,625 | +6.81% | 1 | 100% | 255 |
| snake_abs_conv | 213,458 | +6.73% | 1 | 100% | 255 |
| intraweek | 213,133 | +6.57% | 30 | 53% | 3,302 |
| oracle | 212,003 | +6.00% | 0 | - | 233 |
| intramonth | 210,996 | +5.50% | 0 | - | 235 |
| random_hold | 207,111 | +3.56% | 9 | 67% | 709 |
| snake_viper_wild | 206,742 | +3.37% | 10 | 50% | 1,825 |
| snake_anaconda | 204,123 | +2.06% | 3 | 33% | 374 |
| snake_viper_tick | 203,209 | +1.60% | 9 | 44% | 1,639 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,807 | +0.40% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,585 | -5.21% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,017 (-4.49%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +9,312 | +4.72% |
| snake_viper_tick | +9,132 | +4.71% |
| snake_abs_exit_conv | +5,243 | +2.47% |
| snake_anaconda | +4,657 | +2.33% |
| snake_abs_exit | +4,178 | +1.97% |
| snake_abs_conv | +3,980 | +1.90% |
| snake_abs | +3,978 | +1.90% |
| benchmark_smallcap | +2,634 | +1.33% |
| random_hold | +2,150 | +1.05% |
| oracle | +2,084 | +0.99% |
| benchmark | +1,170 | +0.54% |
| intramonth | +387 | +0.18% |
| unified | +67 | +0.03% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -1,409 | -0.66% |
| gold | -2,548 | -1.33% |

Average per day so far: unified Rs +639, benchmark Rs +621, snake_abs_exit_conv Rs +613, snake_abs_exit Rs +577, snake_abs_conv Rs +481, snake_abs Rs +470, intraweek Rs +424, oracle Rs +387, intramonth Rs +355, snake_viper_wild Rs +293, random_hold Rs +229, snake_viper_tick Rs +160, snake_anaconda Rs +159, nifty_calls Rs +59, benchmark_smallcap Rs +30, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -336, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.