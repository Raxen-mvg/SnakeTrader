# Paper trading report

Updated 2026-11-26 09:31 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,352 | +12.68% | 0 | - | 237 |
| unified | 224,137 | +12.07% | 0 | - | 236 |
| oracle | 213,939 | +6.97% | 0 | - | 233 |
| intramonth | 211,829 | +5.91% | 0 | - | 235 |
| random_hold | 210,153 | +5.08% | 13 | 69% | 1,037 |
| intraweek | 207,735 | +3.87% | 40 | 55% | 4,400 |
| snake_abs_exit | 204,085 | +2.04% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,469 | +1.74% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,217 | +0.61% | 1 | 100% | 255 |
| snake_abs_conv | 201,046 | +0.52% | 1 | 100% | 255 |
| benchmark_smallcap | 200,538 | +0.27% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,814 | -1.59% | 16 | 50% | 2,827 |
| snake_anaconda | 195,677 | -2.16% | 3 | 33% | 374 |
| snake_viper_tick | 193,462 | -3.27% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,898 | -16.55% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,503 (-5.25%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,302 | +1.40% |
| snake_abs_exit | +1,829 | +0.90% |
| benchmark_smallcap | +1,726 | +0.87% |
| snake_abs_exit_conv | +1,494 | +0.74% |
| snake_anaconda | +1,124 | +0.58% |
| snake_abs_conv | +1,074 | +0.54% |
| snake_abs | +1,067 | +0.53% |
| intraweek | +992 | +0.48% |
| random_hold | +660 | +0.32% |
| benchmark | +329 | +0.15% |
| oracle | +144 | +0.07% |
| intramonth | +136 | +0.06% |
| unified | +37 | +0.02% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -714 | -0.37% |
| snake_viper_wild | -730 | -0.37% |

Average per day so far: benchmark Rs +618, unified Rs +589, oracle Rs +340, intramonth Rs +289, random_hold Rs +248, intraweek Rs +189, snake_abs_exit Rs +107, snake_abs_exit_conv Rs +91, nifty_calls Rs +45, snake_abs Rs +31, snake_abs_conv Rs +28, benchmark_smallcap Rs +15, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_viper_wild Rs -97, snake_anaconda Rs -120, snake_viper_tick Rs -218, snake_nonews Rs -284, snake Rs -304, gold Rs -807

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.