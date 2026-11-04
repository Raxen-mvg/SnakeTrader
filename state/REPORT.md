# Paper trading report

Updated 2026-11-04 14:01 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,304 | +7.15% | 0 | - | 236 |
| snake_abs_exit_conv | 213,394 | +6.70% | 1 | 100% | 255 |
| snake_abs_exit | 213,261 | +6.63% | 1 | 100% | 260 |
| snake_abs | 210,287 | +5.14% | 1 | 100% | 255 |
| snake_abs_conv | 210,135 | +5.07% | 1 | 100% | 255 |
| intraweek | 209,502 | +4.75% | 25 | 48% | 2,757 |
| benchmark | 208,445 | +4.22% | 0 | - | 237 |
| snake_viper_wild | 207,416 | +3.71% | 3 | 33% | 702 |
| intramonth | 206,524 | +3.26% | 0 | - | 235 |
| snake_viper_tick | 203,796 | +1.90% | 2 | 0% | 532 |
| random_hold | 202,942 | +1.47% | 8 | 62% | 649 |
| snake_anaconda | 201,896 | +0.95% | 3 | 33% | 361 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,181 | +0.59% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,031 | -1.98% | 0 | - | 237 |
| gold | 191,081 | -4.46% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,530 (-5.23%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +9,247 | +4.53% |
| snake_abs_exit_conv | +9,056 | +4.43% |
| snake_abs_conv | +8,994 | +4.47% |
| snake_abs | +8,978 | +4.46% |
| snake_anaconda | +8,072 | +4.17% |
| gold | +5,803 | +3.13% |
| intraweek | +4,417 | +2.15% |
| benchmark_smallcap | +3,094 | +1.60% |
| intramonth | +2,553 | +1.25% |
| random_hold | +2,474 | +1.23% |
| unified | +2,303 | +1.09% |
| benchmark | +1,744 | +0.84% |
| oracle | +1,192 | +0.60% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,371 | -1.63% |
| snake_viper_wild | -3,477 | -1.65% |

Average per day so far: snake_abs_exit_conv Rs +558, snake_abs_exit Rs +553, unified Rs +530, snake_abs_conv Rs +422, snake_abs Rs +411, snake_viper_wild Rs +390, intraweek Rs +352, benchmark Rs +313, intramonth Rs +242, snake_viper_tick Rs +237, random_hold Rs +109, snake_anaconda Rs +86, nifty_calls Rs +68, oracle Rs +44, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -173, gold Rs -330, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.