# Paper trading report

Updated 2026-11-18 14:53 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,253 | +11.13% | 0 | - | 236 |
| benchmark | 220,280 | +10.14% | 0 | - | 237 |
| snake_abs_exit | 214,450 | +7.22% | 2 | 50% | 345 |
| snake_abs_exit_conv | 212,748 | +6.37% | 2 | 50% | 345 |
| intramonth | 211,991 | +6.00% | 0 | - | 235 |
| intraweek | 211,901 | +5.95% | 35 | 54% | 3,851 |
| oracle | 211,182 | +5.59% | 0 | - | 233 |
| snake_abs | 209,856 | +4.93% | 1 | 100% | 255 |
| snake_abs_conv | 209,746 | +4.87% | 1 | 100% | 255 |
| snake_viper_wild | 207,332 | +3.67% | 16 | 50% | 2,827 |
| random_hold | 206,834 | +3.42% | 10 | 70% | 733 |
| snake_anaconda | 204,686 | +2.34% | 3 | 33% | 374 |
| snake_viper_tick | 203,790 | +1.90% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,686 | -0.16% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,206 | -11.40% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,690 (-4.65%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_conv | +1,326 | +0.64% |
| snake_abs_exit | +1,308 | +0.61% |
| snake_abs | +1,298 | +0.62% |
| snake_abs_exit_conv | +1,174 | +0.56% |
| unified | +815 | +0.37% |
| snake_anaconda | +631 | +0.31% |
| intramonth | +449 | +0.21% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| benchmark_smallcap | -886 | -0.44% |
| oracle | -1,304 | -0.61% |
| benchmark | -1,323 | -0.60% |
| intraweek | -1,422 | -0.67% |
| random_hold | -1,598 | -0.77% |
| snake_viper_tick | -2,047 | -0.99% |
| snake_viper_wild | -2,083 | -0.99% |
| gold | -3,518 | -1.95% |

Average per day so far: unified Rs +618, benchmark Rs +563, snake_abs_exit Rs +438, snake_abs_exit_conv Rs +386, intramonth Rs +333, intraweek Rs +331, oracle Rs +311, snake_abs_conv Rs +295, snake_abs Rs +290, snake_viper_wild Rs +262, random_hold Rs +190, snake_viper_tick Rs +152, snake_anaconda Rs +151, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -10, snake_nonews Rs -326, snake Rs -347, gold Rs -633

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.