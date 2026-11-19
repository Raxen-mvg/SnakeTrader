# Paper trading report

Updated 2026-11-19 13:49 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,919 | +11.96% | 0 | - | 236 |
| benchmark | 221,840 | +10.92% | 0 | - | 237 |
| intramonth | 213,469 | +6.73% | 0 | - | 235 |
| snake_abs_exit | 213,227 | +6.61% | 2 | 50% | 345 |
| intraweek | 211,945 | +5.97% | 35 | 54% | 3,851 |
| oracle | 211,588 | +5.79% | 0 | - | 233 |
| snake_abs_exit_conv | 210,947 | +5.47% | 2 | 50% | 345 |
| snake_abs | 208,799 | +4.40% | 1 | 100% | 255 |
| snake_abs_conv | 208,676 | +4.34% | 1 | 100% | 255 |
| random_hold | 207,763 | +3.88% | 10 | 70% | 733 |
| snake_viper_wild | 207,456 | +3.73% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,911 | +1.96% | 15 | 47% | 2,625 |
| snake_anaconda | 203,320 | +1.66% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,605 | +0.30% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,085 | -12.46% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,408 (-4.30%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,545 | +0.70% |
| unified | +1,307 | +0.59% |
| benchmark_smallcap | +1,278 | +0.64% |
| intramonth | +1,195 | +0.56% |
| random_hold | +831 | +0.40% |
| oracle | +792 | +0.38% |
| snake_viper_wild | +416 | +0.20% |
| snake_viper_tick | +408 | +0.20% |
| intraweek | +105 | +0.05% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -637 | -0.30% |
| snake_abs_conv | -649 | -0.31% |
| snake_abs_exit | -805 | -0.38% |
| snake_anaconda | -1,081 | -0.53% |
| snake_abs_exit_conv | -1,437 | -0.68% |
| gold | -2,236 | -1.26% |

Average per day so far: unified Rs +646, benchmark Rs +590, snake_abs_exit Rs +389, intramonth Rs +364, intraweek Rs +323, snake_abs_exit_conv Rs +322, oracle Rs +313, snake_viper_wild Rs +257, snake_abs_conv Rs +255, snake_abs Rs +251, random_hold Rs +210, snake_viper_tick Rs +150, snake_anaconda Rs +104, nifty_calls Rs +50, benchmark_smallcap Rs +18, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -673

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.