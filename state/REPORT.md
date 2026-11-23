# Paper trading report

Updated 2026-11-23 12:27 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,129 | +12.06% | 0 | - | 236 |
| benchmark | 222,980 | +11.49% | 0 | - | 237 |
| intraweek | 212,481 | +6.24% | 40 | 55% | 4,400 |
| oracle | 212,082 | +6.04% | 0 | - | 233 |
| intramonth | 211,937 | +5.97% | 0 | - | 235 |
| random_hold | 208,849 | +4.42% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,292 | +3.65% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,055 | +3.03% | 2 | 50% | 345 |
| snake_abs | 205,015 | +2.51% | 1 | 100% | 255 |
| snake_abs_conv | 204,854 | +2.43% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,340 | +0.67% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,663 | -0.17% | 0 | - | 237 |
| snake_anaconda | 198,540 | -0.73% | 3 | 33% | 374 |
| snake_viper_tick | 197,904 | -1.05% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,972 | -15.01% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,261 (-4.87%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,923 | +1.15% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -396 | -0.19% |
| snake_abs_exit_conv | -562 | -0.27% |
| snake_abs | -905 | -0.44% |
| snake_abs_conv | -929 | -0.45% |
| benchmark_smallcap | -1,244 | -0.62% |
| snake_abs_exit | -1,270 | -0.61% |
| snake_anaconda | -1,366 | -0.68% |
| snake_viper_tick | -1,468 | -0.74% |
| snake_viper_wild | -1,489 | -0.73% |
| random_hold | -1,910 | -0.91% |
| unified | -2,053 | -0.91% |
| benchmark | -2,157 | -0.96% |
| intramonth | -3,067 | -1.43% |
| intraweek | -3,231 | -1.50% |

Average per day so far: unified Rs +619, benchmark Rs +589, intraweek Rs +320, oracle Rs +310, intramonth Rs +306, random_hold Rs +227, snake_abs_exit Rs +203, snake_abs_exit_conv Rs +168, snake_abs Rs +136, snake_abs_conv Rs +135, nifty_calls Rs +47, snake_viper_wild Rs +43, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -10, snake_anaconda Rs -43, snake_viper_tick Rs -75, snake_nonews Rs -300, snake Rs -320, gold Rs -770

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.