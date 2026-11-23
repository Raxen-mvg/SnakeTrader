# Paper trading report

Updated 2026-11-23 13:19 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,842 | +11.92% | 0 | - | 236 |
| benchmark | 222,445 | +11.22% | 0 | - | 237 |
| intraweek | 212,262 | +6.13% | 40 | 55% | 4,400 |
| intramonth | 212,046 | +6.02% | 0 | - | 235 |
| oracle | 211,674 | +5.84% | 0 | - | 233 |
| random_hold | 208,861 | +4.43% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,760 | +3.38% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,358 | +2.68% | 2 | 50% | 345 |
| snake_abs | 204,274 | +2.14% | 1 | 100% | 255 |
| snake_abs_conv | 204,107 | +2.05% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,831 | +0.42% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,237 | -0.38% | 0 | - | 237 |
| snake_anaconda | 197,893 | -1.05% | 3 | 33% | 374 |
| snake_viper_tick | 197,406 | -1.30% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,055 | -14.97% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,024 (-4.99%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,006 | +1.19% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -804 | -0.38% |
| snake_abs_exit_conv | -1,258 | -0.61% |
| snake_abs | -1,646 | -0.80% |
| benchmark_smallcap | -1,670 | -0.83% |
| snake_abs_conv | -1,676 | -0.81% |
| snake_abs_exit | -1,802 | -0.86% |
| random_hold | -1,898 | -0.90% |
| snake_viper_tick | -1,966 | -0.99% |
| snake_viper_wild | -1,998 | -0.98% |
| snake_anaconda | -2,013 | -1.01% |
| unified | -2,340 | -1.03% |
| benchmark | -2,693 | -1.20% |
| intramonth | -2,958 | -1.38% |
| intraweek | -3,450 | -1.60% |

Average per day so far: unified Rs +611, benchmark Rs +576, intraweek Rs +314, intramonth Rs +309, oracle Rs +299, random_hold Rs +227, snake_abs_exit Rs +188, snake_abs_exit_conv Rs +149, snake_abs Rs +116, snake_abs_conv Rs +114, nifty_calls Rs +47, snake_viper_wild Rs +27, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -22, snake_anaconda Rs -62, snake_viper_tick Rs -93, snake_nonews Rs -300, snake Rs -320, gold Rs -768

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.