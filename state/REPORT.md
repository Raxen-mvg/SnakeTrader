# Paper trading report

Updated 2026-11-23 14:55 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,967 | +11.98% | 0 | - | 236 |
| benchmark | 221,527 | +10.76% | 0 | - | 237 |
| intraweek | 211,963 | +5.98% | 40 | 55% | 4,400 |
| oracle | 211,831 | +5.92% | 0 | - | 233 |
| intramonth | 211,730 | +5.87% | 0 | - | 235 |
| random_hold | 208,872 | +4.44% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,222 | +3.61% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,578 | +3.29% | 2 | 50% | 345 |
| snake_abs | 205,255 | +2.63% | 1 | 100% | 255 |
| snake_abs_conv | 205,077 | +2.54% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,249 | +0.62% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,843 | -0.08% | 0 | - | 237 |
| snake_anaconda | 198,163 | -0.92% | 3 | 33% | 374 |
| snake_viper_tick | 197,815 | -1.09% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,545 | -15.23% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,131 (-4.93%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,496 | +0.89% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -39 | -0.02% |
| oracle | -648 | -0.30% |
| snake_abs | -664 | -0.32% |
| snake_abs_conv | -706 | -0.34% |
| benchmark_smallcap | -1,065 | -0.53% |
| snake_abs_exit | -1,340 | -0.64% |
| snake_viper_tick | -1,557 | -0.78% |
| snake_viper_wild | -1,580 | -0.78% |
| snake_anaconda | -1,743 | -0.87% |
| random_hold | -1,887 | -0.90% |
| unified | -2,214 | -0.98% |
| intramonth | -3,274 | -1.52% |
| benchmark | -3,611 | -1.60% |
| intraweek | -3,749 | -1.74% |

Average per day so far: unified Rs +615, benchmark Rs +552, intraweek Rs +307, oracle Rs +303, intramonth Rs +301, random_hold Rs +227, snake_abs_exit Rs +201, snake_abs_exit_conv Rs +183, snake_abs Rs +142, snake_abs_conv Rs +141, nifty_calls Rs +47, snake_viper_wild Rs +40, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -4, snake_anaconda Rs -54, snake_viper_tick Rs -78, snake_nonews Rs -300, snake Rs -320, gold Rs -781

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.