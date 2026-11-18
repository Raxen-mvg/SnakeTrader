# Paper trading report

Updated 2026-11-18 12:37 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,465 | +11.23% | 0 | - | 236 |
| benchmark | 219,920 | +9.96% | 0 | - | 237 |
| intraweek | 213,324 | +6.66% | 35 | 54% | 3,851 |
| snake_abs_exit | 212,739 | +6.37% | 2 | 50% | 345 |
| intramonth | 212,523 | +6.26% | 0 | - | 235 |
| oracle | 211,832 | +5.92% | 0 | - | 233 |
| snake_abs_exit_conv | 210,940 | +5.47% | 2 | 50% | 345 |
| snake_abs | 207,989 | +3.99% | 1 | 100% | 255 |
| snake_abs_conv | 207,850 | +3.92% | 1 | 100% | 255 |
| snake_viper_wild | 207,279 | +3.64% | 16 | 50% | 2,827 |
| random_hold | 207,017 | +3.51% | 10 | 70% | 733 |
| snake_viper_tick | 203,738 | +1.87% | 15 | 47% | 2,625 |
| snake_anaconda | 202,909 | +1.45% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,293 | -0.35% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 176,910 | -11.54% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,106 (-4.45%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,027 | +0.46% |
| intramonth | +980 | +0.46% |
| intraweek | +1 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs_exit | -403 | -0.19% |
| snake_abs | -570 | -0.27% |
| snake_abs_conv | -570 | -0.27% |
| snake_abs_exit_conv | -634 | -0.30% |
| oracle | -655 | -0.31% |
| snake_anaconda | -1,146 | -0.56% |
| benchmark_smallcap | -1,278 | -0.64% |
| random_hold | -1,416 | -0.68% |
| benchmark | -1,683 | -0.76% |
| snake_viper_tick | -2,098 | -1.02% |
| snake_viper_wild | -2,136 | -1.02% |
| gold | -3,814 | -2.11% |

Average per day so far: unified Rs +624, benchmark Rs +553, snake_abs_exit Rs +386, intraweek Rs +370, intramonth Rs +348, snake_abs_exit_conv Rs +332, oracle Rs +329, snake_viper_wild Rs +260, snake_abs_conv Rs +238, snake_abs Rs +235, random_hold Rs +195, snake_viper_tick Rs +150, snake_anaconda Rs +94, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -22, snake_nonews Rs -326, snake Rs -347, gold Rs -641

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.