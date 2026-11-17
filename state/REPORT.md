# Paper trading report

Updated 2026-11-17 10:41 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,944 | +10.97% | 0 | - | 236 |
| benchmark | 221,420 | +10.71% | 0 | - | 237 |
| snake_abs_exit | 215,353 | +7.68% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,532 | +6.77% | 2 | 50% | 345 |
| intraweek | 213,520 | +6.76% | 35 | 54% | 3,851 |
| oracle | 212,433 | +6.22% | 0 | - | 233 |
| intramonth | 211,857 | +5.93% | 0 | - | 235 |
| snake_abs | 210,072 | +5.04% | 1 | 100% | 255 |
| snake_abs_conv | 209,923 | +4.96% | 1 | 100% | 255 |
| random_hold | 208,253 | +4.13% | 10 | 70% | 733 |
| snake_viper_wild | 207,203 | +3.60% | 14 | 50% | 2,496 |
| snake_anaconda | 205,575 | +2.79% | 3 | 33% | 374 |
| snake_viper_tick | 203,660 | +1.83% | 13 | 46% | 2,299 |
| benchmark_smallcap | 201,950 | +0.97% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,464 | -9.27% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,382 (-4.31%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,254 | +1.07% |
| benchmark | +1,339 | +0.61% |
| benchmark_smallcap | +1,121 | +0.56% |
| snake_viper_wild | +1,058 | +0.51% |
| snake_viper_tick | +1,040 | +0.51% |
| snake_abs_exit | +944 | +0.44% |
| gold | +510 | +0.28% |
| unified | +507 | +0.23% |
| snake_anaconda | +472 | +0.23% |
| random_hold | +460 | +0.22% |
| oracle | +410 | +0.19% |
| snake_abs_exit_conv | +315 | +0.15% |
| intramonth | +238 | +0.11% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs | -61 | -0.03% |
| snake_abs_conv | -67 | -0.03% |

Average per day so far: unified Rs +627, benchmark Rs +612, snake_abs_exit Rs +480, snake_abs_exit_conv Rs +423, intraweek Rs +386, oracle Rs +355, intramonth Rs +339, snake_abs_conv Rs +310, snake_abs Rs +305, snake_viper_wild Rs +267, random_hold Rs +236, snake_anaconda Rs +186, snake_viper_tick Rs +152, benchmark_smallcap Rs +63, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -530

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.