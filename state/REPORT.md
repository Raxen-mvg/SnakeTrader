# Paper trading report

Updated 2026-11-19 09:32 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,614 | +11.81% | 0 | - | 236 |
| benchmark | 219,339 | +9.67% | 0 | - | 237 |
| intramonth | 213,546 | +6.77% | 0 | - | 235 |
| snake_abs_exit | 213,008 | +6.50% | 2 | 50% | 345 |
| intraweek | 211,566 | +5.78% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,382 | +5.69% | 2 | 50% | 345 |
| oracle | 211,088 | +5.54% | 0 | - | 233 |
| snake_abs | 208,789 | +4.39% | 1 | 100% | 255 |
| snake_abs_conv | 208,664 | +4.33% | 1 | 100% | 255 |
| snake_viper_wild | 207,855 | +3.93% | 16 | 50% | 2,827 |
| random_hold | 207,289 | +3.65% | 10 | 70% | 733 |
| snake_viper_tick | 204,302 | +2.15% | 15 | 47% | 2,625 |
| snake_anaconda | 203,597 | +1.80% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,282 | -0.36% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,658 | -12.67% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,132 (-4.43%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| intramonth | +1,273 | +0.60% |
| unified | +1,003 | +0.45% |
| snake_viper_wild | +816 | +0.39% |
| snake_viper_tick | +799 | +0.39% |
| random_hold | +357 | +0.17% |
| oracle | +292 | +0.14% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| benchmark_smallcap | -45 | -0.02% |
| intraweek | -273 | -0.13% |
| snake_abs | -647 | -0.31% |
| snake_abs_conv | -661 | -0.32% |
| snake_anaconda | -804 | -0.39% |
| benchmark | -956 | -0.43% |
| snake_abs_exit_conv | -1,001 | -0.47% |
| snake_abs_exit | -1,024 | -0.48% |
| gold | -2,663 | -1.50% |

Average per day so far: unified Rs +638, benchmark Rs +523, snake_abs_exit Rs +383, intramonth Rs +366, snake_abs_exit_conv Rs +335, intraweek Rs +313, oracle Rs +300, snake_viper_wild Rs +271, snake_abs_conv Rs +255, snake_abs Rs +251, random_hold Rs +197, snake_viper_tick Rs +165, snake_anaconda Rs +112, nifty_calls Rs +50, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -22, snake_nonews Rs -317, snake Rs -337, gold Rs -685

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.