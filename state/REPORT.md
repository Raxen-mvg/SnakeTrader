# Paper trading report

Updated 2026-11-17 10:12 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,571 | +11.29% | 0 | - | 236 |
| benchmark | 221,297 | +10.65% | 0 | - | 237 |
| snake_abs_exit | 215,981 | +7.99% | 2 | 50% | 345 |
| snake_abs_exit_conv | 214,504 | +7.25% | 2 | 50% | 345 |
| intraweek | 213,045 | +6.52% | 35 | 54% | 3,851 |
| oracle | 212,983 | +6.49% | 0 | - | 233 |
| intramonth | 212,578 | +6.29% | 0 | - | 235 |
| snake_abs | 210,679 | +5.34% | 1 | 100% | 255 |
| snake_abs_conv | 210,534 | +5.27% | 1 | 100% | 255 |
| random_hold | 208,023 | +4.01% | 10 | 70% | 733 |
| snake_viper_wild | 206,977 | +3.49% | 14 | 50% | 2,496 |
| snake_anaconda | 206,045 | +3.02% | 3 | 33% | 374 |
| snake_viper_tick | 203,438 | +1.72% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,253 | +1.13% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,316 | -9.34% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,704 (-4.15%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,779 | +0.84% |
| snake_abs_exit | +1,571 | +0.73% |
| benchmark_smallcap | +1,424 | +0.71% |
| snake_abs_exit_conv | +1,286 | +0.60% |
| benchmark | +1,216 | +0.55% |
| unified | +1,134 | +0.51% |
| oracle | +960 | +0.45% |
| intramonth | +959 | +0.45% |
| snake_anaconda | +942 | +0.46% |
| snake_viper_wild | +832 | +0.40% |
| snake_viper_tick | +818 | +0.40% |
| snake_abs | +546 | +0.26% |
| snake_abs_conv | +544 | +0.26% |
| gold | +362 | +0.20% |
| random_hold | +230 | +0.11% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +645, benchmark Rs +608, snake_abs_exit Rs +499, snake_abs_exit_conv Rs +453, intraweek Rs +373, oracle Rs +371, intramonth Rs +359, snake_abs_conv Rs +329, snake_abs Rs +324, snake_viper_wild Rs +258, random_hold Rs +229, snake_anaconda Rs +201, snake_viper_tick Rs +143, benchmark_smallcap Rs +73, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -534

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.