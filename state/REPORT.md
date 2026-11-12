# Paper trading report

Updated 2026-11-12 14:31 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,895 | +10.45% | 0 | - | 236 |
| benchmark | 220,379 | +10.19% | 0 | - | 237 |
| snake_abs_exit_conv | 218,404 | +9.20% | 2 | 50% | 345 |
| snake_abs_exit | 217,349 | +8.67% | 2 | 50% | 345 |
| snake_abs | 215,453 | +7.73% | 1 | 100% | 255 |
| snake_abs_conv | 215,278 | +7.64% | 1 | 100% | 255 |
| intraweek | 214,479 | +7.24% | 30 | 53% | 3,302 |
| oracle | 212,836 | +6.42% | 0 | - | 233 |
| intramonth | 211,656 | +5.83% | 0 | - | 235 |
| random_hold | 207,876 | +3.94% | 10 | 70% | 733 |
| snake_viper_wild | 206,677 | +3.34% | 10 | 50% | 1,825 |
| snake_anaconda | 206,100 | +3.05% | 3 | 33% | 374 |
| snake_viper_tick | 203,143 | +1.57% | 9 | 44% | 1,639 |
| benchmark_smallcap | 202,959 | +1.48% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,785 | -7.61% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,911 (-4.04%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,152 | +1.07% |
| snake_anaconda | +1,977 | +0.97% |
| snake_abs | +1,829 | +0.86% |
| snake_abs_conv | +1,821 | +0.85% |
| intraweek | +1,346 | +0.63% |
| snake_abs_exit_conv | +1,252 | +0.58% |
| snake_abs_exit | +1,187 | +0.55% |
| benchmark | +1,117 | +0.51% |
| unified | +1,081 | +0.49% |
| oracle | +833 | +0.39% |
| random_hold | +766 | +0.37% |
| intramonth | +660 | +0.31% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_wild | -65 | -0.03% |
| snake_viper_tick | -66 | -0.03% |
| gold | -4,800 | -2.53% |

Average per day so far: unified Rs +653, benchmark Rs +637, snake_abs_exit_conv Rs +635, snake_abs_exit Rs +598, snake_abs_conv Rs +527, snake_abs Rs +515, intraweek Rs +452, oracle Rs +401, intramonth Rs +364, snake_viper_wild Rs +278, random_hold Rs +246, snake_anaconda Rs +226, snake_viper_tick Rs +150, benchmark_smallcap Rs +106, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -475

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.