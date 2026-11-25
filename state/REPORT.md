# Paper trading report

Updated 2026-11-25 11:03 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,887 | +12.94% | 0 | - | 237 |
| unified | 225,119 | +12.56% | 0 | - | 236 |
| intramonth | 212,839 | +6.42% | 0 | - | 235 |
| oracle | 212,087 | +6.04% | 0 | - | 233 |
| random_hold | 209,964 | +4.98% | 12 | 75% | 1,009 |
| intraweek | 208,535 | +4.27% | 40 | 55% | 4,400 |
| snake_abs_exit | 201,891 | +0.94% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,389 | +0.69% | 2 | 50% | 345 |
| snake_abs | 201,139 | +0.57% | 1 | 100% | 255 |
| snake_abs_conv | 200,949 | +0.47% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,461 | -0.27% | 0 | - | 237 |
| snake_viper_wild | 195,374 | -2.31% | 16 | 50% | 2,827 |
| snake_anaconda | 193,449 | -3.28% | 3 | 33% | 374 |
| snake_viper_tick | 192,052 | -3.97% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,320 | -17.34% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,371 (-5.31%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,414 | +1.99% |
| random_hold | +1,537 | +0.74% |
| unified | +834 | +0.37% |
| benchmark_smallcap | +482 | +0.24% |
| intramonth | +87 | +0.04% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| oracle | -255 | -0.12% |
| intraweek | -3,084 | -1.46% |
| gold | -4,110 | -2.43% |
| snake_abs | -4,322 | -2.10% |
| snake_abs_conv | -4,354 | -2.12% |
| snake_anaconda | -5,255 | -2.65% |
| snake_abs_exit | -5,604 | -2.70% |
| snake_viper_tick | -5,640 | -2.85% |
| snake_abs_exit_conv | -5,657 | -2.73% |
| snake_viper_wild | -5,751 | -2.86% |

Average per day so far: benchmark Rs +647, unified Rs +628, intramonth Rs +321, oracle Rs +302, random_hold Rs +249, intraweek Rs +213, snake_abs_exit Rs +51, nifty_calls Rs +46, snake_abs_exit_conv Rs +38, snake_abs Rs +30, snake_abs_conv Rs +26, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -15, snake_viper_wild Rs -145, snake_anaconda Rs -187, snake_viper_tick Rs -274, snake_nonews Rs -292, snake Rs -311, gold Rs -867

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.