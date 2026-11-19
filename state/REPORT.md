# Paper trading report

Updated 2026-11-19 10:07 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,910 | +11.96% | 0 | - | 236 |
| benchmark | 220,586 | +10.29% | 0 | - | 237 |
| intramonth | 213,718 | +6.86% | 0 | - | 235 |
| snake_abs_exit | 213,695 | +6.85% | 2 | 50% | 345 |
| intraweek | 212,426 | +6.21% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,902 | +5.95% | 2 | 50% | 345 |
| oracle | 211,445 | +5.72% | 0 | - | 233 |
| snake_abs | 209,204 | +4.60% | 1 | 100% | 255 |
| snake_abs_conv | 209,080 | +4.54% | 1 | 100% | 255 |
| random_hold | 207,950 | +3.98% | 10 | 70% | 733 |
| snake_viper_wild | 207,846 | +3.92% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,293 | +2.15% | 15 | 47% | 2,625 |
| snake_anaconda | 203,978 | +1.99% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,381 | +0.19% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,674 | -12.66% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,531 (-4.23%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| intramonth | +1,444 | +0.68% |
| unified | +1,298 | +0.58% |
| benchmark_smallcap | +1,054 | +0.53% |
| random_hold | +1,018 | +0.49% |
| snake_viper_wild | +806 | +0.39% |
| snake_viper_tick | +790 | +0.39% |
| oracle | +649 | +0.31% |
| intraweek | +587 | +0.28% |
| benchmark | +291 | +0.13% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -233 | -0.11% |
| snake_abs_conv | -245 | -0.12% |
| snake_abs_exit | -337 | -0.16% |
| snake_anaconda | -423 | -0.21% |
| snake_abs_exit_conv | -482 | -0.23% |
| gold | -2,647 | -1.49% |

Average per day so far: unified Rs +646, benchmark Rs +556, snake_abs_exit Rs +403, intramonth Rs +371, snake_abs_exit_conv Rs +350, intraweek Rs +336, oracle Rs +309, snake_viper_wild Rs +271, snake_abs_conv Rs +267, snake_abs Rs +263, random_hold Rs +215, snake_viper_tick Rs +165, snake_anaconda Rs +124, nifty_calls Rs +50, benchmark_smallcap Rs +12, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -684

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.