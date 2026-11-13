# Paper trading report

Updated 2026-11-13 14:49 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,281 | +10.14% | 0 | - | 236 |
| benchmark | 219,347 | +9.67% | 0 | - | 237 |
| snake_abs_exit | 217,436 | +8.72% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,969 | +8.48% | 2 | 50% | 345 |
| intraweek | 216,061 | +8.03% | 30 | 53% | 3,302 |
| oracle | 213,240 | +6.62% | 0 | - | 233 |
| snake_abs | 213,159 | +6.58% | 1 | 100% | 255 |
| snake_abs_conv | 212,992 | +6.50% | 1 | 100% | 255 |
| intramonth | 210,789 | +5.39% | 0 | - | 235 |
| random_hold | 207,104 | +3.55% | 10 | 70% | 733 |
| snake_anaconda | 205,476 | +2.74% | 3 | 33% | 374 |
| snake_viper_wild | 205,294 | +2.65% | 14 | 50% | 2,496 |
| benchmark_smallcap | 202,993 | +1.50% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,783 | +0.89% | 13 | 46% | 2,299 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,996 | -8.00% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,904 (-4.05%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,403 | +0.65% |
| oracle | +125 | +0.06% |
| snake_viper_tick | +1 | +0.00% |
| snake_viper_wild | +1 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_abs_exit | -7 | -0.00% |
| benchmark_smallcap | -213 | -0.10% |
| unified | -416 | -0.19% |
| snake_anaconda | -452 | -0.22% |
| intramonth | -804 | -0.38% |
| random_hold | -950 | -0.46% |
| benchmark | -1,201 | -0.55% |
| gold | -1,315 | -0.71% |
| snake_abs_exit_conv | -1,705 | -0.78% |
| snake_abs_conv | -2,543 | -1.18% |
| snake_abs | -2,552 | -1.18% |

Average per day so far: unified Rs +615, benchmark Rs +586, snake_abs_exit Rs +581, snake_abs_exit_conv Rs +566, intraweek Rs +487, snake_abs_conv Rs +433, snake_abs Rs +424, oracle Rs +401, intramonth Rs +327, random_hold Rs +215, snake_viper_wild Rs +212, snake_anaconda Rs +196, benchmark_smallcap Rs +103, snake_viper_tick Rs +81, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -485

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.