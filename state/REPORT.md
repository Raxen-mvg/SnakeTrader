# Paper trading report

Updated 2026-11-13 10:37 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,674 | +10.34% | 0 | - | 236 |
| benchmark | 219,959 | +9.98% | 0 | - | 237 |
| snake_abs_exit_conv | 217,158 | +8.58% | 2 | 50% | 345 |
| snake_abs_exit | 216,904 | +8.45% | 2 | 50% | 345 |
| intraweek | 216,390 | +8.20% | 30 | 53% | 3,302 |
| oracle | 213,765 | +6.88% | 0 | - | 233 |
| snake_abs | 213,296 | +6.65% | 1 | 100% | 255 |
| snake_abs_conv | 213,130 | +6.57% | 1 | 100% | 255 |
| intramonth | 211,489 | +5.75% | 0 | - | 235 |
| random_hold | 207,382 | +3.69% | 10 | 70% | 733 |
| snake_viper_wild | 206,805 | +3.40% | 14 | 50% | 2,496 |
| snake_anaconda | 205,269 | +2.63% | 3 | 33% | 374 |
| benchmark_smallcap | 203,699 | +1.85% | 0 | - | 237 |
| snake_viper_tick | 203,268 | +1.63% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,538 | -7.73% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,290 (-3.86%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,732 | +0.81% |
| snake_viper_wild | +1,512 | +0.74% |
| snake_viper_tick | +1,486 | +0.74% |
| oracle | +650 | +0.30% |
| benchmark_smallcap | +493 | +0.24% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -23 | -0.01% |
| intramonth | -104 | -0.05% |
| snake_abs_exit | -538 | -0.25% |
| benchmark | -589 | -0.27% |
| snake_anaconda | -658 | -0.32% |
| random_hold | -672 | -0.32% |
| gold | -773 | -0.42% |
| snake_abs_exit_conv | -1,516 | -0.69% |
| snake_abs_conv | -2,406 | -1.12% |
| snake_abs | -2,415 | -1.12% |

Average per day so far: unified Rs +626, benchmark Rs +605, snake_abs_exit_conv Rs +572, snake_abs_exit Rs +563, intraweek Rs +497, snake_abs_conv Rs +438, snake_abs Rs +429, oracle Rs +417, intramonth Rs +348, snake_viper_wild Rs +272, random_hold Rs +224, snake_anaconda Rs +188, snake_viper_tick Rs +149, benchmark_smallcap Rs +128, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -469

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.