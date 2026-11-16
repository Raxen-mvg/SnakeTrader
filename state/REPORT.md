# Paper trading report

Updated 2026-11-16 14:15 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,408 | +10.20% | 0 | - | 236 |
| benchmark | 219,752 | +9.88% | 0 | - | 237 |
| snake_abs_exit | 213,268 | +6.63% | 2 | 50% | 345 |
| snake_abs_exit_conv | 212,075 | +6.04% | 2 | 50% | 345 |
| oracle | 211,054 | +5.53% | 0 | - | 233 |
| intramonth | 210,884 | +5.44% | 0 | - | 235 |
| intraweek | 210,653 | +5.33% | 35 | 54% | 3,851 |
| snake_abs | 209,400 | +4.70% | 1 | 100% | 255 |
| snake_abs_conv | 209,238 | +4.62% | 1 | 100% | 255 |
| random_hold | 207,655 | +3.83% | 10 | 70% | 733 |
| snake_viper_wild | 205,423 | +2.71% | 14 | 50% | 2,496 |
| snake_anaconda | 203,765 | +1.88% | 3 | 33% | 374 |
| snake_viper_tick | 201,910 | +0.95% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,156 | +0.08% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,217 | -9.39% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,103 (-4.95%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,388 | +0.63% |
| intramonth | +827 | +0.39% |
| snake_viper_wild | +666 | +0.33% |
| snake_viper_tick | +655 | +0.33% |
| random_hold | +429 | +0.21% |
| benchmark | +413 | +0.19% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_anaconda | -1,127 | -0.55% |
| oracle | -2,043 | -0.96% |
| benchmark_smallcap | -2,713 | -1.34% |
| gold | -2,778 | -1.51% |
| snake_abs_conv | -3,128 | -1.47% |
| snake_abs | -3,140 | -1.48% |
| snake_abs_exit | -3,717 | -1.71% |
| snake_abs_exit_conv | -4,307 | -1.99% |
| intraweek | -5,492 | -2.54% |

Average per day so far: unified Rs +600, benchmark Rs +581, snake_abs_exit Rs +428, snake_abs_exit_conv Rs +390, oracle Rs +325, intramonth Rs +320, intraweek Rs +313, snake_abs_conv Rs +298, snake_abs Rs +294, random_hold Rs +225, snake_viper_wild Rs +209, snake_anaconda Rs +130, snake_viper_tick Rs +83, nifty_calls Rs +54, benchmark_smallcap Rs +5, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -347, snake Rs -368, gold Rs -552

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.