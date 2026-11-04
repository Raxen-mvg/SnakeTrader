# Paper trading report

Updated 2026-11-04 10:14 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 212,864 | +6.43% | 0 | - | 236 |
| snake_abs_exit_conv | 209,077 | +4.54% | 1 | 100% | 255 |
| snake_abs_exit | 208,920 | +4.46% | 1 | 100% | 260 |
| intraweek | 208,668 | +4.33% | 25 | 48% | 2,757 |
| benchmark | 208,529 | +4.26% | 0 | - | 237 |
| snake_viper_wild | 206,611 | +3.31% | 3 | 33% | 702 |
| snake_abs | 205,979 | +2.99% | 1 | 100% | 255 |
| snake_abs_conv | 205,829 | +2.91% | 1 | 100% | 255 |
| intramonth | 205,376 | +2.69% | 0 | - | 235 |
| snake_viper_tick | 203,008 | +1.50% | 2 | 0% | 532 |
| random_hold | 202,571 | +1.28% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,494 | +0.25% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,809 | -1.10% | 3 | 33% | 361 |
| benchmark_smallcap | 194,675 | -2.66% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 187,234 | -6.38% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,713 (-5.64%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,906 | +2.40% |
| snake_abs_exit_conv | +4,738 | +2.32% |
| snake_abs_conv | +4,688 | +2.33% |
| snake_abs | +4,669 | +2.32% |
| snake_anaconda | +3,984 | +2.06% |
| intraweek | +3,583 | +1.75% |
| random_hold | +2,102 | +1.05% |
| gold | +1,956 | +1.06% |
| benchmark | +1,828 | +0.89% |
| benchmark_smallcap | +1,738 | +0.90% |
| intramonth | +1,405 | +0.69% |
| unified | +863 | +0.41% |
| oracle | +504 | +0.25% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -4,159 | -2.01% |
| snake_viper_wild | -4,282 | -2.03% |

Average per day so far: unified Rs +476, snake_abs_exit_conv Rs +378, snake_abs_exit Rs +372, snake_viper_wild Rs +348, intraweek Rs +321, benchmark Rs +316, snake_abs_conv Rs +243, snake_abs Rs +239, intramonth Rs +199, snake_viper_tick Rs +188, random_hold Rs +95, nifty_calls Rs +68, oracle Rs +18, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -100, benchmark_smallcap Rs -232, snake_nonews Rs -444, snake Rs -467, gold Rs -473

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.