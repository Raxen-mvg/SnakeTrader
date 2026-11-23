# Paper trading report

Updated 2026-11-23 10:31 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,712 | +12.36% | 0 | - | 236 |
| benchmark | 223,516 | +11.76% | 0 | - | 237 |
| intraweek | 213,094 | +6.55% | 40 | 55% | 4,400 |
| intramonth | 212,781 | +6.39% | 0 | - | 235 |
| oracle | 211,325 | +5.66% | 0 | - | 233 |
| random_hold | 209,949 | +4.97% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,861 | +3.93% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,854 | +3.43% | 2 | 50% | 345 |
| snake_abs | 205,082 | +2.54% | 1 | 100% | 255 |
| snake_abs_conv | 204,934 | +2.47% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,937 | +0.47% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,753 | -0.12% | 0 | - | 237 |
| snake_anaconda | 198,701 | -0.65% | 3 | 33% | 374 |
| snake_viper_tick | 197,509 | -1.25% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,446 | -15.28% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,636 (-4.68%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,397 | +0.83% |
| snake_abs_exit_conv | +237 | +0.12% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -701 | -0.34% |
| random_hold | -811 | -0.39% |
| snake_abs | -837 | -0.41% |
| snake_abs_conv | -849 | -0.41% |
| oracle | -1,154 | -0.54% |
| benchmark_smallcap | -1,155 | -0.57% |
| snake_anaconda | -1,204 | -0.60% |
| unified | -1,470 | -0.65% |
| benchmark | -1,622 | -0.72% |
| snake_viper_tick | -1,862 | -0.93% |
| snake_viper_wild | -1,892 | -0.93% |
| intramonth | -2,223 | -1.03% |
| intraweek | -2,618 | -1.21% |

Average per day so far: unified Rs +634, benchmark Rs +603, intraweek Rs +336, intramonth Rs +328, oracle Rs +290, random_hold Rs +255, snake_abs_exit Rs +218, snake_abs_exit_conv Rs +190, snake_abs Rs +137, snake_abs_conv Rs +137, nifty_calls Rs +47, snake_viper_wild Rs +30, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -7, snake_anaconda Rs -38, snake_viper_tick Rs -89, snake_nonews Rs -300, snake Rs -320, gold Rs -783

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.