# Paper trading report

Updated 2026-11-23 14:28 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,116 | +12.06% | 0 | - | 236 |
| benchmark | 222,269 | +11.13% | 0 | - | 237 |
| intramonth | 212,206 | +6.10% | 0 | - | 235 |
| intraweek | 212,163 | +6.08% | 40 | 55% | 4,400 |
| oracle | 211,990 | +6.00% | 0 | - | 233 |
| random_hold | 208,760 | +4.38% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,001 | +3.50% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,252 | +3.13% | 2 | 50% | 345 |
| snake_abs | 204,918 | +2.46% | 1 | 100% | 255 |
| snake_abs_conv | 204,741 | +2.37% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,822 | +0.41% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,663 | -0.17% | 0 | - | 237 |
| snake_anaconda | 198,022 | -0.99% | 3 | 33% | 374 |
| snake_viper_tick | 197,397 | -1.30% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,545 | -15.23% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,196 (-4.90%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,496 | +0.89% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -364 | -0.18% |
| oracle | -488 | -0.23% |
| snake_abs | -1,001 | -0.49% |
| snake_abs_conv | -1,042 | -0.51% |
| benchmark_smallcap | -1,244 | -0.62% |
| snake_abs_exit | -1,561 | -0.75% |
| snake_anaconda | -1,883 | -0.94% |
| snake_viper_tick | -1,975 | -0.99% |
| random_hold | -2,000 | -0.95% |
| snake_viper_wild | -2,007 | -0.99% |
| unified | -2,066 | -0.91% |
| intramonth | -2,798 | -1.30% |
| benchmark | -2,869 | -1.27% |
| intraweek | -3,550 | -1.65% |

Average per day so far: unified Rs +618, benchmark Rs +571, intramonth Rs +313, intraweek Rs +312, oracle Rs +307, random_hold Rs +225, snake_abs_exit Rs +194, snake_abs_exit_conv Rs +174, snake_abs Rs +133, snake_abs_conv Rs +132, nifty_calls Rs +47, snake_viper_wild Rs +27, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -10, snake_anaconda Rs -58, snake_viper_tick Rs -93, snake_nonews Rs -300, snake Rs -320, gold Rs -781

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.