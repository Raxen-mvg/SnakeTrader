# Paper trading report

Updated 2026-11-25 12:48 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,119 | +12.56% | 0 | - | 236 |
| benchmark | 224,809 | +12.40% | 0 | - | 237 |
| intramonth | 213,276 | +6.64% | 0 | - | 235 |
| oracle | 212,939 | +6.47% | 0 | - | 233 |
| random_hold | 210,233 | +5.12% | 12 | 75% | 1,009 |
| intraweek | 208,556 | +4.28% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,169 | +1.08% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,009 | +1.00% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,429 | +0.21% | 1 | 100% | 255 |
| snake_abs_conv | 200,250 | +0.12% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,327 | -0.34% | 0 | - | 237 |
| snake_viper_wild | 196,862 | -1.57% | 16 | 50% | 2,827 |
| snake_anaconda | 193,963 | -3.02% | 3 | 33% | 374 |
| snake_viper_tick | 193,509 | -3.25% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,596 | -17.70% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,590 (-5.21%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,335 | +1.51% |
| random_hold | +1,807 | +0.87% |
| unified | +833 | +0.37% |
| oracle | +597 | +0.28% |
| intramonth | +524 | +0.25% |
| benchmark_smallcap | +348 | +0.17% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -3,063 | -1.45% |
| snake_viper_tick | -4,183 | -2.12% |
| snake_viper_wild | -4,263 | -2.12% |
| snake_anaconda | -4,740 | -2.38% |
| gold | -4,833 | -2.85% |
| snake_abs | -5,032 | -2.45% |
| snake_abs_exit_conv | -5,037 | -2.43% |
| snake_abs_conv | -5,053 | -2.46% |
| snake_abs_exit | -5,326 | -2.57% |

Average per day so far: unified Rs +628, benchmark Rs +620, intramonth Rs +332, oracle Rs +323, random_hold Rs +256, intraweek Rs +214, snake_abs_exit Rs +59, snake_abs_exit_conv Rs +54, nifty_calls Rs +46, snake_abs Rs +11, snake_abs_conv Rs +7, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -19, snake_viper_wild Rs -98, snake_anaconda Rs -172, snake_viper_tick Rs -224, snake_nonews Rs -292, snake Rs -311, gold Rs -885

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.