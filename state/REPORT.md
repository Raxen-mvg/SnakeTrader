# Paper trading report

Updated 2026-11-25 14:07 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,661 | +12.33% | 0 | - | 236 |
| benchmark | 224,571 | +12.29% | 0 | - | 237 |
| oracle | 212,583 | +6.29% | 0 | - | 233 |
| intramonth | 212,248 | +6.12% | 0 | - | 235 |
| random_hold | 209,389 | +4.69% | 12 | 75% | 1,009 |
| intraweek | 207,022 | +3.51% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,255 | +0.63% | 2 | 50% | 345 |
| snake_abs_exit_conv | 200,958 | +0.48% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,495 | -0.25% | 1 | 100% | 255 |
| snake_abs_conv | 199,296 | -0.35% | 1 | 100% | 255 |
| benchmark_smallcap | 198,766 | -0.62% | 0 | - | 237 |
| snake_viper_wild | 196,967 | -1.52% | 16 | 50% | 2,827 |
| snake_viper_tick | 193,613 | -3.19% | 15 | 47% | 2,625 |
| snake_anaconda | 193,009 | -3.50% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,123 | -17.44% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,869 (-5.57%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,098 | +1.40% |
| random_hold | +962 | +0.46% |
| unified | +375 | +0.17% |
| oracle | +240 | +0.11% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -213 | -0.11% |
| intramonth | -504 | -0.24% |
| snake_viper_tick | -4,080 | -2.06% |
| snake_viper_wild | -4,157 | -2.07% |
| gold | -4,307 | -2.54% |
| intraweek | -4,597 | -2.17% |
| snake_anaconda | -5,695 | -2.87% |
| snake_abs | -5,966 | -2.90% |
| snake_abs_conv | -6,007 | -2.93% |
| snake_abs_exit_conv | -6,088 | -2.94% |
| snake_abs_exit | -6,240 | -3.01% |

Average per day so far: unified Rs +617, benchmark Rs +614, oracle Rs +315, intramonth Rs +306, random_hold Rs +235, intraweek Rs +176, nifty_calls Rs +46, snake_abs_exit Rs +34, snake_abs_exit_conv Rs +26, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -13, snake_abs_conv Rs -19, benchmark_smallcap Rs -34, snake_viper_wild Rs -95, snake_anaconda Rs -200, snake_viper_tick Rs -220, snake_nonews Rs -292, snake Rs -311, gold Rs -872

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.