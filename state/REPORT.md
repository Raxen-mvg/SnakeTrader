# Paper trading report

Updated 2026-11-25 12:01 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,849 | +12.93% | 0 | - | 237 |
| unified | 225,393 | +12.70% | 0 | - | 236 |
| intramonth | 213,117 | +6.56% | 0 | - | 235 |
| oracle | 212,612 | +6.31% | 0 | - | 233 |
| random_hold | 209,738 | +4.87% | 12 | 75% | 1,009 |
| intraweek | 207,759 | +3.88% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,414 | +1.21% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,812 | +0.91% | 2 | 50% | 345 |
| snake_abs | 201,168 | +0.58% | 1 | 100% | 255 |
| snake_abs_conv | 200,979 | +0.49% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,719 | -0.14% | 0 | - | 237 |
| snake_viper_wild | 196,881 | -1.56% | 16 | 50% | 2,827 |
| snake_anaconda | 193,977 | -3.01% | 3 | 33% | 374 |
| snake_viper_tick | 193,528 | -3.24% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,547 | -17.73% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,493 (-5.25%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,376 | +1.98% |
| random_hold | +1,312 | +0.63% |
| unified | +1,108 | +0.49% |
| benchmark_smallcap | +740 | +0.37% |
| intramonth | +365 | +0.17% |
| oracle | +270 | +0.13% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -3,860 | -1.82% |
| snake_viper_tick | -4,164 | -2.11% |
| snake_viper_wild | -4,243 | -2.11% |
| snake_abs | -4,293 | -2.09% |
| snake_abs_conv | -4,324 | -2.11% |
| snake_anaconda | -4,727 | -2.38% |
| gold | -4,883 | -2.88% |
| snake_abs_exit | -5,081 | -2.45% |
| snake_abs_exit_conv | -5,234 | -2.53% |

Average per day so far: benchmark Rs +646, unified Rs +635, intramonth Rs +328, oracle Rs +315, random_hold Rs +243, intraweek Rs +194, snake_abs_exit Rs +65, snake_abs_exit_conv Rs +49, nifty_calls Rs +46, snake_abs Rs +31, snake_abs_conv Rs +26, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -8, snake_viper_wild Rs -97, snake_anaconda Rs -172, snake_viper_tick Rs -223, snake_nonews Rs -292, snake Rs -311, gold Rs -886

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.