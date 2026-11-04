# Paper trading report

Updated 2026-11-04 11:40 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,380 | +6.69% | 0 | - | 236 |
| intraweek | 208,840 | +4.42% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,436 | +4.22% | 1 | 100% | 255 |
| snake_abs_exit | 208,317 | +4.16% | 1 | 100% | 260 |
| benchmark | 207,451 | +3.73% | 0 | - | 237 |
| snake_viper_wild | 206,782 | +3.39% | 3 | 33% | 702 |
| intramonth | 205,701 | +2.85% | 0 | - | 235 |
| snake_abs | 205,349 | +2.67% | 1 | 100% | 255 |
| snake_abs_conv | 205,196 | +2.60% | 1 | 100% | 255 |
| snake_viper_tick | 203,180 | +1.59% | 2 | 0% | 532 |
| random_hold | 202,575 | +1.29% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,808 | +0.40% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,311 | -1.34% | 3 | 33% | 361 |
| benchmark_smallcap | 194,675 | -2.66% | 0 | - | 237 |
| gold | 190,144 | -4.93% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 188,942 (-5.53%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +4,866 | +2.63% |
| snake_abs_exit | +4,302 | +2.11% |
| snake_abs_exit_conv | +4,097 | +2.00% |
| snake_abs_conv | +4,055 | +2.02% |
| snake_abs | +4,040 | +2.01% |
| intraweek | +3,755 | +1.83% |
| snake_anaconda | +3,486 | +1.80% |
| random_hold | +2,107 | +1.05% |
| benchmark_smallcap | +1,738 | +0.90% |
| intramonth | +1,730 | +0.85% |
| unified | +1,379 | +0.65% |
| oracle | +818 | +0.41% |
| benchmark | +750 | +0.36% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,987 | -1.92% |
| snake_viper_wild | -4,111 | -1.95% |

Average per day so far: unified Rs +496, snake_viper_wild Rs +357, snake_abs_exit_conv Rs +351, snake_abs_exit Rs +347, intraweek Rs +327, benchmark Rs +276, snake_abs_conv Rs +217, snake_abs Rs +214, intramonth Rs +211, snake_viper_tick Rs +199, random_hold Rs +95, nifty_calls Rs +68, oracle Rs +30, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -122, benchmark_smallcap Rs -232, gold Rs -365, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.