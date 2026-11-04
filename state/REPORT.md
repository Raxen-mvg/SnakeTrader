# Paper trading report

Updated 2026-11-04 11:52 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,500 | +6.75% | 0 | - | 236 |
| intraweek | 208,906 | +4.45% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,494 | +4.25% | 1 | 100% | 255 |
| snake_abs_exit | 208,356 | +4.18% | 1 | 100% | 260 |
| benchmark | 207,458 | +3.73% | 0 | - | 237 |
| snake_viper_wild | 206,776 | +3.39% | 3 | 33% | 702 |
| intramonth | 205,623 | +2.81% | 0 | - | 235 |
| snake_abs | 205,406 | +2.70% | 1 | 100% | 255 |
| snake_abs_conv | 205,253 | +2.63% | 1 | 100% | 255 |
| snake_viper_tick | 203,175 | +1.59% | 2 | 0% | 532 |
| random_hold | 202,502 | +1.25% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,734 | +0.37% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,362 | -1.32% | 3 | 33% | 361 |
| benchmark_smallcap | 194,596 | -2.70% | 0 | - | 237 |
| gold | 190,670 | -4.67% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 188,967 (-5.52%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +5,392 | +2.91% |
| snake_abs_exit | +4,342 | +2.13% |
| snake_abs_exit_conv | +4,155 | +2.03% |
| snake_abs_conv | +4,112 | +2.04% |
| snake_abs | +4,097 | +2.04% |
| intraweek | +3,821 | +1.86% |
| snake_anaconda | +3,537 | +1.82% |
| random_hold | +2,034 | +1.01% |
| benchmark_smallcap | +1,659 | +0.86% |
| intramonth | +1,652 | +0.81% |
| unified | +1,499 | +0.71% |
| benchmark | +757 | +0.37% |
| oracle | +745 | +0.37% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,991 | -1.93% |
| snake_viper_wild | -4,116 | -1.95% |

Average per day so far: unified Rs +500, snake_viper_wild Rs +357, snake_abs_exit_conv Rs +354, snake_abs_exit Rs +348, intraweek Rs +330, benchmark Rs +276, snake_abs_conv Rs +219, snake_abs Rs +216, intramonth Rs +208, snake_viper_tick Rs +198, random_hold Rs +93, nifty_calls Rs +68, oracle Rs +27, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -120, benchmark_smallcap Rs -235, gold Rs -346, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.