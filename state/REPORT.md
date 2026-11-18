# Paper trading report

Updated 2026-11-18 13:30 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,956 | +11.48% | 0 | - | 236 |
| benchmark | 219,913 | +9.96% | 0 | - | 237 |
| intramonth | 212,776 | +6.39% | 0 | - | 235 |
| snake_abs_exit | 212,524 | +6.26% | 2 | 50% | 345 |
| oracle | 212,310 | +6.16% | 0 | - | 233 |
| intraweek | 212,307 | +6.15% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 210,815 | +5.41% | 2 | 50% | 345 |
| snake_abs | 207,809 | +3.90% | 1 | 100% | 255 |
| snake_abs_conv | 207,673 | +3.84% | 1 | 100% | 255 |
| random_hold | 207,045 | +3.52% | 10 | 70% | 733 |
| snake_viper_wild | 206,751 | +3.38% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,221 | +1.61% | 15 | 47% | 2,625 |
| snake_anaconda | 202,949 | +1.48% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,170 | -0.41% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,568 | -11.22% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,178 (-4.41%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,518 | +0.69% |
| intramonth | +1,234 | +0.58% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| oracle | -177 | -0.08% |
| snake_abs_exit | -618 | -0.29% |
| snake_abs_conv | -746 | -0.36% |
| snake_abs | -749 | -0.36% |
| snake_abs_exit_conv | -759 | -0.36% |
| intraweek | -1,016 | -0.48% |
| snake_anaconda | -1,106 | -0.54% |
| random_hold | -1,387 | -0.67% |
| benchmark_smallcap | -1,401 | -0.70% |
| benchmark | -1,691 | -0.76% |
| snake_viper_tick | -2,615 | -1.27% |
| snake_viper_wild | -2,664 | -1.27% |
| gold | -3,156 | -1.75% |

Average per day so far: unified Rs +638, benchmark Rs +553, snake_abs_exit Rs +380, intramonth Rs +355, oracle Rs +342, intraweek Rs +342, snake_abs_exit_conv Rs +328, snake_viper_wild Rs +241, snake_abs_conv Rs +233, snake_abs Rs +230, random_hold Rs +196, snake_viper_tick Rs +129, snake_anaconda Rs +95, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -26, snake_nonews Rs -326, snake Rs -347, gold Rs -623

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.