# Paper trading report

Updated 2026-11-23 13:34 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,890 | +11.95% | 0 | - | 236 |
| benchmark | 222,330 | +11.16% | 0 | - | 237 |
| intramonth | 212,082 | +6.04% | 0 | - | 235 |
| intraweek | 211,928 | +5.96% | 40 | 55% | 4,400 |
| oracle | 211,646 | +5.82% | 0 | - | 233 |
| random_hold | 208,852 | +4.43% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,600 | +3.30% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,231 | +2.62% | 2 | 50% | 345 |
| snake_abs | 204,120 | +2.06% | 1 | 100% | 255 |
| snake_abs_conv | 203,951 | +1.98% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,553 | +0.28% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,237 | -0.38% | 0 | - | 237 |
| snake_anaconda | 197,681 | -1.16% | 3 | 33% | 374 |
| snake_viper_tick | 197,133 | -1.43% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,413 | -15.29% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,962 (-5.02%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,365 | +0.81% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -832 | -0.39% |
| snake_abs_exit_conv | -1,386 | -0.67% |
| benchmark_smallcap | -1,670 | -0.83% |
| snake_abs | -1,800 | -0.87% |
| snake_abs_conv | -1,832 | -0.89% |
| random_hold | -1,907 | -0.91% |
| snake_abs_exit | -1,963 | -0.94% |
| snake_anaconda | -2,224 | -1.11% |
| snake_viper_tick | -2,238 | -1.12% |
| snake_viper_wild | -2,276 | -1.12% |
| unified | -2,292 | -1.01% |
| benchmark | -2,808 | -1.25% |
| intramonth | -2,923 | -1.36% |
| intraweek | -3,784 | -1.75% |

Average per day so far: unified Rs +613, benchmark Rs +573, intramonth Rs +310, intraweek Rs +306, oracle Rs +299, random_hold Rs +227, snake_abs_exit Rs +183, snake_abs_exit_conv Rs +145, snake_abs Rs +111, snake_abs_conv Rs +110, nifty_calls Rs +47, snake_viper_wild Rs +18, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -22, snake_anaconda Rs -68, snake_viper_tick Rs -102, snake_nonews Rs -300, snake Rs -320, gold Rs -784

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.