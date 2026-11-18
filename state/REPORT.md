# Paper trading report

Updated 2026-11-18 09:17 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,513 | +10.76% | 0 | - | 236 |
| benchmark | 221,121 | +10.56% | 0 | - | 237 |
| intraweek | 213,933 | +6.97% | 35 | 54% | 3,851 |
| snake_abs_exit | 213,798 | +6.90% | 2 | 50% | 345 |
| oracle | 212,583 | +6.29% | 0 | - | 233 |
| snake_abs_exit_conv | 211,969 | +5.98% | 2 | 50% | 345 |
| intramonth | 211,336 | +5.67% | 0 | - | 235 |
| snake_viper_wild | 209,075 | +4.54% | 14 | 50% | 2,496 |
| snake_abs | 208,910 | +4.46% | 1 | 100% | 255 |
| snake_abs_conv | 208,779 | +4.39% | 1 | 100% | 255 |
| random_hold | 208,312 | +4.16% | 10 | 70% | 733 |
| snake_viper_tick | 205,503 | +2.75% | 13 | 46% | 2,299 |
| snake_anaconda | 203,923 | +1.96% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,851 | +0.43% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,321 | -11.34% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,217 (-4.39%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +656 | +0.31% |
| intraweek | +610 | +0.29% |
| snake_abs_exit_conv | +395 | +0.19% |
| snake_abs_conv | +359 | +0.17% |
| snake_abs | +351 | +0.17% |
| benchmark_smallcap | +280 | +0.14% |
| oracle | +97 | +0.05% |
| unified | +74 | +0.03% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| random_hold | -121 | -0.06% |
| snake_anaconda | -132 | -0.07% |
| intramonth | -206 | -0.10% |
| snake_viper_tick | -334 | -0.16% |
| snake_viper_wild | -340 | -0.16% |
| benchmark | -482 | -0.22% |
| gold | -3,403 | -1.88% |

Average per day so far: unified Rs +598, benchmark Rs +587, snake_abs_exit Rs +418, intraweek Rs +387, snake_abs_exit_conv Rs +363, oracle Rs +350, snake_viper_wild Rs +324, intramonth Rs +315, snake_abs_conv Rs +266, snake_abs Rs +262, random_hold Rs +231, snake_viper_tick Rs +220, snake_anaconda Rs +127, nifty_calls Rs +51, benchmark_smallcap Rs +27, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -326, snake Rs -347, gold Rs -630

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.