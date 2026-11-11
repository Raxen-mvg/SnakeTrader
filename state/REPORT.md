# Paper trading report

Updated 2026-11-11 13:16 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,755 | +10.38% | 0 | - | 236 |
| benchmark | 220,532 | +10.27% | 0 | - | 237 |
| snake_abs_exit_conv | 218,447 | +9.22% | 2 | 50% | 345 |
| snake_abs_exit | 217,392 | +8.70% | 2 | 50% | 345 |
| snake_abs | 215,029 | +7.51% | 1 | 100% | 255 |
| snake_abs_conv | 214,877 | +7.44% | 1 | 100% | 255 |
| intraweek | 213,535 | +6.77% | 30 | 53% | 3,302 |
| oracle | 212,053 | +6.03% | 0 | - | 233 |
| intramonth | 211,747 | +5.87% | 0 | - | 235 |
| random_hold | 207,198 | +3.60% | 9 | 67% | 709 |
| snake_viper_wild | 205,561 | +2.78% | 10 | 50% | 1,825 |
| snake_anaconda | 205,342 | +2.67% | 3 | 33% | 374 |
| snake_viper_tick | 202,052 | +1.03% | 9 | 44% | 1,639 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,468 | +0.73% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,980 | -5.01% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,528 (-4.24%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +8,131 | +4.12% |
| snake_viper_tick | +7,976 | +4.11% |
| snake_abs_exit_conv | +6,538 | +3.08% |
| snake_anaconda | +5,876 | +2.95% |
| snake_abs_exit | +5,408 | +2.55% |
| snake_abs_conv | +5,399 | +2.58% |
| snake_abs | +5,383 | +2.57% |
| benchmark_smallcap | +3,296 | +1.66% |
| benchmark | +2,440 | +1.12% |
| random_hold | +2,238 | +1.09% |
| oracle | +2,134 | +1.02% |
| intramonth | +1,138 | +0.54% |
| unified | +1,009 | +0.46% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -1,007 | -0.47% |
| gold | -2,154 | -1.12% |

Average per day so far: unified Rs +670, benchmark Rs +662, snake_abs_exit_conv Rs +659, snake_abs_exit Rs +621, snake_abs_conv Rs +531, snake_abs Rs +518, intraweek Rs +437, oracle Rs +389, intramonth Rs +379, snake_viper_wild Rs +242, random_hold Rs +232, snake_anaconda Rs +205, snake_viper_tick Rs +103, nifty_calls Rs +59, benchmark_smallcap Rs +54, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -323, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.