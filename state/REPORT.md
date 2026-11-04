# Paper trading report

Updated 2026-11-04 13:43 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,049 | +7.02% | 0 | - | 236 |
| snake_abs_exit_conv | 212,494 | +6.25% | 1 | 100% | 255 |
| snake_abs_exit | 212,362 | +6.18% | 1 | 100% | 260 |
| snake_abs | 209,395 | +4.70% | 1 | 100% | 255 |
| intraweek | 209,306 | +4.65% | 25 | 48% | 2,757 |
| snake_abs_conv | 209,240 | +4.62% | 1 | 100% | 255 |
| benchmark | 208,606 | +4.30% | 0 | - | 237 |
| snake_viper_wild | 207,157 | +3.58% | 3 | 33% | 702 |
| intramonth | 206,299 | +3.15% | 0 | - | 235 |
| snake_viper_tick | 203,548 | +1.77% | 2 | 0% | 532 |
| random_hold | 202,638 | +1.32% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,287 | +0.64% | 0 | - | 233 |
| snake_anaconda | 201,032 | +0.52% | 3 | 33% | 361 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,065 | -1.97% | 0 | - | 237 |
| gold | 191,410 | -4.29% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,339 (-5.33%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +8,347 | +4.09% |
| snake_abs_exit_conv | +8,155 | +3.99% |
| snake_abs_conv | +8,099 | +4.03% |
| snake_abs | +8,085 | +4.02% |
| snake_anaconda | +7,208 | +3.72% |
| gold | +6,132 | +3.31% |
| intraweek | +4,220 | +2.06% |
| benchmark_smallcap | +3,128 | +1.62% |
| intramonth | +2,328 | +1.14% |
| random_hold | +2,170 | +1.08% |
| unified | +2,048 | +0.97% |
| benchmark | +1,905 | +0.92% |
| oracle | +1,298 | +0.65% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,619 | -1.75% |
| snake_viper_wild | -3,735 | -1.77% |

Average per day so far: snake_abs_exit_conv Rs +521, unified Rs +520, snake_abs_exit Rs +515, snake_abs_conv Rs +385, snake_viper_wild Rs +377, snake_abs Rs +376, intraweek Rs +345, benchmark Rs +319, intramonth Rs +233, snake_viper_tick Rs +222, random_hold Rs +98, nifty_calls Rs +68, oracle Rs +48, snake_anaconda Rs +47, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -171, gold Rs -318, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.