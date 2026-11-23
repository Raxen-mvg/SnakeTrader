# Paper trading report

Updated 2026-11-23 09:59 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,423 | +12.71% | 0 | - | 236 |
| benchmark | 223,784 | +11.89% | 0 | - | 237 |
| intraweek | 213,328 | +6.66% | 40 | 55% | 4,400 |
| intramonth | 213,259 | +6.63% | 0 | - | 235 |
| oracle | 211,624 | +5.81% | 0 | - | 233 |
| random_hold | 210,411 | +5.21% | 12 | 75% | 1,009 |
| snake_abs_exit | 208,334 | +4.17% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,618 | +3.31% | 2 | 50% | 345 |
| snake_abs | 205,562 | +2.78% | 1 | 100% | 255 |
| snake_abs_conv | 205,416 | +2.71% | 1 | 100% | 255 |
| snake_viper_wild | 203,588 | +1.79% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 200,114 | +0.06% | 15 | 47% | 2,625 |
| benchmark_smallcap | 200,056 | +0.03% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,485 | -0.26% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,249 | -15.38% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,063 (-4.47%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,200 | +0.71% |
| snake_viper_wild | +758 | +0.37% |
| snake_viper_tick | +743 | +0.37% |
| snake_abs_exit_conv | +1 | +0.00% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_abs_exit | -229 | -0.11% |
| random_hold | -349 | -0.17% |
| snake_abs | -357 | -0.17% |
| snake_abs_conv | -367 | -0.18% |
| snake_anaconda | -421 | -0.21% |
| unified | -758 | -0.34% |
| benchmark_smallcap | -852 | -0.42% |
| oracle | -854 | -0.40% |
| benchmark | -1,354 | -0.60% |
| intramonth | -1,746 | -0.81% |
| intraweek | -2,384 | -1.10% |

Average per day so far: unified Rs +652, benchmark Rs +610, intraweek Rs +342, intramonth Rs +340, oracle Rs +298, random_hold Rs +267, snake_abs_exit Rs +231, snake_abs_exit_conv Rs +184, snake_abs_conv Rs +150, snake_abs Rs +150, snake_viper_wild Rs +116, nifty_calls Rs +47, snake_viper_tick Rs +4, benchmark_smallcap Rs +2, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_anaconda Rs -15, snake_nonews Rs -300, snake Rs -320, gold Rs -788

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.