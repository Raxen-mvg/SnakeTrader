# Paper trading report

Updated 2026-11-19 11:43 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,775 | +11.89% | 0 | - | 236 |
| benchmark | 221,022 | +10.51% | 0 | - | 237 |
| intramonth | 213,280 | +6.64% | 0 | - | 235 |
| snake_abs_exit | 213,054 | +6.53% | 2 | 50% | 345 |
| intraweek | 211,927 | +5.96% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,215 | +5.61% | 2 | 50% | 345 |
| oracle | 211,129 | +5.57% | 0 | - | 233 |
| snake_abs | 208,579 | +4.29% | 1 | 100% | 255 |
| snake_abs_conv | 208,447 | +4.22% | 1 | 100% | 255 |
| random_hold | 207,706 | +3.85% | 10 | 70% | 733 |
| snake_viper_wild | 207,427 | +3.71% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,883 | +1.94% | 15 | 47% | 2,625 |
| snake_anaconda | 202,836 | +1.42% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,493 | +0.25% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,184 | -12.41% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,226 (-4.39%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,166 | +0.58% |
| unified | +1,164 | +0.52% |
| intramonth | +1,006 | +0.47% |
| random_hold | +773 | +0.37% |
| benchmark | +727 | +0.33% |
| snake_viper_wild | +387 | +0.19% |
| snake_viper_tick | +380 | +0.19% |
| oracle | +333 | +0.16% |
| intraweek | +88 | +0.04% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -857 | -0.41% |
| snake_abs_conv | -878 | -0.42% |
| snake_abs_exit | -978 | -0.46% |
| snake_abs_exit_conv | -1,168 | -0.55% |
| snake_anaconda | -1,565 | -0.77% |
| gold | -2,137 | -1.21% |

Average per day so far: unified Rs +643, benchmark Rs +568, snake_abs_exit Rs +384, intramonth Rs +359, snake_abs_exit_conv Rs +330, intraweek Rs +322, oracle Rs +301, snake_viper_wild Rs +256, snake_abs_conv Rs +248, snake_abs Rs +245, random_hold Rs +208, snake_viper_tick Rs +149, snake_anaconda Rs +89, nifty_calls Rs +50, benchmark_smallcap Rs +15, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -671

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.