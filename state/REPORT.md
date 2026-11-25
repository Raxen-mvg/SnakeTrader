# Paper trading report

Updated 2026-11-25 13:40 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,624 | +12.31% | 0 | - | 236 |
| benchmark | 224,281 | +12.14% | 0 | - | 237 |
| oracle | 212,440 | +6.22% | 0 | - | 233 |
| intramonth | 212,237 | +6.12% | 0 | - | 235 |
| random_hold | 209,557 | +4.78% | 12 | 75% | 1,009 |
| intraweek | 207,605 | +3.80% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,521 | +0.76% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,224 | +0.61% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,734 | -0.13% | 1 | 100% | 255 |
| snake_abs_conv | 199,538 | -0.23% | 1 | 100% | 255 |
| benchmark_smallcap | 198,822 | -0.59% | 0 | - | 237 |
| snake_viper_wild | 197,006 | -1.50% | 16 | 50% | 2,827 |
| snake_viper_tick | 193,650 | -3.17% | 15 | 47% | 2,625 |
| snake_anaconda | 193,255 | -3.37% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,580 | -17.71% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,973 (-5.51%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,808 | +1.27% |
| random_hold | +1,130 | +0.54% |
| unified | +339 | +0.15% |
| oracle | +98 | +0.05% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -157 | -0.08% |
| intramonth | -514 | -0.24% |
| intraweek | -4,014 | -1.90% |
| snake_viper_tick | -4,042 | -2.04% |
| snake_viper_wild | -4,119 | -2.05% |
| gold | -4,850 | -2.86% |
| snake_anaconda | -5,449 | -2.74% |
| snake_abs | -5,727 | -2.79% |
| snake_abs_conv | -5,764 | -2.81% |
| snake_abs_exit_conv | -5,822 | -2.81% |
| snake_abs_exit | -5,974 | -2.88% |

Average per day so far: unified Rs +616, benchmark Rs +607, oracle Rs +311, intramonth Rs +306, random_hold Rs +239, intraweek Rs +190, nifty_calls Rs +46, snake_abs_exit Rs +41, snake_abs_exit_conv Rs +33, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -7, snake_abs_conv Rs -12, benchmark_smallcap Rs -33, snake_viper_wild Rs -94, snake_anaconda Rs -193, snake_viper_tick Rs -219, snake_nonews Rs -292, snake Rs -311, gold Rs -885

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.