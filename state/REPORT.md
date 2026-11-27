# Paper trading report

Updated 2026-11-27 11:28 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,090 | +12.04% | 0 | - | 237 |
| unified | 222,423 | +11.21% | 0 | - | 236 |
| oracle | 211,882 | +5.94% | 0 | - | 233 |
| intramonth | 210,495 | +5.25% | 0 | - | 235 |
| random_hold | 210,317 | +5.16% | 13 | 69% | 1,037 |
| intraweek | 207,717 | +3.86% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,089 | +2.54% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,927 | +1.96% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,636 | +0.82% | 0 | - | 237 |
| snake_abs | 200,822 | +0.41% | 1 | 100% | 255 |
| snake_abs_conv | 200,644 | +0.32% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,277 | -2.86% | 3 | 33% | 374 |
| snake_viper_wild | 193,436 | -3.28% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,146 | -4.93% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,019 | -15.49% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,521 (-5.74%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,011 | +2.00% |
| snake_abs_exit_conv | +3,530 | +1.76% |
| gold | +3,025 | +1.82% |
| snake_abs_conv | +2,278 | +1.15% |
| snake_abs | +2,270 | +1.14% |
| snake_anaconda | +1,980 | +1.03% |
| random_hold | +1,723 | +0.83% |
| snake_viper_wild | +1,230 | +0.64% |
| snake_viper_tick | +1,205 | +0.64% |
| benchmark_smallcap | +796 | +0.40% |
| intraweek | +668 | +0.32% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intramonth | -38 | -0.02% |
| oracle | -353 | -0.17% |
| unified | -655 | -0.29% |
| benchmark | -1,897 | -0.84% |

Average per day so far: benchmark Rs +574, unified Rs +534, oracle Rs +283, intramonth Rs +250, random_hold Rs +246, intraweek Rs +184, snake_abs_exit Rs +130, snake_abs_exit_conv Rs +101, nifty_calls Rs +44, benchmark_smallcap Rs +43, snake_abs Rs +21, snake_abs_conv Rs +17, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -155, snake_viper_wild Rs -193, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -318, gold Rs -738

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.