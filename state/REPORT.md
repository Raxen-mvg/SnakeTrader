# Paper trading report

Updated 2026-11-18 12:13 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,077 | +11.54% | 0 | - | 236 |
| benchmark | 220,134 | +10.07% | 0 | - | 237 |
| intraweek | 214,062 | +7.03% | 35 | 54% | 3,851 |
| snake_abs_exit | 213,189 | +6.59% | 2 | 50% | 345 |
| intramonth | 212,970 | +6.49% | 0 | - | 235 |
| oracle | 212,434 | +6.22% | 0 | - | 233 |
| snake_abs_exit_conv | 211,458 | +5.73% | 2 | 50% | 345 |
| snake_abs | 208,409 | +4.21% | 1 | 100% | 255 |
| snake_abs_conv | 208,280 | +4.14% | 1 | 100% | 255 |
| random_hold | 207,463 | +3.73% | 10 | 70% | 733 |
| snake_viper_wild | 207,174 | +3.59% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,635 | +1.82% | 15 | 47% | 2,625 |
| snake_anaconda | 203,509 | +1.75% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,439 | -0.28% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,107 | -11.45% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,596 (-4.20%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,638 | +0.74% |
| intramonth | +1,428 | +0.68% |
| intraweek | +740 | +0.35% |
| snake_abs_exit | +47 | +0.02% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -52 | -0.03% |
| snake_abs_exit_conv | -116 | -0.06% |
| snake_abs_conv | -140 | -0.07% |
| snake_abs | -149 | -0.07% |
| snake_anaconda | -546 | -0.27% |
| random_hold | -969 | -0.47% |
| benchmark_smallcap | -1,132 | -0.56% |
| benchmark | -1,469 | -0.66% |
| snake_viper_tick | -2,202 | -1.07% |
| snake_viper_wild | -2,241 | -1.07% |
| gold | -3,617 | -2.00% |

Average per day so far: unified Rs +641, benchmark Rs +559, snake_abs_exit Rs +400, intraweek Rs +391, intramonth Rs +360, snake_abs_exit_conv Rs +347, oracle Rs +345, snake_viper_wild Rs +256, snake_abs_conv Rs +251, snake_abs Rs +247, random_hold Rs +207, snake_viper_tick Rs +145, snake_anaconda Rs +113, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -18, snake_nonews Rs -326, snake Rs -347, gold Rs -636

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.