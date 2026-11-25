# Paper trading report

Updated 2026-11-25 13:26 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,627 | +12.31% | 0 | - | 236 |
| benchmark | 223,975 | +11.99% | 0 | - | 237 |
| oracle | 212,328 | +6.16% | 0 | - | 233 |
| intramonth | 212,263 | +6.13% | 0 | - | 235 |
| random_hold | 209,677 | +4.84% | 12 | 75% | 1,009 |
| intraweek | 208,350 | +4.17% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,524 | +0.76% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,166 | +0.58% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,821 | -0.09% | 1 | 100% | 255 |
| snake_abs_conv | 199,623 | -0.19% | 1 | 100% | 255 |
| benchmark_smallcap | 198,878 | -0.56% | 0 | - | 237 |
| snake_viper_wild | 197,025 | -1.49% | 16 | 50% | 2,827 |
| snake_viper_tick | 193,669 | -3.17% | 15 | 47% | 2,625 |
| snake_anaconda | 193,251 | -3.37% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,646 | -17.68% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,065 (-5.47%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,502 | +1.13% |
| random_hold | +1,250 | +0.60% |
| unified | +342 | +0.15% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -14 | -0.01% |
| benchmark_smallcap | -101 | -0.05% |
| intramonth | -488 | -0.23% |
| intraweek | -3,269 | -1.54% |
| snake_viper_tick | -4,023 | -2.04% |
| snake_viper_wild | -4,099 | -2.04% |
| gold | -4,784 | -2.82% |
| snake_anaconda | -5,452 | -2.74% |
| snake_abs | -5,640 | -2.75% |
| snake_abs_conv | -5,680 | -2.77% |
| snake_abs_exit_conv | -5,880 | -2.84% |
| snake_abs_exit | -5,971 | -2.88% |

Average per day so far: unified Rs +616, benchmark Rs +599, oracle Rs +308, intramonth Rs +307, random_hold Rs +242, intraweek Rs +209, nifty_calls Rs +46, snake_abs_exit Rs +41, snake_abs_exit_conv Rs +32, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -5, snake_abs_conv Rs -10, benchmark_smallcap Rs -31, snake_viper_wild Rs -93, snake_anaconda Rs -193, snake_viper_tick Rs -218, snake_nonews Rs -292, snake Rs -311, gold Rs -884

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.