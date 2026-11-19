# Paper trading report

Updated 2026-11-19 09:42 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,123 | +12.06% | 0 | - | 236 |
| benchmark | 219,997 | +10.00% | 0 | - | 237 |
| intramonth | 213,924 | +6.96% | 0 | - | 235 |
| snake_abs_exit | 213,791 | +6.89% | 2 | 50% | 345 |
| snake_abs_exit_conv | 212,041 | +6.02% | 2 | 50% | 345 |
| intraweek | 212,001 | +6.00% | 35 | 54% | 3,851 |
| oracle | 211,271 | +5.64% | 0 | - | 233 |
| snake_abs | 209,246 | +4.62% | 1 | 100% | 255 |
| snake_abs_conv | 209,125 | +4.56% | 1 | 100% | 255 |
| random_hold | 207,990 | +4.00% | 10 | 70% | 733 |
| snake_viper_wild | 207,591 | +3.80% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,044 | +2.02% | 15 | 47% | 2,625 |
| snake_anaconda | 203,977 | +1.99% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,246 | +0.12% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,102 | -12.45% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,520 (-4.24%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| intramonth | +1,650 | +0.78% |
| unified | +1,511 | +0.68% |
| random_hold | +1,057 | +0.51% |
| benchmark_smallcap | +919 | +0.46% |
| snake_viper_wild | +552 | +0.27% |
| snake_viper_tick | +540 | +0.27% |
| oracle | +475 | +0.23% |
| intraweek | +162 | +0.08% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs | -190 | -0.09% |
| snake_abs_conv | -200 | -0.10% |
| snake_abs_exit | -241 | -0.11% |
| benchmark | -298 | -0.14% |
| snake_abs_exit_conv | -343 | -0.16% |
| snake_anaconda | -424 | -0.21% |
| gold | -2,219 | -1.25% |

Average per day so far: unified Rs +652, benchmark Rs +540, snake_abs_exit Rs +406, intramonth Rs +376, snake_abs_exit_conv Rs +354, intraweek Rs +324, oracle Rs +305, snake_abs_conv Rs +268, snake_abs Rs +264, snake_viper_wild Rs +262, random_hold Rs +216, snake_viper_tick Rs +156, snake_anaconda Rs +124, nifty_calls Rs +50, benchmark_smallcap Rs +7, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -673

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.