# Paper trading report

Updated 2026-11-17 11:07 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,259 | +11.13% | 0 | - | 236 |
| benchmark | 221,718 | +10.86% | 0 | - | 237 |
| snake_abs_exit | 216,446 | +8.22% | 2 | 50% | 345 |
| snake_abs_exit_conv | 214,217 | +7.11% | 2 | 50% | 345 |
| intraweek | 214,054 | +7.03% | 35 | 54% | 3,851 |
| oracle | 212,955 | +6.48% | 0 | - | 233 |
| intramonth | 212,326 | +6.16% | 0 | - | 235 |
| snake_abs | 210,505 | +5.25% | 1 | 100% | 255 |
| snake_abs_conv | 210,357 | +5.18% | 1 | 100% | 255 |
| random_hold | 208,264 | +4.13% | 10 | 70% | 733 |
| snake_viper_wild | 207,426 | +3.71% | 14 | 50% | 2,496 |
| snake_anaconda | 205,964 | +2.98% | 3 | 33% | 374 |
| snake_viper_tick | 203,879 | +1.94% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,331 | +1.17% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,776 | -9.11% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,754 (-4.12%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,788 | +1.32% |
| snake_abs_exit | +2,037 | +0.95% |
| benchmark | +1,637 | +0.74% |
| benchmark_smallcap | +1,502 | +0.75% |
| snake_viper_wild | +1,281 | +0.62% |
| snake_viper_tick | +1,259 | +0.62% |
| snake_abs_exit_conv | +999 | +0.47% |
| oracle | +932 | +0.44% |
| snake_anaconda | +861 | +0.42% |
| gold | +822 | +0.45% |
| unified | +821 | +0.37% |
| intramonth | +708 | +0.33% |
| random_hold | +470 | +0.23% |
| snake_abs | +371 | +0.18% |
| snake_abs_conv | +367 | +0.17% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +636, benchmark Rs +621, snake_abs_exit Rs +514, snake_abs_exit_conv Rs +444, intraweek Rs +402, oracle Rs +370, intramonth Rs +352, snake_abs_conv Rs +324, snake_abs Rs +318, snake_viper_wild Rs +275, random_hold Rs +236, snake_anaconda Rs +199, snake_viper_tick Rs +162, benchmark_smallcap Rs +75, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -521

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.