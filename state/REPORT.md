# Paper trading report

Updated 2026-11-11 11:40 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,381 | +10.69% | 0 | - | 237 |
| unified | 220,686 | +10.34% | 0 | - | 236 |
| snake_abs_exit_conv | 216,614 | +8.31% | 2 | 50% | 345 |
| snake_abs_exit | 215,381 | +7.69% | 2 | 50% | 345 |
| intraweek | 214,164 | +7.08% | 30 | 53% | 3,302 |
| snake_abs | 212,982 | +6.49% | 1 | 100% | 255 |
| snake_abs_conv | 212,831 | +6.42% | 1 | 100% | 255 |
| oracle | 212,197 | +6.10% | 0 | - | 233 |
| intramonth | 211,648 | +5.82% | 0 | - | 235 |
| random_hold | 207,030 | +3.52% | 9 | 67% | 709 |
| snake_anaconda | 203,220 | +1.61% | 3 | 33% | 374 |
| snake_viper_wild | 201,997 | +1.00% | 10 | 50% | 1,825 |
| benchmark_smallcap | 201,860 | +0.93% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 198,563 | -0.72% | 9 | 44% | 1,639 |
| gold | 189,881 | -5.06% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,427 (-4.29%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,705 | +2.22% |
| snake_viper_wild | +4,567 | +2.31% |
| snake_viper_tick | +4,486 | +2.31% |
| snake_anaconda | +3,754 | +1.88% |
| benchmark_smallcap | +3,688 | +1.86% |
| snake_abs_exit | +3,397 | +1.60% |
| snake_abs_conv | +3,354 | +1.60% |
| snake_abs | +3,336 | +1.59% |
| benchmark | +3,289 | +1.51% |
| oracle | +2,279 | +1.08% |
| random_hold | +2,069 | +1.01% |
| intramonth | +1,039 | +0.49% |
| unified | +939 | +0.43% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -378 | -0.18% |
| gold | -2,252 | -1.17% |

Average per day so far: benchmark Rs +690, unified Rs +667, snake_abs_exit_conv Rs +593, snake_abs_exit Rs +549, snake_abs_conv Rs +458, intraweek Rs +457, snake_abs Rs +448, oracle Rs +393, intramonth Rs +376, random_hold Rs +227, snake_anaconda Rs +124, snake_viper_wild Rs +87, benchmark_smallcap Rs +69, nifty_calls Rs +59, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -72, gold Rs -326, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.