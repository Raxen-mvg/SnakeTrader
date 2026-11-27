# Paper trading report

Updated 2026-11-27 09:35 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,658 | +12.83% | 0 | - | 237 |
| unified | 223,358 | +11.68% | 0 | - | 236 |
| oracle | 212,418 | +6.21% | 0 | - | 233 |
| intramonth | 210,984 | +5.49% | 0 | - | 235 |
| random_hold | 209,628 | +4.81% | 13 | 69% | 1,037 |
| intraweek | 207,941 | +3.97% | 40 | 55% | 4,400 |
| snake_abs_exit | 203,988 | +1.99% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,140 | +1.57% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,816 | +0.91% | 0 | - | 237 |
| snake_abs | 200,268 | +0.13% | 1 | 100% | 255 |
| snake_abs_conv | 200,080 | +0.04% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,844 | -3.08% | 3 | 33% | 374 |
| snake_viper_wild | 192,892 | -3.55% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,613 | -5.19% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,934 | -16.03% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,789 (-5.61%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +2,911 | +1.45% |
| snake_abs_exit_conv | +2,743 | +1.37% |
| gold | +1,940 | +1.17% |
| snake_abs | +1,716 | +0.86% |
| snake_abs_conv | +1,713 | +0.86% |
| snake_anaconda | +1,547 | +0.81% |
| random_hold | +1,034 | +0.50% |
| benchmark_smallcap | +975 | +0.49% |
| intraweek | +893 | +0.43% |
| snake_viper_wild | +686 | +0.36% |
| snake_viper_tick | +672 | +0.36% |
| intramonth | +450 | +0.21% |
| unified | +280 | +0.12% |
| oracle | +182 | +0.09% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -329 | -0.15% |

Average per day so far: benchmark Rs +611, unified Rs +556, oracle Rs +296, intramonth Rs +262, random_hold Rs +229, intraweek Rs +189, snake_abs_exit Rs +102, snake_abs_exit_conv Rs +81, benchmark_smallcap Rs +48, nifty_calls Rs +44, snake_abs Rs +7, snake_abs_conv Rs +2, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -166, snake_viper_wild Rs -209, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -335, gold Rs -763

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.