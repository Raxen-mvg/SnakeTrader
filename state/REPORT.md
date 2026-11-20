# Paper trading report

Updated 2026-11-20 11:09 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,501 | +12.75% | 0 | - | 236 |
| benchmark | 222,774 | +11.39% | 0 | - | 237 |
| intramonth | 214,456 | +7.23% | 0 | - | 235 |
| intraweek | 213,994 | +7.00% | 35 | 54% | 3,851 |
| oracle | 212,920 | +6.46% | 0 | - | 233 |
| snake_abs_exit | 210,747 | +5.37% | 2 | 50% | 345 |
| random_hold | 209,055 | +4.53% | 11 | 73% | 979 |
| snake_abs_exit_conv | 208,381 | +4.19% | 2 | 50% | 345 |
| snake_abs | 207,447 | +3.72% | 1 | 100% | 255 |
| snake_abs_conv | 207,309 | +3.65% | 1 | 100% | 255 |
| snake_viper_wild | 206,838 | +3.42% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,307 | +1.65% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,574 | +0.79% | 3 | 33% | 374 |
| benchmark_smallcap | 200,190 | +0.10% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,073 | -17.46% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,926 (-4.04%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,105 | +0.52% |
| unified | +886 | +0.39% |
| oracle | +831 | +0.39% |
| random_hold | +602 | +0.29% |
| intramonth | +448 | +0.21% |
| benchmark | +398 | +0.18% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -669 | -0.33% |
| snake_viper_wild | -684 | -0.33% |
| benchmark_smallcap | -1,278 | -0.63% |
| snake_abs | -1,533 | -0.73% |
| snake_abs_conv | -1,551 | -0.74% |
| snake_anaconda | -1,890 | -0.93% |
| snake_abs_exit | -2,604 | -1.22% |
| snake_abs_exit_conv | -2,684 | -1.27% |
| gold | -9,700 | -5.55% |

Average per day so far: unified Rs +671, benchmark Rs +599, intramonth Rs +380, intraweek Rs +368, oracle Rs +340, snake_abs_exit Rs +307, snake_abs_exit_conv Rs +239, random_hold Rs +238, snake_viper_wild Rs +228, snake_abs_conv Rs +209, snake_abs Rs +207, snake_viper_tick Rs +122, nifty_calls Rs +48, snake_anaconda Rs +48, benchmark_smallcap Rs +6, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -919

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.