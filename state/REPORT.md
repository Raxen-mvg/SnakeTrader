# Paper trading report

Updated 2026-11-23 14:07 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,848 | +11.92% | 0 | - | 236 |
| benchmark | 222,024 | +11.01% | 0 | - | 237 |
| intraweek | 212,241 | +6.12% | 40 | 55% | 4,400 |
| intramonth | 211,970 | +5.99% | 0 | - | 235 |
| oracle | 211,603 | +5.80% | 0 | - | 233 |
| random_hold | 208,828 | +4.41% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,830 | +3.42% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,804 | +2.90% | 2 | 50% | 345 |
| snake_abs | 204,504 | +2.25% | 1 | 100% | 255 |
| snake_abs_conv | 204,329 | +2.16% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,158 | +0.58% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,372 | -0.31% | 0 | - | 237 |
| snake_anaconda | 197,929 | -1.03% | 3 | 33% | 374 |
| snake_viper_tick | 197,726 | -1.14% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,331 | -15.33% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,037 (-4.98%).

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
| snake_abs_exit_conv | -813 | -0.39% |
| oracle | -875 | -0.41% |
| snake_abs | -1,416 | -0.69% |
| snake_abs_conv | -1,454 | -0.71% |
| benchmark_smallcap | -1,536 | -0.76% |
| snake_viper_tick | -1,646 | -0.83% |
| snake_viper_wild | -1,671 | -0.82% |
| snake_abs_exit | -1,732 | -0.83% |
| random_hold | -1,932 | -0.92% |
| snake_anaconda | -1,976 | -0.99% |
| unified | -2,333 | -1.03% |
| intramonth | -3,034 | -1.41% |
| benchmark | -3,114 | -1.38% |
| intraweek | -3,471 | -1.61% |

Average per day so far: unified Rs +611, benchmark Rs +565, intraweek Rs +314, intramonth Rs +307, oracle Rs +298, random_hold Rs +226, snake_abs_exit Rs +190, snake_abs_exit_conv Rs +161, snake_abs Rs +122, snake_abs_conv Rs +120, nifty_calls Rs +47, snake_viper_wild Rs +37, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -18, snake_anaconda Rs -61, snake_viper_tick Rs -81, snake_nonews Rs -300, snake Rs -320, gold Rs -786

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.