# Paper trading report

Updated 2026-11-16 11:25 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,184 | +10.59% | 0 | - | 236 |
| benchmark | 219,959 | +9.98% | 0 | - | 237 |
| oracle | 213,306 | +6.65% | 0 | - | 233 |
| intraweek | 213,016 | +6.51% | 35 | 54% | 3,851 |
| snake_abs_exit | 212,796 | +6.40% | 2 | 50% | 345 |
| intramonth | 211,691 | +5.85% | 0 | - | 235 |
| snake_abs_exit_conv | 211,431 | +5.72% | 2 | 50% | 345 |
| snake_abs | 208,520 | +4.26% | 1 | 100% | 255 |
| snake_abs_conv | 208,353 | +4.18% | 1 | 100% | 255 |
| random_hold | 207,795 | +3.90% | 10 | 70% | 733 |
| snake_viper_wild | 204,809 | +2.40% | 14 | 50% | 2,496 |
| snake_anaconda | 203,015 | +1.51% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,306 | +0.65% | 13 | 46% | 2,299 |
| benchmark_smallcap | 200,762 | +0.38% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,609 | -9.70% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,374 (-4.31%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +2,164 | +0.99% |
| intramonth | +1,634 | +0.78% |
| benchmark | +620 | +0.28% |
| random_hold | +569 | +0.28% |
| oracle | +209 | +0.10% |
| snake_viper_wild | +52 | +0.03% |
| snake_viper_tick | +51 | +0.03% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_anaconda | -1,877 | -0.92% |
| benchmark_smallcap | -2,107 | -1.04% |
| intraweek | -3,129 | -1.45% |
| gold | -3,387 | -1.84% |
| snake_abs_conv | -4,014 | -1.89% |
| snake_abs | -4,021 | -1.89% |
| snake_abs_exit | -4,189 | -1.93% |
| snake_abs_exit_conv | -4,950 | -2.29% |

Average per day so far: unified Rs +623, benchmark Rs +587, snake_abs_exit Rs +413, oracle Rs +391, intraweek Rs +383, snake_abs_exit_conv Rs +369, intramonth Rs +344, snake_abs_conv Rs +269, snake_abs Rs +266, random_hold Rs +229, snake_viper_wild Rs +185, snake_anaconda Rs +104, snake_viper_tick Rs +57, nifty_calls Rs +54, benchmark_smallcap Rs +25, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -347, snake Rs -368, gold Rs -570

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.