# Paper trading report

Updated 2026-11-05 12:16 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,086 | +9.04% | 0 | - | 236 |
| snake_abs_exit_conv | 213,598 | +6.80% | 1 | 100% | 255 |
| snake_abs_exit | 213,291 | +6.65% | 1 | 100% | 260 |
| benchmark | 212,836 | +6.42% | 0 | - | 237 |
| intraweek | 211,434 | +5.72% | 25 | 48% | 2,757 |
| snake_abs | 210,485 | +5.24% | 1 | 100% | 255 |
| snake_abs_conv | 210,349 | +5.17% | 1 | 100% | 255 |
| intramonth | 209,934 | +4.97% | 0 | - | 235 |
| snake_viper_wild | 206,740 | +3.37% | 3 | 33% | 702 |
| random_hold | 206,626 | +3.31% | 8 | 62% | 649 |
| oracle | 204,086 | +2.04% | 0 | - | 233 |
| snake_viper_tick | 203,184 | +1.59% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,795 | +0.90% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,181 | -0.41% | 0 | - | 237 |
| gold | 194,008 | -3.00% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,087 (-4.96%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,077 | +1.95% |
| unified | +3,647 | +1.70% |
| random_hold | +3,317 | +1.63% |
| intramonth | +2,918 | +1.41% |
| gold | +2,614 | +1.37% |
| benchmark_smallcap | +2,511 | +1.28% |
| oracle | +2,293 | +1.14% |
| intraweek | +1,736 | +0.83% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -1,409 | -0.67% |
| snake_abs_exit_conv | -1,417 | -0.66% |
| snake_abs | -1,418 | -0.67% |
| snake_abs_exit | -1,609 | -0.75% |
| snake_anaconda | -2,025 | -0.99% |
| snake_viper_tick | -2,217 | -1.08% |
| snake_viper_wild | -2,290 | -1.10% |

Average per day so far: unified Rs +646, snake_abs_exit_conv Rs +544, snake_abs_exit Rs +532, benchmark Rs +458, snake_abs_conv Rs +414, intraweek Rs +408, snake_abs Rs +403, intramonth Rs +355, snake_viper_wild Rs +337, random_hold Rs +237, snake_viper_tick Rs +187, oracle Rs +146, snake_anaconda Rs +78, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -34, gold Rs -214, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.