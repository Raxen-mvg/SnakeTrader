# Paper trading report

Updated 2026-11-25 11:13 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,933 | +12.97% | 0 | - | 237 |
| unified | 224,893 | +12.45% | 0 | - | 236 |
| intramonth | 212,728 | +6.36% | 0 | - | 235 |
| oracle | 211,854 | +5.93% | 0 | - | 233 |
| random_hold | 210,284 | +5.14% | 12 | 75% | 1,009 |
| intraweek | 208,493 | +4.25% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,726 | +0.86% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,178 | +0.59% | 2 | 50% | 345 |
| snake_abs | 201,144 | +0.57% | 1 | 100% | 255 |
| snake_abs_conv | 200,949 | +0.47% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,417 | -0.29% | 0 | - | 237 |
| snake_viper_wild | 195,330 | -2.33% | 16 | 50% | 2,827 |
| snake_anaconda | 193,255 | -3.37% | 3 | 33% | 374 |
| snake_viper_tick | 192,010 | -4.00% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,810 | -17.59% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,306 (-5.35%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,460 | +2.01% |
| random_hold | +1,858 | +0.89% |
| unified | +608 | +0.27% |
| benchmark_smallcap | +437 | +0.22% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -23 | -0.01% |
| oracle | -488 | -0.23% |
| intraweek | -3,126 | -1.48% |
| snake_abs | -4,316 | -2.10% |
| snake_abs_conv | -4,354 | -2.12% |
| gold | -4,620 | -2.73% |
| snake_anaconda | -5,448 | -2.74% |
| snake_viper_tick | -5,682 | -2.87% |
| snake_abs_exit | -5,769 | -2.78% |
| snake_viper_wild | -5,794 | -2.88% |
| snake_abs_exit_conv | -5,867 | -2.83% |

Average per day so far: benchmark Rs +648, unified Rs +622, intramonth Rs +318, oracle Rs +296, random_hold Rs +257, intraweek Rs +212, snake_abs_exit Rs +47, nifty_calls Rs +46, snake_abs_exit_conv Rs +32, snake_abs Rs +30, snake_abs_conv Rs +26, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -16, snake_viper_wild Rs -146, snake_anaconda Rs -193, snake_viper_tick Rs -276, snake_nonews Rs -292, snake Rs -311, gold Rs -880

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.