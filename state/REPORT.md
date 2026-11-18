# Paper trading report

Updated 2026-11-18 13:04 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,894 | +11.45% | 0 | - | 236 |
| benchmark | 219,714 | +9.86% | 0 | - | 237 |
| intraweek | 212,738 | +6.37% | 35 | 54% | 3,851 |
| intramonth | 212,685 | +6.34% | 0 | - | 235 |
| snake_abs_exit | 212,220 | +6.11% | 2 | 50% | 345 |
| oracle | 212,053 | +6.03% | 0 | - | 233 |
| snake_abs_exit_conv | 210,460 | +5.23% | 2 | 50% | 345 |
| snake_abs | 207,623 | +3.81% | 1 | 100% | 255 |
| snake_abs_conv | 207,483 | +3.74% | 1 | 100% | 255 |
| random_hold | 207,124 | +3.56% | 10 | 70% | 733 |
| snake_viper_wild | 206,814 | +3.41% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,282 | +1.64% | 15 | 47% | 2,625 |
| snake_anaconda | 202,616 | +1.31% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,170 | -0.41% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 176,926 | -11.54% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,159 (-4.42%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,456 | +0.66% |
| intramonth | +1,142 | +0.54% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| oracle | -433 | -0.20% |
| intraweek | -585 | -0.27% |
| snake_abs_exit | -922 | -0.43% |
| snake_abs | -935 | -0.45% |
| snake_abs_conv | -937 | -0.45% |
| snake_abs_exit_conv | -1,114 | -0.53% |
| random_hold | -1,308 | -0.63% |
| benchmark_smallcap | -1,401 | -0.70% |
| snake_anaconda | -1,439 | -0.70% |
| benchmark | -1,890 | -0.85% |
| snake_viper_tick | -2,554 | -1.24% |
| snake_viper_wild | -2,601 | -1.24% |
| gold | -3,798 | -2.10% |

Average per day so far: unified Rs +636, benchmark Rs +548, snake_abs_exit Rs +370, intraweek Rs +354, intramonth Rs +352, oracle Rs +335, snake_abs_exit_conv Rs +317, snake_viper_wild Rs +243, snake_abs_conv Rs +227, snake_abs Rs +224, random_hold Rs +198, snake_viper_tick Rs +131, snake_anaconda Rs +84, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -26, snake_nonews Rs -326, snake Rs -347, gold Rs -641

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.