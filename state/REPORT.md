# Paper trading report

Updated 2026-11-19 15:22 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,515 | +12.26% | 0 | - | 236 |
| benchmark | 222,590 | +11.29% | 0 | - | 237 |
| intramonth | 213,802 | +6.90% | 0 | - | 235 |
| snake_abs_exit | 213,226 | +6.61% | 2 | 50% | 345 |
| intraweek | 213,064 | +6.53% | 35 | 54% | 3,851 |
| oracle | 212,222 | +6.11% | 0 | - | 233 |
| snake_abs_exit_conv | 210,913 | +5.46% | 2 | 50% | 345 |
| snake_abs | 208,739 | +4.37% | 1 | 100% | 255 |
| snake_abs_conv | 208,618 | +4.31% | 1 | 100% | 255 |
| random_hold | 208,435 | +4.22% | 10 | 70% | 733 |
| snake_viper_wild | 207,523 | +3.76% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,977 | +1.99% | 15 | 47% | 2,625 |
| snake_anaconda | 203,265 | +1.63% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,726 | +0.86% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,756 | -12.62% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,970 (-4.01%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,399 | +1.20% |
| benchmark | +2,295 | +1.04% |
| unified | +1,903 | +0.85% |
| intramonth | +1,528 | +0.72% |
| random_hold | +1,503 | +0.73% |
| oracle | +1,426 | +0.68% |
| intraweek | +1,225 | +0.58% |
| snake_viper_wild | +483 | +0.23% |
| snake_viper_tick | +474 | +0.23% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -697 | -0.33% |
| snake_abs_conv | -706 | -0.34% |
| snake_abs_exit | -806 | -0.38% |
| snake_anaconda | -1,136 | -0.56% |
| snake_abs_exit_conv | -1,470 | -0.69% |
| gold | -2,565 | -1.45% |

Average per day so far: unified Rs +663, benchmark Rs +611, snake_abs_exit Rs +389, intramonth Rs +373, intraweek Rs +353, oracle Rs +330, snake_abs_exit_conv Rs +321, snake_viper_wild Rs +259, snake_abs_conv Rs +253, snake_abs Rs +250, random_hold Rs +228, snake_viper_tick Rs +153, snake_anaconda Rs +102, benchmark_smallcap Rs +52, nifty_calls Rs +50, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -682

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.