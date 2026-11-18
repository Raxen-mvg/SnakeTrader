# Paper trading report

Updated 2026-11-18 14:27 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,305 | +11.15% | 0 | - | 236 |
| benchmark | 220,418 | +10.21% | 0 | - | 237 |
| snake_abs_exit | 214,637 | +7.32% | 2 | 50% | 345 |
| snake_abs_exit_conv | 212,785 | +6.39% | 2 | 50% | 345 |
| intraweek | 212,140 | +6.07% | 35 | 54% | 3,851 |
| intramonth | 212,022 | +6.01% | 0 | - | 235 |
| oracle | 211,914 | +5.96% | 0 | - | 233 |
| snake_abs | 209,597 | +4.80% | 1 | 100% | 255 |
| snake_abs_conv | 209,494 | +4.75% | 1 | 100% | 255 |
| snake_viper_wild | 207,212 | +3.61% | 16 | 50% | 2,827 |
| random_hold | 206,873 | +3.44% | 10 | 70% | 733 |
| snake_anaconda | 204,889 | +2.44% | 3 | 33% | 374 |
| snake_viper_tick | 203,672 | +1.84% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,663 | -0.17% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,124 | -11.44% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,900 (-4.55%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +1,495 | +0.70% |
| snake_abs_exit_conv | +1,211 | +0.57% |
| snake_abs_conv | +1,074 | +0.52% |
| snake_abs | +1,038 | +0.50% |
| unified | +867 | +0.39% |
| snake_anaconda | +834 | +0.41% |
| intramonth | +480 | +0.23% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -572 | -0.27% |
| benchmark_smallcap | -908 | -0.45% |
| intraweek | -1,183 | -0.55% |
| benchmark | -1,186 | -0.54% |
| random_hold | -1,559 | -0.75% |
| snake_viper_tick | -2,164 | -1.05% |
| snake_viper_wild | -2,203 | -1.05% |
| gold | -3,600 | -1.99% |

Average per day so far: unified Rs +620, benchmark Rs +567, snake_abs_exit Rs +444, snake_abs_exit_conv Rs +387, intraweek Rs +337, intramonth Rs +334, oracle Rs +331, snake_abs_conv Rs +288, snake_abs Rs +282, snake_viper_wild Rs +258, random_hold Rs +191, snake_anaconda Rs +158, snake_viper_tick Rs +147, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -11, snake_nonews Rs -326, snake Rs -347, gold Rs -635

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.