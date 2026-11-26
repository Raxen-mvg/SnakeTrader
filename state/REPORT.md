# Paper trading report

Updated 2026-11-26 09:38 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,183 | +12.59% | 0 | - | 237 |
| unified | 224,056 | +12.03% | 0 | - | 236 |
| oracle | 213,827 | +6.91% | 0 | - | 233 |
| intramonth | 211,699 | +5.85% | 0 | - | 235 |
| random_hold | 210,824 | +5.41% | 13 | 69% | 1,037 |
| intraweek | 207,772 | +3.89% | 40 | 55% | 4,400 |
| snake_abs_exit | 203,944 | +1.97% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,215 | +1.61% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,021 | +0.51% | 1 | 100% | 255 |
| snake_abs_conv | 200,849 | +0.42% | 1 | 100% | 255 |
| benchmark_smallcap | 200,672 | +0.34% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,799 | -1.60% | 16 | 50% | 2,827 |
| snake_anaconda | 195,573 | -2.21% | 3 | 33% | 374 |
| snake_viper_tick | 193,448 | -3.28% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,882 | -16.56% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,557 (-5.22%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,285 | +1.39% |
| benchmark_smallcap | +1,861 | +0.94% |
| snake_abs_exit | +1,689 | +0.83% |
| random_hold | +1,331 | +0.64% |
| snake_abs_exit_conv | +1,240 | +0.61% |
| intraweek | +1,029 | +0.50% |
| snake_anaconda | +1,020 | +0.52% |
| snake_abs_conv | +877 | +0.44% |
| snake_abs | +871 | +0.43% |
| benchmark | +161 | +0.07% |
| oracle | +32 | +0.01% |
| intramonth | +6 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| unified | -44 | -0.02% |
| snake_viper_tick | -728 | -0.38% |
| snake_viper_wild | -744 | -0.38% |

Average per day so far: benchmark Rs +614, unified Rs +587, oracle Rs +337, intramonth Rs +285, random_hold Rs +264, intraweek Rs +190, snake_abs_exit Rs +104, snake_abs_exit_conv Rs +85, nifty_calls Rs +45, snake_abs Rs +26, snake_abs_conv Rs +22, benchmark_smallcap Rs +18, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_viper_wild Rs -97, snake_anaconda Rs -123, snake_viper_tick Rs -218, snake_nonews Rs -284, snake Rs -304, gold Rs -808

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.