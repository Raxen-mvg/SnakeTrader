# Paper trading report

Updated 2026-11-04 14:19 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,910 | +7.46% | 0 | - | 236 |
| snake_abs_exit_conv | 214,216 | +7.11% | 1 | 100% | 255 |
| snake_abs_exit | 214,094 | +7.05% | 1 | 100% | 260 |
| snake_abs | 211,100 | +5.55% | 1 | 100% | 255 |
| snake_abs_conv | 210,952 | +5.48% | 1 | 100% | 255 |
| intraweek | 209,553 | +4.78% | 25 | 48% | 2,757 |
| benchmark | 208,491 | +4.25% | 0 | - | 237 |
| snake_viper_wild | 207,630 | +3.81% | 3 | 33% | 702 |
| intramonth | 207,444 | +3.72% | 0 | - | 235 |
| snake_viper_tick | 204,008 | +2.00% | 2 | 0% | 532 |
| random_hold | 203,098 | +1.55% | 8 | 62% | 649 |
| snake_anaconda | 202,671 | +1.34% | 3 | 33% | 361 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,358 | +0.68% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,054 | -1.97% | 0 | - | 237 |
| gold | 191,410 | -4.29% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,846 (-5.08%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +10,079 | +4.94% |
| snake_abs_exit_conv | +9,878 | +4.83% |
| snake_abs_conv | +9,811 | +4.88% |
| snake_abs | +9,790 | +4.86% |
| snake_anaconda | +8,847 | +4.56% |
| gold | +6,132 | +3.31% |
| intraweek | +4,468 | +2.18% |
| intramonth | +3,473 | +1.70% |
| benchmark_smallcap | +3,116 | +1.61% |
| unified | +2,909 | +1.37% |
| random_hold | +2,630 | +1.31% |
| benchmark | +1,790 | +0.87% |
| oracle | +1,369 | +0.68% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,159 | -1.52% |
| snake_viper_wild | -3,263 | -1.55% |

Average per day so far: snake_abs_exit_conv Rs +592, snake_abs_exit Rs +587, unified Rs +552, snake_abs_conv Rs +456, snake_abs Rs +444, snake_viper_wild Rs +402, intraweek Rs +354, benchmark Rs +314, intramonth Rs +276, snake_viper_tick Rs +250, snake_anaconda Rs +121, random_hold Rs +115, nifty_calls Rs +68, oracle Rs +50, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -172, gold Rs -318, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.