# Paper trading report

Updated 2026-11-18 10:37 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,946 | +10.97% | 0 | - | 236 |
| benchmark | 220,341 | +10.17% | 0 | - | 237 |
| intraweek | 214,755 | +7.38% | 35 | 54% | 3,851 |
| snake_abs_exit | 212,534 | +6.27% | 2 | 50% | 345 |
| intramonth | 211,919 | +5.96% | 0 | - | 235 |
| oracle | 211,788 | +5.89% | 0 | - | 233 |
| snake_abs_exit_conv | 210,823 | +5.41% | 2 | 50% | 345 |
| snake_abs | 207,757 | +3.88% | 1 | 100% | 255 |
| snake_abs_conv | 207,617 | +3.81% | 1 | 100% | 255 |
| random_hold | 207,216 | +3.61% | 10 | 70% | 733 |
| snake_viper_wild | 207,116 | +3.56% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,578 | +1.79% | 15 | 47% | 2,625 |
| snake_anaconda | 202,780 | +1.39% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,775 | -0.11% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,354 | -11.32% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,144 (-4.43%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,432 | +0.67% |
| unified | +507 | +0.23% |
| intramonth | +376 | +0.18% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs_exit | -608 | -0.28% |
| oracle | -699 | -0.33% |
| snake_abs_exit_conv | -751 | -0.35% |
| benchmark_smallcap | -796 | -0.40% |
| snake_abs | -801 | -0.38% |
| snake_abs_conv | -803 | -0.39% |
| random_hold | -1,216 | -0.58% |
| benchmark | -1,262 | -0.57% |
| snake_anaconda | -1,275 | -0.62% |
| snake_viper_tick | -2,258 | -1.10% |
| snake_viper_wild | -2,299 | -1.10% |
| gold | -3,370 | -1.86% |

Average per day so far: unified Rs +610, benchmark Rs +565, intraweek Rs +410, snake_abs_exit Rs +380, intramonth Rs +331, snake_abs_exit_conv Rs +328, oracle Rs +327, snake_viper_wild Rs +254, snake_abs_conv Rs +231, snake_abs Rs +228, random_hold Rs +200, snake_viper_tick Rs +143, snake_anaconda Rs +90, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -7, snake_nonews Rs -326, snake Rs -347, gold Rs -629

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.