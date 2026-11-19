# Paper trading report

Updated 2026-11-19 12:33 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,799 | +11.90% | 0 | - | 236 |
| benchmark | 221,603 | +10.80% | 0 | - | 237 |
| intramonth | 213,447 | +6.72% | 0 | - | 235 |
| snake_abs_exit | 212,737 | +6.37% | 2 | 50% | 345 |
| intraweek | 211,694 | +5.85% | 35 | 54% | 3,851 |
| oracle | 210,998 | +5.50% | 0 | - | 233 |
| snake_abs_exit_conv | 210,803 | +5.40% | 2 | 50% | 345 |
| snake_abs | 208,529 | +4.26% | 1 | 100% | 255 |
| snake_abs_conv | 208,399 | +4.20% | 1 | 100% | 255 |
| random_hold | 207,700 | +3.85% | 10 | 70% | 733 |
| snake_viper_wild | 207,460 | +3.73% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,916 | +1.96% | 15 | 47% | 2,625 |
| snake_anaconda | 202,802 | +1.40% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,560 | +0.28% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,987 | -12.51% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,203 (-4.40%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,308 | +0.59% |
| benchmark_smallcap | +1,233 | +0.62% |
| unified | +1,188 | +0.53% |
| intramonth | +1,173 | +0.55% |
| random_hold | +768 | +0.37% |
| snake_viper_wild | +421 | +0.20% |
| snake_viper_tick | +413 | +0.20% |
| oracle | +202 | +0.10% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -146 | -0.07% |
| snake_abs | -907 | -0.43% |
| snake_abs_conv | -926 | -0.44% |
| snake_abs_exit | -1,294 | -0.60% |
| snake_abs_exit_conv | -1,580 | -0.74% |
| snake_anaconda | -1,599 | -0.78% |
| gold | -2,334 | -1.32% |

Average per day so far: unified Rs +643, benchmark Rs +584, snake_abs_exit Rs +375, intramonth Rs +363, snake_abs_exit_conv Rs +318, intraweek Rs +316, oracle Rs +297, snake_viper_wild Rs +257, snake_abs_conv Rs +247, snake_abs Rs +244, random_hold Rs +208, snake_viper_tick Rs +151, snake_anaconda Rs +88, nifty_calls Rs +50, benchmark_smallcap Rs +17, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -676

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.