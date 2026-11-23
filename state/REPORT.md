# Paper trading report

Updated 2026-11-23 13:28 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,834 | +11.92% | 0 | - | 236 |
| benchmark | 222,284 | +11.14% | 0 | - | 237 |
| intramonth | 212,056 | +6.03% | 0 | - | 235 |
| intraweek | 211,971 | +5.99% | 40 | 55% | 4,400 |
| oracle | 211,571 | +5.79% | 0 | - | 233 |
| random_hold | 208,528 | +4.26% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,745 | +3.37% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,349 | +2.67% | 2 | 50% | 345 |
| snake_abs | 204,212 | +2.11% | 1 | 100% | 255 |
| snake_abs_conv | 204,044 | +2.02% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,553 | +0.28% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,237 | -0.38% | 0 | - | 237 |
| snake_anaconda | 197,772 | -1.11% | 3 | 33% | 374 |
| snake_viper_tick | 197,133 | -1.43% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,759 | -15.12% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,917 (-5.04%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,710 | +1.02% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -907 | -0.43% |
| snake_abs_exit_conv | -1,268 | -0.61% |
| benchmark_smallcap | -1,670 | -0.83% |
| snake_abs | -1,708 | -0.83% |
| snake_abs_conv | -1,738 | -0.84% |
| snake_abs_exit | -1,817 | -0.87% |
| snake_anaconda | -2,134 | -1.07% |
| random_hold | -2,231 | -1.06% |
| snake_viper_tick | -2,238 | -1.12% |
| snake_viper_wild | -2,276 | -1.12% |
| unified | -2,348 | -1.04% |
| benchmark | -2,853 | -1.27% |
| intramonth | -2,948 | -1.37% |
| intraweek | -3,741 | -1.73% |

Average per day so far: unified Rs +611, benchmark Rs +571, intramonth Rs +309, intraweek Rs +307, oracle Rs +297, random_hold Rs +219, snake_abs_exit Rs +187, snake_abs_exit_conv Rs +149, snake_abs Rs +114, snake_abs_conv Rs +112, nifty_calls Rs +47, snake_viper_wild Rs +18, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -22, snake_anaconda Rs -66, snake_viper_tick Rs -102, snake_nonews Rs -300, snake Rs -320, gold Rs -775

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.