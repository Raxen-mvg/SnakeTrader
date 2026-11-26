# Paper trading report

Updated 2026-11-26 12:21 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,117 | +13.06% | 0 | - | 237 |
| unified | 223,464 | +11.73% | 0 | - | 236 |
| oracle | 213,135 | +6.57% | 0 | - | 233 |
| intramonth | 210,623 | +5.31% | 0 | - | 235 |
| random_hold | 209,788 | +4.89% | 13 | 69% | 1,037 |
| intraweek | 208,287 | +4.14% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,582 | +0.29% | 0 | - | 237 |
| snake_abs_exit | 200,553 | +0.28% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit_conv | 199,984 | -0.01% | 2 | 50% | 345 |
| snake_abs | 198,282 | -0.86% | 1 | 100% | 255 |
| snake_abs_conv | 198,087 | -0.96% | 1 | 100% | 255 |
| snake_anaconda | 192,165 | -3.92% | 3 | 33% | 374 |
| snake_viper_wild | 191,956 | -4.02% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,697 | -5.65% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,928 | -17.04% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,811 (-5.59%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,771 | +0.89% |
| intraweek | +1,544 | +0.75% |
| gold | +1,332 | +0.81% |
| benchmark | +1,094 | +0.49% |
| random_hold | +295 | +0.14% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| unified | -636 | -0.28% |
| oracle | -660 | -0.31% |
| intramonth | -1,070 | -0.51% |
| snake_abs_exit | -1,703 | -0.84% |
| snake_abs | -1,868 | -0.93% |
| snake_abs_conv | -1,885 | -0.94% |
| snake_abs_exit_conv | -1,992 | -0.99% |
| snake_anaconda | -2,388 | -1.23% |
| snake_viper_tick | -5,480 | -2.82% |
| snake_viper_wild | -5,587 | -2.83% |

Average per day so far: benchmark Rs +637, unified Rs +572, oracle Rs +320, intramonth Rs +259, random_hold Rs +239, intraweek Rs +202, nifty_calls Rs +45, benchmark_smallcap Rs +16, snake_abs_exit Rs +15, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_abs_exit_conv Rs -0, snake_abs Rs -44, snake_abs_conv Rs -50, snake_anaconda Rs -218, snake_viper_wild Rs -244, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -377, gold Rs -831

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.