# Paper trading report

Updated 2026-11-05 10:03 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,128 | +9.56% | 0 | - | 236 |
| snake_abs_exit_conv | 215,901 | +7.95% | 1 | 100% | 255 |
| snake_abs_exit | 215,682 | +7.84% | 1 | 100% | 260 |
| snake_abs | 212,781 | +6.39% | 1 | 100% | 255 |
| snake_abs_conv | 212,628 | +6.31% | 1 | 100% | 255 |
| benchmark | 212,569 | +6.28% | 0 | - | 237 |
| intramonth | 210,913 | +5.46% | 0 | - | 235 |
| intraweek | 210,444 | +5.22% | 25 | 48% | 2,757 |
| random_hold | 206,666 | +3.33% | 8 | 62% | 649 |
| snake_viper_wild | 205,778 | +2.89% | 3 | 33% | 702 |
| oracle | 204,609 | +2.30% | 0 | - | 233 |
| snake_anaconda | 202,965 | +1.48% | 3 | 33% | 374 |
| snake_viper_tick | 202,249 | +1.12% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,686 | -0.16% | 0 | - | 237 |
| gold | 194,912 | -2.54% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,666 (-4.67%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +4,689 | +2.19% |
| intramonth | +3,898 | +1.88% |
| benchmark | +3,810 | +1.82% |
| gold | +3,518 | +1.84% |
| random_hold | +3,357 | +1.65% |
| benchmark_smallcap | +3,015 | +1.53% |
| oracle | +2,817 | +1.40% |
| snake_abs_exit_conv | +886 | +0.41% |
| snake_abs | +878 | +0.41% |
| snake_abs_conv | +869 | +0.41% |
| snake_abs_exit | +782 | +0.36% |
| intraweek | +746 | +0.36% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_anaconda | -856 | -0.42% |
| snake_viper_tick | -3,152 | -1.53% |
| snake_viper_wild | -3,252 | -1.56% |

Average per day so far: unified Rs +683, snake_abs_exit_conv Rs +636, snake_abs_exit Rs +627, snake_abs_conv Rs +505, snake_abs Rs +492, benchmark Rs +449, intramonth Rs +390, intraweek Rs +373, snake_viper_wild Rs +289, random_hold Rs +238, oracle Rs +165, snake_viper_tick Rs +132, snake_anaconda Rs +129, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -13, gold Rs -182, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.