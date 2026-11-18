# Paper trading report

Updated 2026-11-18 11:31 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,313 | +11.66% | 0 | - | 236 |
| benchmark | 220,364 | +10.18% | 0 | - | 237 |
| intraweek | 214,205 | +7.10% | 35 | 54% | 3,851 |
| intramonth | 213,075 | +6.54% | 0 | - | 235 |
| oracle | 212,950 | +6.47% | 0 | - | 233 |
| snake_abs_exit | 212,823 | +6.41% | 2 | 50% | 345 |
| snake_abs_exit_conv | 211,245 | +5.62% | 2 | 50% | 345 |
| snake_abs | 208,203 | +4.10% | 1 | 100% | 255 |
| snake_abs_conv | 208,068 | +4.03% | 1 | 100% | 255 |
| random_hold | 207,625 | +3.81% | 10 | 70% | 733 |
| snake_viper_wild | 206,881 | +3.44% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,348 | +1.67% | 15 | 47% | 2,625 |
| snake_anaconda | 203,276 | +1.64% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,574 | -0.21% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,420 | -11.29% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,795 (-4.10%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,874 | +0.85% |
| intramonth | +1,533 | +0.72% |
| intraweek | +883 | +0.41% |
| oracle | +464 | +0.22% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -319 | -0.15% |
| snake_abs_exit_conv | -328 | -0.15% |
| snake_abs_conv | -352 | -0.17% |
| snake_abs | -355 | -0.17% |
| snake_anaconda | -779 | -0.38% |
| random_hold | -808 | -0.39% |
| benchmark_smallcap | -998 | -0.50% |
| benchmark | -1,239 | -0.56% |
| snake_viper_tick | -2,488 | -1.21% |
| snake_viper_wild | -2,534 | -1.21% |
| gold | -3,304 | -1.83% |

Average per day so far: unified Rs +648, benchmark Rs +566, intraweek Rs +395, snake_abs_exit Rs +389, intramonth Rs +363, oracle Rs +360, snake_abs_exit_conv Rs +341, snake_viper_wild Rs +246, snake_abs_conv Rs +244, snake_abs Rs +241, random_hold Rs +212, snake_viper_tick Rs +134, snake_anaconda Rs +106, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -13, snake_nonews Rs -326, snake Rs -347, gold Rs -627

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.