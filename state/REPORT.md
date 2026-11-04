# Paper trading report

Updated 2026-11-04 13:07 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,745 | +6.87% | 0 | - | 236 |
| snake_abs_exit_conv | 212,530 | +6.26% | 1 | 100% | 255 |
| snake_abs_exit | 212,368 | +6.18% | 1 | 100% | 260 |
| intraweek | 209,563 | +4.78% | 25 | 48% | 2,757 |
| snake_abs | 209,429 | +4.71% | 1 | 100% | 255 |
| snake_abs_conv | 209,276 | +4.64% | 1 | 100% | 255 |
| benchmark | 207,933 | +3.97% | 0 | - | 237 |
| snake_viper_wild | 207,079 | +3.54% | 3 | 33% | 702 |
| intramonth | 206,058 | +3.03% | 0 | - | 235 |
| snake_viper_tick | 203,471 | +1.74% | 2 | 0% | 532 |
| random_hold | 202,571 | +1.29% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,068 | +0.53% | 0 | - | 233 |
| snake_anaconda | 201,037 | +0.52% | 3 | 33% | 361 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 195,067 | -2.47% | 0 | - | 237 |
| gold | 191,032 | -4.48% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,255 (-5.37%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +8,353 | +4.09% |
| snake_abs_exit_conv | +8,192 | +4.01% |
| snake_abs_conv | +8,135 | +4.04% |
| snake_abs | +8,120 | +4.03% |
| snake_anaconda | +7,213 | +3.72% |
| gold | +5,754 | +3.11% |
| intraweek | +4,478 | +2.18% |
| benchmark_smallcap | +2,130 | +1.10% |
| random_hold | +2,103 | +1.05% |
| intramonth | +2,087 | +1.02% |
| unified | +1,744 | +0.82% |
| benchmark | +1,232 | +0.60% |
| oracle | +1,078 | +0.54% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,695 | -1.78% |
| snake_viper_wild | -3,813 | -1.81% |

Average per day so far: snake_abs_exit_conv Rs +522, snake_abs_exit Rs +515, unified Rs +509, snake_abs_conv Rs +387, snake_abs Rs +377, snake_viper_wild Rs +373, intraweek Rs +354, benchmark Rs +294, intramonth Rs +224, snake_viper_tick Rs +217, random_hold Rs +95, nifty_calls Rs +68, snake_anaconda Rs +47, oracle Rs +40, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -214, gold Rs -332, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.