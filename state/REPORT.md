# Paper trading report

Updated 2026-11-27 10:49 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,046 | +12.52% | 0 | - | 237 |
| unified | 223,161 | +11.58% | 0 | - | 236 |
| oracle | 212,638 | +6.32% | 0 | - | 233 |
| intramonth | 210,838 | +5.42% | 0 | - | 235 |
| random_hold | 209,593 | +4.80% | 13 | 69% | 1,037 |
| intraweek | 207,790 | +3.90% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,503 | +2.75% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,263 | +2.13% | 2 | 50% | 345 |
| benchmark_smallcap | 202,174 | +1.09% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,101 | +0.55% | 1 | 100% | 255 |
| snake_abs_conv | 200,925 | +0.46% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,702 | -2.65% | 3 | 33% | 374 |
| snake_viper_wild | 193,623 | -3.19% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,330 | -4.83% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,756 | -15.62% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,788 (-5.61%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,426 | +2.20% |
| snake_abs_exit_conv | +3,867 | +1.93% |
| gold | +2,762 | +1.66% |
| snake_abs_conv | +2,558 | +1.29% |
| snake_abs | +2,549 | +1.28% |
| snake_anaconda | +2,405 | +1.25% |
| snake_viper_wild | +1,418 | +0.74% |
| snake_viper_tick | +1,389 | +0.73% |
| benchmark_smallcap | +1,334 | +0.66% |
| random_hold | +999 | +0.48% |
| intraweek | +741 | +0.36% |
| oracle | +402 | +0.19% |
| intramonth | +305 | +0.14% |
| unified | +82 | +0.04% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -941 | -0.42% |

Average per day so far: benchmark Rs +596, unified Rs +551, oracle Rs +301, intramonth Rs +258, random_hold Rs +228, intraweek Rs +185, snake_abs_exit Rs +141, snake_abs_exit_conv Rs +109, benchmark_smallcap Rs +57, nifty_calls Rs +44, snake_abs Rs +28, snake_abs_conv Rs +24, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -143, snake_viper_wild Rs -188, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -312, gold Rs -744

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.