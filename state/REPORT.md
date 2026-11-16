# Paper trading report

Updated 2026-11-16 11:32 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,242 | +10.62% | 0 | - | 236 |
| benchmark | 220,027 | +10.01% | 0 | - | 237 |
| oracle | 213,407 | +6.70% | 0 | - | 233 |
| intraweek | 213,304 | +6.65% | 35 | 54% | 3,851 |
| snake_abs_exit | 212,888 | +6.44% | 2 | 50% | 345 |
| intramonth | 211,828 | +5.91% | 0 | - | 235 |
| snake_abs_exit_conv | 211,518 | +5.76% | 2 | 50% | 345 |
| snake_abs | 208,659 | +4.33% | 1 | 100% | 255 |
| snake_abs_conv | 208,491 | +4.25% | 1 | 100% | 255 |
| random_hold | 207,757 | +3.88% | 10 | 70% | 733 |
| snake_viper_wild | 204,652 | +2.33% | 14 | 50% | 2,496 |
| snake_anaconda | 203,072 | +1.54% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,152 | +0.58% | 13 | 46% | 2,299 |
| benchmark_smallcap | 200,818 | +0.41% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,642 | -9.68% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,487 (-4.26%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +2,221 | +1.01% |
| intramonth | +1,772 | +0.84% |
| benchmark | +688 | +0.31% |
| random_hold | +531 | +0.26% |
| oracle | +309 | +0.14% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_viper_tick | -103 | -0.05% |
| snake_viper_wild | -105 | -0.05% |
| snake_anaconda | -1,820 | -0.89% |
| benchmark_smallcap | -2,051 | -1.01% |
| intraweek | -2,841 | -1.31% |
| gold | -3,354 | -1.82% |
| snake_abs_conv | -3,875 | -1.82% |
| snake_abs | -3,881 | -1.83% |
| snake_abs_exit | -4,097 | -1.89% |
| snake_abs_exit_conv | -4,864 | -2.25% |

Average per day so far: unified Rs +625, benchmark Rs +589, snake_abs_exit Rs +416, oracle Rs +394, intraweek Rs +391, snake_abs_exit_conv Rs +372, intramonth Rs +348, snake_abs_conv Rs +274, snake_abs Rs +271, random_hold Rs +228, snake_viper_wild Rs +179, snake_anaconda Rs +106, nifty_calls Rs +54, snake_viper_tick Rs +50, benchmark_smallcap Rs +27, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -347, snake Rs -368, gold Rs -569

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.