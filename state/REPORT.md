# Paper trading report

Updated 2026-11-20 11:16 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,532 | +12.77% | 0 | - | 236 |
| benchmark | 222,789 | +11.39% | 0 | - | 237 |
| intramonth | 214,526 | +7.26% | 0 | - | 235 |
| intraweek | 214,229 | +7.12% | 35 | 54% | 3,851 |
| oracle | 212,595 | +6.30% | 0 | - | 233 |
| snake_abs_exit | 210,675 | +5.34% | 2 | 50% | 345 |
| random_hold | 209,144 | +4.57% | 11 | 73% | 979 |
| snake_abs_exit_conv | 208,287 | +4.14% | 2 | 50% | 345 |
| snake_abs | 207,425 | +3.71% | 1 | 100% | 255 |
| snake_abs_conv | 207,286 | +3.64% | 1 | 100% | 255 |
| snake_viper_wild | 206,151 | +3.08% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,632 | +1.32% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,331 | +0.67% | 3 | 33% | 374 |
| benchmark_smallcap | 200,403 | +0.20% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,106 | -17.45% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,899 (-4.05%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,340 | +0.63% |
| unified | +916 | +0.41% |
| random_hold | +691 | +0.33% |
| intramonth | +518 | +0.24% |
| oracle | +506 | +0.24% |
| benchmark | +413 | +0.19% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -1,065 | -0.53% |
| snake_viper_tick | -1,345 | -0.66% |
| snake_viper_wild | -1,372 | -0.66% |
| snake_abs | -1,555 | -0.74% |
| snake_abs_conv | -1,574 | -0.75% |
| snake_anaconda | -2,133 | -1.05% |
| snake_abs_exit | -2,676 | -1.25% |
| snake_abs_exit_conv | -2,777 | -1.32% |
| gold | -9,667 | -5.53% |

Average per day so far: unified Rs +672, benchmark Rs +600, intramonth Rs +382, intraweek Rs +374, oracle Rs +331, snake_abs_exit Rs +305, random_hold Rs +241, snake_abs_exit_conv Rs +237, snake_abs_conv Rs +208, snake_abs Rs +206, snake_viper_wild Rs +205, snake_viper_tick Rs +97, nifty_calls Rs +48, snake_anaconda Rs +40, benchmark_smallcap Rs +12, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -918

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.