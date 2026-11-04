# Paper trading report

Updated 2026-11-04 13:34 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,966 | +6.98% | 0 | - | 236 |
| snake_abs_exit_conv | 212,503 | +6.25% | 1 | 100% | 255 |
| snake_abs_exit | 212,372 | +6.19% | 1 | 100% | 260 |
| snake_abs | 209,405 | +4.70% | 1 | 100% | 255 |
| intraweek | 209,257 | +4.63% | 25 | 48% | 2,757 |
| snake_abs_conv | 209,250 | +4.62% | 1 | 100% | 255 |
| benchmark | 208,445 | +4.22% | 0 | - | 237 |
| snake_viper_wild | 206,975 | +3.49% | 3 | 33% | 702 |
| intramonth | 206,176 | +3.09% | 0 | - | 235 |
| snake_viper_tick | 203,369 | +1.69% | 2 | 0% | 532 |
| random_hold | 202,652 | +1.33% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,240 | +0.62% | 0 | - | 233 |
| snake_anaconda | 201,043 | +0.52% | 3 | 33% | 361 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 195,717 | -2.14% | 0 | - | 237 |
| gold | 190,785 | -4.61% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,246 (-5.38%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +8,358 | +4.10% |
| snake_abs_exit_conv | +8,165 | +4.00% |
| snake_abs_conv | +8,109 | +4.03% |
| snake_abs | +8,096 | +4.02% |
| snake_anaconda | +7,218 | +3.72% |
| gold | +5,507 | +2.97% |
| intraweek | +4,172 | +2.03% |
| benchmark_smallcap | +2,780 | +1.44% |
| intramonth | +2,205 | +1.08% |
| random_hold | +2,184 | +1.09% |
| unified | +1,965 | +0.93% |
| benchmark | +1,744 | +0.84% |
| oracle | +1,251 | +0.62% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,798 | -1.83% |
| snake_viper_wild | -3,917 | -1.86% |

Average per day so far: snake_abs_exit_conv Rs +521, unified Rs +517, snake_abs_exit Rs +516, snake_abs_conv Rs +385, snake_abs Rs +376, snake_viper_wild Rs +367, intraweek Rs +343, benchmark Rs +313, intramonth Rs +229, snake_viper_tick Rs +211, random_hold Rs +98, nifty_calls Rs +68, snake_anaconda Rs +47, oracle Rs +46, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -186, gold Rs -341, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.