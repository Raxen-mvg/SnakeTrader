# Paper trading report

Updated 2026-11-16 11:28 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,272 | +10.64% | 0 | - | 236 |
| benchmark | 219,959 | +9.98% | 0 | - | 237 |
| oracle | 213,294 | +6.65% | 0 | - | 233 |
| intraweek | 213,036 | +6.52% | 35 | 54% | 3,851 |
| snake_abs_exit | 212,869 | +6.43% | 2 | 50% | 345 |
| intramonth | 211,824 | +5.91% | 0 | - | 235 |
| snake_abs_exit_conv | 211,494 | +5.75% | 2 | 50% | 345 |
| snake_abs | 208,638 | +4.32% | 1 | 100% | 255 |
| snake_abs_conv | 208,470 | +4.24% | 1 | 100% | 255 |
| random_hold | 207,782 | +3.89% | 10 | 70% | 733 |
| snake_viper_wild | 204,809 | +2.40% | 14 | 50% | 2,496 |
| snake_anaconda | 203,050 | +1.52% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,306 | +0.65% | 13 | 46% | 2,299 |
| benchmark_smallcap | 200,784 | +0.39% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,560 | -9.72% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,410 (-4.29%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +2,252 | +1.03% |
| intramonth | +1,767 | +0.84% |
| benchmark | +620 | +0.28% |
| random_hold | +556 | +0.27% |
| oracle | +197 | +0.09% |
| snake_viper_wild | +52 | +0.03% |
| snake_viper_tick | +51 | +0.03% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_anaconda | -1,842 | -0.90% |
| benchmark_smallcap | -2,085 | -1.03% |
| intraweek | -3,109 | -1.44% |
| gold | -3,436 | -1.87% |
| snake_abs_conv | -3,897 | -1.83% |
| snake_abs | -3,902 | -1.84% |
| snake_abs_exit | -4,116 | -1.90% |
| snake_abs_exit_conv | -4,887 | -2.26% |

Average per day so far: unified Rs +626, benchmark Rs +587, snake_abs_exit Rs +415, oracle Rs +391, intraweek Rs +383, snake_abs_exit_conv Rs +371, intramonth Rs +348, snake_abs_conv Rs +273, snake_abs Rs +270, random_hold Rs +229, snake_viper_wild Rs +185, snake_anaconda Rs +105, snake_viper_tick Rs +57, nifty_calls Rs +54, benchmark_smallcap Rs +26, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -347, snake Rs -368, gold Rs -572

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.