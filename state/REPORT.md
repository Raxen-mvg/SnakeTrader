# Paper trading report

Updated 2026-11-04 13:01 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,746 | +6.87% | 0 | - | 236 |
| snake_abs_exit_conv | 212,357 | +6.18% | 1 | 100% | 255 |
| snake_abs_exit | 212,202 | +6.10% | 1 | 100% | 260 |
| snake_abs | 209,261 | +4.63% | 1 | 100% | 255 |
| snake_abs_conv | 209,106 | +4.55% | 1 | 100% | 255 |
| intraweek | 208,775 | +4.39% | 25 | 48% | 2,757 |
| benchmark | 207,948 | +3.97% | 0 | - | 237 |
| snake_viper_wild | 207,178 | +3.59% | 3 | 33% | 702 |
| intramonth | 206,088 | +3.04% | 0 | - | 235 |
| snake_viper_tick | 203,568 | +1.78% | 2 | 0% | 532 |
| random_hold | 202,676 | +1.34% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,043 | +0.52% | 0 | - | 233 |
| snake_anaconda | 200,881 | +0.44% | 3 | 33% | 361 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 195,067 | -2.47% | 0 | - | 237 |
| gold | 190,720 | -4.64% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,180 (-5.41%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +8,188 | +4.01% |
| snake_abs_exit_conv | +8,018 | +3.92% |
| snake_abs_conv | +7,965 | +3.96% |
| snake_abs | +7,952 | +3.95% |
| snake_anaconda | +7,057 | +3.64% |
| gold | +5,442 | +2.94% |
| intraweek | +3,690 | +1.80% |
| random_hold | +2,207 | +1.10% |
| benchmark_smallcap | +2,130 | +1.10% |
| intramonth | +2,117 | +1.04% |
| unified | +1,745 | +0.82% |
| benchmark | +1,247 | +0.60% |
| oracle | +1,054 | +0.53% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,599 | -1.74% |
| snake_viper_wild | -3,714 | -1.76% |

Average per day so far: snake_abs_exit_conv Rs +515, unified Rs +509, snake_abs_exit Rs +508, snake_abs_conv Rs +379, snake_viper_wild Rs +378, snake_abs Rs +370, intraweek Rs +325, benchmark Rs +294, intramonth Rs +225, snake_viper_tick Rs +223, random_hold Rs +99, nifty_calls Rs +68, snake_anaconda Rs +40, oracle Rs +39, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -214, gold Rs -344, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.