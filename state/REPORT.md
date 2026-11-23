# Paper trading report

Updated 2026-11-23 11:10 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,308 | +12.15% | 0 | - | 236 |
| benchmark | 223,271 | +11.63% | 0 | - | 237 |
| intraweek | 212,916 | +6.46% | 40 | 55% | 4,400 |
| intramonth | 212,372 | +6.19% | 0 | - | 235 |
| oracle | 211,184 | +5.59% | 0 | - | 233 |
| random_hold | 209,685 | +4.84% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,984 | +3.49% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,992 | +3.00% | 2 | 50% | 345 |
| snake_abs | 204,338 | +2.17% | 1 | 100% | 255 |
| snake_abs_conv | 204,184 | +2.09% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,558 | +0.28% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,361 | -0.32% | 0 | - | 237 |
| snake_anaconda | 197,993 | -1.00% | 3 | 33% | 374 |
| snake_viper_tick | 197,138 | -1.43% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,087 | -14.96% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,299 (-4.85%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,039 | +1.21% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -624 | -0.30% |
| random_hold | -1,074 | -0.51% |
| oracle | -1,294 | -0.61% |
| benchmark_smallcap | -1,547 | -0.77% |
| snake_abs_exit | -1,578 | -0.76% |
| snake_abs | -1,582 | -0.77% |
| snake_abs_conv | -1,599 | -0.78% |
| benchmark | -1,867 | -0.83% |
| unified | -1,873 | -0.83% |
| snake_anaconda | -1,913 | -0.96% |
| snake_viper_tick | -2,234 | -1.12% |
| snake_viper_wild | -2,271 | -1.12% |
| intramonth | -2,632 | -1.22% |
| intraweek | -2,796 | -1.30% |

Average per day so far: unified Rs +623, benchmark Rs +597, intraweek Rs +331, intramonth Rs +317, oracle Rs +287, random_hold Rs +248, snake_abs_exit Rs +194, snake_abs_exit_conv Rs +166, snake_abs Rs +117, snake_abs_conv Rs +116, nifty_calls Rs +47, snake_viper_wild Rs +18, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -18, snake_anaconda Rs -59, snake_viper_tick Rs -102, snake_nonews Rs -300, snake Rs -320, gold Rs -767

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.