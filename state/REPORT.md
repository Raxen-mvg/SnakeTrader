# Paper trading report

Updated 2026-11-19 10:39 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,827 | +11.91% | 0 | - | 236 |
| benchmark | 220,609 | +10.30% | 0 | - | 237 |
| intramonth | 213,382 | +6.69% | 0 | - | 235 |
| snake_abs_exit | 213,331 | +6.67% | 2 | 50% | 345 |
| intraweek | 211,870 | +5.93% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,560 | +5.78% | 2 | 50% | 345 |
| oracle | 210,895 | +5.45% | 0 | - | 233 |
| snake_abs | 209,122 | +4.56% | 1 | 100% | 255 |
| snake_abs_conv | 208,995 | +4.50% | 1 | 100% | 255 |
| snake_viper_wild | 207,720 | +3.86% | 16 | 50% | 2,827 |
| random_hold | 207,696 | +3.85% | 10 | 70% | 733 |
| snake_viper_tick | 204,170 | +2.08% | 15 | 47% | 2,625 |
| snake_anaconda | 203,277 | +1.64% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,212 | +0.11% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,003 | -12.50% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,210 (-4.39%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,216 | +0.55% |
| intramonth | +1,108 | +0.52% |
| benchmark_smallcap | +886 | +0.44% |
| random_hold | +764 | +0.37% |
| snake_viper_wild | +680 | +0.33% |
| snake_viper_tick | +666 | +0.33% |
| benchmark | +314 | +0.14% |
| oracle | +99 | +0.05% |
| intraweek | +31 | +0.01% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -314 | -0.15% |
| snake_abs_conv | -330 | -0.16% |
| snake_abs_exit | -700 | -0.33% |
| snake_abs_exit_conv | -823 | -0.39% |
| snake_anaconda | -1,124 | -0.55% |
| gold | -2,318 | -1.31% |

Average per day so far: unified Rs +644, benchmark Rs +557, snake_abs_exit Rs +392, intramonth Rs +362, snake_abs_exit_conv Rs +340, intraweek Rs +321, oracle Rs +294, snake_viper_wild Rs +266, snake_abs_conv Rs +265, snake_abs Rs +261, random_hold Rs +208, snake_viper_tick Rs +160, snake_anaconda Rs +102, nifty_calls Rs +50, benchmark_smallcap Rs +6, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -676

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.