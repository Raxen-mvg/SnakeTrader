# Paper trading report

Updated 2026-11-04 12:28 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,182 | +7.09% | 0 | - | 236 |
| snake_abs_exit_conv | 211,512 | +5.76% | 1 | 100% | 255 |
| snake_abs_exit | 211,348 | +5.67% | 1 | 100% | 260 |
| intraweek | 208,768 | +4.38% | 25 | 48% | 2,757 |
| snake_abs | 208,411 | +4.21% | 1 | 100% | 255 |
| snake_abs_conv | 208,256 | +4.13% | 1 | 100% | 255 |
| benchmark | 207,719 | +3.86% | 0 | - | 237 |
| snake_viper_wild | 207,262 | +3.63% | 3 | 33% | 702 |
| intramonth | 206,368 | +3.18% | 0 | - | 235 |
| snake_viper_tick | 203,653 | +1.83% | 2 | 0% | 532 |
| random_hold | 203,010 | +1.50% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,313 | +0.66% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,846 | -0.08% | 3 | 33% | 361 |
| benchmark_smallcap | 194,832 | -2.58% | 0 | - | 237 |
| gold | 190,818 | -4.59% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,339 (-5.33%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +7,333 | +3.59% |
| snake_abs_exit_conv | +7,173 | +3.51% |
| snake_abs_conv | +7,115 | +3.54% |
| snake_abs | +7,101 | +3.53% |
| snake_anaconda | +6,022 | +3.11% |
| gold | +5,540 | +2.99% |
| intraweek | +3,683 | +1.80% |
| random_hold | +2,542 | +1.27% |
| intramonth | +2,397 | +1.18% |
| unified | +2,181 | +1.03% |
| benchmark_smallcap | +1,894 | +0.98% |
| oracle | +1,324 | +0.66% |
| benchmark | +1,017 | +0.49% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,514 | -1.70% |
| snake_viper_wild | -3,630 | -1.72% |

Average per day so far: unified Rs +525, snake_abs_exit_conv Rs +480, snake_abs_exit Rs +473, snake_viper_wild Rs +382, snake_abs_conv Rs +344, snake_abs Rs +336, intraweek Rs +325, benchmark Rs +286, intramonth Rs +236, snake_viper_tick Rs +228, random_hold Rs +111, nifty_calls Rs +68, oracle Rs +49, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -7, benchmark_smallcap Rs -225, gold Rs -340, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.