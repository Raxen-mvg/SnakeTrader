# Paper trading report

Updated 2026-11-23 10:24 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,847 | +12.42% | 0 | - | 236 |
| benchmark | 223,531 | +11.77% | 0 | - | 237 |
| intraweek | 212,941 | +6.47% | 40 | 55% | 4,400 |
| intramonth | 212,803 | +6.40% | 0 | - | 235 |
| oracle | 211,327 | +5.66% | 0 | - | 233 |
| random_hold | 210,030 | +5.01% | 12 | 75% | 1,009 |
| snake_abs_exit | 208,093 | +4.05% | 2 | 50% | 345 |
| snake_abs_exit_conv | 207,002 | +3.50% | 2 | 50% | 345 |
| snake_abs | 205,290 | +2.65% | 1 | 100% | 255 |
| snake_abs_conv | 205,143 | +2.57% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,355 | +0.68% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,730 | -0.14% | 0 | - | 237 |
| snake_anaconda | 199,099 | -0.45% | 3 | 33% | 374 |
| snake_viper_tick | 197,918 | -1.04% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,561 | -15.22% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,694 (-4.65%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,512 | +0.90% |
| snake_abs_exit_conv | +386 | +0.19% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -470 | -0.23% |
| snake_abs | -630 | -0.31% |
| snake_abs_conv | -640 | -0.31% |
| random_hold | -729 | -0.35% |
| snake_anaconda | -807 | -0.40% |
| oracle | -1,152 | -0.54% |
| benchmark_smallcap | -1,177 | -0.59% |
| unified | -1,334 | -0.59% |
| snake_viper_tick | -1,453 | -0.73% |
| snake_viper_wild | -1,475 | -0.73% |
| benchmark | -1,606 | -0.71% |
| intramonth | -2,202 | -1.02% |
| intraweek | -2,771 | -1.28% |

Average per day so far: unified Rs +637, benchmark Rs +603, intraweek Rs +332, intramonth Rs +328, oracle Rs +290, random_hold Rs +257, snake_abs_exit Rs +225, snake_abs_exit_conv Rs +194, snake_abs Rs +143, snake_abs_conv Rs +143, nifty_calls Rs +47, snake_viper_wild Rs +44, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -8, snake_anaconda Rs -27, snake_viper_tick Rs -74, snake_nonews Rs -300, snake Rs -320, gold Rs -780

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.