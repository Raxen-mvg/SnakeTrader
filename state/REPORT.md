# Paper trading report

Updated 2026-11-18 10:43 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,027 | +11.01% | 0 | - | 236 |
| benchmark | 220,219 | +10.11% | 0 | - | 237 |
| intraweek | 214,441 | +7.22% | 35 | 54% | 3,851 |
| snake_abs_exit | 212,812 | +6.41% | 2 | 50% | 345 |
| intramonth | 212,083 | +6.04% | 0 | - | 235 |
| oracle | 211,786 | +5.89% | 0 | - | 233 |
| snake_abs_exit_conv | 211,156 | +5.58% | 2 | 50% | 345 |
| snake_abs | 207,996 | +4.00% | 1 | 100% | 255 |
| snake_abs_conv | 207,857 | +3.93% | 1 | 100% | 255 |
| random_hold | 207,160 | +3.58% | 10 | 70% | 733 |
| snake_viper_wild | 207,126 | +3.56% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,588 | +1.79% | 15 | 47% | 2,625 |
| snake_anaconda | 203,015 | +1.51% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,663 | -0.17% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,370 | -11.31% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,139 (-4.43%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,119 | +0.52% |
| unified | +588 | +0.27% |
| intramonth | +541 | +0.26% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs_exit | -330 | -0.15% |
| snake_abs_exit_conv | -418 | -0.20% |
| snake_abs | -563 | -0.27% |
| snake_abs_conv | -563 | -0.27% |
| oracle | -700 | -0.33% |
| benchmark_smallcap | -908 | -0.45% |
| snake_anaconda | -1,040 | -0.51% |
| random_hold | -1,272 | -0.61% |
| benchmark | -1,385 | -0.62% |
| snake_viper_tick | -2,249 | -1.09% |
| snake_viper_wild | -2,289 | -1.09% |
| gold | -3,354 | -1.86% |

Average per day so far: unified Rs +612, benchmark Rs +562, intraweek Rs +401, snake_abs_exit Rs +388, snake_abs_exit_conv Rs +338, intramonth Rs +336, oracle Rs +327, snake_viper_wild Rs +254, snake_abs_conv Rs +238, snake_abs Rs +235, random_hold Rs +199, snake_viper_tick Rs +144, snake_anaconda Rs +97, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -11, snake_nonews Rs -326, snake Rs -347, gold Rs -629

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.