# Paper trading report

Updated 2026-11-23 11:55 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,382 | +12.19% | 0 | - | 236 |
| benchmark | 222,980 | +11.49% | 0 | - | 237 |
| intraweek | 213,055 | +6.53% | 40 | 55% | 4,400 |
| intramonth | 212,440 | +6.22% | 0 | - | 235 |
| oracle | 211,723 | +5.86% | 0 | - | 233 |
| random_hold | 210,042 | +5.02% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,224 | +3.61% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,302 | +3.15% | 2 | 50% | 345 |
| snake_abs | 204,916 | +2.46% | 1 | 100% | 255 |
| snake_abs_conv | 204,744 | +2.37% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,604 | +0.80% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,506 | -0.25% | 0 | - | 237 |
| snake_anaconda | 198,233 | -0.88% | 3 | 33% | 374 |
| snake_viper_tick | 198,163 | -0.92% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,923 | -15.04% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,536 (-4.73%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,874 | +1.11% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -314 | -0.15% |
| random_hold | -717 | -0.34% |
| oracle | -756 | -0.36% |
| snake_abs | -1,004 | -0.49% |
| snake_abs_conv | -1,039 | -0.51% |
| snake_viper_tick | -1,209 | -0.61% |
| snake_viper_wild | -1,225 | -0.60% |
| snake_abs_exit | -1,338 | -0.64% |
| benchmark_smallcap | -1,401 | -0.70% |
| snake_anaconda | -1,672 | -0.84% |
| unified | -1,800 | -0.80% |
| benchmark | -2,157 | -0.96% |
| intramonth | -2,565 | -1.19% |
| intraweek | -2,657 | -1.23% |

Average per day so far: unified Rs +625, benchmark Rs +589, intraweek Rs +335, intramonth Rs +319, oracle Rs +301, random_hold Rs +257, snake_abs_exit Rs +201, snake_abs_exit_conv Rs +175, snake_abs Rs +133, snake_abs_conv Rs +132, snake_viper_wild Rs +52, nifty_calls Rs +47, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -14, snake_anaconda Rs -52, snake_viper_tick Rs -66, snake_nonews Rs -300, snake Rs -320, gold Rs -771

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.