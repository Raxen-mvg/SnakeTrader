# Paper trading report

Updated 2026-11-23 11:17 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,414 | +12.21% | 0 | - | 236 |
| benchmark | 223,806 | +11.90% | 0 | - | 237 |
| intraweek | 212,899 | +6.45% | 40 | 55% | 4,400 |
| intramonth | 212,565 | +6.28% | 0 | - | 235 |
| oracle | 211,408 | +5.70% | 0 | - | 233 |
| random_hold | 209,852 | +4.93% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,716 | +3.36% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,784 | +2.89% | 2 | 50% | 345 |
| snake_abs | 204,000 | +2.00% | 1 | 100% | 255 |
| snake_abs_conv | 203,836 | +1.92% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,534 | +0.27% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,775 | -0.11% | 0 | - | 237 |
| snake_anaconda | 197,622 | -1.19% | 3 | 33% | 374 |
| snake_viper_tick | 197,115 | -1.44% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,907 | -15.05% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,369 (-4.82%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,858 | +1.10% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -832 | -0.40% |
| random_hold | -908 | -0.43% |
| oracle | -1,071 | -0.50% |
| benchmark_smallcap | -1,132 | -0.56% |
| benchmark | -1,331 | -0.59% |
| unified | -1,767 | -0.78% |
| snake_abs_exit | -1,847 | -0.89% |
| snake_abs | -1,920 | -0.93% |
| snake_abs_conv | -1,947 | -0.95% |
| snake_viper_tick | -2,257 | -1.13% |
| snake_anaconda | -2,284 | -1.14% |
| snake_viper_wild | -2,295 | -1.13% |
| intramonth | -2,439 | -1.14% |
| intraweek | -2,813 | -1.30% |

Average per day so far: unified Rs +626, benchmark Rs +610, intraweek Rs +331, intramonth Rs +322, oracle Rs +293, random_hold Rs +253, snake_abs_exit Rs +187, snake_abs_exit_conv Rs +161, snake_abs Rs +108, snake_abs_conv Rs +107, nifty_calls Rs +47, snake_viper_wild Rs +17, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -6, snake_anaconda Rs -70, snake_viper_tick Rs -103, snake_nonews Rs -300, snake Rs -320, gold Rs -772

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.