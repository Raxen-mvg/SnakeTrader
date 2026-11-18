# Paper trading report

Updated 2026-11-18 13:38 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,885 | +11.44% | 0 | - | 236 |
| benchmark | 219,653 | +9.83% | 0 | - | 237 |
| intramonth | 212,665 | +6.33% | 0 | - | 235 |
| snake_abs_exit | 212,440 | +6.22% | 2 | 50% | 345 |
| oracle | 212,145 | +6.07% | 0 | - | 233 |
| intraweek | 212,083 | +6.04% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 210,747 | +5.37% | 2 | 50% | 345 |
| snake_abs | 207,732 | +3.87% | 1 | 100% | 255 |
| snake_abs_conv | 207,597 | +3.80% | 1 | 100% | 255 |
| random_hold | 206,993 | +3.50% | 10 | 70% | 733 |
| snake_viper_wild | 206,511 | +3.26% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,986 | +1.49% | 15 | 47% | 2,625 |
| snake_anaconda | 202,865 | +1.43% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,148 | -0.43% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,288 | -11.36% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,067 (-4.47%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,446 | +0.65% |
| intramonth | +1,123 | +0.53% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| oracle | -342 | -0.16% |
| snake_abs_exit | -702 | -0.33% |
| snake_abs_conv | -822 | -0.39% |
| snake_abs | -826 | -0.40% |
| snake_abs_exit_conv | -826 | -0.39% |
| snake_anaconda | -1,190 | -0.58% |
| intraweek | -1,240 | -0.58% |
| benchmark_smallcap | -1,424 | -0.71% |
| random_hold | -1,439 | -0.69% |
| benchmark | -1,951 | -0.88% |
| snake_viper_tick | -2,850 | -1.39% |
| snake_viper_wild | -2,904 | -1.39% |
| gold | -3,436 | -1.90% |

Average per day so far: unified Rs +636, benchmark Rs +546, snake_abs_exit Rs +377, intramonth Rs +352, oracle Rs +337, intraweek Rs +336, snake_abs_exit_conv Rs +326, snake_viper_wild Rs +233, snake_abs_conv Rs +230, snake_abs Rs +227, random_hold Rs +194, snake_viper_tick Rs +119, snake_anaconda Rs +92, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -27, snake_nonews Rs -326, snake Rs -347, gold Rs -631

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.