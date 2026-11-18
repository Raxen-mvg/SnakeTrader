# Paper trading report

Updated 2026-11-18 12:34 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,828 | +11.41% | 0 | - | 236 |
| benchmark | 219,981 | +9.99% | 0 | - | 237 |
| intraweek | 213,662 | +6.83% | 35 | 54% | 3,851 |
| intramonth | 212,854 | +6.43% | 0 | - | 235 |
| snake_abs_exit | 212,677 | +6.34% | 2 | 50% | 345 |
| oracle | 212,107 | +6.05% | 0 | - | 233 |
| snake_abs_exit_conv | 210,974 | +5.49% | 2 | 50% | 345 |
| snake_abs | 207,916 | +3.96% | 1 | 100% | 255 |
| snake_abs_conv | 207,779 | +3.89% | 1 | 100% | 255 |
| random_hold | 207,336 | +3.67% | 10 | 70% | 733 |
| snake_viper_wild | 207,294 | +3.65% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,752 | +1.88% | 15 | 47% | 2,625 |
| snake_anaconda | 202,932 | +1.47% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,405 | -0.30% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 176,976 | -11.51% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,372 (-4.31%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,389 | +0.63% |
| intramonth | +1,312 | +0.62% |
| intraweek | +339 | +0.16% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -380 | -0.18% |
| snake_abs_exit | -465 | -0.22% |
| snake_abs_exit_conv | -600 | -0.28% |
| snake_abs_conv | -641 | -0.31% |
| snake_abs | -642 | -0.31% |
| random_hold | -1,097 | -0.53% |
| snake_anaconda | -1,123 | -0.55% |
| benchmark_smallcap | -1,166 | -0.58% |
| benchmark | -1,622 | -0.73% |
| snake_viper_tick | -2,084 | -1.01% |
| snake_viper_wild | -2,121 | -1.01% |
| gold | -3,748 | -2.07% |

Average per day so far: unified Rs +634, benchmark Rs +555, snake_abs_exit Rs +384, intraweek Rs +379, intramonth Rs +357, oracle Rs +336, snake_abs_exit_conv Rs +333, snake_viper_wild Rs +260, snake_abs_conv Rs +236, snake_abs Rs +233, random_hold Rs +204, snake_viper_tick Rs +150, snake_anaconda Rs +95, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -19, snake_nonews Rs -326, snake Rs -347, gold Rs -640

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.