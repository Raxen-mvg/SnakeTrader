# Paper trading report

Updated 2026-11-18 14:20 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,348 | +11.17% | 0 | - | 236 |
| benchmark | 220,517 | +10.26% | 0 | - | 237 |
| snake_abs_exit | 214,345 | +7.17% | 2 | 50% | 345 |
| snake_abs_exit_conv | 212,593 | +6.30% | 2 | 50% | 345 |
| intraweek | 212,317 | +6.16% | 35 | 54% | 3,851 |
| oracle | 212,120 | +6.06% | 0 | - | 233 |
| intramonth | 212,042 | +6.02% | 0 | - | 235 |
| snake_abs | 209,373 | +4.69% | 1 | 100% | 255 |
| snake_abs_conv | 209,268 | +4.63% | 1 | 100% | 255 |
| random_hold | 207,063 | +3.53% | 10 | 70% | 733 |
| snake_viper_wild | 206,996 | +3.50% | 16 | 50% | 2,827 |
| snake_anaconda | 204,699 | +2.35% | 3 | 33% | 374 |
| snake_viper_tick | 203,461 | +1.73% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,630 | -0.18% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,140 | -11.43% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,986 (-4.51%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +1,203 | +0.56% |
| snake_abs_exit_conv | +1,019 | +0.48% |
| unified | +909 | +0.41% |
| snake_abs_conv | +848 | +0.41% |
| snake_abs | +815 | +0.39% |
| snake_anaconda | +644 | +0.32% |
| intramonth | +500 | +0.24% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -366 | -0.17% |
| benchmark_smallcap | -942 | -0.47% |
| intraweek | -1,005 | -0.47% |
| benchmark | -1,086 | -0.49% |
| random_hold | -1,370 | -0.66% |
| snake_viper_tick | -2,376 | -1.15% |
| snake_viper_wild | -2,419 | -1.16% |
| gold | -3,584 | -1.98% |

Average per day so far: unified Rs +621, benchmark Rs +570, snake_abs_exit Rs +435, snake_abs_exit_conv Rs +382, intraweek Rs +342, oracle Rs +337, intramonth Rs +334, snake_abs_conv Rs +281, snake_abs Rs +276, snake_viper_wild Rs +250, random_hold Rs +196, snake_anaconda Rs +152, snake_viper_tick Rs +138, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -12, snake_nonews Rs -326, snake Rs -347, gold Rs -635

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.