# Paper trading report

Updated 2026-11-17 09:49 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,150 | +11.57% | 0 | - | 236 |
| benchmark | 221,205 | +10.60% | 0 | - | 237 |
| snake_abs_exit | 214,776 | +7.39% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,528 | +6.76% | 2 | 50% | 345 |
| intramonth | 213,409 | +6.70% | 0 | - | 235 |
| oracle | 212,971 | +6.49% | 0 | - | 233 |
| intraweek | 212,676 | +6.34% | 35 | 54% | 3,851 |
| snake_abs | 210,088 | +5.04% | 1 | 100% | 255 |
| snake_abs_conv | 209,941 | +4.97% | 1 | 100% | 255 |
| random_hold | 208,059 | +4.03% | 10 | 70% | 733 |
| snake_viper_wild | 206,825 | +3.41% | 14 | 50% | 2,496 |
| snake_anaconda | 205,498 | +2.75% | 3 | 33% | 374 |
| snake_viper_tick | 203,289 | +1.64% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,062 | +1.03% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,086 | -9.46% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,915 (-4.04%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intramonth | +1,790 | +0.85% |
| unified | +1,712 | +0.77% |
| intraweek | +1,410 | +0.67% |
| benchmark_smallcap | +1,233 | +0.61% |
| benchmark | +1,125 | +0.51% |
| oracle | +948 | +0.45% |
| snake_viper_wild | +681 | +0.33% |
| snake_viper_tick | +669 | +0.33% |
| snake_anaconda | +395 | +0.19% |
| snake_abs_exit | +367 | +0.17% |
| snake_abs_exit_conv | +311 | +0.15% |
| random_hold | +265 | +0.13% |
| gold | +132 | +0.07% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs | -46 | -0.02% |
| snake_abs_conv | -49 | -0.02% |

Average per day so far: unified Rs +661, benchmark Rs +606, snake_abs_exit Rs +462, snake_abs_exit_conv Rs +423, intramonth Rs +383, oracle Rs +371, intraweek Rs +362, snake_abs_conv Rs +311, snake_abs Rs +306, snake_viper_wild Rs +253, random_hold Rs +230, snake_anaconda Rs +183, snake_viper_tick Rs +137, benchmark_smallcap Rs +67, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -540

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.