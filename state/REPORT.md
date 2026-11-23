# Paper trading report

Updated 2026-11-23 15:26 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,882 | +12.44% | 0 | - | 236 |
| benchmark | 221,351 | +10.68% | 0 | - | 237 |
| intramonth | 213,793 | +6.90% | 0 | - | 235 |
| oracle | 212,692 | +6.35% | 0 | - | 233 |
| intraweek | 211,326 | +5.66% | 40 | 55% | 4,400 |
| random_hold | 208,083 | +4.04% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,727 | +3.86% | 2 | 50% | 345 |
| snake_abs_exit_conv | 207,235 | +3.62% | 2 | 50% | 345 |
| snake_abs | 205,793 | +2.90% | 1 | 100% | 255 |
| snake_abs_conv | 205,640 | +2.82% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,115 | +0.56% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 198,946 | -0.53% | 3 | 33% | 374 |
| benchmark_smallcap | 198,497 | -0.75% | 0 | - | 237 |
| snake_viper_tick | 197,683 | -1.16% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,282 | -15.36% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,500 (-4.75%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,233 | +0.73% |
| snake_abs_exit_conv | +618 | +0.30% |
| oracle | +213 | +0.10% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_abs | -126 | -0.06% |
| snake_abs_conv | -143 | -0.07% |
| snake_abs_exit | -835 | -0.40% |
| snake_anaconda | -960 | -0.48% |
| intramonth | -1,212 | -0.56% |
| unified | -1,299 | -0.57% |
| snake_viper_tick | -1,688 | -0.85% |
| snake_viper_wild | -1,715 | -0.84% |
| benchmark_smallcap | -2,410 | -1.20% |
| random_hold | -2,677 | -1.27% |
| benchmark | -3,787 | -1.68% |
| intraweek | -4,386 | -2.03% |

Average per day so far: unified Rs +638, benchmark Rs +547, intramonth Rs +354, oracle Rs +325, intraweek Rs +290, snake_abs_exit Rs +215, random_hold Rs +207, snake_abs_exit_conv Rs +201, snake_abs_conv Rs +157, snake_abs Rs +157, nifty_calls Rs +47, snake_viper_wild Rs +36, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, snake_anaconda Rs -31, benchmark_smallcap Rs -43, snake_viper_tick Rs -83, snake_nonews Rs -300, snake Rs -320, gold Rs -788

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.