# Paper trading report

Updated 2026-11-17 11:01 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,039 | +11.02% | 0 | - | 236 |
| benchmark | 221,672 | +10.84% | 0 | - | 237 |
| snake_abs_exit | 215,970 | +7.99% | 2 | 50% | 345 |
| intraweek | 214,134 | +7.07% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 214,051 | +7.03% | 2 | 50% | 345 |
| oracle | 212,761 | +6.38% | 0 | - | 233 |
| intramonth | 211,906 | +5.95% | 0 | - | 235 |
| snake_abs | 210,502 | +5.25% | 1 | 100% | 255 |
| snake_abs_conv | 210,354 | +5.18% | 1 | 100% | 255 |
| random_hold | 208,329 | +4.16% | 10 | 70% | 733 |
| snake_viper_wild | 207,222 | +3.61% | 14 | 50% | 2,496 |
| snake_anaconda | 205,965 | +2.98% | 3 | 33% | 374 |
| snake_viper_tick | 203,679 | +1.84% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,298 | +1.15% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,809 | -9.10% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,599 (-4.20%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,869 | +1.36% |
| benchmark | +1,591 | +0.72% |
| snake_abs_exit | +1,560 | +0.73% |
| benchmark_smallcap | +1,469 | +0.73% |
| snake_viper_wild | +1,077 | +0.52% |
| snake_viper_tick | +1,059 | +0.52% |
| snake_anaconda | +862 | +0.42% |
| gold | +855 | +0.47% |
| snake_abs_exit_conv | +834 | +0.39% |
| oracle | +738 | +0.35% |
| unified | +602 | +0.27% |
| random_hold | +536 | +0.26% |
| snake_abs | +369 | +0.17% |
| snake_abs_conv | +364 | +0.17% |
| intramonth | +287 | +0.14% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +630, benchmark Rs +619, snake_abs_exit Rs +499, snake_abs_exit_conv Rs +439, intraweek Rs +404, oracle Rs +365, intramonth Rs +340, snake_abs_conv Rs +324, snake_abs Rs +318, snake_viper_wild Rs +267, random_hold Rs +238, snake_anaconda Rs +199, snake_viper_tick Rs +153, benchmark_smallcap Rs +74, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -520

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.