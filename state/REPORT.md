# Paper trading report

Updated 2026-11-26 11:33 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,811 | +12.90% | 0 | - | 237 |
| unified | 223,366 | +11.68% | 0 | - | 236 |
| oracle | 213,047 | +6.52% | 0 | - | 233 |
| intramonth | 210,624 | +5.31% | 0 | - | 235 |
| random_hold | 209,803 | +4.90% | 13 | 69% | 1,037 |
| intraweek | 208,349 | +4.17% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,641 | +0.82% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,074 | +0.54% | 2 | 50% | 345 |
| benchmark_smallcap | 200,448 | +0.22% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,388 | -0.31% | 1 | 100% | 255 |
| snake_abs_conv | 199,198 | -0.40% | 1 | 100% | 255 |
| snake_viper_wild | 193,329 | -3.34% | 16 | 50% | 2,827 |
| snake_anaconda | 193,224 | -3.39% | 3 | 33% | 374 |
| snake_viper_tick | 190,041 | -4.98% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,980 | -16.51% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,867 (-5.57%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,384 | +1.45% |
| benchmark_smallcap | +1,637 | +0.82% |
| intraweek | +1,605 | +0.78% |
| benchmark | +788 | +0.35% |
| random_hold | +311 | +0.15% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -615 | -0.30% |
| unified | -734 | -0.33% |
| oracle | -748 | -0.35% |
| snake_abs | -762 | -0.38% |
| snake_abs_conv | -774 | -0.39% |
| snake_abs_exit_conv | -902 | -0.45% |
| intramonth | -1,069 | -0.51% |
| snake_anaconda | -1,329 | -0.68% |
| snake_viper_tick | -4,136 | -2.13% |
| snake_viper_wild | -4,215 | -2.13% |

Average per day so far: benchmark Rs +630, unified Rs +570, oracle Rs +318, intramonth Rs +259, random_hold Rs +239, intraweek Rs +204, nifty_calls Rs +45, snake_abs_exit Rs +43, snake_abs_exit_conv Rs +28, benchmark_smallcap Rs +12, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -16, snake_abs_conv Rs -21, snake_anaconda Rs -188, snake_viper_wild Rs -202, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -332, gold Rs -805

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.