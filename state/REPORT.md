# Paper trading report

Updated 2026-11-18 10:40 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,737 | +10.87% | 0 | - | 236 |
| benchmark | 220,303 | +10.15% | 0 | - | 237 |
| intraweek | 214,499 | +7.25% | 35 | 54% | 3,851 |
| snake_abs_exit | 212,758 | +6.38% | 2 | 50% | 345 |
| intramonth | 211,816 | +5.91% | 0 | - | 235 |
| oracle | 211,744 | +5.87% | 0 | - | 233 |
| snake_abs_exit_conv | 211,052 | +5.53% | 2 | 50% | 345 |
| snake_abs | 207,910 | +3.96% | 1 | 100% | 255 |
| snake_abs_conv | 207,770 | +3.88% | 1 | 100% | 255 |
| random_hold | 207,255 | +3.63% | 10 | 70% | 733 |
| snake_viper_wild | 207,116 | +3.56% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,578 | +1.79% | 15 | 47% | 2,625 |
| snake_anaconda | 202,928 | +1.46% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,786 | -0.11% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,370 | -11.31% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,050 (-4.47%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,176 | +0.55% |
| unified | +298 | +0.14% |
| intramonth | +273 | +0.13% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs_exit | -384 | -0.18% |
| snake_abs_exit_conv | -521 | -0.25% |
| snake_abs | -649 | -0.31% |
| snake_abs_conv | -650 | -0.31% |
| oracle | -742 | -0.35% |
| benchmark_smallcap | -785 | -0.39% |
| snake_anaconda | -1,127 | -0.55% |
| random_hold | -1,178 | -0.56% |
| benchmark | -1,300 | -0.59% |
| snake_viper_tick | -2,258 | -1.10% |
| snake_viper_wild | -2,299 | -1.10% |
| gold | -3,354 | -1.86% |

Average per day so far: unified Rs +604, benchmark Rs +564, intraweek Rs +403, snake_abs_exit Rs +387, snake_abs_exit_conv Rs +335, intramonth Rs +328, oracle Rs +326, snake_viper_wild Rs +254, snake_abs_conv Rs +235, snake_abs Rs +233, random_hold Rs +202, snake_viper_tick Rs +143, snake_anaconda Rs +94, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -7, snake_nonews Rs -326, snake Rs -347, gold Rs -629

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.