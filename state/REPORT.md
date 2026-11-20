# Paper trading report

Updated 2026-11-20 13:55 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,288 | +13.14% | 0 | - | 236 |
| benchmark | 224,434 | +12.22% | 0 | - | 237 |
| intraweek | 215,513 | +7.76% | 35 | 54% | 3,851 |
| intramonth | 215,113 | +7.56% | 0 | - | 235 |
| oracle | 212,831 | +6.42% | 0 | - | 233 |
| random_hold | 209,856 | +4.93% | 11 | 73% | 979 |
| snake_abs_exit | 208,833 | +4.42% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,850 | +3.42% | 2 | 50% | 345 |
| snake_abs | 205,944 | +2.97% | 1 | 100% | 255 |
| snake_abs_conv | 205,809 | +2.90% | 1 | 100% | 255 |
| snake_viper_wild | 203,556 | +1.78% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,356 | +0.68% | 0 | - | 237 |
| snake_anaconda | 200,099 | +0.05% | 3 | 33% | 374 |
| snake_viper_tick | 200,085 | +0.04% | 15 | 47% | 2,625 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,934 | -16.03% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,028 (-3.99%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,624 | +1.23% |
| benchmark | +2,058 | +0.93% |
| unified | +1,673 | +0.74% |
| random_hold | +1,403 | +0.67% |
| intramonth | +1,106 | +0.52% |
| oracle | +742 | +0.35% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -112 | -0.06% |
| snake_abs | -3,036 | -1.45% |
| snake_abs_conv | -3,051 | -1.46% |
| snake_anaconda | -3,364 | -1.65% |
| snake_viper_tick | -3,892 | -1.91% |
| snake_viper_wild | -3,967 | -1.91% |
| snake_abs_exit_conv | -4,214 | -2.00% |
| snake_abs_exit | -4,518 | -2.12% |
| gold | -6,839 | -3.91% |

Average per day so far: unified Rs +692, benchmark Rs +643, intraweek Rs +408, intramonth Rs +398, oracle Rs +338, random_hold Rs +259, snake_abs_exit Rs +252, snake_abs_exit_conv Rs +196, snake_abs_conv Rs +166, snake_abs Rs +165, snake_viper_wild Rs +119, nifty_calls Rs +48, benchmark_smallcap Rs +40, snake_viper_tick Rs +3, snake_anaconda Rs +3, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -844

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.