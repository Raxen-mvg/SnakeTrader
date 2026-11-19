# Paper trading report

Updated 2026-11-19 10:28 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,573 | +11.79% | 0 | - | 236 |
| benchmark | 220,479 | +10.24% | 0 | - | 237 |
| snake_abs_exit | 213,634 | +6.82% | 2 | 50% | 345 |
| intramonth | 213,126 | +6.56% | 0 | - | 235 |
| intraweek | 211,854 | +5.93% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,807 | +5.90% | 2 | 50% | 345 |
| oracle | 211,532 | +5.77% | 0 | - | 233 |
| snake_abs | 209,338 | +4.67% | 1 | 100% | 255 |
| snake_abs_conv | 209,216 | +4.61% | 1 | 100% | 255 |
| snake_viper_wild | 207,878 | +3.94% | 16 | 50% | 2,827 |
| random_hold | 207,762 | +3.88% | 10 | 70% | 733 |
| snake_viper_tick | 204,325 | +2.16% | 15 | 47% | 2,625 |
| snake_anaconda | 203,958 | +1.98% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,313 | +0.16% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,576 | -12.71% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,260 (-4.37%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +986 | +0.49% |
| unified | +962 | +0.43% |
| intramonth | +853 | +0.40% |
| snake_viper_wild | +839 | +0.41% |
| random_hold | +830 | +0.40% |
| snake_viper_tick | +822 | +0.40% |
| oracle | +736 | +0.35% |
| benchmark | +184 | +0.08% |
| intraweek | +15 | +0.01% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -98 | -0.05% |
| snake_abs_conv | -109 | -0.05% |
| snake_abs_exit | -398 | -0.19% |
| snake_anaconda | -443 | -0.22% |
| snake_abs_exit_conv | -576 | -0.27% |
| gold | -2,745 | -1.55% |

Average per day so far: unified Rs +637, benchmark Rs +553, snake_abs_exit Rs +401, intramonth Rs +355, snake_abs_exit_conv Rs +347, intraweek Rs +320, oracle Rs +312, snake_viper_wild Rs +272, snake_abs_conv Rs +271, snake_abs Rs +267, random_hold Rs +210, snake_viper_tick Rs +166, snake_anaconda Rs +124, nifty_calls Rs +50, benchmark_smallcap Rs +9, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -687

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.