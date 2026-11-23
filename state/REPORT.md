# Paper trading report

Updated 2026-11-23 10:38 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,271 | +12.13% | 0 | - | 236 |
| benchmark | 223,286 | +11.64% | 0 | - | 237 |
| intraweek | 212,768 | +6.38% | 40 | 55% | 4,400 |
| intramonth | 212,140 | +6.07% | 0 | - | 235 |
| oracle | 211,071 | +5.54% | 0 | - | 233 |
| random_hold | 209,778 | +4.89% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,947 | +3.47% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,093 | +3.05% | 2 | 50% | 345 |
| snake_abs | 204,338 | +2.17% | 1 | 100% | 255 |
| snake_abs_conv | 204,187 | +2.09% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,419 | +0.21% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,574 | -0.21% | 0 | - | 237 |
| snake_anaconda | 197,953 | -1.02% | 3 | 33% | 374 |
| snake_viper_tick | 197,002 | -1.50% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,282 | -15.36% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,250 (-4.87%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,233 | +0.73% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -524 | -0.25% |
| random_hold | -981 | -0.47% |
| benchmark_smallcap | -1,334 | -0.66% |
| oracle | -1,407 | -0.66% |
| snake_abs | -1,582 | -0.77% |
| snake_abs_conv | -1,596 | -0.78% |
| snake_abs_exit | -1,615 | -0.77% |
| benchmark | -1,851 | -0.82% |
| unified | -1,911 | -0.84% |
| snake_anaconda | -1,953 | -0.98% |
| snake_viper_tick | -2,370 | -1.19% |
| snake_viper_wild | -2,411 | -1.19% |
| intramonth | -2,864 | -1.33% |
| intraweek | -2,944 | -1.36% |

Average per day so far: unified Rs +622, benchmark Rs +597, intraweek Rs +327, intramonth Rs +311, oracle Rs +284, random_hold Rs +251, snake_abs_exit Rs +193, snake_abs_exit_conv Rs +169, snake_abs Rs +117, snake_abs_conv Rs +116, nifty_calls Rs +47, snake_viper_wild Rs +14, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -12, snake_anaconda Rs -60, snake_viper_tick Rs -107, snake_nonews Rs -300, snake Rs -320, gold Rs -788

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.