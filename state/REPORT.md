# Paper trading report

Updated 2026-11-19 11:04 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,496 | +11.75% | 0 | - | 236 |
| benchmark | 220,877 | +10.44% | 0 | - | 237 |
| snake_abs_exit | 213,839 | +6.92% | 2 | 50% | 345 |
| intramonth | 213,049 | +6.52% | 0 | - | 235 |
| snake_abs_exit_conv | 211,850 | +5.92% | 2 | 50% | 345 |
| intraweek | 211,691 | +5.84% | 35 | 54% | 3,851 |
| oracle | 210,823 | +5.41% | 0 | - | 233 |
| snake_abs | 209,483 | +4.74% | 1 | 100% | 255 |
| snake_abs_conv | 209,358 | +4.68% | 1 | 100% | 255 |
| random_hold | 207,620 | +3.81% | 10 | 70% | 733 |
| snake_viper_wild | 207,600 | +3.80% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,052 | +2.03% | 15 | 47% | 2,625 |
| snake_anaconda | 203,509 | +1.75% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,302 | +0.15% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,003 | -12.50% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,047 (-4.48%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +975 | +0.49% |
| unified | +884 | +0.40% |
| intramonth | +775 | +0.36% |
| random_hold | +688 | +0.33% |
| benchmark | +581 | +0.26% |
| snake_viper_wild | +560 | +0.27% |
| snake_viper_tick | +549 | +0.27% |
| snake_abs | +47 | +0.02% |
| snake_abs_conv | +33 | +0.02% |
| oracle | +27 | +0.01% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraweek | -148 | -0.07% |
| snake_abs_exit | -193 | -0.09% |
| snake_abs_exit_conv | -533 | -0.25% |
| snake_anaconda | -892 | -0.44% |
| gold | -2,318 | -1.31% |

Average per day so far: unified Rs +635, benchmark Rs +564, snake_abs_exit Rs +407, intramonth Rs +353, snake_abs_exit_conv Rs +349, intraweek Rs +316, oracle Rs +293, snake_abs_conv Rs +275, snake_abs Rs +271, snake_viper_wild Rs +262, random_hold Rs +206, snake_viper_tick Rs +156, snake_anaconda Rs +110, nifty_calls Rs +50, benchmark_smallcap Rs +9, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -676

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.