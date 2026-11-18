# Paper trading report

Updated 2026-11-18 12:40 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,262 | +11.13% | 0 | - | 236 |
| benchmark | 219,928 | +9.96% | 0 | - | 237 |
| intraweek | 213,314 | +6.66% | 35 | 54% | 3,851 |
| snake_abs_exit | 212,675 | +6.34% | 2 | 50% | 345 |
| intramonth | 212,283 | +6.14% | 0 | - | 235 |
| oracle | 211,638 | +5.82% | 0 | - | 233 |
| snake_abs_exit_conv | 210,836 | +5.42% | 2 | 50% | 345 |
| snake_abs | 207,925 | +3.96% | 1 | 100% | 255 |
| snake_abs_conv | 207,786 | +3.89% | 1 | 100% | 255 |
| snake_viper_wild | 207,059 | +3.53% | 16 | 50% | 2,827 |
| random_hold | 206,951 | +3.48% | 10 | 70% | 733 |
| snake_viper_tick | 203,522 | +1.76% | 15 | 47% | 2,625 |
| snake_anaconda | 202,810 | +1.41% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,237 | -0.38% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 176,910 | -11.54% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,971 (-4.51%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +824 | +0.37% |
| intramonth | +741 | +0.35% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraweek | -9 | -0.00% |
| snake_abs_exit | -467 | -0.22% |
| snake_abs | -633 | -0.30% |
| snake_abs_conv | -634 | -0.30% |
| snake_abs_exit_conv | -738 | -0.35% |
| oracle | -848 | -0.40% |
| snake_anaconda | -1,245 | -0.61% |
| benchmark_smallcap | -1,334 | -0.67% |
| random_hold | -1,481 | -0.71% |
| benchmark | -1,675 | -0.76% |
| snake_viper_tick | -2,315 | -1.12% |
| snake_viper_wild | -2,356 | -1.12% |
| gold | -3,814 | -2.11% |

Average per day so far: unified Rs +618, benchmark Rs +554, snake_abs_exit Rs +384, intraweek Rs +370, intramonth Rs +341, snake_abs_exit_conv Rs +328, oracle Rs +323, snake_viper_wild Rs +252, snake_abs_conv Rs +236, snake_abs Rs +233, random_hold Rs +193, snake_viper_tick Rs +141, snake_anaconda Rs +91, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -24, snake_nonews Rs -326, snake Rs -347, gold Rs -641

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.