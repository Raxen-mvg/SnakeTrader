# Paper trading report

Updated 2026-11-27 15:22 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 223,432 | +11.72% | 0 | - | 237 |
| unified | 223,315 | +11.66% | 0 | - | 236 |
| oracle | 211,674 | +5.84% | 0 | - | 233 |
| random_hold | 211,478 | +5.74% | 13 | 69% | 1,037 |
| intramonth | 211,050 | +5.53% | 0 | - | 235 |
| intraweek | 207,863 | +3.93% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 206,276 | +3.14% | 2 | 50% | 345 |
| snake_abs_exit | 204,047 | +2.02% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,569 | +0.78% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,520 | -0.24% | 1 | 100% | 255 |
| snake_abs_conv | 199,329 | -0.34% | 1 | 100% | 255 |
| snake_anaconda | 192,708 | -3.65% | 3 | 33% | 374 |
| snake_viper_wild | 192,394 | -3.80% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,127 | -5.44% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,778 | -14.61% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,938 (-5.53%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +5,879 | +2.93% |
| gold | +4,784 | +2.88% |
| snake_abs_exit | +2,969 | +1.48% |
| random_hold | +2,883 | +1.38% |
| snake_abs | +968 | +0.49% |
| snake_abs_conv | +962 | +0.48% |
| intraweek | +814 | +0.39% |
| benchmark_smallcap | +729 | +0.36% |
| intramonth | +516 | +0.24% |
| snake_anaconda | +411 | +0.21% |
| unified | +237 | +0.11% |
| snake_viper_wild | +189 | +0.10% |
| snake_viper_tick | +185 | +0.10% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -561 | -0.26% |
| benchmark | -2,555 | -1.13% |

Average per day so far: benchmark Rs +558, unified Rs +555, oracle Rs +278, random_hold Rs +273, intramonth Rs +263, intraweek Rs +187, snake_abs_exit_conv Rs +161, snake_abs_exit Rs +104, nifty_calls Rs +44, benchmark_smallcap Rs +41, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -12, snake_abs_conv Rs -17, snake_anaconda Rs -197, snake_viper_wild Rs -224, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -351, gold Rs -696

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.