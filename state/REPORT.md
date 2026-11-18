# Paper trading report

Updated 2026-11-18 09:42 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,965 | +10.48% | 0 | - | 236 |
| benchmark | 220,196 | +10.10% | 0 | - | 237 |
| intraweek | 212,873 | +6.44% | 35 | 54% | 3,851 |
| snake_abs_exit | 212,371 | +6.18% | 2 | 50% | 345 |
| oracle | 211,333 | +5.67% | 0 | - | 233 |
| intramonth | 211,056 | +5.53% | 0 | - | 235 |
| snake_abs_exit_conv | 210,948 | +5.47% | 2 | 50% | 345 |
| snake_abs | 208,476 | +4.24% | 1 | 100% | 255 |
| snake_abs_conv | 208,336 | +4.17% | 1 | 100% | 255 |
| random_hold | 206,914 | +3.46% | 10 | 70% | 733 |
| snake_viper_wild | 206,446 | +3.22% | 16 | 50% | 2,827 |
| snake_anaconda | 203,248 | +1.62% | 3 | 33% | 374 |
| snake_viper_tick | 202,922 | +1.46% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,248 | -0.38% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 176,877 | -11.56% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,393 (-4.80%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs | -83 | -0.04% |
| snake_abs_conv | -84 | -0.04% |
| intraweek | -449 | -0.21% |
| unified | -474 | -0.21% |
| intramonth | -486 | -0.23% |
| snake_abs_exit_conv | -626 | -0.30% |
| snake_abs_exit | -771 | -0.36% |
| snake_anaconda | -807 | -0.40% |
| oracle | -1,154 | -0.54% |
| benchmark_smallcap | -1,323 | -0.66% |
| benchmark | -1,408 | -0.64% |
| random_hold | -1,518 | -0.73% |
| snake_viper_tick | -2,915 | -1.42% |
| snake_viper_wild | -2,969 | -1.42% |
| gold | -3,847 | -2.13% |

Average per day so far: unified Rs +582, benchmark Rs +561, snake_abs_exit Rs +375, intraweek Rs +358, snake_abs_exit_conv Rs +332, oracle Rs +315, intramonth Rs +307, snake_abs_conv Rs +253, snake_abs Rs +249, snake_viper_wild Rs +230, random_hold Rs +192, snake_viper_tick Rs +117, snake_anaconda Rs +105, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -23, snake_nonews Rs -326, snake Rs -347, gold Rs -642

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.