# Paper trading report

Updated 2026-11-18 12:28 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,136 | +11.57% | 0 | - | 236 |
| benchmark | 220,188 | +10.09% | 0 | - | 237 |
| intraweek | 213,897 | +6.95% | 35 | 54% | 3,851 |
| intramonth | 213,114 | +6.56% | 0 | - | 235 |
| snake_abs_exit | 212,898 | +6.45% | 2 | 50% | 345 |
| oracle | 212,329 | +6.16% | 0 | - | 233 |
| snake_abs_exit_conv | 211,091 | +5.54% | 2 | 50% | 345 |
| snake_abs | 208,152 | +4.08% | 1 | 100% | 255 |
| snake_abs_conv | 208,018 | +4.01% | 1 | 100% | 255 |
| random_hold | 207,512 | +3.76% | 10 | 70% | 733 |
| snake_viper_wild | 207,294 | +3.65% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,752 | +1.88% | 15 | 47% | 2,625 |
| snake_anaconda | 203,135 | +1.57% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,551 | -0.22% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,124 | -11.44% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,585 (-4.21%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,698 | +0.77% |
| intramonth | +1,572 | +0.74% |
| intraweek | +574 | +0.27% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -157 | -0.07% |
| snake_abs_exit | -244 | -0.11% |
| snake_abs_conv | -401 | -0.19% |
| snake_abs | -406 | -0.20% |
| snake_abs_exit_conv | -483 | -0.23% |
| random_hold | -920 | -0.44% |
| snake_anaconda | -920 | -0.45% |
| benchmark_smallcap | -1,020 | -0.51% |
| benchmark | -1,415 | -0.64% |
| snake_viper_tick | -2,084 | -1.01% |
| snake_viper_wild | -2,121 | -1.01% |
| gold | -3,600 | -1.99% |

Average per day so far: unified Rs +643, benchmark Rs +561, snake_abs_exit Rs +391, intraweek Rs +386, intramonth Rs +364, oracle Rs +342, snake_abs_exit_conv Rs +336, snake_viper_wild Rs +260, snake_abs_conv Rs +243, snake_abs Rs +240, random_hold Rs +209, snake_viper_tick Rs +150, snake_anaconda Rs +101, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -14, snake_nonews Rs -326, snake Rs -347, gold Rs -635

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.