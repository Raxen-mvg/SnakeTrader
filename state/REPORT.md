# Paper trading report

Updated 2026-11-26 14:19 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,421 | +12.71% | 0 | - | 237 |
| unified | 223,255 | +11.63% | 0 | - | 236 |
| oracle | 213,027 | +6.51% | 0 | - | 233 |
| intramonth | 210,496 | +5.25% | 0 | - | 235 |
| random_hold | 209,325 | +4.66% | 13 | 69% | 1,037 |
| intraweek | 207,885 | +3.94% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,336 | +0.17% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit | 199,908 | -0.05% | 2 | 50% | 345 |
| snake_abs_exit_conv | 199,337 | -0.33% | 2 | 50% | 345 |
| snake_abs | 197,647 | -1.18% | 1 | 100% | 255 |
| snake_abs_conv | 197,439 | -1.28% | 1 | 100% | 255 |
| snake_viper_wild | 192,359 | -3.82% | 16 | 50% | 2,827 |
| snake_anaconda | 191,401 | -4.30% | 3 | 33% | 374 |
| snake_viper_tick | 189,092 | -5.45% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,586 | -16.71% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,553 (-5.72%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,989 | +1.21% |
| benchmark_smallcap | +1,525 | +0.77% |
| intraweek | +1,142 | +0.55% |
| benchmark | +398 | +0.18% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -167 | -0.08% |
| oracle | -769 | -0.36% |
| unified | -845 | -0.38% |
| intramonth | -1,197 | -0.56% |
| snake_abs_exit | -2,347 | -1.16% |
| snake_abs | -2,503 | -1.25% |
| snake_abs_conv | -2,533 | -1.27% |
| snake_abs_exit_conv | -2,639 | -1.31% |
| snake_anaconda | -3,152 | -1.62% |
| snake_viper_tick | -5,085 | -2.62% |
| snake_viper_wild | -5,184 | -2.62% |

Average per day so far: benchmark Rs +620, unified Rs +567, oracle Rs +318, intramonth Rs +256, random_hold Rs +227, intraweek Rs +192, nifty_calls Rs +45, benchmark_smallcap Rs +9, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_abs_exit Rs -2, snake_abs_exit_conv Rs -17, snake_abs Rs -60, snake_abs_conv Rs -67, snake_viper_wild Rs -232, snake_anaconda Rs -239, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -364, gold Rs -815

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.