# Paper trading report

Updated 2026-11-19 12:57 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,768 | +11.88% | 0 | - | 236 |
| benchmark | 221,672 | +10.84% | 0 | - | 237 |
| intramonth | 213,430 | +6.71% | 0 | - | 235 |
| snake_abs_exit | 212,862 | +6.43% | 2 | 50% | 345 |
| intraweek | 211,747 | +5.87% | 35 | 54% | 3,851 |
| oracle | 211,601 | +5.80% | 0 | - | 233 |
| snake_abs_exit_conv | 211,007 | +5.50% | 2 | 50% | 345 |
| snake_abs | 208,505 | +4.25% | 1 | 100% | 255 |
| snake_abs_conv | 208,376 | +4.19% | 1 | 100% | 255 |
| random_hold | 207,733 | +3.87% | 10 | 70% | 733 |
| snake_viper_wild | 207,388 | +3.69% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,845 | +1.92% | 15 | 47% | 2,625 |
| snake_anaconda | 203,300 | +1.65% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,672 | +0.34% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,135 | -12.43% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,340 (-4.33%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,377 | +0.62% |
| benchmark_smallcap | +1,345 | +0.68% |
| intramonth | +1,157 | +0.55% |
| unified | +1,156 | +0.52% |
| oracle | +805 | +0.38% |
| random_hold | +801 | +0.39% |
| snake_viper_wild | +349 | +0.17% |
| snake_viper_tick | +342 | +0.17% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -93 | -0.04% |
| snake_abs | -932 | -0.45% |
| snake_abs_conv | -949 | -0.45% |
| snake_anaconda | -1,101 | -0.54% |
| snake_abs_exit | -1,170 | -0.55% |
| snake_abs_exit_conv | -1,376 | -0.65% |
| gold | -2,187 | -1.23% |

Average per day so far: unified Rs +642, benchmark Rs +586, snake_abs_exit Rs +378, intramonth Rs +363, snake_abs_exit_conv Rs +324, intraweek Rs +317, oracle Rs +314, snake_viper_wild Rs +255, snake_abs_conv Rs +246, snake_abs Rs +243, random_hold Rs +209, snake_viper_tick Rs +148, snake_anaconda Rs +103, nifty_calls Rs +50, benchmark_smallcap Rs +20, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -672

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.