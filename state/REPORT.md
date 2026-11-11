# Paper trading report

Updated 2026-11-11 15:00 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,628 | +10.31% | 0 | - | 236 |
| benchmark | 219,461 | +9.73% | 0 | - | 237 |
| snake_abs_exit_conv | 216,537 | +8.27% | 2 | 50% | 345 |
| snake_abs_exit | 215,656 | +7.83% | 2 | 50% | 345 |
| intraweek | 213,306 | +6.65% | 30 | 53% | 3,302 |
| snake_abs | 213,199 | +6.60% | 1 | 100% | 255 |
| snake_abs_conv | 213,029 | +6.51% | 1 | 100% | 255 |
| oracle | 211,985 | +5.99% | 0 | - | 233 |
| intramonth | 211,568 | +5.78% | 0 | - | 235 |
| random_hold | 207,072 | +3.54% | 9 | 67% | 709 |
| snake_viper_wild | 206,128 | +3.06% | 10 | 50% | 1,825 |
| snake_anaconda | 203,554 | +1.78% | 3 | 33% | 374 |
| snake_viper_tick | 202,607 | +1.30% | 9 | 44% | 1,639 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,199 | +0.60% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,602 | -5.20% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,224 (-4.39%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +8,698 | +4.41% |
| snake_viper_tick | +8,531 | +4.40% |
| snake_abs_exit_conv | +4,628 | +2.18% |
| snake_anaconda | +4,087 | +2.05% |
| snake_abs_exit | +3,672 | +1.73% |
| snake_abs | +3,552 | +1.69% |
| snake_abs_conv | +3,552 | +1.70% |
| benchmark_smallcap | +3,027 | +1.53% |
| random_hold | +2,112 | +1.03% |
| oracle | +2,066 | +0.98% |
| benchmark | +1,369 | +0.63% |
| intramonth | +958 | +0.46% |
| unified | +881 | +0.40% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -1,236 | -0.58% |
| gold | -2,532 | -1.32% |

Average per day so far: unified Rs +665, benchmark Rs +628, snake_abs_exit_conv Rs +591, snake_abs_exit Rs +559, snake_abs_conv Rs +465, snake_abs Rs +455, intraweek Rs +429, oracle Rs +387, intramonth Rs +373, snake_viper_wild Rs +266, random_hold Rs +228, snake_anaconda Rs +137, snake_viper_tick Rs +130, nifty_calls Rs +59, benchmark_smallcap Rs +44, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -335, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.