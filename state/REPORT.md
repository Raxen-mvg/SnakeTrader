# Paper trading report

Updated 2026-11-18 11:24 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,426 | +11.71% | 0 | - | 236 |
| benchmark | 220,387 | +10.19% | 0 | - | 237 |
| intraweek | 214,474 | +7.24% | 35 | 54% | 3,851 |
| intramonth | 213,268 | +6.63% | 0 | - | 235 |
| oracle | 213,041 | +6.52% | 0 | - | 233 |
| snake_abs_exit | 212,970 | +6.49% | 2 | 50% | 345 |
| snake_abs_exit_conv | 211,382 | +5.69% | 2 | 50% | 345 |
| snake_abs | 208,262 | +4.13% | 1 | 100% | 255 |
| snake_abs_conv | 208,130 | +4.07% | 1 | 100% | 255 |
| random_hold | 207,734 | +3.87% | 10 | 70% | 733 |
| snake_viper_wild | 206,991 | +3.50% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,456 | +1.73% | 15 | 47% | 2,625 |
| snake_anaconda | 203,398 | +1.70% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,753 | -0.12% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,469 | -11.27% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,933 (-4.03%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,987 | +0.90% |
| intramonth | +1,725 | +0.82% |
| intraweek | +1,151 | +0.54% |
| oracle | +555 | +0.26% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -172 | -0.08% |
| snake_abs_exit_conv | -192 | -0.09% |
| snake_abs_conv | -289 | -0.14% |
| snake_abs | -297 | -0.14% |
| snake_anaconda | -657 | -0.32% |
| random_hold | -698 | -0.34% |
| benchmark_smallcap | -818 | -0.41% |
| benchmark | -1,216 | -0.55% |
| snake_viper_tick | -2,380 | -1.16% |
| snake_viper_wild | -2,424 | -1.16% |
| gold | -3,255 | -1.80% |

Average per day so far: unified Rs +651, benchmark Rs +566, intraweek Rs +402, snake_abs_exit Rs +393, intramonth Rs +369, oracle Rs +362, snake_abs_exit_conv Rs +345, snake_viper_wild Rs +250, snake_abs_conv Rs +246, snake_abs Rs +243, random_hold Rs +215, snake_viper_tick Rs +138, snake_anaconda Rs +110, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -8, snake_nonews Rs -326, snake Rs -347, gold Rs -626

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.