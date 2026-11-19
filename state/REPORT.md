# Paper trading report

Updated 2026-11-19 13:37 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,854 | +11.93% | 0 | - | 236 |
| benchmark | 221,741 | +10.87% | 0 | - | 237 |
| intramonth | 213,364 | +6.68% | 0 | - | 235 |
| snake_abs_exit | 213,038 | +6.52% | 2 | 50% | 345 |
| intraweek | 211,934 | +5.97% | 35 | 54% | 3,851 |
| oracle | 211,563 | +5.78% | 0 | - | 233 |
| snake_abs_exit_conv | 211,052 | +5.53% | 2 | 50% | 345 |
| snake_abs | 208,581 | +4.29% | 1 | 100% | 255 |
| snake_abs_conv | 208,459 | +4.23% | 1 | 100% | 255 |
| random_hold | 207,721 | +3.86% | 10 | 70% | 733 |
| snake_viper_wild | 207,288 | +3.64% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,747 | +1.87% | 15 | 47% | 2,625 |
| snake_anaconda | 203,150 | +1.57% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,638 | +0.32% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,987 | -12.51% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,358 (-4.32%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,446 | +0.66% |
| benchmark_smallcap | +1,312 | +0.66% |
| unified | +1,243 | +0.56% |
| intramonth | +1,091 | +0.51% |
| random_hold | +788 | +0.38% |
| oracle | +767 | +0.36% |
| snake_viper_wild | +248 | +0.12% |
| snake_viper_tick | +243 | +0.12% |
| intraweek | +95 | +0.04% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -855 | -0.41% |
| snake_abs_conv | -866 | -0.41% |
| snake_abs_exit | -993 | -0.46% |
| snake_anaconda | -1,251 | -0.61% |
| snake_abs_exit_conv | -1,331 | -0.63% |
| gold | -2,334 | -1.32% |

Average per day so far: unified Rs +645, benchmark Rs +588, snake_abs_exit Rs +383, intramonth Rs +361, snake_abs_exit_conv Rs +325, intraweek Rs +323, oracle Rs +313, snake_viper_wild Rs +251, snake_abs_conv Rs +249, snake_abs Rs +245, random_hold Rs +209, snake_viper_tick Rs +144, snake_anaconda Rs +98, nifty_calls Rs +50, benchmark_smallcap Rs +19, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -676

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.