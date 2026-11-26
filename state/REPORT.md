# Paper trading report

Updated 2026-11-26 10:51 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,346 | +13.17% | 0 | - | 237 |
| unified | 223,547 | +11.77% | 0 | - | 236 |
| oracle | 212,906 | +6.45% | 0 | - | 233 |
| intramonth | 210,828 | +5.41% | 0 | - | 235 |
| random_hold | 209,733 | +4.87% | 13 | 69% | 1,037 |
| intraweek | 207,714 | +3.86% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,089 | +1.04% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,481 | +0.74% | 2 | 50% | 345 |
| benchmark_smallcap | 200,616 | +0.31% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,710 | -0.14% | 1 | 100% | 255 |
| snake_abs_conv | 199,525 | -0.24% | 1 | 100% | 255 |
| snake_anaconda | 193,456 | -3.27% | 3 | 33% | 374 |
| snake_viper_wild | 193,286 | -3.36% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,999 | -5.00% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,950 | -16.02% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,869 (-5.57%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +3,354 | +2.04% |
| benchmark_smallcap | +1,805 | +0.91% |
| benchmark | +1,323 | +0.59% |
| intraweek | +970 | +0.47% |
| random_hold | +240 | +0.11% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -167 | -0.08% |
| snake_abs | -440 | -0.22% |
| snake_abs_conv | -447 | -0.22% |
| snake_abs_exit_conv | -495 | -0.24% |
| unified | -553 | -0.25% |
| intramonth | -865 | -0.41% |
| oracle | -889 | -0.42% |
| snake_anaconda | -1,097 | -0.56% |
| snake_viper_tick | -4,178 | -2.15% |
| snake_viper_wild | -4,258 | -2.15% |

Average per day so far: benchmark Rs +643, unified Rs +574, oracle Rs +315, intramonth Rs +264, random_hold Rs +237, intraweek Rs +188, snake_abs_exit Rs +55, nifty_calls Rs +45, snake_abs_exit_conv Rs +39, benchmark_smallcap Rs +17, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -7, snake_abs_conv Rs -12, snake_anaconda Rs -182, snake_viper_wild Rs -203, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -333, gold Rs -782

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.