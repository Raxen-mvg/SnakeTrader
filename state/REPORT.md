# Paper trading report

Updated 2026-11-18 14:49 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,271 | +11.14% | 0 | - | 236 |
| benchmark | 220,287 | +10.14% | 0 | - | 237 |
| snake_abs_exit | 214,488 | +7.24% | 2 | 50% | 345 |
| snake_abs_exit_conv | 212,784 | +6.39% | 2 | 50% | 345 |
| intramonth | 211,990 | +6.00% | 0 | - | 235 |
| intraweek | 211,674 | +5.84% | 35 | 54% | 3,851 |
| oracle | 211,301 | +5.65% | 0 | - | 233 |
| snake_abs | 209,912 | +4.96% | 1 | 100% | 255 |
| snake_abs_conv | 209,803 | +4.90% | 1 | 100% | 255 |
| snake_viper_wild | 207,135 | +3.57% | 16 | 50% | 2,827 |
| random_hold | 206,850 | +3.42% | 10 | 70% | 733 |
| snake_anaconda | 204,734 | +2.37% | 3 | 33% | 374 |
| snake_viper_tick | 203,597 | +1.80% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,708 | -0.15% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,173 | -11.41% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,686 (-4.66%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_conv | +1,384 | +0.66% |
| snake_abs | +1,353 | +0.65% |
| snake_abs_exit | +1,346 | +0.63% |
| snake_abs_exit_conv | +1,210 | +0.57% |
| unified | +833 | +0.38% |
| snake_anaconda | +679 | +0.33% |
| intramonth | +448 | +0.21% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| benchmark_smallcap | -863 | -0.43% |
| oracle | -1,185 | -0.56% |
| benchmark | -1,316 | -0.59% |
| random_hold | -1,582 | -0.76% |
| intraweek | -1,649 | -0.77% |
| snake_viper_tick | -2,239 | -1.09% |
| snake_viper_wild | -2,280 | -1.09% |
| gold | -3,551 | -1.97% |

Average per day so far: unified Rs +619, benchmark Rs +564, snake_abs_exit Rs +439, snake_abs_exit_conv Rs +387, intramonth Rs +333, intraweek Rs +324, oracle Rs +314, snake_abs_conv Rs +297, snake_abs Rs +292, snake_viper_wild Rs +255, random_hold Rs +190, snake_anaconda Rs +153, snake_viper_tick Rs +144, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -9, snake_nonews Rs -326, snake Rs -347, gold Rs -634

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.