# Paper trading report

Updated 2026-11-25 14:43 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,457 | +12.23% | 0 | - | 237 |
| unified | 224,366 | +12.18% | 0 | - | 236 |
| oracle | 212,801 | +6.40% | 0 | - | 233 |
| intramonth | 211,831 | +5.92% | 0 | - | 235 |
| random_hold | 210,083 | +5.04% | 12 | 75% | 1,009 |
| intraweek | 207,423 | +3.71% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,532 | +0.77% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,240 | +0.62% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,674 | -0.16% | 1 | 100% | 255 |
| snake_abs_conv | 199,479 | -0.26% | 1 | 100% | 255 |
| benchmark_smallcap | 198,834 | -0.58% | 0 | - | 237 |
| snake_viper_wild | 197,433 | -1.28% | 16 | 50% | 2,827 |
| snake_viper_tick | 194,069 | -2.97% | 15 | 47% | 2,625 |
| snake_anaconda | 193,405 | -3.30% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,254 | -17.37% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,996 (-5.50%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,984 | +1.35% |
| random_hold | +1,656 | +0.80% |
| oracle | +459 | +0.22% |
| unified | +80 | +0.04% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -146 | -0.07% |
| intramonth | -921 | -0.43% |
| snake_viper_tick | -3,624 | -1.83% |
| snake_viper_wild | -3,691 | -1.83% |
| gold | -4,176 | -2.46% |
| intraweek | -4,196 | -1.98% |
| snake_anaconda | -5,298 | -2.67% |
| snake_abs | -5,787 | -2.82% |
| snake_abs_exit_conv | -5,805 | -2.80% |
| snake_abs_conv | -5,824 | -2.84% |
| snake_abs_exit | -5,963 | -2.87% |

Average per day so far: benchmark Rs +611, unified Rs +609, oracle Rs +320, intramonth Rs +296, random_hold Rs +252, intraweek Rs +186, nifty_calls Rs +46, snake_abs_exit Rs +41, snake_abs_exit_conv Rs +34, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -9, snake_abs_conv Rs -14, benchmark_smallcap Rs -32, snake_viper_wild Rs -80, snake_anaconda Rs -188, snake_viper_tick Rs -205, snake_nonews Rs -292, snake Rs -311, gold Rs -869

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.