# Paper trading report

Updated 2026-11-19 15:08 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,613 | +12.31% | 0 | - | 236 |
| benchmark | 222,361 | +11.18% | 0 | - | 237 |
| intramonth | 214,028 | +7.01% | 0 | - | 235 |
| snake_abs_exit | 213,678 | +6.84% | 2 | 50% | 345 |
| intraweek | 212,893 | +6.45% | 35 | 54% | 3,851 |
| oracle | 212,053 | +6.03% | 0 | - | 233 |
| snake_abs_exit_conv | 211,397 | +5.70% | 2 | 50% | 345 |
| snake_abs | 209,034 | +4.52% | 1 | 100% | 255 |
| snake_abs_conv | 208,917 | +4.46% | 1 | 100% | 255 |
| random_hold | 208,394 | +4.20% | 10 | 70% | 733 |
| snake_viper_wild | 207,710 | +3.85% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,160 | +2.08% | 15 | 47% | 2,625 |
| snake_anaconda | 203,729 | +1.86% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,401 | +0.70% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,855 | -12.57% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,983 (-4.01%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,074 | +1.04% |
| benchmark | +2,065 | +0.94% |
| unified | +2,002 | +0.90% |
| intramonth | +1,754 | +0.83% |
| random_hold | +1,462 | +0.71% |
| oracle | +1,257 | +0.60% |
| intraweek | +1,054 | +0.50% |
| snake_viper_wild | +671 | +0.32% |
| snake_viper_tick | +657 | +0.32% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs_exit | -353 | -0.17% |
| snake_abs | -403 | -0.19% |
| snake_abs_conv | -408 | -0.20% |
| snake_anaconda | -672 | -0.33% |
| snake_abs_exit_conv | -986 | -0.46% |
| gold | -2,466 | -1.39% |

Average per day so far: unified Rs +665, benchmark Rs +604, snake_abs_exit Rs +402, intramonth Rs +379, intraweek Rs +348, snake_abs_exit_conv Rs +335, oracle Rs +326, snake_viper_wild Rs +266, snake_abs_conv Rs +262, snake_abs Rs +258, random_hold Rs +227, snake_viper_tick Rs +160, snake_anaconda Rs +117, nifty_calls Rs +50, benchmark_smallcap Rs +42, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -680

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.