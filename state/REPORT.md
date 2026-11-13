# Paper trading report

Updated 2026-11-13 15:25 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 219,369 | +9.69% | 0 | - | 237 |
| unified | 218,866 | +9.43% | 0 | - | 236 |
| snake_abs_exit | 216,802 | +8.40% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,290 | +8.14% | 2 | 50% | 345 |
| intraweek | 216,089 | +8.04% | 30 | 53% | 3,302 |
| oracle | 213,223 | +6.61% | 0 | - | 233 |
| snake_abs | 212,542 | +6.27% | 1 | 100% | 255 |
| snake_abs_conv | 212,370 | +6.18% | 1 | 100% | 255 |
| intramonth | 210,011 | +5.00% | 0 | - | 235 |
| random_hold | 207,309 | +3.65% | 10 | 70% | 733 |
| snake_viper_wild | 205,014 | +2.51% | 14 | 50% | 2,496 |
| snake_anaconda | 204,928 | +2.46% | 3 | 33% | 374 |
| benchmark_smallcap | 202,443 | +1.22% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,507 | +0.75% | 13 | 46% | 2,299 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,061 | -7.97% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,540 (-4.23%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,431 | +0.67% |
| oracle | +107 | +0.05% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_viper_tick | -274 | -0.14% |
| snake_viper_wild | -279 | -0.14% |
| snake_abs_exit | -640 | -0.29% |
| random_hold | -744 | -0.36% |
| benchmark_smallcap | -762 | -0.38% |
| snake_anaconda | -999 | -0.48% |
| benchmark | -1,178 | -0.53% |
| gold | -1,249 | -0.67% |
| intramonth | -1,582 | -0.75% |
| unified | -1,831 | -0.83% |
| snake_abs_exit_conv | -2,384 | -1.09% |
| snake_abs_conv | -3,165 | -1.47% |
| snake_abs | -3,169 | -1.47% |

Average per day so far: benchmark Rs +587, unified Rs +572, snake_abs_exit Rs +560, snake_abs_exit_conv Rs +543, intraweek Rs +488, snake_abs_conv Rs +412, snake_abs Rs +405, oracle Rs +401, intramonth Rs +303, random_hold Rs +221, snake_viper_wild Rs +201, snake_anaconda Rs +176, benchmark_smallcap Rs +84, snake_viper_tick Rs +69, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -483

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.