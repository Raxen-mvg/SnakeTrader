# Paper trading report

Updated 2026-11-17 10:18 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,612 | +10.81% | 0 | - | 236 |
| benchmark | 221,565 | +10.78% | 0 | - | 237 |
| snake_abs_exit | 216,153 | +8.08% | 2 | 50% | 345 |
| snake_abs_exit_conv | 214,661 | +7.33% | 2 | 50% | 345 |
| intraweek | 213,343 | +6.67% | 35 | 54% | 3,851 |
| oracle | 212,519 | +6.26% | 0 | - | 233 |
| intramonth | 211,722 | +5.86% | 0 | - | 235 |
| snake_abs | 210,849 | +5.42% | 1 | 100% | 255 |
| snake_abs_conv | 210,702 | +5.35% | 1 | 100% | 255 |
| random_hold | 208,085 | +4.04% | 10 | 70% | 733 |
| snake_viper_wild | 207,143 | +3.57% | 14 | 50% | 2,496 |
| snake_anaconda | 206,208 | +3.10% | 3 | 33% | 374 |
| snake_viper_tick | 203,601 | +1.80% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,219 | +1.11% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,382 | -9.31% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,282 (-4.36%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,077 | +0.98% |
| snake_abs_exit | +1,744 | +0.81% |
| benchmark | +1,484 | +0.67% |
| snake_abs_exit_conv | +1,443 | +0.68% |
| benchmark_smallcap | +1,390 | +0.69% |
| snake_anaconda | +1,105 | +0.54% |
| snake_viper_wild | +999 | +0.48% |
| snake_viper_tick | +982 | +0.48% |
| snake_abs | +716 | +0.34% |
| snake_abs_conv | +712 | +0.34% |
| oracle | +496 | +0.23% |
| gold | +427 | +0.24% |
| random_hold | +292 | +0.14% |
| unified | +174 | +0.08% |
| intramonth | +103 | +0.05% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +617, benchmark Rs +616, snake_abs_exit Rs +505, snake_abs_exit_conv Rs +458, intraweek Rs +381, oracle Rs +358, intramonth Rs +335, snake_abs_conv Rs +334, snake_abs Rs +329, snake_viper_wild Rs +265, random_hold Rs +231, snake_anaconda Rs +207, snake_viper_tick Rs +150, benchmark_smallcap Rs +72, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -532

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.