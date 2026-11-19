# Paper trading report

Updated 2026-11-19 13:46 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,975 | +11.99% | 0 | - | 236 |
| benchmark | 221,833 | +10.92% | 0 | - | 237 |
| intramonth | 213,498 | +6.75% | 0 | - | 235 |
| snake_abs_exit | 213,307 | +6.65% | 2 | 50% | 345 |
| intraweek | 211,953 | +5.98% | 35 | 54% | 3,851 |
| oracle | 211,611 | +5.81% | 0 | - | 233 |
| snake_abs_exit_conv | 211,128 | +5.56% | 2 | 50% | 345 |
| snake_abs | 208,884 | +4.44% | 1 | 100% | 255 |
| snake_abs_conv | 208,760 | +4.38% | 1 | 100% | 255 |
| random_hold | 207,787 | +3.89% | 10 | 70% | 733 |
| snake_viper_wild | 207,710 | +3.85% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,160 | +2.08% | 15 | 47% | 2,625 |
| snake_anaconda | 203,412 | +1.71% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,672 | +0.34% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,102 | -12.45% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,439 (-4.28%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,538 | +0.70% |
| unified | +1,364 | +0.61% |
| benchmark_smallcap | +1,345 | +0.68% |
| intramonth | +1,224 | +0.58% |
| random_hold | +855 | +0.41% |
| oracle | +815 | +0.39% |
| snake_viper_wild | +671 | +0.32% |
| snake_viper_tick | +657 | +0.32% |
| intraweek | +113 | +0.05% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -553 | -0.26% |
| snake_abs_conv | -565 | -0.27% |
| snake_abs_exit | -725 | -0.34% |
| snake_anaconda | -989 | -0.48% |
| snake_abs_exit_conv | -1,256 | -0.59% |
| gold | -2,219 | -1.25% |

Average per day so far: unified Rs +648, benchmark Rs +590, snake_abs_exit Rs +391, intramonth Rs +365, snake_abs_exit_conv Rs +327, intraweek Rs +323, oracle Rs +314, snake_viper_wild Rs +266, snake_abs_conv Rs +258, snake_abs Rs +254, random_hold Rs +210, snake_viper_tick Rs +160, snake_anaconda Rs +107, nifty_calls Rs +50, benchmark_smallcap Rs +20, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -673

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.