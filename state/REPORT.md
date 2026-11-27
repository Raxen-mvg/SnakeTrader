# Paper trading report

Updated 2026-11-27 11:22 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,105 | +12.05% | 0 | - | 237 |
| unified | 222,304 | +11.15% | 0 | - | 236 |
| oracle | 211,931 | +5.97% | 0 | - | 233 |
| random_hold | 210,423 | +5.21% | 13 | 69% | 1,037 |
| intramonth | 210,101 | +5.05% | 0 | - | 235 |
| intraweek | 207,895 | +3.95% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,116 | +2.56% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,012 | +2.01% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,569 | +0.78% | 0 | - | 237 |
| snake_abs | 200,885 | +0.44% | 1 | 100% | 255 |
| snake_abs_conv | 200,708 | +0.35% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,477 | -2.76% | 3 | 33% | 374 |
| snake_viper_wild | 193,330 | -3.33% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,043 | -4.98% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,002 | -15.50% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,486 (-5.76%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,038 | +2.01% |
| snake_abs_exit_conv | +3,615 | +1.80% |
| gold | +3,009 | +1.81% |
| snake_abs_conv | +2,342 | +1.18% |
| snake_abs | +2,333 | +1.18% |
| snake_anaconda | +2,180 | +1.13% |
| random_hold | +1,829 | +0.88% |
| snake_viper_wild | +1,125 | +0.58% |
| snake_viper_tick | +1,102 | +0.58% |
| intraweek | +846 | +0.41% |
| benchmark_smallcap | +729 | +0.36% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -304 | -0.14% |
| intramonth | -432 | -0.20% |
| unified | -774 | -0.35% |
| benchmark | -1,882 | -0.83% |

Average per day so far: benchmark Rs +574, unified Rs +531, oracle Rs +284, random_hold Rs +248, intramonth Rs +241, intraweek Rs +188, snake_abs_exit Rs +131, snake_abs_exit_conv Rs +103, nifty_calls Rs +44, benchmark_smallcap Rs +41, snake_abs Rs +22, snake_abs_conv Rs +18, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -149, snake_viper_wild Rs -196, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -321, gold Rs -738

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.