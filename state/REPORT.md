# Paper trading report

Updated 2026-11-26 11:57 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,193 | +13.10% | 0 | - | 237 |
| unified | 223,225 | +11.61% | 0 | - | 236 |
| oracle | 213,210 | +6.61% | 0 | - | 233 |
| intramonth | 210,415 | +5.21% | 0 | - | 235 |
| random_hold | 209,783 | +4.89% | 13 | 69% | 1,037 |
| intraweek | 208,428 | +4.21% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,171 | +0.58% | 2 | 50% | 345 |
| benchmark_smallcap | 200,706 | +0.35% | 0 | - | 237 |
| snake_abs_exit_conv | 200,660 | +0.33% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 198,933 | -0.53% | 1 | 100% | 255 |
| snake_abs_conv | 198,744 | -0.63% | 1 | 100% | 255 |
| snake_anaconda | 192,820 | -3.59% | 3 | 33% | 374 |
| snake_viper_wild | 192,398 | -3.80% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,129 | -5.43% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,356 | -16.82% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,834 (-5.58%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,894 | +0.95% |
| gold | +1,759 | +1.07% |
| intraweek | +1,684 | +0.81% |
| benchmark | +1,170 | +0.52% |
| random_hold | +290 | +0.14% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -586 | -0.27% |
| unified | -875 | -0.39% |
| snake_abs_exit | -1,085 | -0.54% |
| snake_abs | -1,217 | -0.61% |
| snake_abs_conv | -1,228 | -0.61% |
| intramonth | -1,278 | -0.60% |
| snake_abs_exit_conv | -1,316 | -0.65% |
| snake_anaconda | -1,733 | -0.89% |
| snake_viper_tick | -5,048 | -2.60% |
| snake_viper_wild | -5,146 | -2.60% |

Average per day so far: benchmark Rs +639, unified Rs +566, oracle Rs +322, intramonth Rs +254, random_hold Rs +239, intraweek Rs +206, nifty_calls Rs +45, snake_abs_exit Rs +31, benchmark_smallcap Rs +19, snake_abs_exit_conv Rs +17, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -27, snake_abs_conv Rs -33, snake_anaconda Rs -199, snake_viper_wild Rs -230, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -362, gold Rs -821

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.