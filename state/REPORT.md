# Paper trading report

Updated 2026-11-18 12:19 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,181 | +11.59% | 0 | - | 236 |
| benchmark | 220,326 | +10.16% | 0 | - | 237 |
| intraweek | 214,046 | +7.02% | 35 | 54% | 3,851 |
| intramonth | 213,068 | +6.53% | 0 | - | 235 |
| snake_abs_exit | 212,909 | +6.45% | 2 | 50% | 345 |
| oracle | 212,460 | +6.23% | 0 | - | 233 |
| snake_abs_exit_conv | 211,131 | +5.57% | 2 | 50% | 345 |
| snake_abs | 208,088 | +4.04% | 1 | 100% | 255 |
| snake_abs_conv | 207,957 | +3.98% | 1 | 100% | 255 |
| random_hold | 207,608 | +3.80% | 10 | 70% | 733 |
| snake_viper_wild | 207,174 | +3.59% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,635 | +1.82% | 15 | 47% | 2,625 |
| snake_anaconda | 203,195 | +1.60% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,618 | -0.19% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,222 | -11.39% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,647 (-4.18%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,743 | +0.79% |
| intramonth | +1,525 | +0.72% |
| intraweek | +723 | +0.34% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -26 | -0.01% |
| snake_abs_exit | -233 | -0.11% |
| snake_abs_exit_conv | -443 | -0.21% |
| snake_abs_conv | -463 | -0.22% |
| snake_abs | -470 | -0.23% |
| random_hold | -825 | -0.40% |
| snake_anaconda | -860 | -0.42% |
| benchmark_smallcap | -953 | -0.47% |
| benchmark | -1,278 | -0.58% |
| snake_viper_tick | -2,202 | -1.07% |
| snake_viper_wild | -2,241 | -1.07% |
| gold | -3,502 | -1.94% |

Average per day so far: unified Rs +644, benchmark Rs +565, snake_abs_exit Rs +391, intraweek Rs +390, intramonth Rs +363, oracle Rs +346, snake_abs_exit_conv Rs +337, snake_viper_wild Rs +256, snake_abs_conv Rs +241, snake_abs Rs +238, random_hold Rs +211, snake_viper_tick Rs +145, snake_anaconda Rs +103, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -12, snake_nonews Rs -326, snake Rs -347, gold Rs -633

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.