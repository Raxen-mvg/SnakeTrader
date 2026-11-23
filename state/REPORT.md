# Paper trading report

Updated 2026-11-23 12:20 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,129 | +12.06% | 0 | - | 236 |
| benchmark | 222,950 | +11.47% | 0 | - | 237 |
| intraweek | 212,429 | +6.21% | 40 | 55% | 4,400 |
| intramonth | 212,008 | +6.00% | 0 | - | 235 |
| oracle | 211,680 | +5.84% | 0 | - | 233 |
| random_hold | 208,999 | +4.50% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,313 | +3.66% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,959 | +2.98% | 2 | 50% | 345 |
| snake_abs | 205,067 | +2.53% | 1 | 100% | 255 |
| snake_abs_conv | 204,901 | +2.45% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,417 | +0.71% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,607 | -0.20% | 0 | - | 237 |
| snake_anaconda | 198,354 | -0.82% | 3 | 33% | 374 |
| snake_viper_tick | 197,979 | -1.01% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,235 | -14.88% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,225 (-4.89%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,187 | +1.30% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -657 | -0.32% |
| oracle | -798 | -0.38% |
| snake_abs | -853 | -0.41% |
| snake_abs_conv | -882 | -0.43% |
| snake_abs_exit | -1,249 | -0.60% |
| benchmark_smallcap | -1,300 | -0.65% |
| snake_viper_tick | -1,392 | -0.70% |
| snake_viper_wild | -1,412 | -0.70% |
| snake_anaconda | -1,551 | -0.78% |
| random_hold | -1,760 | -0.83% |
| unified | -2,053 | -0.91% |
| benchmark | -2,188 | -0.97% |
| intramonth | -2,996 | -1.39% |
| intraweek | -3,283 | -1.52% |

Average per day so far: unified Rs +619, benchmark Rs +588, intraweek Rs +319, intramonth Rs +308, oracle Rs +299, random_hold Rs +231, snake_abs_exit Rs +203, snake_abs_exit_conv Rs +166, snake_abs Rs +137, snake_abs_conv Rs +136, nifty_calls Rs +47, snake_viper_wild Rs +46, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -11, snake_anaconda Rs -48, snake_viper_tick Rs -72, snake_nonews Rs -300, snake Rs -320, gold Rs -763

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.