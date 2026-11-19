# Paper trading report

Updated 2026-11-19 13:52 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,836 | +11.92% | 0 | - | 236 |
| benchmark | 221,840 | +10.92% | 0 | - | 237 |
| intramonth | 213,371 | +6.68% | 0 | - | 235 |
| snake_abs_exit | 213,220 | +6.61% | 2 | 50% | 345 |
| intraweek | 211,880 | +5.94% | 35 | 54% | 3,851 |
| oracle | 211,504 | +5.75% | 0 | - | 233 |
| snake_abs_exit_conv | 210,857 | +5.43% | 2 | 50% | 345 |
| snake_abs | 208,834 | +4.42% | 1 | 100% | 255 |
| snake_abs_conv | 208,711 | +4.36% | 1 | 100% | 255 |
| random_hold | 207,750 | +3.88% | 10 | 70% | 733 |
| snake_viper_wild | 207,566 | +3.78% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,019 | +2.01% | 15 | 47% | 2,625 |
| snake_anaconda | 203,337 | +1.67% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,605 | +0.30% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,003 | -12.50% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,346 (-4.33%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,545 | +0.70% |
| benchmark_smallcap | +1,278 | +0.64% |
| unified | +1,224 | +0.55% |
| intramonth | +1,097 | +0.52% |
| random_hold | +817 | +0.40% |
| oracle | +708 | +0.34% |
| snake_viper_wild | +527 | +0.25% |
| snake_viper_tick | +516 | +0.25% |
| intraweek | +41 | +0.02% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -602 | -0.29% |
| snake_abs_conv | -614 | -0.29% |
| snake_abs_exit | -811 | -0.38% |
| snake_anaconda | -1,064 | -0.52% |
| snake_abs_exit_conv | -1,526 | -0.72% |
| gold | -2,318 | -1.31% |

Average per day so far: unified Rs +644, benchmark Rs +590, snake_abs_exit Rs +389, intramonth Rs +361, intraweek Rs +321, snake_abs_exit_conv Rs +319, oracle Rs +311, snake_viper_wild Rs +261, snake_abs_conv Rs +256, snake_abs Rs +252, random_hold Rs +209, snake_viper_tick Rs +155, snake_anaconda Rs +104, nifty_calls Rs +50, benchmark_smallcap Rs +18, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -676

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.