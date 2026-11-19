# Paper trading report

Updated 2026-11-19 10:14 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,349 | +12.17% | 0 | - | 236 |
| benchmark | 220,609 | +10.30% | 0 | - | 237 |
| intramonth | 214,070 | +7.04% | 0 | - | 235 |
| snake_abs_exit | 213,371 | +6.69% | 2 | 50% | 345 |
| intraweek | 212,997 | +6.50% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,547 | +5.77% | 2 | 50% | 345 |
| oracle | 211,527 | +5.76% | 0 | - | 233 |
| snake_abs | 208,813 | +4.41% | 1 | 100% | 255 |
| snake_abs_conv | 208,681 | +4.34% | 1 | 100% | 255 |
| random_hold | 208,102 | +4.05% | 10 | 70% | 733 |
| snake_viper_wild | 207,673 | +3.84% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,124 | +2.06% | 15 | 47% | 2,625 |
| snake_anaconda | 203,533 | +1.77% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,650 | +0.33% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,658 | -12.67% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,792 (-4.10%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| intramonth | +1,796 | +0.85% |
| unified | +1,737 | +0.78% |
| benchmark_smallcap | +1,323 | +0.66% |
| random_hold | +1,170 | +0.56% |
| intraweek | +1,157 | +0.55% |
| oracle | +731 | +0.35% |
| snake_viper_wild | +634 | +0.31% |
| snake_viper_tick | +620 | +0.30% |
| benchmark | +314 | +0.14% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -623 | -0.30% |
| snake_abs_conv | -644 | -0.31% |
| snake_abs_exit | -661 | -0.31% |
| snake_abs_exit_conv | -837 | -0.39% |
| snake_anaconda | -868 | -0.42% |
| gold | -2,663 | -1.50% |

Average per day so far: unified Rs +658, benchmark Rs +557, snake_abs_exit Rs +393, intramonth Rs +380, intraweek Rs +351, snake_abs_exit_conv Rs +340, oracle Rs +312, snake_viper_wild Rs +265, snake_abs_conv Rs +255, snake_abs Rs +252, random_hold Rs +219, snake_viper_tick Rs +159, snake_anaconda Rs +110, nifty_calls Rs +50, benchmark_smallcap Rs +20, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -685

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.