# Paper trading report

Updated 2026-11-18 12:55 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,675 | +11.34% | 0 | - | 236 |
| benchmark | 219,959 | +9.98% | 0 | - | 237 |
| intraweek | 213,267 | +6.63% | 35 | 54% | 3,851 |
| intramonth | 212,708 | +6.35% | 0 | - | 235 |
| snake_abs_exit | 212,289 | +6.14% | 2 | 50% | 345 |
| oracle | 211,644 | +5.82% | 0 | - | 233 |
| snake_abs_exit_conv | 210,505 | +5.25% | 2 | 50% | 345 |
| snake_abs | 207,633 | +3.82% | 1 | 100% | 255 |
| snake_abs_conv | 207,493 | +3.75% | 1 | 100% | 255 |
| random_hold | 207,172 | +3.59% | 10 | 70% | 733 |
| snake_viper_wild | 206,670 | +3.33% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,141 | +1.57% | 15 | 47% | 2,625 |
| snake_anaconda | 202,453 | +1.23% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,204 | -0.40% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 176,959 | -11.52% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,118 (-4.44%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,236 | +0.56% |
| intramonth | +1,165 | +0.55% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraweek | -56 | -0.03% |
| oracle | -842 | -0.40% |
| snake_abs_exit | -853 | -0.40% |
| snake_abs | -926 | -0.44% |
| snake_abs_conv | -926 | -0.44% |
| snake_abs_exit_conv | -1,068 | -0.51% |
| random_hold | -1,260 | -0.60% |
| benchmark_smallcap | -1,368 | -0.68% |
| snake_anaconda | -1,602 | -0.79% |
| benchmark | -1,645 | -0.74% |
| snake_viper_tick | -2,695 | -1.31% |
| snake_viper_wild | -2,745 | -1.31% |
| gold | -3,765 | -2.08% |

Average per day so far: unified Rs +630, benchmark Rs +554, snake_abs_exit Rs +372, intraweek Rs +369, intramonth Rs +353, oracle Rs +323, snake_abs_exit_conv Rs +318, snake_viper_wild Rs +238, snake_abs_conv Rs +227, snake_abs Rs +224, random_hold Rs +199, snake_viper_tick Rs +126, snake_anaconda Rs +79, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -25, snake_nonews Rs -326, snake Rs -347, gold Rs -640

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.