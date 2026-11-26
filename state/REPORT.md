# Paper trading report

Updated 2026-11-26 13:38 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,390 | +12.70% | 0 | - | 237 |
| unified | 223,120 | +11.56% | 0 | - | 236 |
| oracle | 212,984 | +6.49% | 0 | - | 233 |
| intramonth | 210,313 | +5.16% | 0 | - | 235 |
| random_hold | 209,239 | +4.62% | 13 | 69% | 1,037 |
| intraweek | 207,909 | +3.95% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,414 | +0.21% | 0 | - | 237 |
| snake_abs_exit | 200,041 | +0.02% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit_conv | 199,456 | -0.27% | 2 | 50% | 345 |
| snake_abs | 197,783 | -1.11% | 1 | 100% | 255 |
| snake_abs_conv | 197,578 | -1.21% | 1 | 100% | 255 |
| snake_viper_wild | 192,038 | -3.98% | 16 | 50% | 2,827 |
| snake_anaconda | 191,460 | -4.27% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,777 | -5.61% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,306 | -16.85% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,504 (-5.75%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,710 | +1.04% |
| benchmark_smallcap | +1,603 | +0.81% |
| intraweek | +1,166 | +0.56% |
| benchmark | +367 | +0.16% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -254 | -0.12% |
| oracle | -811 | -0.38% |
| unified | -980 | -0.44% |
| intramonth | -1,380 | -0.65% |
| snake_abs_exit | -2,215 | -1.09% |
| snake_abs | -2,367 | -1.18% |
| snake_abs_conv | -2,395 | -1.20% |
| snake_abs_exit_conv | -2,519 | -1.25% |
| snake_anaconda | -3,093 | -1.59% |
| snake_viper_tick | -5,400 | -2.78% |
| snake_viper_wild | -5,506 | -2.79% |

Average per day so far: benchmark Rs +619, unified Rs +564, oracle Rs +317, intramonth Rs +252, random_hold Rs +225, intraweek Rs +193, nifty_calls Rs +45, benchmark_smallcap Rs +11, snake_abs_exit Rs +1, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_abs_exit_conv Rs -14, snake_abs Rs -57, snake_abs_conv Rs -64, snake_anaconda Rs -237, snake_viper_wild Rs -241, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -374, gold Rs -822

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.