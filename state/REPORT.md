# Paper trading report

Updated 2026-11-27 10:10 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,788 | +12.89% | 0 | - | 237 |
| unified | 223,130 | +11.56% | 0 | - | 236 |
| oracle | 212,532 | +6.27% | 0 | - | 233 |
| intramonth | 210,778 | +5.39% | 0 | - | 235 |
| random_hold | 210,044 | +5.02% | 13 | 69% | 1,037 |
| intraweek | 208,489 | +4.24% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,538 | +2.77% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,389 | +2.19% | 2 | 50% | 345 |
| benchmark_smallcap | 202,219 | +1.11% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,335 | +0.67% | 1 | 100% | 255 |
| snake_abs_conv | 201,157 | +0.58% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 195,072 | -2.46% | 3 | 33% | 374 |
| snake_viper_wild | 193,262 | -3.37% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,975 | -5.01% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,575 | -15.71% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,906 (-5.55%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,461 | +2.22% |
| snake_abs_exit_conv | +3,992 | +1.99% |
| snake_abs_conv | +2,791 | +1.41% |
| snake_abs | +2,782 | +1.40% |
| snake_anaconda | +2,776 | +1.44% |
| gold | +2,581 | +1.55% |
| random_hold | +1,450 | +0.69% |
| intraweek | +1,440 | +0.70% |
| benchmark_smallcap | +1,379 | +0.69% |
| snake_viper_wild | +1,056 | +0.55% |
| snake_viper_tick | +1,034 | +0.55% |
| oracle | +296 | +0.14% |
| intramonth | +244 | +0.12% |
| unified | +52 | +0.02% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -199 | -0.09% |

Average per day so far: benchmark Rs +614, unified Rs +551, oracle Rs +298, intramonth Rs +257, random_hold Rs +239, intraweek Rs +202, snake_abs_exit Rs +142, snake_abs_exit_conv Rs +113, benchmark_smallcap Rs +58, nifty_calls Rs +44, snake_abs Rs +33, snake_abs_conv Rs +30, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -133, snake_viper_wild Rs -198, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -323, gold Rs -748

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.