# Paper trading report

Updated 2026-11-19 14:04 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,947 | +11.97% | 0 | - | 236 |
| benchmark | 222,024 | +11.01% | 0 | - | 237 |
| intramonth | 213,496 | +6.75% | 0 | - | 235 |
| snake_abs_exit | 212,985 | +6.49% | 2 | 50% | 345 |
| intraweek | 211,901 | +5.95% | 35 | 54% | 3,851 |
| oracle | 211,615 | +5.81% | 0 | - | 233 |
| snake_abs_exit_conv | 210,790 | +5.39% | 2 | 50% | 345 |
| snake_abs | 208,653 | +4.33% | 1 | 100% | 255 |
| snake_abs_conv | 208,524 | +4.26% | 1 | 100% | 255 |
| random_hold | 207,897 | +3.95% | 10 | 70% | 733 |
| snake_viper_wild | 207,566 | +3.78% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,019 | +2.01% | 15 | 47% | 2,625 |
| snake_anaconda | 203,150 | +1.57% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,605 | +0.30% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,069 | -12.47% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,421 (-4.29%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,729 | +0.79% |
| unified | +1,336 | +0.60% |
| benchmark_smallcap | +1,278 | +0.64% |
| intramonth | +1,222 | +0.58% |
| random_hold | +965 | +0.47% |
| oracle | +819 | +0.39% |
| snake_viper_wild | +527 | +0.25% |
| snake_viper_tick | +516 | +0.25% |
| intraweek | +62 | +0.03% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -783 | -0.37% |
| snake_abs_conv | -801 | -0.38% |
| snake_abs_exit | -1,046 | -0.49% |
| snake_anaconda | -1,251 | -0.61% |
| snake_abs_exit_conv | -1,593 | -0.75% |
| gold | -2,252 | -1.27% |

Average per day so far: unified Rs +647, benchmark Rs +595, snake_abs_exit Rs +382, intramonth Rs +365, intraweek Rs +322, snake_abs_exit_conv Rs +317, oracle Rs +314, snake_viper_wild Rs +261, snake_abs_conv Rs +251, snake_abs Rs +247, random_hold Rs +213, snake_viper_tick Rs +155, snake_anaconda Rs +98, nifty_calls Rs +50, benchmark_smallcap Rs +18, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -674

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.