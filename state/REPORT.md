# Paper trading report

Updated 2026-11-26 13:55 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,138 | +12.57% | 0 | - | 237 |
| unified | 223,120 | +11.56% | 0 | - | 236 |
| oracle | 212,863 | +6.43% | 0 | - | 233 |
| intramonth | 210,252 | +5.13% | 0 | - | 235 |
| random_hold | 209,205 | +4.60% | 13 | 69% | 1,037 |
| intraweek | 207,732 | +3.87% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,201 | +0.10% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit | 199,991 | -0.01% | 2 | 50% | 345 |
| snake_abs_exit_conv | 199,415 | -0.29% | 2 | 50% | 345 |
| snake_abs | 197,784 | -1.11% | 1 | 100% | 255 |
| snake_abs_conv | 197,577 | -1.21% | 1 | 100% | 255 |
| snake_viper_wild | 192,225 | -3.89% | 16 | 50% | 2,827 |
| snake_anaconda | 191,485 | -4.26% | 3 | 33% | 374 |
| snake_viper_tick | 188,960 | -5.52% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,142 | -16.93% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,434 (-5.78%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,545 | +0.94% |
| benchmark_smallcap | +1,390 | +0.70% |
| intraweek | +989 | +0.48% |
| benchmark | +115 | +0.05% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -288 | -0.14% |
| oracle | -932 | -0.44% |
| unified | -980 | -0.44% |
| intramonth | -1,441 | -0.68% |
| snake_abs_exit | -2,265 | -1.12% |
| snake_abs | -2,366 | -1.18% |
| snake_abs_conv | -2,395 | -1.20% |
| snake_abs_exit_conv | -2,561 | -1.27% |
| snake_anaconda | -3,068 | -1.58% |
| snake_viper_tick | -5,217 | -2.69% |
| snake_viper_wild | -5,319 | -2.69% |

Average per day so far: benchmark Rs +613, unified Rs +564, oracle Rs +314, intramonth Rs +250, random_hold Rs +225, intraweek Rs +189, nifty_calls Rs +45, benchmark_smallcap Rs +5, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_abs_exit Rs -0, snake_abs_exit_conv Rs -15, snake_abs Rs -57, snake_abs_conv Rs -64, snake_viper_wild Rs -236, snake_anaconda Rs -237, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -368, gold Rs -826

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.