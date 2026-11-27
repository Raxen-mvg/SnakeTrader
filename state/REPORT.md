# Paper trading report

Updated 2026-11-27 12:10 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,441 | +12.22% | 0 | - | 237 |
| unified | 223,377 | +11.69% | 0 | - | 236 |
| oracle | 211,953 | +5.98% | 0 | - | 233 |
| intramonth | 211,046 | +5.52% | 0 | - | 235 |
| random_hold | 210,145 | +5.07% | 13 | 69% | 1,037 |
| intraweek | 207,980 | +3.99% | 40 | 55% | 4,400 |
| snake_abs_exit | 204,995 | +2.50% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,853 | +1.93% | 2 | 50% | 345 |
| benchmark_smallcap | 201,905 | +0.95% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,611 | +0.30% | 1 | 100% | 255 |
| snake_abs_conv | 200,433 | +0.22% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,955 | -3.02% | 3 | 33% | 374 |
| snake_viper_wild | 192,476 | -3.76% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,206 | -5.40% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,183 | -15.41% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,813 (-5.59%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +3,918 | +1.95% |
| snake_abs_exit_conv | +3,456 | +1.72% |
| gold | +3,189 | +1.92% |
| snake_abs_conv | +2,067 | +1.04% |
| snake_abs | +2,058 | +1.04% |
| snake_anaconda | +1,658 | +0.86% |
| random_hold | +1,550 | +0.74% |
| benchmark_smallcap | +1,065 | +0.53% |
| intraweek | +931 | +0.45% |
| intramonth | +512 | +0.24% |
| unified | +299 | +0.13% |
| snake_viper_wild | +270 | +0.14% |
| snake_viper_tick | +265 | +0.14% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -282 | -0.13% |
| benchmark | -1,545 | -0.68% |

Average per day so far: benchmark Rs +582, unified Rs +557, oracle Rs +285, intramonth Rs +263, random_hold Rs +242, intraweek Rs +190, snake_abs_exit Rs +128, snake_abs_exit_conv Rs +99, benchmark_smallcap Rs +50, nifty_calls Rs +44, snake_abs Rs +15, snake_abs_conv Rs +11, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -163, snake_viper_wild Rs -221, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -348, gold Rs -734

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.