# Paper trading report

Updated 2026-11-18 10:03 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,422 | +11.21% | 0 | - | 236 |
| benchmark | 220,685 | +10.34% | 0 | - | 237 |
| intraweek | 214,496 | +7.25% | 35 | 54% | 3,851 |
| oracle | 212,414 | +6.21% | 0 | - | 233 |
| snake_abs_exit | 212,355 | +6.18% | 2 | 50% | 345 |
| intramonth | 212,284 | +6.14% | 0 | - | 235 |
| snake_abs_exit_conv | 210,769 | +5.38% | 2 | 50% | 345 |
| snake_abs | 208,155 | +4.08% | 1 | 100% | 255 |
| snake_abs_conv | 208,001 | +4.00% | 1 | 100% | 255 |
| random_hold | 207,414 | +3.71% | 10 | 70% | 733 |
| snake_viper_wild | 207,161 | +3.58% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,622 | +1.81% | 15 | 47% | 2,625 |
| snake_anaconda | 203,090 | +1.54% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,168 | +0.08% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,370 | -11.31% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,432 (-4.28%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,174 | +0.55% |
| unified | +983 | +0.44% |
| intramonth | +742 | +0.35% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -72 | -0.03% |
| snake_abs | -403 | -0.19% |
| benchmark_smallcap | -404 | -0.20% |
| snake_abs_conv | -418 | -0.20% |
| snake_abs_exit | -787 | -0.37% |
| snake_abs_exit_conv | -805 | -0.38% |
| benchmark | -918 | -0.41% |
| snake_anaconda | -964 | -0.47% |
| random_hold | -1,019 | -0.49% |
| snake_viper_tick | -2,215 | -1.08% |
| snake_viper_wild | -2,254 | -1.08% |
| gold | -3,354 | -1.86% |

Average per day so far: unified Rs +623, benchmark Rs +575, intraweek Rs +403, snake_abs_exit Rs +374, oracle Rs +345, intramonth Rs +341, snake_abs_exit_conv Rs +326, snake_viper_wild Rs +256, snake_abs_conv Rs +242, snake_abs Rs +240, random_hold Rs +206, snake_viper_tick Rs +145, snake_anaconda Rs +100, nifty_calls Rs +51, benchmark_smallcap Rs +5, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -326, snake Rs -347, gold Rs -629

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.