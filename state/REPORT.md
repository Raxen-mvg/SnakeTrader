# Paper trading report

Updated 2026-11-11 10:19 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,152 | +10.58% | 0 | - | 237 |
| unified | 220,286 | +10.14% | 0 | - | 236 |
| snake_abs_exit_conv | 216,076 | +8.04% | 2 | 50% | 345 |
| intraweek | 214,863 | +7.43% | 30 | 53% | 3,302 |
| snake_abs_exit | 214,589 | +7.29% | 2 | 50% | 345 |
| snake_abs | 212,754 | +6.38% | 1 | 100% | 255 |
| snake_abs_conv | 212,596 | +6.30% | 1 | 100% | 255 |
| oracle | 211,176 | +5.59% | 0 | - | 233 |
| intramonth | 210,880 | +5.44% | 0 | - | 235 |
| random_hold | 206,359 | +3.18% | 9 | 67% | 709 |
| snake_anaconda | 202,423 | +1.21% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,333 | +0.67% | 0 | - | 237 |
| snake_viper_wild | 200,471 | +0.23% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 197,067 | -1.47% | 9 | 44% | 1,639 |
| gold | 189,322 | -5.34% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,149 (-4.43%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,167 | +1.97% |
| benchmark_smallcap | +3,161 | +1.59% |
| snake_abs_conv | +3,118 | +1.49% |
| snake_abs | +3,107 | +1.48% |
| benchmark | +3,060 | +1.40% |
| snake_viper_wild | +3,041 | +1.54% |
| snake_viper_tick | +2,991 | +1.54% |
| snake_anaconda | +2,957 | +1.48% |
| snake_abs_exit | +2,605 | +1.23% |
| random_hold | +1,399 | +0.68% |
| oracle | +1,258 | +0.60% |
| unified | +539 | +0.24% |
| intraweek | +321 | +0.15% |
| intramonth | +271 | +0.13% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -2,811 | -1.46% |

Average per day so far: benchmark Rs +682, unified Rs +654, snake_abs_exit_conv Rs +574, snake_abs_exit Rs +521, intraweek Rs +479, snake_abs_conv Rs +450, snake_abs Rs +440, oracle Rs +361, intramonth Rs +351, random_hold Rs +205, snake_anaconda Rs +93, nifty_calls Rs +59, benchmark_smallcap Rs +49, snake_viper_wild Rs +20, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -147, gold Rs -344, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.