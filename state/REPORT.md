# Paper trading report

Updated 2026-11-23 12:40 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,077 | +12.04% | 0 | - | 236 |
| benchmark | 222,904 | +11.45% | 0 | - | 237 |
| intraweek | 212,243 | +6.12% | 40 | 55% | 4,400 |
| intramonth | 212,200 | +6.10% | 0 | - | 235 |
| oracle | 211,960 | +5.98% | 0 | - | 233 |
| random_hold | 208,775 | +4.39% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,998 | +3.50% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,854 | +2.93% | 2 | 50% | 345 |
| snake_abs | 204,743 | +2.37% | 1 | 100% | 255 |
| snake_abs_conv | 204,580 | +2.29% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,951 | +0.48% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,585 | -0.21% | 0 | - | 237 |
| snake_anaconda | 198,197 | -0.90% | 3 | 33% | 374 |
| snake_viper_tick | 197,523 | -1.24% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,120 | -14.94% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,183 (-4.91%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,071 | +1.23% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -519 | -0.24% |
| snake_abs_exit_conv | -763 | -0.37% |
| snake_abs | -1,177 | -0.57% |
| snake_abs_conv | -1,203 | -0.58% |
| benchmark_smallcap | -1,323 | -0.66% |
| snake_abs_exit | -1,564 | -0.75% |
| snake_anaconda | -1,708 | -0.85% |
| snake_viper_tick | -1,848 | -0.93% |
| snake_viper_wild | -1,878 | -0.93% |
| random_hold | -1,985 | -0.94% |
| unified | -2,105 | -0.93% |
| benchmark | -2,234 | -0.99% |
| intramonth | -2,804 | -1.30% |
| intraweek | -3,469 | -1.61% |

Average per day so far: unified Rs +617, benchmark Rs +587, intraweek Rs +314, intramonth Rs +313, oracle Rs +307, random_hold Rs +225, snake_abs_exit Rs +194, snake_abs_exit_conv Rs +163, snake_abs Rs +128, snake_abs_conv Rs +127, nifty_calls Rs +47, snake_viper_wild Rs +31, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -12, snake_anaconda Rs -53, snake_viper_tick Rs -88, snake_nonews Rs -300, snake Rs -320, gold Rs -766

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.