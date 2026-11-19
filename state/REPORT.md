# Paper trading report

Updated 2026-11-19 13:12 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,678 | +11.84% | 0 | - | 236 |
| benchmark | 221,580 | +10.79% | 0 | - | 237 |
| intramonth | 213,288 | +6.64% | 0 | - | 235 |
| snake_abs_exit | 212,372 | +6.19% | 2 | 50% | 345 |
| intraweek | 211,759 | +5.88% | 35 | 54% | 3,851 |
| oracle | 211,638 | +5.82% | 0 | - | 233 |
| snake_abs_exit_conv | 210,510 | +5.25% | 2 | 50% | 345 |
| snake_abs | 208,100 | +4.05% | 1 | 100% | 255 |
| snake_abs_conv | 207,964 | +3.98% | 1 | 100% | 255 |
| random_hold | 207,632 | +3.82% | 10 | 70% | 733 |
| snake_viper_wild | 207,518 | +3.76% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,972 | +1.99% | 15 | 47% | 2,625 |
| snake_anaconda | 202,912 | +1.46% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,560 | +0.28% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,987 | -12.51% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,272 (-4.36%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,285 | +0.58% |
| benchmark_smallcap | +1,233 | +0.62% |
| unified | +1,066 | +0.48% |
| intramonth | +1,015 | +0.48% |
| oracle | +842 | +0.40% |
| random_hold | +699 | +0.34% |
| snake_viper_wild | +479 | +0.23% |
| snake_viper_tick | +469 | +0.23% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -80 | -0.04% |
| snake_abs | -1,337 | -0.64% |
| snake_abs_conv | -1,361 | -0.65% |
| snake_anaconda | -1,489 | -0.73% |
| snake_abs_exit | -1,660 | -0.78% |
| snake_abs_exit_conv | -1,873 | -0.88% |
| gold | -2,334 | -1.32% |

Average per day so far: unified Rs +640, benchmark Rs +583, snake_abs_exit Rs +364, intramonth Rs +359, intraweek Rs +318, oracle Rs +315, snake_abs_exit_conv Rs +309, snake_viper_wild Rs +259, snake_abs_conv Rs +234, snake_abs Rs +231, random_hold Rs +206, snake_viper_tick Rs +153, snake_anaconda Rs +91, nifty_calls Rs +50, benchmark_smallcap Rs +17, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -676

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.