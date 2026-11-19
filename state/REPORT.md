# Paper trading report

Updated 2026-11-19 12:50 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,849 | +11.93% | 0 | - | 236 |
| benchmark | 221,534 | +10.77% | 0 | - | 237 |
| intramonth | 213,514 | +6.76% | 0 | - | 235 |
| snake_abs_exit | 212,891 | +6.45% | 2 | 50% | 345 |
| intraweek | 211,855 | +5.93% | 35 | 54% | 3,851 |
| oracle | 211,081 | +5.54% | 0 | - | 233 |
| snake_abs_exit_conv | 210,995 | +5.50% | 2 | 50% | 345 |
| snake_abs | 208,495 | +4.25% | 1 | 100% | 255 |
| snake_abs_conv | 208,366 | +4.18% | 1 | 100% | 255 |
| random_hold | 207,800 | +3.90% | 10 | 70% | 733 |
| snake_viper_wild | 207,484 | +3.74% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,939 | +1.97% | 15 | 47% | 2,625 |
| snake_anaconda | 202,875 | +1.44% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,571 | +0.29% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,003 | -12.50% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,278 (-4.36%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,244 | +0.62% |
| intramonth | +1,240 | +0.58% |
| benchmark | +1,239 | +0.56% |
| unified | +1,238 | +0.56% |
| random_hold | +867 | +0.42% |
| snake_viper_wild | +445 | +0.21% |
| snake_viper_tick | +436 | +0.21% |
| oracle | +285 | +0.14% |
| intraweek | +16 | +0.01% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -942 | -0.45% |
| snake_abs_conv | -959 | -0.46% |
| snake_abs_exit | -1,140 | -0.53% |
| snake_abs_exit_conv | -1,388 | -0.65% |
| snake_anaconda | -1,526 | -0.75% |
| gold | -2,318 | -1.31% |

Average per day so far: unified Rs +645, benchmark Rs +582, snake_abs_exit Rs +379, intramonth Rs +365, snake_abs_exit_conv Rs +323, intraweek Rs +320, oracle Rs +299, snake_viper_wild Rs +258, snake_abs_conv Rs +246, snake_abs Rs +243, random_hold Rs +211, snake_viper_tick Rs +152, snake_anaconda Rs +90, nifty_calls Rs +50, benchmark_smallcap Rs +17, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -676

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.