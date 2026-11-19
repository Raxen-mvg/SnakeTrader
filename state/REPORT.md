# Paper trading report

Updated 2026-11-19 10:25 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,730 | +11.87% | 0 | - | 236 |
| benchmark | 220,555 | +10.28% | 0 | - | 237 |
| snake_abs_exit | 213,586 | +6.79% | 2 | 50% | 345 |
| intramonth | 213,177 | +6.59% | 0 | - | 235 |
| intraweek | 212,096 | +6.05% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,770 | +5.88% | 2 | 50% | 345 |
| oracle | 211,085 | +5.54% | 0 | - | 233 |
| snake_abs | 209,291 | +4.64% | 1 | 100% | 255 |
| snake_abs_conv | 209,167 | +4.58% | 1 | 100% | 255 |
| random_hold | 207,929 | +3.96% | 10 | 70% | 733 |
| snake_viper_wild | 207,835 | +3.92% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,282 | +2.14% | 15 | 47% | 2,625 |
| snake_anaconda | 203,470 | +1.74% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,414 | +0.21% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,608 | -12.70% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,252 (-4.37%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,119 | +0.50% |
| benchmark_smallcap | +1,087 | +0.55% |
| random_hold | +996 | +0.48% |
| intramonth | +903 | +0.42% |
| snake_viper_wild | +795 | +0.38% |
| snake_viper_tick | +779 | +0.38% |
| oracle | +289 | +0.14% |
| benchmark | +260 | +0.12% |
| intraweek | +257 | +0.12% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -146 | -0.07% |
| snake_abs_conv | -158 | -0.07% |
| snake_abs_exit | -446 | -0.21% |
| snake_abs_exit_conv | -613 | -0.29% |
| snake_anaconda | -931 | -0.46% |
| gold | -2,713 | -1.53% |

Average per day so far: unified Rs +641, benchmark Rs +556, snake_abs_exit Rs +400, intramonth Rs +356, snake_abs_exit_conv Rs +346, intraweek Rs +327, oracle Rs +300, snake_viper_wild Rs +270, snake_abs_conv Rs +270, snake_abs Rs +265, random_hold Rs +214, snake_viper_tick Rs +165, snake_anaconda Rs +108, nifty_calls Rs +50, benchmark_smallcap Rs +13, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -686

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.