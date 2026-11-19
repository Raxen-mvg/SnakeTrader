# Paper trading report

Updated 2026-11-19 15:11 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,670 | +12.34% | 0 | - | 236 |
| benchmark | 222,475 | +11.24% | 0 | - | 237 |
| intramonth | 214,077 | +7.04% | 0 | - | 235 |
| snake_abs_exit | 213,350 | +6.67% | 2 | 50% | 345 |
| intraweek | 212,788 | +6.39% | 35 | 54% | 3,851 |
| oracle | 212,106 | +6.05% | 0 | - | 233 |
| snake_abs_exit_conv | 211,078 | +5.54% | 2 | 50% | 345 |
| snake_abs | 208,826 | +4.41% | 1 | 100% | 255 |
| snake_abs_conv | 208,705 | +4.35% | 1 | 100% | 255 |
| random_hold | 208,437 | +4.22% | 10 | 70% | 733 |
| snake_viper_wild | 207,614 | +3.81% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,066 | +2.03% | 15 | 47% | 2,625 |
| snake_anaconda | 203,426 | +1.71% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,446 | +0.72% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,904 | -12.55% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,991 (-4.00%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,180 | +0.99% |
| benchmark_smallcap | +2,119 | +1.06% |
| unified | +2,058 | +0.93% |
| intramonth | +1,804 | +0.85% |
| random_hold | +1,504 | +0.73% |
| oracle | +1,310 | +0.62% |
| intraweek | +949 | +0.45% |
| snake_viper_wild | +575 | +0.28% |
| snake_viper_tick | +563 | +0.28% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -611 | -0.29% |
| snake_abs_conv | -620 | -0.30% |
| snake_abs_exit | -682 | -0.32% |
| snake_anaconda | -975 | -0.48% |
| snake_abs_exit_conv | -1,305 | -0.61% |
| gold | -2,417 | -1.36% |

Average per day so far: unified Rs +667, benchmark Rs +607, snake_abs_exit Rs +393, intramonth Rs +380, intraweek Rs +346, oracle Rs +327, snake_abs_exit_conv Rs +326, snake_viper_wild Rs +263, snake_abs_conv Rs +256, snake_abs Rs +252, random_hold Rs +228, snake_viper_tick Rs +156, snake_anaconda Rs +107, nifty_calls Rs +50, benchmark_smallcap Rs +44, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -678

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.