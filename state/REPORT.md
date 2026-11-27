# Paper trading report

Updated 2026-11-27 15:16 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 223,424 | +11.71% | 0 | - | 237 |
| unified | 223,071 | +11.54% | 0 | - | 236 |
| oracle | 211,463 | +5.73% | 0 | - | 233 |
| random_hold | 211,201 | +5.60% | 13 | 69% | 1,037 |
| intramonth | 210,877 | +5.44% | 0 | - | 235 |
| intraweek | 207,695 | +3.85% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 206,437 | +3.22% | 2 | 50% | 345 |
| snake_abs_exit | 204,221 | +2.11% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,053 | +0.53% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,478 | -0.26% | 1 | 100% | 255 |
| snake_abs_conv | 199,289 | -0.35% | 1 | 100% | 255 |
| snake_anaconda | 192,853 | -3.57% | 3 | 33% | 374 |
| snake_viper_wild | 192,567 | -3.72% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,296 | -5.35% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,663 | -14.67% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,712 (-5.64%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +6,040 | +3.01% |
| gold | +4,669 | +2.81% |
| snake_abs_exit | +3,144 | +1.56% |
| random_hold | +2,607 | +1.25% |
| snake_abs | +926 | +0.47% |
| snake_abs_conv | +923 | +0.47% |
| intraweek | +647 | +0.31% |
| snake_anaconda | +557 | +0.29% |
| snake_viper_wild | +362 | +0.19% |
| snake_viper_tick | +355 | +0.19% |
| intramonth | +343 | +0.16% |
| benchmark_smallcap | +213 | +0.11% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| unified | -7 | -0.00% |
| oracle | -773 | -0.36% |
| benchmark | -2,563 | -1.13% |

Average per day so far: benchmark Rs +558, unified Rs +549, oracle Rs +273, random_hold Rs +267, intramonth Rs +259, intraweek Rs +183, snake_abs_exit_conv Rs +165, snake_abs_exit Rs +108, nifty_calls Rs +44, benchmark_smallcap Rs +28, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -13, snake_abs_conv Rs -18, snake_anaconda Rs -193, snake_viper_wild Rs -219, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -345, gold Rs -699

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.