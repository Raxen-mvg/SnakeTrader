# Paper trading report

Updated 2026-11-23 13:55 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,689 | +11.84% | 0 | - | 236 |
| benchmark | 222,215 | +11.11% | 0 | - | 237 |
| intraweek | 212,316 | +6.16% | 40 | 55% | 4,400 |
| intramonth | 211,836 | +5.92% | 0 | - | 235 |
| oracle | 211,398 | +5.70% | 0 | - | 233 |
| random_hold | 208,901 | +4.45% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,850 | +3.42% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,641 | +2.82% | 2 | 50% | 345 |
| snake_abs | 204,618 | +2.31% | 1 | 100% | 255 |
| snake_abs_conv | 204,445 | +2.22% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,831 | +0.42% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,484 | -0.26% | 0 | - | 237 |
| snake_anaconda | 197,758 | -1.12% | 3 | 33% | 374 |
| snake_viper_tick | 197,406 | -1.30% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,331 | -15.33% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,985 (-5.01%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,282 | +0.76% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -976 | -0.47% |
| oracle | -1,081 | -0.51% |
| snake_abs | -1,302 | -0.63% |
| snake_abs_conv | -1,338 | -0.65% |
| benchmark_smallcap | -1,424 | -0.71% |
| snake_abs_exit | -1,712 | -0.82% |
| random_hold | -1,858 | -0.88% |
| snake_viper_tick | -1,966 | -0.99% |
| snake_viper_wild | -1,998 | -0.98% |
| snake_anaconda | -2,148 | -1.07% |
| unified | -2,493 | -1.10% |
| benchmark | -2,922 | -1.30% |
| intramonth | -3,168 | -1.47% |
| intraweek | -3,396 | -1.57% |

Average per day so far: unified Rs +607, benchmark Rs +570, intraweek Rs +316, intramonth Rs +303, oracle Rs +292, random_hold Rs +228, snake_abs_exit Rs +190, snake_abs_exit_conv Rs +157, snake_abs Rs +125, snake_abs_conv Rs +123, nifty_calls Rs +47, snake_viper_wild Rs +27, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -15, snake_anaconda Rs -66, snake_viper_tick Rs -93, snake_nonews Rs -300, snake Rs -320, gold Rs -786

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.