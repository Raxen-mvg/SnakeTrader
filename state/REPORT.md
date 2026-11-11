# Paper trading report

Updated 2026-11-11 14:45 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,153 | +10.08% | 0 | - | 236 |
| benchmark | 219,997 | +10.00% | 0 | - | 237 |
| snake_abs_exit_conv | 217,489 | +8.74% | 2 | 50% | 345 |
| snake_abs_exit | 216,665 | +8.33% | 2 | 50% | 345 |
| snake_abs | 214,235 | +7.12% | 1 | 100% | 255 |
| snake_abs_conv | 214,074 | +7.04% | 1 | 100% | 255 |
| intraweek | 213,298 | +6.65% | 30 | 53% | 3,302 |
| oracle | 211,610 | +5.80% | 0 | - | 233 |
| intramonth | 211,108 | +5.55% | 0 | - | 235 |
| random_hold | 207,106 | +3.55% | 9 | 67% | 709 |
| snake_viper_wild | 206,716 | +3.36% | 10 | 50% | 1,825 |
| snake_anaconda | 204,413 | +2.21% | 3 | 33% | 374 |
| snake_viper_tick | 203,182 | +1.59% | 9 | 44% | 1,639 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,289 | +0.64% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,322 | -5.34% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,127 (-4.44%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +9,286 | +4.70% |
| snake_viper_tick | +9,106 | +4.69% |
| snake_abs_exit_conv | +5,580 | +2.63% |
| snake_anaconda | +4,947 | +2.48% |
| snake_abs_exit | +4,681 | +2.21% |
| snake_abs_conv | +4,597 | +2.19% |
| snake_abs | +4,589 | +2.19% |
| benchmark_smallcap | +3,116 | +1.57% |
| random_hold | +2,146 | +1.05% |
| benchmark | +1,905 | +0.87% |
| oracle | +1,692 | +0.81% |
| intramonth | +499 | +0.24% |
| unified | +406 | +0.18% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -1,244 | -0.58% |
| gold | -2,811 | -1.46% |

Average per day so far: unified Rs +650, benchmark Rs +645, snake_abs_exit_conv Rs +625, snake_abs_exit Rs +595, snake_abs_conv Rs +503, snake_abs Rs +491, intraweek Rs +429, oracle Rs +375, intramonth Rs +358, snake_viper_wild Rs +292, random_hold Rs +229, snake_anaconda Rs +170, snake_viper_tick Rs +159, nifty_calls Rs +59, benchmark_smallcap Rs +48, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -344, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.