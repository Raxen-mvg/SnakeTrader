# Paper trading report

Updated 2026-11-27 11:40 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,296 | +12.15% | 0 | - | 237 |
| unified | 222,208 | +11.10% | 0 | - | 236 |
| oracle | 212,003 | +6.00% | 0 | - | 233 |
| intramonth | 210,398 | +5.20% | 0 | - | 235 |
| random_hold | 210,359 | +5.18% | 13 | 69% | 1,037 |
| intraweek | 207,750 | +3.88% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,783 | +2.89% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,292 | +2.15% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,793 | +0.90% | 0 | - | 237 |
| snake_abs | 200,979 | +0.49% | 1 | 100% | 255 |
| snake_abs_conv | 200,803 | +0.40% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,469 | -2.77% | 3 | 33% | 374 |
| snake_viper_wild | 193,206 | -3.40% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,921 | -5.04% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,117 | -15.44% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,516 (-5.74%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,706 | +2.34% |
| snake_abs_exit_conv | +3,895 | +1.94% |
| gold | +3,124 | +1.88% |
| snake_abs_conv | +2,436 | +1.23% |
| snake_abs | +2,426 | +1.22% |
| snake_anaconda | +2,173 | +1.13% |
| random_hold | +1,765 | +0.85% |
| snake_viper_wild | +1,000 | +0.52% |
| snake_viper_tick | +980 | +0.52% |
| benchmark_smallcap | +953 | +0.47% |
| intraweek | +702 | +0.34% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intramonth | -135 | -0.06% |
| oracle | -232 | -0.11% |
| unified | -871 | -0.39% |
| benchmark | -1,691 | -0.75% |

Average per day so far: benchmark Rs +578, unified Rs +529, oracle Rs +286, intramonth Rs +248, random_hold Rs +247, intraweek Rs +185, snake_abs_exit Rs +148, snake_abs_exit_conv Rs +110, benchmark_smallcap Rs +47, nifty_calls Rs +44, snake_abs Rs +24, snake_abs_conv Rs +21, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -149, snake_viper_wild Rs -200, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -325, gold Rs -735

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.