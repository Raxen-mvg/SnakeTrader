# Paper trading report

Updated 2026-11-17 10:25 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,763 | +10.88% | 0 | - | 236 |
| benchmark | 221,527 | +10.76% | 0 | - | 237 |
| snake_abs_exit | 215,664 | +7.83% | 2 | 50% | 345 |
| snake_abs_exit_conv | 214,313 | +7.16% | 2 | 50% | 345 |
| intraweek | 213,248 | +6.62% | 35 | 54% | 3,851 |
| oracle | 212,530 | +6.26% | 0 | - | 233 |
| intramonth | 211,720 | +5.86% | 0 | - | 235 |
| snake_abs | 210,593 | +5.30% | 1 | 100% | 255 |
| snake_abs_conv | 210,445 | +5.22% | 1 | 100% | 255 |
| random_hold | 208,146 | +4.07% | 10 | 70% | 733 |
| snake_viper_wild | 207,023 | +3.51% | 14 | 50% | 2,496 |
| snake_anaconda | 206,006 | +3.00% | 3 | 33% | 374 |
| snake_viper_tick | 203,483 | +1.74% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,163 | +1.08% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,530 | -9.23% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,303 (-4.35%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,983 | +0.94% |
| benchmark | +1,446 | +0.66% |
| benchmark_smallcap | +1,334 | +0.66% |
| snake_abs_exit | +1,255 | +0.58% |
| snake_abs_exit_conv | +1,096 | +0.51% |
| snake_anaconda | +903 | +0.44% |
| snake_viper_wild | +879 | +0.43% |
| snake_viper_tick | +863 | +0.43% |
| gold | +575 | +0.32% |
| oracle | +507 | +0.24% |
| snake_abs | +459 | +0.22% |
| snake_abs_conv | +455 | +0.22% |
| random_hold | +353 | +0.17% |
| unified | +325 | +0.15% |
| intramonth | +101 | +0.05% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +622, benchmark Rs +615, snake_abs_exit Rs +490, snake_abs_exit_conv Rs +447, intraweek Rs +379, oracle Rs +358, intramonth Rs +335, snake_abs_conv Rs +326, snake_abs Rs +321, snake_viper_wild Rs +260, random_hold Rs +233, snake_anaconda Rs +200, snake_viper_tick Rs +145, benchmark_smallcap Rs +70, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -528

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.