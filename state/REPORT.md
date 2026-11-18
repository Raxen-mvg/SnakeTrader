# Paper trading report

Updated 2026-11-18 13:23 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,053 | +11.53% | 0 | - | 236 |
| benchmark | 219,913 | +9.96% | 0 | - | 237 |
| intramonth | 212,971 | +6.49% | 0 | - | 235 |
| snake_abs_exit | 212,640 | +6.32% | 2 | 50% | 345 |
| intraweek | 212,364 | +6.18% | 35 | 54% | 3,851 |
| oracle | 212,301 | +6.15% | 0 | - | 233 |
| snake_abs_exit_conv | 210,872 | +5.44% | 2 | 50% | 345 |
| snake_abs | 207,841 | +3.92% | 1 | 100% | 255 |
| snake_abs_conv | 207,706 | +3.85% | 1 | 100% | 255 |
| random_hold | 206,998 | +3.50% | 10 | 70% | 733 |
| snake_viper_wild | 206,598 | +3.30% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,071 | +1.53% | 15 | 47% | 2,625 |
| snake_anaconda | 202,975 | +1.49% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,327 | -0.34% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 176,926 | -11.54% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,241 (-4.38%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,614 | +0.73% |
| intramonth | +1,429 | +0.68% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| oracle | -185 | -0.09% |
| snake_abs_exit | -502 | -0.24% |
| snake_abs_exit_conv | -701 | -0.33% |
| snake_abs_conv | -713 | -0.34% |
| snake_abs | -718 | -0.34% |
| intraweek | -958 | -0.45% |
| snake_anaconda | -1,080 | -0.53% |
| benchmark_smallcap | -1,244 | -0.62% |
| random_hold | -1,435 | -0.69% |
| benchmark | -1,691 | -0.76% |
| snake_viper_tick | -2,766 | -1.34% |
| snake_viper_wild | -2,817 | -1.34% |
| gold | -3,798 | -2.10% |

Average per day so far: unified Rs +640, benchmark Rs +553, snake_abs_exit Rs +383, intramonth Rs +360, intraweek Rs +343, oracle Rs +342, snake_abs_exit_conv Rs +329, snake_viper_wild Rs +236, snake_abs_conv Rs +234, snake_abs Rs +231, random_hold Rs +194, snake_viper_tick Rs +123, snake_anaconda Rs +96, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -21, snake_nonews Rs -326, snake Rs -347, gold Rs -641

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.