# Paper trading report

Updated 2026-11-27 14:16 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,105 | +12.05% | 0 | - | 237 |
| unified | 223,528 | +11.76% | 0 | - | 236 |
| oracle | 212,233 | +6.12% | 0 | - | 233 |
| random_hold | 211,262 | +5.63% | 13 | 69% | 1,037 |
| intramonth | 210,933 | +5.47% | 0 | - | 235 |
| intraweek | 208,477 | +4.24% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 206,427 | +3.21% | 2 | 50% | 345 |
| snake_abs_exit | 204,266 | +2.13% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,625 | +0.81% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,574 | -0.21% | 1 | 100% | 255 |
| snake_abs_conv | 199,382 | -0.31% | 1 | 100% | 255 |
| snake_anaconda | 193,007 | -3.50% | 3 | 33% | 374 |
| snake_viper_wild | 192,342 | -3.83% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,075 | -5.46% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,646 | -14.68% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,101 (-5.45%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +6,030 | +3.01% |
| gold | +4,653 | +2.80% |
| snake_abs_exit | +3,188 | +1.59% |
| random_hold | +2,668 | +1.28% |
| intraweek | +1,429 | +0.69% |
| snake_abs | +1,021 | +0.51% |
| snake_abs_conv | +1,016 | +0.51% |
| benchmark_smallcap | +785 | +0.39% |
| snake_anaconda | +710 | +0.37% |
| unified | +449 | +0.20% |
| intramonth | +399 | +0.19% |
| snake_viper_wild | +136 | +0.07% |
| snake_viper_tick | +134 | +0.07% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -2 | -0.00% |
| benchmark | -1,882 | -0.83% |

Average per day so far: benchmark Rs +574, unified Rs +560, oracle Rs +291, random_hold Rs +268, intramonth Rs +260, intraweek Rs +202, snake_abs_exit_conv Rs +165, snake_abs_exit Rs +109, nifty_calls Rs +44, benchmark_smallcap Rs +43, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -11, snake_abs_conv Rs -16, snake_anaconda Rs -189, snake_viper_wild Rs -225, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -352, gold Rs -699

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.