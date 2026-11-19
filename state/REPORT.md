# Paper trading report

Updated 2026-11-19 14:58 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,309 | +12.15% | 0 | - | 236 |
| benchmark | 222,292 | +11.15% | 0 | - | 237 |
| intramonth | 213,739 | +6.87% | 0 | - | 235 |
| snake_abs_exit | 213,668 | +6.83% | 2 | 50% | 345 |
| intraweek | 212,493 | +6.25% | 35 | 54% | 3,851 |
| oracle | 212,107 | +6.05% | 0 | - | 233 |
| snake_abs_exit_conv | 211,374 | +5.69% | 2 | 50% | 345 |
| snake_abs | 208,970 | +4.49% | 1 | 100% | 255 |
| snake_abs_conv | 208,856 | +4.43% | 1 | 100% | 255 |
| random_hold | 208,249 | +4.12% | 10 | 70% | 733 |
| snake_viper_wild | 207,518 | +3.76% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,972 | +1.99% | 15 | 47% | 2,625 |
| snake_anaconda | 203,841 | +1.92% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,412 | +0.71% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,707 | -12.65% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,809 (-4.10%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,085 | +1.05% |
| benchmark | +1,997 | +0.91% |
| unified | +1,698 | +0.76% |
| intramonth | +1,465 | +0.69% |
| random_hold | +1,317 | +0.64% |
| oracle | +1,311 | +0.62% |
| intraweek | +654 | +0.31% |
| snake_viper_wild | +479 | +0.23% |
| snake_viper_tick | +469 | +0.23% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs_exit | -364 | -0.17% |
| snake_abs | -467 | -0.22% |
| snake_abs_conv | -469 | -0.22% |
| snake_anaconda | -560 | -0.27% |
| snake_abs_exit_conv | -1,010 | -0.47% |
| gold | -2,614 | -1.47% |

Average per day so far: unified Rs +657, benchmark Rs +602, snake_abs_exit Rs +402, intramonth Rs +371, intraweek Rs +338, snake_abs_exit_conv Rs +335, oracle Rs +327, snake_abs_conv Rs +260, snake_viper_wild Rs +259, snake_abs Rs +256, random_hold Rs +223, snake_viper_tick Rs +153, snake_anaconda Rs +120, nifty_calls Rs +50, benchmark_smallcap Rs +43, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -684

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.