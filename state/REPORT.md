# Paper trading report

Updated 2026-11-17 09:24 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,816 | +11.41% | 0 | - | 236 |
| benchmark | 220,984 | +10.49% | 0 | - | 237 |
| snake_abs_exit | 214,412 | +7.21% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,742 | +6.87% | 2 | 50% | 345 |
| intramonth | 213,052 | +6.53% | 0 | - | 235 |
| intraweek | 213,017 | +6.51% | 35 | 54% | 3,851 |
| oracle | 212,897 | +6.45% | 0 | - | 233 |
| snake_abs | 210,406 | +5.20% | 1 | 100% | 255 |
| snake_abs_conv | 210,253 | +5.13% | 1 | 100% | 255 |
| random_hold | 207,843 | +3.92% | 10 | 70% | 733 |
| snake_viper_wild | 206,410 | +3.21% | 14 | 50% | 2,496 |
| snake_anaconda | 205,498 | +2.75% | 3 | 33% | 374 |
| snake_viper_tick | 202,880 | +1.44% | 13 | 46% | 2,299 |
| benchmark_smallcap | 201,961 | +0.98% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,332 | -9.33% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,792 (-4.10%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,751 | +0.83% |
| intramonth | +1,433 | +0.68% |
| unified | +1,378 | +0.62% |
| benchmark_smallcap | +1,132 | +0.56% |
| benchmark | +903 | +0.41% |
| oracle | +874 | +0.41% |
| snake_abs_exit_conv | +525 | +0.25% |
| snake_anaconda | +396 | +0.19% |
| gold | +378 | +0.21% |
| snake_abs | +272 | +0.13% |
| snake_viper_wild | +265 | +0.13% |
| snake_abs_conv | +264 | +0.13% |
| snake_viper_tick | +261 | +0.13% |
| random_hold | +50 | +0.02% |
| snake_abs_exit | +2 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +652, benchmark Rs +600, snake_abs_exit Rs +450, snake_abs_exit_conv Rs +429, intramonth Rs +373, intraweek Rs +372, oracle Rs +368, snake_abs_conv Rs +320, snake_abs Rs +315, snake_viper_wild Rs +237, random_hold Rs +224, snake_anaconda Rs +183, snake_viper_tick Rs +120, benchmark_smallcap Rs +63, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -533

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.