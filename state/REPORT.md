# Paper trading report

Updated 2026-11-18 09:28 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,412 | +10.71% | 0 | - | 236 |
| benchmark | 220,609 | +10.30% | 0 | - | 237 |
| snake_abs_exit | 213,629 | +6.82% | 2 | 50% | 345 |
| intraweek | 212,364 | +6.18% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 212,007 | +6.00% | 2 | 50% | 345 |
| oracle | 211,790 | +5.89% | 0 | - | 233 |
| intramonth | 211,374 | +5.69% | 0 | - | 235 |
| snake_abs | 209,107 | +4.55% | 1 | 100% | 255 |
| snake_abs_conv | 208,970 | +4.49% | 1 | 100% | 255 |
| snake_viper_wild | 207,926 | +3.96% | 14 | 50% | 2,496 |
| random_hold | 207,145 | +3.57% | 10 | 70% | 733 |
| snake_viper_tick | 204,372 | +2.19% | 13 | 46% | 2,299 |
| snake_anaconda | 204,101 | +2.05% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,887 | -0.06% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,091 | -11.46% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,647 (-4.68%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_conv | +551 | +0.26% |
| snake_abs | +549 | +0.26% |
| snake_abs_exit | +488 | +0.23% |
| snake_abs_exit_conv | +433 | +0.20% |
| snake_anaconda | +46 | +0.02% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| unified | -27 | -0.01% |
| intramonth | -168 | -0.08% |
| benchmark_smallcap | -684 | -0.34% |
| oracle | -696 | -0.33% |
| intraweek | -958 | -0.45% |
| benchmark | -994 | -0.45% |
| random_hold | -1,287 | -0.62% |
| snake_viper_tick | -1,465 | -0.71% |
| snake_viper_wild | -1,489 | -0.71% |
| gold | -3,633 | -2.01% |

Average per day so far: unified Rs +595, benchmark Rs +572, snake_abs_exit Rs +413, snake_abs_exit_conv Rs +364, intraweek Rs +343, oracle Rs +328, intramonth Rs +316, snake_viper_wild Rs +283, snake_abs_conv Rs +272, snake_abs Rs +268, random_hold Rs +198, snake_viper_tick Rs +175, snake_anaconda Rs +132, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -4, snake_nonews Rs -326, snake Rs -347, gold Rs -636

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.