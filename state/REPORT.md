# Paper trading report

Updated 2026-11-23 09:24 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,747 | +12.87% | 0 | - | 236 |
| benchmark | 224,908 | +12.45% | 0 | - | 237 |
| intraweek | 215,668 | +7.83% | 35 | 54% | 3,851 |
| intramonth | 214,153 | +7.08% | 0 | - | 235 |
| oracle | 212,205 | +6.10% | 0 | - | 233 |
| random_hold | 211,679 | +5.84% | 11 | 73% | 979 |
| snake_abs_exit | 208,455 | +4.23% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,998 | +3.50% | 2 | 50% | 345 |
| snake_abs | 205,513 | +2.76% | 1 | 100% | 255 |
| snake_abs_conv | 205,374 | +2.69% | 1 | 100% | 255 |
| snake_viper_wild | 203,741 | +1.87% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,336 | +0.17% | 0 | - | 237 |
| snake_viper_tick | 200,265 | +0.13% | 15 | 47% | 2,625 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,645 | -0.18% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,183 | -15.41% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,809 (-4.10%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,134 | +0.68% |
| random_hold | +920 | +0.44% |
| snake_viper_wild | +912 | +0.45% |
| snake_viper_tick | +893 | +0.45% |
| snake_abs_exit_conv | +381 | +0.18% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -44 | -0.02% |
| snake_abs_exit | -107 | -0.05% |
| benchmark | -230 | -0.10% |
| snake_anaconda | -260 | -0.13% |
| oracle | -273 | -0.13% |
| snake_abs | -406 | -0.20% |
| snake_abs_conv | -409 | -0.20% |
| unified | -435 | -0.19% |
| benchmark_smallcap | -572 | -0.28% |
| intramonth | -851 | -0.40% |

Average per day so far: unified Rs +660, benchmark Rs +639, intraweek Rs +402, intramonth Rs +363, oracle Rs +313, random_hold Rs +299, snake_abs_exit Rs +235, snake_abs_exit_conv Rs +194, snake_abs_conv Rs +149, snake_abs Rs +149, snake_viper_wild Rs +121, nifty_calls Rs +47, benchmark_smallcap Rs +10, snake_viper_tick Rs +9, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_anaconda Rs -10, snake_nonews Rs -300, snake Rs -320, gold Rs -790

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.