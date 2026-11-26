# Paper trading report

Updated 2026-11-26 10:27 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,620 | +12.81% | 0 | - | 237 |
| unified | 223,636 | +11.82% | 0 | - | 236 |
| oracle | 213,087 | +6.54% | 0 | - | 233 |
| intramonth | 210,909 | +5.45% | 0 | - | 235 |
| random_hold | 209,918 | +4.96% | 13 | 69% | 1,037 |
| intraweek | 207,649 | +3.83% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,783 | +1.39% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,158 | +1.08% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,672 | +0.34% | 0 | - | 237 |
| snake_abs | 200,261 | +0.13% | 1 | 100% | 255 |
| snake_abs_conv | 200,083 | +0.04% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,074 | -2.96% | 3 | 33% | 374 |
| snake_viper_wild | 193,295 | -3.35% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,008 | -5.00% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,704 | -16.15% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,007 (-5.50%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +3,107 | +1.89% |
| benchmark_smallcap | +1,861 | +0.94% |
| intraweek | +906 | +0.44% |
| benchmark | +597 | +0.27% |
| snake_abs_exit | +527 | +0.26% |
| random_hold | +425 | +0.20% |
| snake_abs_exit_conv | +182 | +0.09% |
| snake_abs_conv | +111 | +0.06% |
| snake_abs | +111 | +0.06% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -464 | -0.21% |
| snake_anaconda | -479 | -0.25% |
| oracle | -708 | -0.33% |
| intramonth | -784 | -0.37% |
| snake_viper_tick | -4,169 | -2.15% |
| snake_viper_wild | -4,248 | -2.15% |

Average per day so far: benchmark Rs +625, unified Rs +576, oracle Rs +319, intramonth Rs +266, random_hold Rs +242, intraweek Rs +187, snake_abs_exit Rs +73, snake_abs_exit_conv Rs +57, nifty_calls Rs +45, benchmark_smallcap Rs +18, snake_abs Rs +7, snake_abs_conv Rs +2, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -165, snake_viper_wild Rs -203, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -333, gold Rs -788

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.