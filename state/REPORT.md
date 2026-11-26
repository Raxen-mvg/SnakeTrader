# Paper trading report

Updated 2026-11-26 10:03 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,428 | +12.71% | 0 | - | 237 |
| unified | 223,973 | +11.99% | 0 | - | 236 |
| oracle | 213,690 | +6.84% | 0 | - | 233 |
| intramonth | 211,694 | +5.85% | 0 | - | 235 |
| random_hold | 210,265 | +5.13% | 13 | 69% | 1,037 |
| intraweek | 208,639 | +4.32% | 40 | 55% | 4,400 |
| snake_abs_exit | 203,194 | +1.60% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,526 | +1.26% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,672 | +0.34% | 0 | - | 237 |
| snake_abs | 200,551 | +0.28% | 1 | 100% | 255 |
| snake_abs_conv | 200,376 | +0.19% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 195,834 | -2.08% | 16 | 50% | 2,827 |
| snake_anaconda | 194,718 | -2.64% | 3 | 33% | 374 |
| snake_viper_tick | 192,504 | -3.75% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,852 | -16.07% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,456 (-5.27%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +3,255 | +1.98% |
| intraweek | +1,895 | +0.92% |
| benchmark_smallcap | +1,861 | +0.94% |
| snake_abs_exit | +938 | +0.46% |
| random_hold | +772 | +0.37% |
| snake_abs_exit_conv | +550 | +0.27% |
| benchmark | +405 | +0.18% |
| snake_abs_conv | +404 | +0.20% |
| snake_abs | +401 | +0.20% |
| snake_anaconda | +165 | +0.09% |
| intramonth | +1 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -106 | -0.05% |
| unified | -127 | -0.06% |
| snake_viper_tick | -1,673 | -0.86% |
| snake_viper_wild | -1,709 | -0.86% |

Average per day so far: benchmark Rs +620, unified Rs +585, oracle Rs +334, intramonth Rs +285, random_hold Rs +250, intraweek Rs +211, snake_abs_exit Rs +84, snake_abs_exit_conv Rs +66, nifty_calls Rs +45, benchmark_smallcap Rs +18, snake_abs Rs +14, snake_abs_conv Rs +10, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_viper_wild Rs -126, snake_anaconda Rs -147, snake_viper_tick Rs -250, snake_nonews Rs -284, snake Rs -304, gold Rs -784

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.