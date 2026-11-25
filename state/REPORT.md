# Paper trading report

Updated 2026-11-25 13:52 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,629 | +12.31% | 0 | - | 236 |
| benchmark | 224,357 | +12.18% | 0 | - | 237 |
| oracle | 212,415 | +6.21% | 0 | - | 233 |
| intramonth | 212,207 | +6.10% | 0 | - | 235 |
| random_hold | 209,455 | +4.73% | 12 | 75% | 1,009 |
| intraweek | 207,700 | +3.85% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,474 | +0.74% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,161 | +0.58% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,723 | -0.14% | 1 | 100% | 255 |
| snake_abs_conv | 199,529 | -0.24% | 1 | 100% | 255 |
| benchmark_smallcap | 198,800 | -0.60% | 0 | - | 237 |
| snake_viper_wild | 197,058 | -1.47% | 16 | 50% | 2,827 |
| snake_viper_tick | 193,702 | -3.15% | 15 | 47% | 2,625 |
| snake_anaconda | 193,258 | -3.37% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,777 | -17.61% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,958 (-5.52%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,884 | +1.30% |
| random_hold | +1,028 | +0.49% |
| unified | +343 | +0.15% |
| oracle | +72 | +0.03% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -179 | -0.09% |
| intramonth | -544 | -0.26% |
| intraweek | -3,919 | -1.85% |
| snake_viper_tick | -3,990 | -2.02% |
| snake_viper_wild | -4,066 | -2.02% |
| gold | -4,653 | -2.75% |
| snake_anaconda | -5,446 | -2.74% |
| snake_abs | -5,738 | -2.79% |
| snake_abs_conv | -5,774 | -2.81% |
| snake_abs_exit_conv | -5,885 | -2.84% |
| snake_abs_exit | -6,021 | -2.90% |

Average per day so far: unified Rs +616, benchmark Rs +609, oracle Rs +310, intramonth Rs +305, random_hold Rs +236, intraweek Rs +192, nifty_calls Rs +46, snake_abs_exit Rs +40, snake_abs_exit_conv Rs +31, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -7, snake_abs_conv Rs -13, benchmark_smallcap Rs -33, snake_viper_wild Rs -92, snake_anaconda Rs -193, snake_viper_tick Rs -217, snake_nonews Rs -292, snake Rs -311, gold Rs -881

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.