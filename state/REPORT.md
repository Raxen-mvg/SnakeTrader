# Paper trading report

Updated 2026-11-25 14:52 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,587 | +12.29% | 0 | - | 237 |
| unified | 224,516 | +12.26% | 0 | - | 236 |
| oracle | 212,848 | +6.42% | 0 | - | 233 |
| intramonth | 211,932 | +5.97% | 0 | - | 235 |
| random_hold | 209,825 | +4.91% | 12 | 75% | 1,009 |
| intraweek | 206,902 | +3.45% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,520 | +0.76% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,202 | +0.60% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,552 | -0.22% | 1 | 100% | 255 |
| snake_abs_conv | 199,357 | -0.32% | 1 | 100% | 255 |
| benchmark_smallcap | 198,991 | -0.51% | 0 | - | 237 |
| snake_viper_wild | 197,476 | -1.26% | 16 | 50% | 2,827 |
| snake_viper_tick | 194,111 | -2.94% | 15 | 47% | 2,625 |
| snake_anaconda | 193,310 | -3.35% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,139 | -17.43% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,945 (-5.53%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,114 | +1.41% |
| random_hold | +1,398 | +0.67% |
| oracle | +506 | +0.24% |
| unified | +230 | +0.10% |
| benchmark_smallcap | +11 | +0.01% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -820 | -0.39% |
| snake_viper_tick | -3,582 | -1.81% |
| snake_viper_wild | -3,648 | -1.81% |
| gold | -4,291 | -2.53% |
| intraweek | -4,717 | -2.23% |
| snake_anaconda | -5,393 | -2.71% |
| snake_abs_exit_conv | -5,843 | -2.82% |
| snake_abs | -5,908 | -2.88% |
| snake_abs_conv | -5,946 | -2.90% |
| snake_abs_exit | -5,975 | -2.88% |

Average per day so far: benchmark Rs +615, unified Rs +613, oracle Rs +321, intramonth Rs +298, random_hold Rs +246, intraweek Rs +173, nifty_calls Rs +46, snake_abs_exit Rs +41, snake_abs_exit_conv Rs +32, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -12, snake_abs_conv Rs -17, benchmark_smallcap Rs -28, snake_viper_wild Rs -79, snake_anaconda Rs -191, snake_viper_tick Rs -203, snake_nonews Rs -292, snake Rs -311, gold Rs -872

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.