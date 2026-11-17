# Paper trading report

Updated 2026-11-17 09:45 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,359 | +11.68% | 0 | - | 236 |
| benchmark | 221,183 | +10.59% | 0 | - | 237 |
| snake_abs_exit | 214,720 | +7.36% | 2 | 50% | 345 |
| intramonth | 213,743 | +6.87% | 0 | - | 235 |
| snake_abs_exit_conv | 213,549 | +6.78% | 2 | 50% | 345 |
| intraweek | 212,905 | +6.45% | 35 | 54% | 3,851 |
| oracle | 212,900 | +6.45% | 0 | - | 233 |
| snake_abs | 210,072 | +5.04% | 1 | 100% | 255 |
| snake_abs_conv | 209,927 | +4.96% | 1 | 100% | 255 |
| random_hold | 208,120 | +4.06% | 10 | 70% | 733 |
| snake_viper_wild | 206,858 | +3.43% | 14 | 50% | 2,496 |
| snake_anaconda | 205,485 | +2.74% | 3 | 33% | 374 |
| snake_viper_tick | 203,321 | +1.66% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,241 | +1.12% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,217 | -9.39% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,048 (-3.98%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intramonth | +2,124 | +1.00% |
| unified | +1,921 | +0.87% |
| intraweek | +1,639 | +0.78% |
| benchmark_smallcap | +1,412 | +0.70% |
| benchmark | +1,102 | +0.50% |
| oracle | +877 | +0.41% |
| snake_viper_wild | +713 | +0.35% |
| snake_viper_tick | +701 | +0.35% |
| snake_anaconda | +382 | +0.19% |
| snake_abs_exit_conv | +332 | +0.16% |
| random_hold | +327 | +0.16% |
| snake_abs_exit | +311 | +0.14% |
| gold | +263 | +0.14% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs | -62 | -0.03% |
| snake_abs_conv | -63 | -0.03% |

Average per day so far: unified Rs +667, benchmark Rs +605, snake_abs_exit Rs +460, snake_abs_exit_conv Rs +423, intramonth Rs +393, intraweek Rs +369, oracle Rs +369, snake_abs_conv Rs +310, snake_abs Rs +305, snake_viper_wild Rs +254, random_hold Rs +232, snake_anaconda Rs +183, snake_viper_tick Rs +138, benchmark_smallcap Rs +72, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -537

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.