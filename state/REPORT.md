# Paper trading report

Updated 2026-11-13 13:01 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,914 | +9.96% | 0 | - | 236 |
| benchmark | 219,278 | +9.64% | 0 | - | 237 |
| snake_abs_exit | 217,000 | +8.50% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,728 | +8.36% | 2 | 50% | 345 |
| intraweek | 215,533 | +7.77% | 30 | 53% | 3,302 |
| oracle | 212,971 | +6.49% | 0 | - | 233 |
| snake_abs | 212,694 | +6.35% | 1 | 100% | 255 |
| snake_abs_conv | 212,525 | +6.26% | 1 | 100% | 255 |
| intramonth | 210,573 | +5.29% | 0 | - | 235 |
| random_hold | 207,102 | +3.55% | 10 | 70% | 733 |
| snake_viper_wild | 205,633 | +2.82% | 14 | 50% | 2,496 |
| snake_anaconda | 204,904 | +2.45% | 3 | 33% | 374 |
| benchmark_smallcap | 202,667 | +1.33% | 0 | - | 237 |
| snake_viper_tick | 202,116 | +1.06% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,470 | -8.27% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,602 (-4.20%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +875 | +0.41% |
| snake_viper_wild | +340 | +0.17% |
| snake_viper_tick | +334 | +0.17% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -144 | -0.07% |
| snake_abs_exit | -442 | -0.20% |
| benchmark_smallcap | -538 | -0.27% |
| unified | -782 | -0.35% |
| random_hold | -952 | -0.46% |
| intramonth | -1,020 | -0.48% |
| snake_anaconda | -1,023 | -0.50% |
| benchmark | -1,270 | -0.58% |
| gold | -1,841 | -0.99% |
| snake_abs_exit_conv | -1,946 | -0.89% |
| snake_abs_conv | -3,010 | -1.40% |
| snake_abs | -3,017 | -1.40% |

Average per day so far: unified Rs +603, benchmark Rs +584, snake_abs_exit Rs +567, snake_abs_exit_conv Rs +558, intraweek Rs +471, snake_abs_conv Rs +417, snake_abs Rs +409, oracle Rs +393, intramonth Rs +320, snake_viper_wild Rs +225, random_hold Rs +215, snake_anaconda Rs +175, snake_viper_tick Rs +96, benchmark_smallcap Rs +92, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -501

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.