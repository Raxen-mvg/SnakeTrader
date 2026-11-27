# Paper trading report

Updated 2026-11-27 14:49 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 223,707 | +11.85% | 0 | - | 237 |
| unified | 223,598 | +11.80% | 0 | - | 236 |
| oracle | 211,997 | +6.00% | 0 | - | 233 |
| random_hold | 211,272 | +5.64% | 13 | 69% | 1,037 |
| intramonth | 210,896 | +5.45% | 0 | - | 235 |
| intraweek | 207,592 | +3.80% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 206,471 | +3.24% | 2 | 50% | 345 |
| snake_abs_exit | 204,174 | +2.09% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,603 | +0.80% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,685 | -0.16% | 1 | 100% | 255 |
| snake_abs_conv | 199,501 | -0.25% | 1 | 100% | 255 |
| snake_anaconda | 193,127 | -3.44% | 3 | 33% | 374 |
| snake_viper_wild | 192,198 | -3.90% | 16 | 50% | 2,827 |
| snake_viper_tick | 188,934 | -5.53% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 171,041 | -14.48% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,977 (-5.51%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +6,074 | +3.03% |
| gold | +5,047 | +3.04% |
| snake_abs_exit | +3,097 | +1.54% |
| random_hold | +2,678 | +1.28% |
| snake_abs_conv | +1,134 | +0.57% |
| snake_abs | +1,132 | +0.57% |
| snake_anaconda | +830 | +0.43% |
| benchmark_smallcap | +762 | +0.38% |
| intraweek | +543 | +0.26% |
| unified | +519 | +0.23% |
| intramonth | +363 | +0.17% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_viper_tick | -7 | -0.00% |
| snake_viper_wild | -8 | -0.00% |
| oracle | -238 | -0.11% |
| benchmark | -2,280 | -1.01% |

Average per day so far: benchmark Rs +564, unified Rs +562, oracle Rs +286, random_hold Rs +268, intramonth Rs +259, intraweek Rs +181, snake_abs_exit_conv Rs +166, snake_abs_exit Rs +107, nifty_calls Rs +44, benchmark_smallcap Rs +42, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -8, snake_abs_conv Rs -13, snake_anaconda Rs -186, snake_viper_wild Rs -229, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -357, gold Rs -690

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.