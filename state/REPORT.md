# Paper trading report

Updated 2026-11-16 10:10 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,100 | +10.55% | 0 | - | 236 |
| benchmark | 220,609 | +10.30% | 0 | - | 237 |
| intraweek | 214,498 | +7.25% | 35 | 54% | 3,851 |
| snake_abs_exit | 213,849 | +6.92% | 2 | 50% | 345 |
| oracle | 213,772 | +6.89% | 0 | - | 233 |
| snake_abs_exit_conv | 212,443 | +6.22% | 2 | 50% | 345 |
| intramonth | 211,423 | +5.71% | 0 | - | 235 |
| snake_abs | 209,843 | +4.92% | 1 | 100% | 255 |
| snake_abs_conv | 209,670 | +4.83% | 1 | 100% | 255 |
| random_hold | 208,432 | +4.22% | 10 | 70% | 733 |
| snake_anaconda | 204,000 | +2.00% | 3 | 33% | 374 |
| snake_viper_wild | 203,523 | +1.76% | 14 | 50% | 2,496 |
| benchmark_smallcap | 201,838 | +0.92% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 200,042 | +0.02% | 13 | 46% | 2,299 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 182,237 | -8.88% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,869 (-4.07%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +2,080 | +0.95% |
| intramonth | +1,366 | +0.65% |
| benchmark | +1,270 | +0.58% |
| random_hold | +1,206 | +0.58% |
| oracle | +675 | +0.32% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_anaconda | -892 | -0.44% |
| benchmark_smallcap | -1,031 | -0.51% |
| snake_viper_tick | -1,213 | -0.60% |
| snake_viper_wild | -1,234 | -0.60% |
| intraweek | -1,647 | -0.76% |
| gold | -1,759 | -0.96% |
| snake_abs_conv | -2,696 | -1.27% |
| snake_abs | -2,697 | -1.27% |
| snake_abs_exit | -3,136 | -1.45% |
| snake_abs_exit_conv | -3,938 | -1.82% |

Average per day so far: unified Rs +621, benchmark Rs +606, snake_abs_exit Rs +447, intraweek Rs +426, oracle Rs +405, snake_abs_exit_conv Rs +401, intramonth Rs +336, snake_abs_conv Rs +312, snake_abs Rs +308, random_hold Rs +248, snake_anaconda Rs +138, snake_viper_wild Rs +136, benchmark_smallcap Rs +61, nifty_calls Rs +54, snake_viper_tick Rs +2, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -347, snake Rs -368, gold Rs -522

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.