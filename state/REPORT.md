# Paper trading report

Updated 2026-11-19 09:56 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,248 | +12.12% | 0 | - | 236 |
| benchmark | 220,425 | +10.21% | 0 | - | 237 |
| intramonth | 214,054 | +7.03% | 0 | - | 235 |
| snake_abs_exit | 213,740 | +6.87% | 2 | 50% | 345 |
| snake_abs_exit_conv | 211,978 | +5.99% | 2 | 50% | 345 |
| intraweek | 211,784 | +5.89% | 35 | 54% | 3,851 |
| oracle | 211,512 | +5.76% | 0 | - | 233 |
| snake_abs | 209,239 | +4.62% | 1 | 100% | 255 |
| snake_abs_conv | 209,120 | +4.56% | 1 | 100% | 255 |
| random_hold | 207,993 | +4.00% | 10 | 70% | 733 |
| snake_viper_wild | 207,591 | +3.80% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,044 | +2.02% | 15 | 47% | 2,625 |
| snake_anaconda | 203,968 | +1.98% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,493 | +0.25% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,871 | -12.56% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,595 (-4.20%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| intramonth | +1,781 | +0.84% |
| unified | +1,636 | +0.73% |
| benchmark_smallcap | +1,166 | +0.58% |
| random_hold | +1,061 | +0.51% |
| oracle | +716 | +0.34% |
| snake_viper_wild | +552 | +0.27% |
| snake_viper_tick | +540 | +0.27% |
| benchmark | +130 | +0.06% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -55 | -0.03% |
| snake_abs | -197 | -0.09% |
| snake_abs_conv | -205 | -0.10% |
| snake_abs_exit | -292 | -0.14% |
| snake_abs_exit_conv | -406 | -0.19% |
| snake_anaconda | -433 | -0.21% |
| gold | -2,450 | -1.38% |

Average per day so far: unified Rs +655, benchmark Rs +552, snake_abs_exit Rs +404, intramonth Rs +380, snake_abs_exit_conv Rs +352, intraweek Rs +318, oracle Rs +311, snake_abs_conv Rs +268, snake_abs Rs +264, snake_viper_wild Rs +262, random_hold Rs +216, snake_viper_tick Rs +156, snake_anaconda Rs +124, nifty_calls Rs +50, benchmark_smallcap Rs +15, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -679

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.