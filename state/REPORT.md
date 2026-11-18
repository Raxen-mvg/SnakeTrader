# Paper trading report

Updated 2026-11-18 13:48 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,933 | +11.47% | 0 | - | 236 |
| benchmark | 219,729 | +9.87% | 0 | - | 237 |
| intramonth | 212,758 | +6.38% | 0 | - | 235 |
| snake_abs_exit | 212,594 | +6.30% | 2 | 50% | 345 |
| oracle | 212,228 | +6.11% | 0 | - | 233 |
| intraweek | 212,146 | +6.07% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 210,861 | +5.43% | 2 | 50% | 345 |
| snake_abs | 208,079 | +4.04% | 1 | 100% | 255 |
| snake_abs_conv | 207,940 | +3.97% | 1 | 100% | 255 |
| random_hold | 207,063 | +3.53% | 10 | 70% | 733 |
| snake_viper_wild | 206,718 | +3.36% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,188 | +1.59% | 15 | 47% | 2,625 |
| snake_anaconda | 203,020 | +1.51% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,181 | -0.41% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 176,910 | -11.54% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,135 (-4.43%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,494 | +0.68% |
| intramonth | +1,216 | +0.57% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| oracle | -258 | -0.12% |
| snake_abs | -480 | -0.23% |
| snake_abs_conv | -480 | -0.23% |
| snake_abs_exit | -548 | -0.26% |
| snake_abs_exit_conv | -713 | -0.34% |
| snake_anaconda | -1,035 | -0.51% |
| intraweek | -1,177 | -0.55% |
| random_hold | -1,370 | -0.66% |
| benchmark_smallcap | -1,390 | -0.69% |
| benchmark | -1,874 | -0.85% |
| snake_viper_tick | -2,648 | -1.29% |
| snake_viper_wild | -2,697 | -1.29% |
| gold | -3,814 | -2.11% |

Average per day so far: unified Rs +637, benchmark Rs +548, snake_abs_exit Rs +382, intramonth Rs +354, oracle Rs +340, intraweek Rs +337, snake_abs_exit_conv Rs +329, snake_abs_conv Rs +241, snake_viper_wild Rs +240, snake_abs Rs +238, random_hold Rs +196, snake_viper_tick Rs +128, snake_anaconda Rs +97, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -26, snake_nonews Rs -326, snake Rs -347, gold Rs -641

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.