# Paper trading report

Updated 2026-11-23 15:22 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,190 | +12.10% | 0 | - | 236 |
| benchmark | 221,450 | +10.72% | 0 | - | 237 |
| intramonth | 212,384 | +6.19% | 0 | - | 235 |
| oracle | 212,244 | +6.12% | 0 | - | 233 |
| intraweek | 211,800 | +5.90% | 40 | 55% | 4,400 |
| random_hold | 208,376 | +4.19% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,401 | +3.70% | 2 | 50% | 345 |
| snake_abs_exit_conv | 207,078 | +3.54% | 2 | 50% | 345 |
| snake_abs | 205,502 | +2.75% | 1 | 100% | 255 |
| snake_abs_conv | 205,346 | +2.67% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,889 | +0.45% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,946 | -0.53% | 0 | - | 237 |
| snake_anaconda | 198,648 | -0.68% | 3 | 33% | 374 |
| snake_viper_tick | 197,462 | -1.27% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,545 | -15.23% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,217 (-4.89%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,496 | +0.89% |
| snake_abs_exit_conv | +462 | +0.22% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -234 | -0.11% |
| snake_abs | -418 | -0.20% |
| snake_abs_conv | -437 | -0.21% |
| snake_abs_exit | -1,161 | -0.56% |
| snake_anaconda | -1,258 | -0.63% |
| snake_viper_tick | -1,909 | -0.96% |
| snake_viper_wild | -1,940 | -0.96% |
| benchmark_smallcap | -1,962 | -0.98% |
| unified | -1,992 | -0.88% |
| random_hold | -2,383 | -1.13% |
| intramonth | -2,621 | -1.22% |
| benchmark | -3,687 | -1.64% |
| intraweek | -3,912 | -1.81% |

Average per day so far: unified Rs +620, benchmark Rs +550, intramonth Rs +318, oracle Rs +314, intraweek Rs +303, random_hold Rs +215, snake_abs_exit Rs +206, snake_abs_exit_conv Rs +197, snake_abs Rs +149, snake_abs_conv Rs +148, nifty_calls Rs +47, snake_viper_wild Rs +29, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -30, snake_anaconda Rs -40, snake_viper_tick Rs -91, snake_nonews Rs -300, snake Rs -320, gold Rs -781

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.