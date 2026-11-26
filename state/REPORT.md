# Paper trading report

Updated 2026-11-26 15:07 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,948 | +12.97% | 0 | - | 237 |
| unified | 223,057 | +11.53% | 0 | - | 236 |
| oracle | 212,485 | +6.24% | 0 | - | 233 |
| intramonth | 210,613 | +5.31% | 0 | - | 235 |
| random_hold | 208,686 | +4.34% | 13 | 69% | 1,037 |
| intraweek | 207,462 | +3.73% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,456 | +0.73% | 2 | 50% | 345 |
| benchmark_smallcap | 200,930 | +0.47% | 0 | - | 237 |
| snake_abs_exit_conv | 200,726 | +0.36% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 198,943 | -0.53% | 1 | 100% | 255 |
| snake_abs_conv | 198,761 | -0.62% | 1 | 100% | 255 |
| snake_anaconda | 192,713 | -3.64% | 3 | 33% | 374 |
| snake_viper_wild | 192,292 | -3.85% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,026 | -5.49% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,208 | -16.90% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,456 (-5.77%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,119 | +1.07% |
| gold | +1,611 | +0.98% |
| benchmark | +926 | +0.41% |
| intraweek | +719 | +0.35% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -800 | -0.40% |
| random_hold | -807 | -0.39% |
| unified | -1,043 | -0.47% |
| intramonth | -1,080 | -0.51% |
| snake_abs | -1,206 | -0.60% |
| snake_abs_conv | -1,211 | -0.61% |
| snake_abs_exit_conv | -1,250 | -0.62% |
| oracle | -1,310 | -0.61% |
| snake_anaconda | -1,840 | -0.95% |
| snake_viper_tick | -5,151 | -2.65% |
| snake_viper_wild | -5,251 | -2.66% |

Average per day so far: benchmark Rs +633, unified Rs +562, oracle Rs +305, intramonth Rs +259, random_hold Rs +212, intraweek Rs +182, nifty_calls Rs +45, snake_abs_exit Rs +38, benchmark_smallcap Rs +25, snake_abs_exit_conv Rs +19, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -27, snake_abs_conv Rs -33, snake_anaconda Rs -202, snake_viper_wild Rs -234, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -366, gold Rs -824

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.