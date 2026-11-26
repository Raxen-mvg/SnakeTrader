# Paper trading report

Updated 2026-11-26 10:16 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,467 | +12.73% | 0 | - | 237 |
| unified | 224,013 | +12.01% | 0 | - | 236 |
| oracle | 213,498 | +6.75% | 0 | - | 233 |
| intramonth | 211,432 | +5.72% | 0 | - | 235 |
| random_hold | 210,159 | +5.08% | 13 | 69% | 1,037 |
| intraweek | 208,409 | +4.20% | 40 | 55% | 4,400 |
| snake_abs_exit | 203,487 | +1.74% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,807 | +1.40% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,788 | +0.39% | 1 | 100% | 255 |
| benchmark_smallcap | 200,784 | +0.39% | 0 | - | 237 |
| snake_abs_conv | 200,613 | +0.31% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,704 | -2.65% | 3 | 33% | 374 |
| snake_viper_wild | 193,727 | -3.14% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,431 | -4.78% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,983 | -16.01% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,381 (-5.31%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +3,387 | +2.06% |
| benchmark_smallcap | +1,973 | +0.99% |
| intraweek | +1,666 | +0.81% |
| snake_abs_exit | +1,231 | +0.61% |
| snake_abs_exit_conv | +831 | +0.41% |
| random_hold | +666 | +0.32% |
| snake_abs_conv | +641 | +0.32% |
| snake_abs | +638 | +0.32% |
| benchmark | +444 | +0.20% |
| snake_anaconda | +151 | +0.08% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| unified | -87 | -0.04% |
| intramonth | -261 | -0.12% |
| oracle | -297 | -0.14% |
| snake_viper_tick | -3,746 | -1.93% |
| snake_viper_wild | -3,816 | -1.93% |

Average per day so far: benchmark Rs +621, unified Rs +586, oracle Rs +329, intramonth Rs +279, random_hold Rs +248, intraweek Rs +205, snake_abs_exit Rs +92, snake_abs_exit_conv Rs +74, nifty_calls Rs +45, benchmark_smallcap Rs +21, snake_abs Rs +20, snake_abs_conv Rs +16, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -147, snake_viper_wild Rs -190, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -319, gold Rs -781

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.