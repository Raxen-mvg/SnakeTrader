# Paper trading report

Updated 2026-11-26 09:45 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,510 | +12.26% | 0 | - | 237 |
| unified | 223,866 | +11.93% | 0 | - | 236 |
| oracle | 213,635 | +6.82% | 0 | - | 233 |
| intramonth | 211,509 | +5.75% | 0 | - | 235 |
| random_hold | 210,368 | +5.18% | 13 | 69% | 1,037 |
| intraweek | 207,386 | +3.69% | 40 | 55% | 4,400 |
| snake_abs_exit | 203,622 | +1.81% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,980 | +1.49% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,865 | +0.43% | 1 | 100% | 255 |
| snake_abs_conv | 200,689 | +0.34% | 1 | 100% | 255 |
| benchmark_smallcap | 200,336 | +0.17% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,540 | -1.73% | 16 | 50% | 2,827 |
| snake_anaconda | 195,151 | -2.42% | 3 | 33% | 374 |
| snake_viper_tick | 193,195 | -3.40% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,161 | -16.42% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,309 (-5.35%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,565 | +1.56% |
| benchmark_smallcap | +1,525 | +0.77% |
| snake_abs_exit | +1,366 | +0.68% |
| snake_abs_exit_conv | +1,004 | +0.50% |
| random_hold | +876 | +0.42% |
| snake_abs_conv | +716 | +0.36% |
| snake_abs | +715 | +0.36% |
| intraweek | +643 | +0.31% |
| snake_anaconda | +598 | +0.31% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -160 | -0.07% |
| intramonth | -184 | -0.09% |
| unified | -233 | -0.10% |
| benchmark | -513 | -0.23% |
| snake_viper_tick | -982 | -0.51% |
| snake_viper_wild | -1,003 | -0.51% |

Average per day so far: benchmark Rs +598, unified Rs +582, oracle Rs +333, intramonth Rs +281, random_hold Rs +253, intraweek Rs +180, snake_abs_exit Rs +95, snake_abs_exit_conv Rs +78, nifty_calls Rs +45, snake_abs Rs +22, snake_abs_conv Rs +18, benchmark_smallcap Rs +9, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_viper_wild Rs -105, snake_anaconda Rs -135, snake_viper_tick Rs -227, snake_nonews Rs -284, snake Rs -304, gold Rs -801

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.