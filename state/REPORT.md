# Paper trading report

Updated 2026-11-13 09:52 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,220 | +10.61% | 0 | - | 236 |
| benchmark | 219,920 | +9.96% | 0 | - | 237 |
| snake_abs_exit_conv | 217,206 | +8.60% | 2 | 50% | 345 |
| snake_abs_exit | 216,692 | +8.35% | 2 | 50% | 345 |
| intraweek | 215,206 | +7.60% | 30 | 53% | 3,302 |
| oracle | 214,159 | +7.08% | 0 | - | 233 |
| snake_abs | 213,802 | +6.90% | 1 | 100% | 255 |
| snake_abs_conv | 213,631 | +6.82% | 1 | 100% | 255 |
| intramonth | 211,957 | +5.98% | 0 | - | 235 |
| random_hold | 207,742 | +3.87% | 10 | 70% | 733 |
| snake_viper_wild | 205,459 | +2.73% | 14 | 50% | 2,496 |
| snake_anaconda | 203,861 | +1.93% | 3 | 33% | 374 |
| benchmark_smallcap | 203,419 | +1.71% | 0 | - | 237 |
| snake_viper_tick | 201,946 | +0.97% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,209 | -7.89% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,267 (-3.87%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| oracle | +1,044 | +0.49% |
| intraweek | +548 | +0.26% |
| unified | +523 | +0.24% |
| intramonth | +364 | +0.17% |
| benchmark_smallcap | +213 | +0.10% |
| snake_viper_wild | +166 | +0.08% |
| snake_viper_tick | +164 | +0.08% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| random_hold | -312 | -0.15% |
| benchmark | -627 | -0.28% |
| snake_abs_exit | -750 | -0.34% |
| gold | -1,101 | -0.59% |
| snake_abs_exit_conv | -1,468 | -0.67% |
| snake_abs_conv | -1,904 | -0.88% |
| snake_abs | -1,910 | -0.89% |
| snake_anaconda | -2,067 | -1.00% |

Average per day so far: unified Rs +643, benchmark Rs +604, snake_abs_exit_conv Rs +574, snake_abs_exit Rs +556, intraweek Rs +461, snake_abs_conv Rs +454, snake_abs Rs +445, oracle Rs +429, intramonth Rs +362, random_hold Rs +235, snake_viper_wild Rs +218, snake_anaconda Rs +138, benchmark_smallcap Rs +118, snake_viper_tick Rs +88, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -479

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.