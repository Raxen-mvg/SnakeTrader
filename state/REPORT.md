# Paper trading report

Updated 2026-11-27 12:49 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,426 | +12.21% | 0 | - | 237 |
| unified | 223,340 | +11.67% | 0 | - | 236 |
| oracle | 211,999 | +6.00% | 0 | - | 233 |
| intramonth | 210,900 | +5.45% | 0 | - | 235 |
| random_hold | 210,554 | +5.28% | 13 | 69% | 1,037 |
| intraweek | 208,294 | +4.15% | 40 | 55% | 4,400 |
| snake_abs_exit | 204,982 | +2.49% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,650 | +1.82% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,681 | +0.84% | 0 | - | 237 |
| snake_abs | 200,483 | +0.24% | 1 | 100% | 255 |
| snake_abs_conv | 200,304 | +0.15% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,902 | -3.05% | 3 | 33% | 374 |
| snake_viper_wild | 192,390 | -3.81% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,122 | -5.44% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,808 | -15.10% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,878 (-5.56%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +3,904 | +1.94% |
| gold | +3,814 | +2.30% |
| snake_abs_exit_conv | +3,253 | +1.62% |
| random_hold | +1,960 | +0.94% |
| snake_abs_conv | +1,937 | +0.98% |
| snake_abs | +1,931 | +0.97% |
| snake_anaconda | +1,605 | +0.83% |
| intraweek | +1,246 | +0.60% |
| benchmark_smallcap | +841 | +0.42% |
| intramonth | +366 | +0.17% |
| unified | +262 | +0.12% |
| snake_viper_wild | +184 | +0.10% |
| snake_viper_tick | +181 | +0.10% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -236 | -0.11% |
| benchmark | -1,561 | -0.69% |

Average per day so far: benchmark Rs +582, unified Rs +556, oracle Rs +286, intramonth Rs +260, random_hold Rs +251, intraweek Rs +197, snake_abs_exit Rs +128, snake_abs_exit_conv Rs +94, benchmark_smallcap Rs +44, nifty_calls Rs +44, snake_abs Rs +12, snake_abs_conv Rs +8, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -165, snake_viper_wild Rs -224, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -351, gold Rs -719

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.