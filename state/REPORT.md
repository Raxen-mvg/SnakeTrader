# Paper trading report

Updated 2026-11-23 15:15 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,819 | +11.91% | 0 | - | 236 |
| benchmark | 221,527 | +10.76% | 0 | - | 237 |
| oracle | 212,179 | +6.09% | 0 | - | 233 |
| intramonth | 211,839 | +5.92% | 0 | - | 235 |
| intraweek | 211,490 | +5.75% | 40 | 55% | 4,400 |
| random_hold | 208,361 | +4.18% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,999 | +4.00% | 2 | 50% | 345 |
| snake_abs_exit_conv | 207,552 | +3.78% | 2 | 50% | 345 |
| snake_abs | 205,857 | +2.93% | 1 | 100% | 255 |
| snake_abs_conv | 205,706 | +2.85% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,225 | +0.61% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,506 | -0.25% | 0 | - | 237 |
| snake_anaconda | 199,186 | -0.41% | 3 | 33% | 374 |
| snake_viper_tick | 197,791 | -1.10% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,463 | -15.27% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,140 (-4.93%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,414 | +0.84% |
| snake_abs_exit_conv | +936 | +0.45% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs | -63 | -0.03% |
| snake_abs_conv | -77 | -0.04% |
| oracle | -300 | -0.14% |
| snake_abs_exit | -564 | -0.27% |
| snake_anaconda | -720 | -0.36% |
| benchmark_smallcap | -1,401 | -0.70% |
| snake_viper_tick | -1,580 | -0.79% |
| snake_viper_wild | -1,604 | -0.79% |
| unified | -2,363 | -1.04% |
| random_hold | -2,398 | -1.14% |
| intramonth | -3,165 | -1.47% |
| benchmark | -3,611 | -1.60% |
| intraweek | -4,222 | -1.96% |

Average per day so far: unified Rs +611, benchmark Rs +552, oracle Rs +312, intramonth Rs +304, intraweek Rs +295, snake_abs_exit Rs +222, random_hold Rs +214, snake_abs_exit_conv Rs +210, snake_abs_conv Rs +158, snake_abs Rs +158, nifty_calls Rs +47, snake_viper_wild Rs +40, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -14, snake_anaconda Rs -24, snake_viper_tick Rs -79, snake_nonews Rs -300, snake Rs -320, gold Rs -783

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.